
### Interval
```python
from datetime import datetime  
  
from flask import Flask  
from flask_apscheduler import APScheduler  
  
sd = APScheduler()  
  
  
class JobConfig:  
    JOBS = [  
        {            'id': 'job1',  
            'func': 'app:job_do_sth',  
            'args': (1, 2),  
            'trigger': 'interval',  
            'seconds': 5  
        }  
    ]  
    SCHEDULER_API_ENABLED = True  
  
  
def job_do_sth(a, b):  
    print(f"{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')} job_do_sth:{a + b}")  
  
  
app = Flask(__name__)  
  
  
@app.route('/')  
def hello_world():  # put application's code here  
    return 'Hello World!'  
  
  
if __name__ == '__main__':  
    app.config.from_object(JobConfig())  
    scheduler = APScheduler()  
    scheduler.init_app(app)  
    scheduler.start()  
    app.run()
```


### cron

```python
from datetime import datetime  
  
from flask import Flask  
from flask_apscheduler import APScheduler  
  
sd = APScheduler()  
  
  
class JobConfig:  
    JOBS = [  
        {            'id': 'job1',  
            'func': 'app:job_do_sth',  
            'args': (1, 2),  
            'trigger': 'cron',  
            'day': '*',  
            'hour': 15,  
            'minute': '08',  
            'second': 5  
        }  
    ]  
    SCHEDULER_API_ENABLED = True  
  
  
def job_do_sth(a, b):  
    print(f"{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')} job_do_sth:{a + b}")  
  
  
app = Flask(__name__)  
  
  
@app.route('/')  
def hello_world():  # put application's code here  
    return 'Hello World!'  
  
  
if __name__ == '__main__':  
    app.config.from_object(JobConfig())  
    scheduler = APScheduler()  
    scheduler.init_app(app)  
    scheduler.start()  
    app.run()
```

### decorator

```python
from datetime import datetime  
  
from flask import Flask  
from flask_apscheduler import APScheduler  
  
sd = APScheduler()  
app = Flask(__name__)  
scheduler = APScheduler()  
  
  
class JobConfig:  
    SCHEDULER_API_ENABLED = True  
  
  
@scheduler.task('cron', id='do_job_sth', minute='*')  
def job_do_sth():  
    print(f"{datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')} job_do_sth")  
  
  
@app.route('/')  
def hello_world():  # put application's code here  
    return 'Hello World!'  
  
  
if __name__ == '__main__':  
    app.config.from_object(JobConfig())  
    scheduler.init_app(app)  
    scheduler.start()  
    app.run()
```


### app_context Error

当项目较大时，结构不像上面的三种使用方法一样简单，如果task中有使用到SQLAlchemy,会导致 No app_context Error
结构：
```
project
    -module
       -tasks
          __init__.py
          -- tasks.py
	   - __init__.py
	-app.py
```

tasks.__init__.py
负责实例化一个scheduler对象，用来避免可能的循环引用
```python
#!/usr/bin/python  
# coding:utf-8  
from flask_apscheduler import APScheduler  
  
scheduler = APScheduler()
```

tasks.tasks.py
定义具体的tasks,需要使用到app_context 
ref:前两个参考没成功，使用的第三种方式

```python
from module.tasks import scheduler

def task1():
	with scheduler.app.app_context():
		print("do sth")
```

module.__init__.py
配置scheduler的任务，并且在create_app中初始化app

```python
from module.tasks import scheduler
class JobConfig:  
    JOBS = [  
        {            'id': 'check_before',  
            'func': 'athena:tasks.tasks.check_before',  
            'trigger': 'cron',  
            'day': '*',  
            'hour': '9-18',  
            'minute': '*/1',  
            'second': 50  
        },  
        {  
            'id': 'check_after',  
            'func': 'athena:tasks.tasks.check_after',  
            'trigger': 'cron',  
            'day': '*',  
            'hour': '9-18',  
            'minute': '*/1',  
            'second': 5  
        }  
    ]  
    SCHEDULER_API_ENABLED = True

def create_app():
    # .... 省略其它代码
	app.config.from_object(JobConfig())  
	scheduler.init_app(app)  
	scheduler.start()
```


tasks.py

```python
def check_before():  
    """  
    一定要带上scheduler.app.app_context() 
    这里尝试使用下面Ref中第2个方式，发现并不解决问题  
    """    
    with scheduler.app.app_context():
	    # 此时有app 上下文
	    pass
```

Ref:
[Flask Context](https://viniciuschiele.github.io/flask-apscheduler/rst/usage.html)
[Querying model in Flask-APScheduler job raises app context RuntimeError](https://stackoverflow.com/questions/40117324/querying-model-in-flask-apscheduler-job-raises-app-context-runtimeerror)]
[Flask-APScheduler定时任务查询操作数据库（多文件/模块](https://www.cnblogs.com/cangqinglang/p/13700082.html)
