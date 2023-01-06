
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


### 多实例重复执行
当flask中使用了多进程或者集群存在多实例时，此时会导致现一任务重复执行的情况。对于因为 `debug=True`  导致执行两次的暂不讨论

这里要说的是使用全局锁的方式：

```python
def register_scheduler():  
    """  
    注册定时任务,使用全局锁，防止重复执行    """    
    f = open("scheduler.lock", "wb")  
    # noinspection PyBroadException  
    try:  
        fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)  
        #   fcntl.LOCK_EX  排他锁
        #   fcntl.LOCK_NB  非阻塞锁, 函数不能获得文件锁就立即返回
        scheduler.start()  
    except:  
        pass  
  
    def unlock():  
        fcntl.flock(f, fcntl.LOCK_UN)   # fcntl.LOCK_UN 解锁 
        f.close()  
  
    atexit.register(unlock)
```

[[17_flask_APScheduler#Interval]] 在将其中的scheduler.start() 修改为执行上面的函数

通过上面的函数，会在开始时创建scheduler.lock文件，并且加上排他锁，非阻塞锁，并启动scheduler,当第二个进程来启动时，发现有锁，而又因为有非阻塞锁，会立马返回不会启动scheduler,从而达到全局只启动一个scheduler的目的。代码上线，有待检验，因windows无fnctl 无法进行本地验证。

Ref:
 - [Multiple instances of shceduler problem · Issue #51 · viniciuschiele/flask-apscheduler · GitHub](https://github.com/viniciuschiele/flask-apscheduler/issues/51?utm_source=ld246.com)
-  [Gunicorn 部署 Flask-Apscheduler 重复执行问题 - 醒日是归时 - 博客园 (cnblogs.com)](https://www.cnblogs.com/cherylgi/p/16911787.html)
- [关于fcntl锁的说明参考这里](https://blog.51cto.com/zhou123/1650185)
- [fcntl在windows上不支持python - ModuleNotFoundError: No module named 'fcntl' - Stack Overflow](https://stackoverflow.com/questions/62788628/modulenotfounderror-no-module-named-fcntl)
- [atexit 退出处理器使用说明]( https://www.bookstack.cn/read/python-3.10.0-zh/e34a1a39f116875d.md)


 