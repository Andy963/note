## flask中除了g能设置全局变量还有哪些方法可以


在 Flask 中，除了使用 `g` 对象设置全局变量之外，还有其他一些方法可以用于在不同上下文间共享数据。以下是几种常见的方法：

1. **使用 `session`**
`session` 是 Flask 内置的一个用于处理用户会话的对象，它通过 cookie 存储数据，用于在请求之间保存用户的状态。可以用于存储小的全局变量，尤其是在多个请求之间需要共享数据时。

```python
from flask import session

# 设置 session 数据
session['user_id'] = 42

# 获取 session 数据
user_id = session.get('user_id')


2. **使用 `current_app`**
`current_app` 是一个全局变量，它指向当前正在处理请求的 Flask 应用实例。可以通过它访问应用的配置或其他全局变量。

```python
from flask import current_app

# 设置全局配置数据
current_app.config['MY_GLOBAL'] = 'some_value'

# 获取全局配置数据
value = current_app.config.get('MY_GLOBAL')
```

 3. **使用 `Flask` 应用实例**
可以在 Flask 应用实例中直接设置全局变量，比如通过配置文件或直接在实例中添加属性。

```python
from flask import Flask

app = Flask(__name__)

# 设置全局变量
app.config['MY_GLOBAL'] = 'some_value'

# 获取全局变量
value = app.config.get('MY_GLOBAL')
```

 4. **使用全局 Python 变量**
虽然不推荐，但你可以在 Python 文件中定义全局变量，所有模块都能访问它。这种方法适合小型应用或单文件应用，但不适合大型项目，因为它会影响代码的可维护性。

```python
# 定义全局变量
my_global_variable = 'some_value'

# 在应用中使用
def my_function():
    global my_global_variable
    return my_global_variable
```

 5. **使用上下文处理器**
Flask 提供了上下文处理器（context processor）功能，可以用来在模板渲染时注入全局变量。

```python
@app.context_processor
def inject_global_variables():
    return dict(my_global='some_value')

# 在模板中使用 my_global
```

 6. **使用蓝图（Blueprints）共享状态**
通过蓝图可以将某些全局状态或数据注入到多个视图中，或者在应用的多个部分之间共享。

```python
from flask import Blueprint

bp = Blueprint('bp', __name__)

# 设置全局变量
bp.config['MY_GLOBAL'] = 'some_value'

# 获取全局变量
value = bp.config.get('MY_GLOBAL')
```

这些方法各有优劣，选择哪种方法应取决于你的应用结构和需求。


## 在不使用nginx 进行负载均衡时，flask 应用如何实现高并发？

1. 使用 WSGI 服务器:
   将 Flask 应用与专业的 WSGI 服务器（如 Gunicorn 或 uWSGI）结合使用，而不是直接使用 Flask 的开发服务器。这些 WSGI 服务器能够更好地处理并发请求。

   示例（使用 Gunicorn）:
      gunicorn --workers 4 --threads 2 app:app
   

2. 异步处理:
   使用异步框架如 Flask-AIOHTTP 或将 Flask 与 Quart（异步 Flask）结合使用，以实现非阻塞 I/O 操作。

3. 使用 gevent:
   使用 gevent 来实现协程，提高 I/O 密集型应用的并发性能。

   示例:
```python

from gevent import monkey
monkey.patch_all()

from flask import Flask
from gevent.pywsgi import WSGIServer

app = Flask(__name__)

... 你的 Flask 路由和视图函数 ...

if __name__ == '__main__':
   http_server = WSGIServer(('', 5000), app)
   http_server.serve_forever()
```
 
   

4. 水平扩展:
   虽然不使用 Nginx，但你仍可以运行多个 Flask 实例，并使用其他负载均衡解决方案（如 HAProxy）来分发流量。

