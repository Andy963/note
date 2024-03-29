
## view

### 视图函数中可以返回哪些值：
1. 可以返回字符串：返回的字符串其实底层将这个字符串包装成了一个`Response`对象。
2. 可以返回元组：元组的形式是(响应体,状态码,头部信息)，也不一定三个都要写，写两个也是可以的。返回的元组，其实在底层也是包装成了一个`Response`对象。
3. 可以返回`Response`及其子类。

### response对象
视图函数中的return默认会带很多其它信息，比如：content-type: text/plain. return 后面跟着：内容 ，状态码，headers
```python
@app.route('/hello/')
def hello():
    headers = {
        'content-type': 'text/plain',
        'location': 'www.baidu.com'
    }
    response = make_response('<html></html>', 301)
    response.headers = headers
    return response
    # return '<html></html>',301,header 与上面构建的response对象效果相同。
```


### 实现一个自定义的`Response`对象：
1. 继承自`Response`类。
2. 实现方法`force_type(cls,rv,environ=None)`。
3. 指定`app.response_class`为你自定义的`Response`对象。
4. 如果视图函数返回的数据，不是字符串，也不是元组，也不是Response对象，那么就会将返回值传给`force_type`，然后再将`force_type`的返回值返回给前端。

```python

from flask import Flask,Response,jsonify,render_template
# flask = werkzeug+sqlalchemy+jinja2
import json

app = Flask(__name__)

# 将视图函数中返回的字典，转换成json对象，然后返回
# restful-api
class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """
        这个方法只有视图函数返回非字符、非元组、非Response对象才会调用
        response：视图函数的返回值
        """
        if isinstance(response,dict):
            # jsonify除了将字典转换成json对象，还将改对象包装成了一个Response对象
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response,environ)

app.response_class = JSONResponse

@app.route('/list1/')
def list1():
    resp = Response('list1')
    resp.set_cookie('country','china')
    return resp

@app.route('/list2/')
def list2():
    return 'list2',200,{'X-NAME':'zhiliao'}

@app.route('/list3/')
def list3():
    return {'username':'zhiliao','age':18}

if __name__ == '__main__':
    app.run(debug=True,port=5000)
```


### 标准类视图：
1. 标准类视图，必须继承自`flask.views.View`.
2. 必须实现`dipatch_request`方法，以后请求过来后，都会执行这个方法。这个方法的返回值就相当于是之前的函数视图一样。也必须返回`Response`或者子类的对象，或者是字符串，或者是元组。
3. 必须通过`app.add_url_rule(rule,endpoint,view_func)`来做url与视图的映射。`view_func`这个参数，需要使用类视图下的`as_view`类方法类转换：`ListView.as_view('list')`。
4. 如果指定了`endpoint`，那么在使用`url_for`反转的时候就必须使用`endpoint`指定的那个值。如果没有指定`endpoint`，那么就可以使用`as_view(视图名字)`中指定的视图名字来作为反转。即as_view中的别名
5. 类视图有以下好处：可以继承，把一些共性的东西抽取出来放到父视图中，子视图直接拿来用就可以了。但是也不是说所有的视图都要使用类视图，这个要根据情况而定。

```python
#类视图会执行dispatch_request方法，所以只需要实现get_data方法即可，会调用父类的dispatch_request
class JSONView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())

class ListView(JSONView):
    def get_data(self):
        return {"username":'zhiliao','password':'111111'}
```

### 基于请求方法的类视图：
1. 基于方法的类视图，是根据请求的`method`来执行不同的方法的。如果用户是发送的`get`请求，那么将会执行这个类的`get`方法。如果用户发送的是`post`请求，那么将会执行这个类的`post`方法。其他的method类似，比如`delete`、`put`。
2. 这种方式，可以让代码更加简洁。所有和`get`请求相关的代码都放在`get`方法中，所有和`post`请求相关的代码都放在`post`方法中。就不需要跟之前的函数一样，通过`request.method == 'GET'`。

```python
class LoginView(views.MethodView):
    def __render(self,error=None):
        return render_template('login.html',error=error)

    def get(self):
        return self.__render()

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'zhiliao' and password == '111111':
            return '登录成功'
        else:
            return self.__render(error='用户名或密码错误')
```

### 类视图中的装饰器：
1. 如果使用的是函数视图，那么自己定义的装饰器必须放在`app.route`下面。否则这个装饰器就起不到任何作用。
2. 类视图的装饰器，需要重写类视图的一个类属性`decorators`，这个类属性是一个列表或者元组都可以，里面装的就是所有的装饰器。

```python

from flask import Flask,request,views
from functools import wraps

app = Flask(__name__)

def login_required(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        # /settings/?username=xxx
        username = request.args.get('username')
        if username and username == 'zhiliao':
            return func(*args,**kwargs)
        else:
            return '请先登录'
    return wrapper

@app.route('/settings/')
@login_required
def settings():
    return '这是设置界面'

# login_required(app.route('/settings/')(settings))
# app.route('/settings/')(login_required(settings))

class ProfileView(views.View):
    decorators = [login_required]
    def dispatch_request(self):
        return '这是个人中心界面'

app.add_url_rule('/profile/',view_func=ProfileView.as_view('profile'))

if __name__ == '__main__':
    app.run(debug=True)

```

## blueprint
1. 蓝图的作用就是让我们的Flask项目更加模块化，结构更加清晰。可以将相同模块的视图函数放在同一个蓝图下，同一个文件中，方便管理。
2. 基本语法：
    * 在蓝图文件中导入Blueprint：

```python
        from flask import Blueprint
        user_bp = Blueprint('user',__name__)
        ```。
    * 在主app文件中注册蓝图：
        ```python
        from blueprints.user import user_bp
        app.regist_blueprint(user_bp)
        ```
 
 user.py
 
```python

from flask import Blueprint

user_bp = Blueprint('user',__name__,url_prefix='/user')

# 个人中的url与视图函数
@user_bp.route('/profile/')
def profile():
    return '个人中心页面'

@user_bp.route('/settings/')
def settings():
    return '个人设置页面'
```

manage.py

```python
from blueprints.user import user_bp
app.regist_blueprint(user_bp)
```
3. 如果想要某个蓝图下的所有url都有一个url前缀，那么可以在定义蓝图的时候，指定url_prefix参数：
    ```python
    user_bp = Blueprint('user',__name__,url_prefix='/user/')
    ```
    在定义url_prefix的时候，要注意后面的斜杠，如果给了，那么以后在定义url与视图函数的时候，就不要再在url前面加斜杠了。

4. 蓝图模版文件的查找：
* 如果项目中的templates文件夹中有相应的模版文件，就直接使用了。
* 如果项目中的templates文件夹中没有相应的模版文件，那么就到在定义蓝图的时候指定的路径中寻找。并且蓝图中指定的路径可以为相对路径，相对的是当前这个蓝图文件所在的目录。比如：
```python
news_bp = Blueprint('news',__name__,url_prefix='/news',template_folder='zhiliao')
```
因为这个蓝图文件是在blueprints/news.py，那么就会到blueprints这个文件夹下的zhiliao文件夹中寻找模版文件。

5. 蓝图中静态文件的查找规则：
    * 在模版文件中，加载静态文件，如果使用url_for('static')，那么就只会在app指定的静态文件夹目录下查找静态文件。
    * 如果在加载静态文件的时候，指定的蓝图的名字，比如`news.static`，那么就会到这个蓝图指定的static_folder下查找静态文件。`<link rel="stylesheet" href="{{ url_for('news.static',filename='news_list.css') }}">`

6. url_for反转蓝图中的视图函数为url：
    * 如果使用蓝图，那么以后想要反转蓝图中的视图函数为url，那么就应该在使用url_for的时候指定这个蓝图。比如`news.news_list`。否则就找不到这个endpoint。在模版中的url_for同样也是要满足这个条件，就是指定蓝图的名字。
    * 即使在同一个蓝图中反转视图函数，也要指定蓝图的名字。
简单点讲，反转蓝图中的url必须要加蓝图的名字

### 蓝图实现子域名：
1. 使用蓝图技术。
2. 在创建蓝图对象的时候，需要传递一个`subdomain`参数，来指定这个子域名的前缀。例如：`cms_bp = Blueprint('cms',__name__,subdomain='cms')`。
3. 需要在主app文件中，需要配置app.config的SERVER_NAME参数。例如：
    ```python
    app.config['SERVER_NAME'] = 'jd.com:5000'
    ```
    * ip地址不能有子域名。
    * localhost也不能有子域名。
4. 在`C:\Windows\System32\drivers\etc`下，找到hosts文件，然后添加域名与本机的映射。例如：
    ```python
    127.0.0.1   jd.com
    127.0.0.1   cms.jd.com
    ```
    域名和子域名都需要做映射。

蓝图中注册的视图函数的endpoint是有蓝图名的前缀的如：web.search

## 手动将flask对象入栈
```python
from flask import flask,current_app

app = Flask(__name__)


ctx = app.app_context()
ctx.push()  # 入栈
a = current_app
d = current_app.config['DEBUG']


with app.app_context():
	a = current_app
	debug = current_app.config['DEBUG']
```

### With

```python
class A:
	def __enter__(self):
		a = 1

	def __exit__(self,exe_type,exe_value,tb):
		b = 2

with A() as obj:
	print(obj) # 此情况下，为None ,因为as 后面的结果为__enter__的返回值，因为Enter什么也没返回 


class MyResource:
	def __enter__(self):
		print('connect to resource')
		return self

	def __exit__(self, exc_type,exc_value,tb):
		if tb:
			print('process exception')
		else:
			print('no exception')
		print('close resource connection')

		# return True or False
		# 如果__exit__返回False,在它的外层代码仍会抛出异常，而如果返回True
		# 则不会再抛出异常，表示在with内部已经处理了异常

	def query(self):
		print('query data')
```
## 其他

### filter
在对字符进行拼接时 如author,publisher,price之间用/拼接，如果中间某一项为空，会导致出现//的情况
```python
intro = filter(lambda x: True if x else False, [author, publisher,price])
'/'.join(intro)
```

### 统一处理404错误
监听所有的404错误，当遇到404时就会通过下面的not_found方法来处理
```python
# web可以是蓝图，也可以是app核心对象
# 在程序的任何地方监听到404错误码就会执行
@ web.app_errorhandler(404)
def not_found(e):
    # 这里写自定义的处理
    return render_template('404.html'), 404
```

### 生成token
使用内置的方法，并放入用户的id
```python
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import TimedJSONWebSignatureSerializer as Ser

db = SQLAlchemy()


class User(db.Model):
    pass

    def generate_token(self, expiration=600):
        s = Ser(secret_key=current_app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id': self.id}).decode('utf-8')
```

### jsonify
```python
jsonify(result) ==> json.dumps(result), 200, {'content_type':'application/json'}
```

### request.args
request.args是不一个不可变字典，要将它转换成可变字典：`request.args.to_dict()`

其它参数
request.args: the key/value pairs in the URL query string
request.form: the key/value pairs in the body, from a HTML post form, or JavaScript request that isn't JSON encoded
request.files: the files in the body, which Flask keeps separate from form. HTML forms must use enctype=multipart/form-data or files will not be uploaded.
request.values: combined args and form, preferring args if keys overlap
request.json: parsed JSON data. The request must have the application/json content type, or use request.get_json(force=True) to ignore the content type.


### login_required
自定义login_required装饰器
```python
    from functools import wraps

    def login_required(fun):
        @wraps(fun)
        def decorated_view(*args, **kwargs):
            if session.get('user_id',None):
                return fun(*args, **kwargs)
            else:
                return redirect('/login/')
        return decorated_view
```


### 装饰器（中间件）
这两个装饰器类型于django中的中间件，
主要有
@app.before_request会在每个请求被创建出来的时候，执行它所装饰的函数。
@app.teardown_request，会在每个请求结束的时候执行

Flask的g对象可以为每个特定请求临时存储任何需要的数据，并且是线程安全的。请求结束的时候，这个对象会被销毁，下一个新的请求到来时，又会为它生成一个新的对象


**代码原则××
```python
if '-' in q and  len(short_q)==10 and short_q.isdigit():
    pass
优先将可能为假的放在前面，这样后面的就可能不会运算
优先将比较耗时的判断放在后面，同样耗时的操作也可能不会执行
```
