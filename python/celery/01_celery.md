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
- 如果在win中,接收到任务但不执行,要注意是否使用了gevent或者pool. `celey -A own_schedule worker -l info -P gevent` or `celery -A own_schedule worker --pool=solo`
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