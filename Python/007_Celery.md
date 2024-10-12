## 01_celery

```python
own_schedule
├── celery.py
├── config.py
├── __init__.py
├── main.py
└── tasks
    ├── bili_sign.py
    └── test.py
```
几点要注意的地方 :
- 如果在win中,接收到任务但不执行,要注意是否使用了gevent或者pool. `celery -A own_schedule worker -l info -P gevent` or `celery -A own_schedule worker --pool=solo`
- config: field is : broker_url, result_backend, imports, beat_schedule
- fix conflict: `from __future__ import absolute_import `

### basic use
```python
from celery import Celery

app = Celery("single", broker="",backend="")

@app.task
def add(x,y):
    return x+y

# celery -A single worker -l info
# the command should run in the folder where single app is.
# you can check it in shell like this:
import sys
dir - "/opt/celery_demo"
sys.path.append(dir)
form single import add
add.delay(1,1)
t = add.delay(1,1)
t.get() # get the result
t.ready() # check if the task is running
```
### schedule task
cmd: `celery -A celery_demo beat`, `celery -A celery_demo worker -l info`

celery.py
```python
from celery import Celery
from celery.schedules import crontab

# app = Celery("celery_demo",broker="",backend=")
app = Celery("celery_demo")
app.config.from_objet("celery_demo_config")
```

config.py
```python
from celery.schedules import crontab
broker_url=""
result_backend=""
imports = [
         "celery_demo.tasks.task1",
         "celery_demo.tasks.task2"]

beat_scheduls = {
    "task1":{
             "task":celery_demo.tasks.task1.celery_task1",
             "schedule":crontab(minute="*/1"),
             "args:()
            },
    "task2":{
             "task":celery_demo.tasks.task2.celery_task2",
             "schedule":crontab(minute="*/1"),
             "args:()
            },
}
```
#add schedule task
```python
@app.on_after_finalize.connect
def setup_periodic_tasks(sender,**kwargs):
    sender.add_periodic_task(10,adds(1,2),name="add_every_10")
# on_after_finalize.connect only use when tasks and app in different folder.
```
### different time zone (UTC)

```python
import datetime
import pytz
def now_fun():
    return datetime.datetime.now(pytz.timezone('Asia/Shanghai'))

'periodic_task': {
    'task': 'api.tasks.periodic',
    'schedule': crontab(hour=6, minute=30, nowfun=now_fun)
}
# or use partial
from functools import partial
cet_crontab = partial(crontab, nowfun=now_fun)
'periodic_task': {
    'task': 'api.tasks.periodic',
    'schedule': cet_crontab(hour=6, minute=30)
}
```
if you use lambda function to define now_fun, it will raise picker errror.

## django中使用celery

### 准备工作

目录结构：
```python
#  注意其中app下面的 tasks.py, djangoCeleryDemo下面的 celery.py
djangoCeleryDemo
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   └── views.py
├── djangoCeleryDemo
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   └── settings.cpython-36.pyc
│   ├── celery.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py
```
### settings 配置
```python
CELERY_BROKER_URL = 'redis://192.168.16.8:6379'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://192.168.16.8:6379'
CELERY_TASK_SERIALIZER = 'json'
```

### 在项目同名目录创建celery.py
```python
#  写配置
import os
from celery import Celery

# set the default Django settings module for the 'celery' program.
# 指定项目的配置文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoCeleryDemo.settings')

app = Celery('django_celery_demo')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
```

### app下创建task.py
```python
#  写任务
from celery import shared_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


```
### 项目同名__init__中导入app
```python
from .celery import app as celery_app

__all__ = ('celery_app',)
```

运行celery
```shell
celery worker -A djangoCeleryDemo -l info
#  遇到问题：
[2020-02-05 15:32:15,173: ERROR/MainProcess] consumer: Cannot connect to amqp://guest:**@127.0.0.1:5672//: [Errno 111] Connection refused

# 因为用的是celery，而不是django celery 所以实例化celery对象时要指定broker
`app = Celery('djangoCeleryDemo',broker=settings.CELERY_BROKER_URL)`但这样只加载了broker。所以正常的做法是在celery.py中 app.config_from_object中指定namespace,这样才能正确加载settings中的所有以CELERY开头的配置。
```

### 编写视图函数
>   delay直接执行
>   apply_async（）则指定时间执行，其中的eta参数用来接收时间，一定要utc时间

```python
import datetime

from django.shortcuts import HttpResponse
from .tasks import add, mul
from celery.result import AsyncResult
from djangoCeleryDemo import celery_app


def create_task(request):
    print('请求来了')
    result = add.delay(2, 2)
    print('执行完毕')
    return HttpResponse(result.id)

def create_async_task(request):
    """创建定时任务"""
    # ETA一定要是utc时间

    ctime = datetime.datetime.now()
    utc_ctime = datetime.datetime.utcfromtimestamp(ctime.timestamp())

    s10 = datetime.timedelta(seconds=5)
    ctime_x = utc_ctime + s10
    print('async tasks')
    result = add.apply_async(args=(1,2),eta=ctime_x)
    return HttpResponse(result.id)

def get_result(request):
    nid = request.GET.get('nid')
    from celery.result import AsyncResult
    # from demos.celery import app
    from djangoCeleryDemo import celery_app
    # 取完数据仍在backends中，如果不需要执行result_object.forget()
    result_object = AsyncResult(id=nid, app=celery_app)
    # result_objcet.revoke() 取消任务，如果任务已经在执行，强制取消result_object.revoke(terminate=True)
    # get可能夯住，所以应该先判断status
    data = result_object.get()
    return HttpResponse(data)

def get_async_result(request):
    nid = request.GET.get('nid')
    result_object = AsyncResult(id=nid, app=celery_app)
    data = result_object.get()
    return  HttpResponse(data)


```

当在不同文件中存在同名task时，使用下面这种方式
```python
result1=app1.tasks.get("s1.add").delay(1,2)
result2=app2.tasks.get("s1.mul").delay(3,2)

```


## Flask中应用Celery

### 文件结构 
```python
pro_flask_celery/
├── app.py
├── celery_tasks
    ├── celery.py
    └── tasks.py
```

### app.py

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask
from celery.result import AsyncResult

from celery_tasks import tasks
from celery_tasks.celery import celery

app = Flask(__name__)

TASK_ID = None


@app.route('/')
def index():
    global TASK_ID
    result = tasks.xxxxx.delay()
    # result = tasks.task.apply_async(args=[1, 3], eta=datetime(2018, 5, 19, 1, 24, 0))
    TASK_ID = result.id

    return "任务已经提交"


@app.route('/result')
def result():
    global TASK_ID
    result = AsyncResult(id=TASK_ID, app=celery)
    if result.ready():
        return result.get()
    return "xxxx"


if __name__ == '__main__':
    app.run()

```

### celery.py

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from celery import Celery
from celery.schedules import crontab

celery = Celery('xxxxxx',
                broker='redis://192.168.10.48:6379',
                backend='redis://192.168.10.48:6379',
                include=['celery_tasks.tasks'])

# 时区
celery.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
celery.conf.enable_utc = False

celery_tasks/celery.py
```

### task.py
```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from .celery import celery


@celery.task
def hello(*args, **kwargs):
    print('执行hello')
    return "hello"


@celery.task
def xxxxx(*args, **kwargs):
    print('执行xxxxx')
    return "xxxxx"


@celery.task
def hhhhhh(*args, **kwargs):
    time.sleep(5)
    return "任务结果"

```

## 周期任务的创建
```python
from celery.schedules import crontab

app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'test_task': {
        'task': 'blog.tasks.download_data',
        'schedule': crontab(),
        'args': (),
    },
}
```
注意：其中的task一定要写 appName.moduleName.taskName,只写tasks.download_data会报错：unregistered 

## 面试题

### 什么是celery 
一个异步的任务队列，主要用于分布式系统中处理任务调度和执行。支持任务的并发、定时任务、工作流。

### celery 包含哪些组件
 任务队列 （broker), 任务执行者(worker), 结果后端（result backend), 任务（Task), 任务生产者（producer)