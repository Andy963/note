## 01_celery
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
