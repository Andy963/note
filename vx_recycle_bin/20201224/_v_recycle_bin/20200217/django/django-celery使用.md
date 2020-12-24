# django中使用celery

## 准备工作

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