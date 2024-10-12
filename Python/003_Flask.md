## URL与视图函数的映射：

当同一视图函数添加多个路由装饰器
```python
@app.route('/')
@app.route('/index')
def home():
    pass
```
即多个路由对应同一函数
基于上面这一点可以将路由中使用默认参数
```python
@app.route('/user/<name>',defaults={'gender':None})
@app.route('/user/<name>/<gender>')
def home(name,gender):
    pass
```
### 传递参数：
传递参数的语法是：`/<参数名>/`。然后在视图函数中，也要定义同名的参数。即加了尖括号会被识别为参数，而非url字符串。

### 参数的数据类型：
1. 如果没有指定具体的数据类型，那么默认就是使用`string`数据类型。
2. `int`数据类型只能传递`int`类型。
3. `float`数据类型只能传递`float`类型。
4. `path`数据类型和`string`有点类似，都是可以接收任意的字符串，但是`path`可以接收路径，也就是说可以包含斜杠。
5. `uuid`数据类型只能接收符合`uuid`的字符串。`uuid`是一个全宇宙都唯一的字符串，一般可以用来作为表的主键。
6. `any`数据类型可以在一个`url`中指定多个路径。例如：
    ```python
    @app.route('/<any(blog,article):url_path>/<id>/')
    def detail(url_path,id):
        if url_path == 'blog':
            return '博客详情：%s' % id
        else:
            return '博客详情：%s' % id
    ```

### 接收用户传递的参数：
1. 第一种：使用path的形式（将参数嵌入到路径中），就是上面讲的。
2. 第二种：使用查询字符串的方式，就是通过`?key=value`的形式传递的。
    ```python
    @app.route('/d/')
    def d():
        wd = request.args.get('wd')
        return '您通过查询字符串的方式传递的参数是：%s' % wd
    ```
3. 如果你的这个页面的想要做`SEO`优化，就是被搜索引擎搜索到，那么推荐使用第一种形式（path的形式）。如果不在乎搜索引擎优化，那么就可以使用第二种（查询字符串的形式）。

### add_url_rule
add_url_rule(rule,endpoint=None,view_func=None)
这个方法用来添加url与视图函数的映射。如果没有填写`endpoint`，那么默认会使用`view_func`的名字作为`endpoint`。以后在使用`url_for`的时候，就要看在映射的时候有没有传递`endpoint`参数，如果传递了，那么就应该使用`endpoint`指定的字符串，如果没有传递，那么就应该使用`view_func`的名字。

### app.route装饰器：
app.route(rule,**options)
这个装饰器底层，其实也是使用`add_url_rule`来实现url与视图函数映射的。

```python
@app.route('/hello/')
def hello():
    return 'Hello world'
    
app.add_url_rule('/hello/',view_func=hello)  # 对于类视图只能使用这种方式 
```
app.config.from_object('config') 如果使用from_object,必须全部大写，否则是读取不到的。在Flask中debug的默认值为False.


### 自定义URL转换器

#### 自定义URL转换器的方式：
1. 实现一个类，继承自`BaseConverter`。
2. 在自定义的类中，重写`regex`，也就是这个变量的正则表达式。
3. 将自定义的类，映射到`app.url_map.converters`上。比如：
    ```python
    app.url_map.converters['tel'] = TelephoneConverter
    ```
实例：

```python
from flask import Flask,url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)

#一个url中，含有手机号码的变量，必须限定这个变量的字符串格式满足手机号码的格式
class TelephoneConveter(BaseConverter):
    regex = r'1[85734]\d{9}'

app.url_map.converters['tel'] = TelephoneConveter

@app.route('/telephone/<tel:my_tel>/')
def my_tel(my_tel):
    return '您的手机号码是：%s' % my_tel

if __name__ == '__main__':
    app.run(debug=True)
```

### url_for, to_python, to_url

#### `url_for`的基本使用：
`url_for`第一个参数，应该是视图函数的名字的字符串。后面的参数就是传递给`url`。如果传递的参数之前在`url`中已经定义了，比如Page,那么这个参数就会被当成`path`的形式给`url`。如果
这个参数之前没有在`url`中定义，那么将变成查询字符串的形式放到`url`中,即`？count=2`的形式。
```python
@app.route('/post/list/<page>/')
def my_list(page):
    return 'my list'

print(url_for('my_list',page=1,count=2))
# 构建出来的url：/my_list/1/?count=2
```

#### 为什么需要`url_for`：
1. 将来如果修改了`URL`，但没有修改该URL对应的函数名，就不用到处去替换URL了。
2. `url_for`会自动的处理那些特殊的字符，不需要手动去处理。
```python
    url = url_for('login',next='/')
    # 会自动的将/编码，不需要手动去处理。
    # url=/login/?next=%2F

模版中的`url_for`跟我们后台视图函数中的`url_for`   使用起来基本是一模一样的。也是传递视图函数的名字，也可以传递参数。
使用的时候，需要在`url_for`左右两边加上一个`{{ url_for('func') }}`, 
传参数：`<p><a href="{{ url_for('login',ref='/',id='1') }}">登录</a></p>`
```

#### `to_python`的作用：
这个方法的返回值，将会传递到view函数中作为参数。
比如：如果传的url中是/post/a+b/,我希望到视图函数中时已经转成a,b两个参数，就可以在to_python中做split，如下

```python
from flask import Flask,url_for
from werkzeug.routing import BaseConverter

# 用户在访问/posts/a+b/
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return "+".join(value)
        # return "hello"
app.url_map.converters['list'] = ListConverter
def posts(boards):
    print(boards)
    return "您提交的板块是：%s" % boards
```

#### `to_url`的作用：
这个方法的返回值，将会在调用url_for函数的时候生成符合要求的URL形式。
比如：我在传入参数时是['a','b'],我希望在url中是/post/a+b/的形式，那么在to_url中对它进行拼接，上面代码中value即传进来的列表['a','b'],然后通过join来处理。


### `GET`请求和`POST`请求：
在网络请求中有许多请求方式，比如：GET、POST、DELETE、PUT请求等。那么最常用的就是`GET`和`POST`请求了。
1. `GET`请求：只会在服务器上获取资源，不会更改服务器的状态。这种请求方式推荐使用`GET`请求。
2. `POST`请求：会给服务器提交一些数据或者文件。一般POST请求是会对服务器的状态产生影响，那么这种请求推荐使用POST请求。
3. 关于参数传递：
    * `GET`请求：把参数放到`url`中，通过`?xx=xxx`的形式传递的。因为会把参数放到url中，所以如果视力好，一眼就能看到你传递给服务器的参数。这样不太安全。
    * `POST`请求：把参数放到`Form Data`中。会把参数放到`Form Data`中，避免了被偷瞄的风险，但是如果别人想要偷看你的密码，那么其实可以通过抓包的形式。因为POST请求可以提交一些数据给服务器，比如可以发送文件，那么这就增加了很大的风险。所以POST请求，对于那些有经验的黑客来讲，其实是更不安全的。

4. 在`Flask`中，`route`方法，默认将只能使用`GET`的方式请求这个url，如果想要设置自己的请求方式，那么应该传递一个`methods`参数。

### url唯一：
在定义url的时候，一定要记得在最后加一个斜杠。
1. 如果不加斜杠，那么在浏览器中访问这个url的时候，如果最后加了斜杠，那么就访问不到。这样用户体验不太好。
2. 搜索引擎会将不加斜杠的和加斜杠的视为两个不同的url。而其实加和不加斜杠的都是同一个url，那么就会给搜索引擎造成一个误解。加了斜杠，就不会出现没有斜杠的情况。

对于app.route('/hello/'),如果不带反斜线，flask为了兼容会让浏览器重定向到带反斜线的url.

flask中所有的url都保存在url_map中，`app.url_map`即可查看所有路由

### 前端显示flash信息
在前端显示flash信息，`get_flashed_messages()`


```python
Flask 中 flash message 只能在前端获取一次的底层原理主要涉及到以下几个方面：

1. 存储机制：

Flask 使用 session 来存储 flash messages。当你调用 flash() 函数时，消息会被添加到 session 中的一个特殊键下。

2. 消息队列：

flash messages 在 session 中以队列的形式存储。每次添加新的 flash message，它会被追加到这个队列的末尾。

3. get_flashed_messages() 函数：

这个函数是获取 flash messages 的关键。它的工作原理如下：

a. 从 session 中检索所有的 flash messages。
b. 清空 session 中的 flash messages。
c. 返回检索到的消息列表。

4. 一次性读取：

由于 get_flashed_messages() 函数在读取消息后会清空 session 中的消息，所以这些消息只能被读取一次。这就是为什么 flash messages 被认为是"一次性"的。

5. 模板渲染：

通常，get_flashed_messages() 会在模板渲染时被调用。一旦模板被渲染，消息就被读取并从 session 中删除，因此在后续的请求中将无法再次访问这些消息。

6. 请求周期：

Flask 的请求-响应周期也在这个机制中起着重要作用。每个请求都有自己的 session 上下文，flash messages 的生命周期通常限于单个请求-响应周期。

7. 配置选项：

Flask 提供了一些配置选项来修改这个行为，比如 SESSION_PERMANENT 和 PERMANENT_SESSION_LIFETIME，它们可以影响 session 数据的持久性。

实现示例：

from flask import session

def flash(message, category='message'):
    flashes = session.get('_flashes', [])
    flashes.append((category, message))
    session['_flashes'] = flashes

def get_flashed_messages(with_categories=False, category_filter=[]):
    flashes = session.pop('_flashes', [])
    if category_filter:
        flashes = [f for f in flashes if f[0] in category_filter]
    if not with_categories:
        return [f[1] for f in flashes]
    return flashes

在视图函数中调用 flash(message, category)
在模板中使用get_flashed_messages()


{% set message = get_flash_message() %} # 此时message变量的范围是当前block,如果又定义了另一个block，则无法使用

{% with message = get_flash_message() %}
  message 的有效范围为with语句内部
{% endwith %}

这个简化的实现展示了 Flask 如何在 session 中存储和检索 flash messages。实际的 Flask 实现更加复杂和健壮，但基本原理是相似的。

总之，flash messages 只能获取一次的机制主要依赖于 get_flashed_messages() 函数在读取消息后立即从 session 中删除这些消息，结合 Flask 的请求-响应周期和 session 管理，实现了这种一次性的行为。

From claude-3-5-sonnet@20240620
```


## 视图函数(view)

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


#### 实现一个自定义的`Response`对象：
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

## 蓝图（blueprint）
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
* 
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

### template_folder
1. 在渲染模版的时候，默认会从项目根目录下的`templates`目录下查找模版。
2. 如果不想把模版文件放在`templates`目录下，那么可以在`Flask`初始化的时候指定`template_folder`来指定模版的路径。

在使用`render_template`渲染模版的时候，可以传递关键字参数。以后直接在模版中使用就可以了。
 如果你的参数过多，那么可以将所有的参数放到一个字典中，然后在传这个字典参数的时候，使用两个星号，将字典打散成关键参数。

### filter：本质是一个python函数
 
 什么是过滤器，语法是什么：
1. 有时候我们想要在模版中对一些变量进行处理，那么就必须需要类似于Python中的函数一样，可以将这个值传到函数中，然后做一些操作。在模版中，过滤器相当于是一个函数，把当前的变量传入到过滤器中，然后过滤器根据自己的功能，再返回相应的值，之后再将结果渲染到页面中。
2. 基本语法：`{{ variable|过滤器名字 }}`。使用管道符号`|`进行组合。

#### 常见过滤器

default 使用方式`{{ value|default('默认值') }}`。如果value这个`key`不存在，那么就会使用`default`过滤器提供的默认值。如果你想使用类似于`python`中判断一个值是否为False（例如：None、空字符串、空列表、空字典等），那么就必须要传递另外一个参数`{{ value|default('默认值',boolean=True) }}`。当指定`boolean=True`时，如果value为False则就使用默认值。
可以使用`or`来替代`default('默认值',boolean=True)`。例如：`{{ signature or '此人很懒，没有留下任何说明' }}`。

1. `safe`过滤器：可以关闭一个字符串的自动转义。
2. `escape`过滤器：对某一个字符串进行转义。
3. `autoescape`标签，可以对他里面的代码块关闭或开启自动转义。
    ```jinja2
    {% autoescape off/on %}
        ...代码块
    {% endautoescape %}
    ```
    

```Jinja2

abs(value)：返回一个数值的绝对值。示例：-1|abs
default(value,default_value,boolean=false)：如果当前变量没有值，则会使用参数中的值来代替。示例：name|default('xiaotuo')——如果name不存在，则会使用xiaotuo来替代。boolean=False默认是在只有这个变量为undefined的时候才会使用default中的值，如果想使用python的形式判断是否为false，则可以传递boolean=true。也可以使用or来替换。
escape(value)或e：转义字符，会将<、>等符号转义成HTML中的符号。示例：content|escape或content|e。
first(value)：返回一个序列的第一个元素。示例：names|first
format(value,*arags,**kwargs)：格式化字符串。比如：

{{ "%s" - "%s"|format('Hello?',"Foo!") }}
将输出：Helloo? - Foo!
last(value)：返回一个序列的最后一个元素。示例：names|last。

length(value)：返回一个序列或者字典的长度。示例：names|length。
join(value,d=u'')：将一个序列用d这个参数的值拼接成字符串。
safe(value)：如果开启了全局转义，那么safe过滤器会将变量关掉转义。示例：content_html|safe。
int(value)：将值转换为int类型。
float(value)：将值转换为float类型。
lower(value)：将字符串转换为小写。
upper(value)：将字符串转换为小写。
replace(value,old,new)： 替换将old替换为new的字符串。
truncate(value,length=255,killwords=False)：截取length长度的字符串。
striptags(value)：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格。
trim：截取字符串前面和后面的空白字符。
string(value)：将变量转换成字符串。
wordcount(s)：计算一个长字符串中单词的个数。
```

#### 自定义模版过滤器：
过滤器本质上就是一个函数。如果在模版中调用这个过滤器，那么就会将这个变量的值作为第一个参数传给过滤器这个函数，然后函数的返回值会作为这个过滤器的返回值。需要使用到一个装饰器：`@app.template_filter('cut')`

```python
@app.template_filter('cut')
def cut(value):
    value = value.replace("hello",'')
    return value
```
```html
<p>{{ article|cut }}</p>
```


#### if
`if`条件判断语句必须放在`{% if statement %}`中间，并且还必须有结束的标签`{% endif %}`。和`python`中的类似，可以使用`>，<，<=，>=，==，!=`来进行判断，也可以通过`and，or，not，()`来进行逻辑合并操作。

#### for
在`jinja2`中的`for`循环，跟`python`中的`for`循环基本上是一模一样的。也是`for...in...`的形式。并且也可以遍历所有的序列以及迭代器。但是唯一不同的是，`jinja2`中的`for`循环没有`break`和`continue`语句。

```Jinja2

<table border="1">
    <tbody>
        {% for x in range(1,10) %}
            <tr>
                {% for y in range(1,10) if y <= x %}
                    <td>{{ y }}*{{ x }}={{ x*y }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </tbody>
</table>
```

#### 宏：
模板中的宏跟python中的函数类似，可以传递参数，但是不能有返回值，可以将一些经常用到的代码片段放到宏中，然后把一些不固定的值抽取出来当成一个变量。
使用宏的时候，参数可以为默认值。相关示例代码如下：
1. 定义宏：
    ```html
    {% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{
    value }}">
    {% endmacro %}
    ```
2. 使用宏：
    ```html
    <p>{{ input('username') }}</p>
    <p>{{ input('password', type='password') }}</p>
    ```

#### 导入宏：
1. `import "宏文件的路径" as xxx`。
2. `from '宏文件的路径' import 宏的名字 [as xxx]`。
3. 宏文件路径，不要以相对路径去寻找，都要以`templates`作为绝对路径去找。
4. 如果想要在导入宏的时候，就把当前模版的一些参数传给宏所在的模版，那么就应该在导入的时候使用`with context`。示例：`from 'xxx.html' import input with context`。这样就能将当前模板中的变量经过宏渲染后再传回来，类似于django中的inclusion_tag

```jinja2

{% from "macros.html" import input as input_field %}
{% import "macros/macros.html" as macros with context %}

<table>
        <tbody>
            <tr>
                <td>用户名：</td>
                <td>{{ macros.input('username') }}</td>
            </tr>
            <tr>
                <td>密码：</td>
                <td>{{ macros.input("password",type="password") }}</td>
            </tr>
            <tr>
                <td></td>
                <td>{{ macros.input(value="提交",type="submit") }}</td>
            </tr>
        </tbody>
    </table>
```

#### include标签：
1. 这个标签相当于是直接将指定的模版中的代码复制粘贴到当前位置。
2. `include`标签，如果想要使用父模版中的变量，直接用就可以了，不需要使用`with context`。
3. `include`的路径，也是跟`import`一样，直接从`templates`根目录下去找，不要以相对路径去找。

#### set/with 

 set语句：
在模版中，可以使用`set`语句来定义变量。示例如下：
```html
{% set username='知了课堂' %}
<p>用户名：{{ username }}</p>
```
一旦定义了这个变量，那么在后面的代码中，都可以使用这个变量，就类似于Python的变量定义是一样的。

 `with`语句：
`with`语句定义的变量，只能在`with`语句块中使用，超过了这个代码块，就不能再使用了。示例代码如下：
```html
{% with classroom = 'zhiliao1班' %}
<p>班级：{{ classroom }}</p>
{% endwith %}
```
`with`语句也不一定要跟一个变量，可以定义一个空的`with`语句，以后在`with`块中通过`set`定义的变量，就只能在这个`with`块中使用了：
```html
{% with %}
    {% set classroom = 'zhiliao1班' %}
    <p>班级：{{ classroom }}</p>
{% endwith %}
```
### 静态文件：
加载静态文件使用的是`url_for`函数。然后第一个参数需要为`static`，第二个参数需要为一个关键字参数`filename='路径'`。示例：
```html
{{ url_for("static",filename='xxx') }}
```
路径查找，要以当前项目的`static`目录作为根目录。

### 模版继承

为什么需要模版继承：
模版继承可以把一些公用的代码单独抽取出来放到一个父模板中。以后子模板直接继承就可以使用了。这样可以重复性的代码，并且以后修改起来也比较方便。

#### 模版继承语法：
使用`extends`语句，来指明继承的父模板。父模板的路径，也是相对于`templates`文件夹下的绝对路径。示例代码如下：
`{% extends "base.html" %}`。

#### block语法：
一般在父模版中，定义一些公共的代码。子模板可能要根据具体的需求实现不同的代码。这时候父模版就应该有能力提供一个接口，让父模板来实现。从而实现具体业务需求的功能。
在父模板中：
```html
{% block block的名字 %}
{% endblock %}
```
在子模板中：
```html
{% block block的名字 %}
子模板中的代码
{% endblock %}
```

#### 调用父模版代码block中的代码：
默认情况下，子模板如果实现了父模版定义的block。那么子模板block中的代码就会覆盖掉父模板中的代码。如果想要在子模板中仍然保持父模板中的代码，那么可以使用`{{ super() }}`来实现。示例如下：
父模板：
```html
{% block body_block %}
        <p style="background: red;">这是父模板中的代码</p>
    {% endblock %}
```

子模板：

```html
{% block body_block %}
    {{ super() }}
    <p style="background: green;">我是子模板中的代码</p>
{% endblock %}
```

#### 调用另外一个block中的代码：
如果想要在另外一个模版中使用其他模版中的代码。那么可以通过`{{ self.其他block名字() }}`就可以了。示例代码如下：
```html
{% block title %}
    知了课堂首页
{% endblock %}

{% block body_block %}
    {{ self.title() }}
    <p style="background: green;">我是子模板中的代码</p>
{% endblock %}
```

#### 其他注意事项：
1. 子模板中的代码，第一行，应该是`extends`。
2. 子模板中，如果要实现自己的代码，应该放到block中。如果放到其他地方，那么就不会被渲染。

### 宏案例

base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static',filename='css/base.css') }}">
    <link rel="stylesheet" href="{{ url_for("static",filename='css/item.css') }}">
    <title>{% block title %}{% endblock %}</title>
    {% block head %}{% endblock %}
</head>
<body>
    <div class="container">
        <div class="search-group">
            <input type="text" class="search-input" placeholder="搜索...">
        </div>
        {% block body %}{% endblock %}
    </div>
</body>
</html>
```

index.html
```html
{% extends 'base.html' %}
{% from "macros.html" import itemGroup,listGroup %}

{% block body %}
    {{ listGroup("电影",movies,1) }}
    {{ listGroup("电视剧",tvs,2) }}
{% endblock %}
```
macro.html
```jinja2
{# itemGroup的宏 #}
{% macro itemGroup(thumbnail,title,rating) %}
    <div class="item-group">
        <img src="{{ thumbnail }}" alt="" class="thumbnail">
        <p class="item-title">{{ title }}</p>
        <p class="item-rating">
            {% set lights = ((rating|int)/2)|int %}
            {% set halfs = (rating|int)%2 %}
            {% set grays = 5 - lights - halfs %}
            {% for light in range(0,lights) %}
                <img src="{{ url_for("static",filename='images/rate_light.png') }}" alt="">
            {% endfor %}
            {% for half in range(0,halfs) %}
                <img src="{{ url_for('static',filename='images/rate_half.jpg') }}" alt="">
            {% endfor %}
            {% for gray in range(0,grays) %}
                <img src="{{ url_for('static',filename='images/rate_gray.png') }}" alt="">
            {% endfor %}
            {{ rating }}
        </p>
    </div>
{% endmacro %}


{# listGroup的宏 #}
{% macro listGroup(module_title,items,category=category) %}
    <div class="item-list-group">
        <div class="item-list-top">
            <span class="module-title">{{ module_title }}</span>
{#            /list/1/#}
{#            /list/?category=1#}
            <a href="{{ url_for("item_list",category=category) }}" class="more-btn">更多</a>
        </div>
        <div class="list-group">
            {% for item in items[0:3] %}
                {{ itemGroup(item.thumbnail,item.title,item.rating) }}
            {% endfor %}
        </div>
    </div>
{% endmacro %}
```

list.html
```html
{% extends 'base.html' %}
{% from "macros.html" import itemGroup %}

{% block body %}
    {% for item in items %}
        {{ itemGroup(item.thumbnail,item.title,item.rating) }}
    {% endfor %}
{% endblock %}
```


### 自动加载模板
`app.config['TEMPLATES_AUTO_RELOAD']=True`


## click 笔记
flask_scipt 已经快10年没有维护了，新版本migrate也已经不支持了，所以这里转换到使用click,下面是一个相对稍高级的用法，将命令直接注册到蓝图上，对于app
同理（理解blueprint和app的关系）

```python

@user_bp.cli.command('create_user')
@click.argument('nick_name')
@click.argument('password')
def create_user(nick_name, password):
    """
    Func: 在蓝图上注册命令：命令行添加user
    Args: user必须的参数:nick_name, password
    Example: flask user create_user 'andy' '123456'
    Return: None
    :Author:  Andy
    :Version: 1.0
    :Created:  2022/3/26 下午9:08
    :Modified: 2022/3/26 下午9:08
    """
    user = User()
    user.nick_name = nick_name
    user.password = password
    with db.auto_commit():
        db.session.add(user)

#对应蓝图
# 因为指定了cli_group所以在命令行时要使用flask user,指定 cli_group=None 会删除嵌套并把命令直接合并到应用级别
user_bp = Blueprint('user', __name__, url_prefix='/user', cli_group='user')

```

Flask-Script的作用是可以通过命令行的形式来操作Flask。例如通过命令跑一个开发版本的服务器、设置数据库，定时任务等。要使用Flask-Script，可以通过`pip install flask-script`安装最新版本。

### 命令的添加方式：
1. 使用`manage.commad`：这个方法是用来添加那些不需要传递参数的命令。示例代码如下：
    ```python
    manager = Manager(app)
    manager.add_command("db",db_manager)

    @manager.command
    def greet():
        print('你好')
    ```
2. `使用manage.option`：这个方法是用来添加那些需要传递参数的命令。有几个参数就需要写几个`option`。示例代码如下：
    ```python
    @manager.option("-u","--username",dest="username")
    @manager.option("-e","--email",dest="email")
    def add_user(username,email):
        user = BackendUser(username=username,email=email)
        db.session.add(user)
        db.session.commit()
    ```

3. 如果有一些命令是针对某个功能的。比如有一堆命令是针对ORM与表映射的，那么可以将这些命令单独放在一个文件中方便管理。也是使用`Manager`的对象来添加。然后到主manage文件中，通过`manager.add_command`来添加。示例代码如下：
db_script.py

```python
from flask_script import Manager

db_manager = Manager()

@db_manager.command
def init():
    print('迁移仓库创建完毕！')

@db_manager.command
def revision():
    print('迁移脚本生成成功！')

@db_manager.command
def upgrade():
    print('脚本映射到数据库成功！')
```

manage.py
```python
from db_script import db_manager

manager = Manager(app)
manager.add_command("db",db_manager)
```
### 实例
```python
from flask_script import Manager
from models import app
from models import NewUser,db

manager = Manager(app)

@manager.command
def greet():
    print('hello')

@manager.option("-n", "--name", dest="name")
@manager.option('-a', '--age', dest='age')
def add_user(name,age):
    print("你要输入的用户名是：%s 年龄是 %s" %(name, age))
    user = NewUser(name=name,age=age)
    db.session.add(user)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
```
然后在shell中运行：`python manage.py add_user -n "andy" -a "18"`


## WTForms笔记：
这个库一般有两个作用。第一个就是做表单验证，把用户提交上来的数据进行验证是否合法。第二个就是做模版渲染。

### 做表单验证：
1. 自定义一个表单类，继承自wtforms.Form类。
2. 定义好需要验证的字段，字段的名字必须和模版中那些需要验证的input标签的name属性值保持一致。
3. 在需要验证的字段上，需要指定好具体的数据类型。
4. 在相关的字段上，指定验证器。
5. 以后在视图中，就只需要使用这个表单类的对象，并且把需要验证的数据，也就是request.form传给这个表单类，以后调用form.validate()方法，如果返回True，那么代表用户输入的数据都是合法的，否则代表用户输入的数据是有问题的。如果验证失败了，那么可以通过form.errors来获取具体的错误信息。
示例代码如下：
ReistForm类的代码：
```python
class RegistForm(Form):
    username = StringField(validators=[Length(min=3,max=10,message='用户名长度必须在3到10位之间')])
    password = StringField(validators=[Length(min=6,max=10)])
    password_repeat = StringField(validators=[Length(min=6,max=10),EqualTo("password")])
```
视图函数中的代码：
```python
form = RegistForm(request.form)
if form.validate():
    return "success"
else:
    print(form.errors)
    return "fail"
```


### 常用的验证器：
数据发送过来，经过表单验证，因此需要验证器来进行验证，以下对一些常用的内置验证器进行讲解：
1. Email：验证上传的数据是否为邮箱。
2. EqualTo：验证上传的数据是否和另外一个字段相等，常用的就是密码和确认密码两个字段是否相等。
3. InputRequire：原始数据的需要验证。如果不是特殊情况，应该使用InputRequired。
3. Length：长度限制，有min和max两个值进行限制。
4. NumberRange：数字的区间，有min和max两个值限制，如果处在这两个数字之间则满足。
5. Regexp：自定义正则表达式。
6. URL：必须要是URL的形式。
7. UUID：验证UUID。

### 自定义验证器：
如果想要对表单中的某个字段进行更细化的验证，那么可以针对这个字段进行单独的验证。步骤如下：
1. 定义一个方法，方法的名字规则是：`validate_字段名(self,filed)`。
2. 在方法中，使用`field.data`可以获取到这个字段的具体的值。
3. 如果数据满足条件，那么可以什么都不做。如果验证失败，那么应该抛出一个`wtforms.validators.ValidationError`的异常，并且把验证失败的信息传到这个异常类中。
示例代码：
```python
captcha = StringField(validators=[Length(4,4)])
    # 1234
    def validate_captcha(self,field):
        if field.data != '1234':
            raise ValidationError('验证码错误！')
```


## 文件上传笔记：
1. 在模版中，form表单中，需要指定`encotype='multipart/form-data'`才能上传文件。
2. 在后台如果想要获取上传的文件，那么应该使用`request.files.get('avatar')`来获取。
3. 保存文件之前，先要使用`werkzeug.utils.secure_filename`来对上传上来的文件名进行一个过滤。这样才能保证不会有安全问题。 
4. 获取到上传上来的文件后，使用`avatar.save(路径)`方法来保存文件。、
5. 从服务器上读取文件，应该定义一个url与视图函数，来获取指定的文件。在这个视图函数中，使用`send_from_directory(文件的目录,文件名)`来获取。
示例代码如下：

```python
@app.route('/upload/',methods=['GET','POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        # 获取描述信息
        desc = request.form.get("desc")
        avatar = request.files.get("avatar")
        filename = secure_filename(avatar.filename)
        avatar.save(os.path.join(UPLOAD_PATH,filename))
        print(desc)
        return '文件上传成功'

@app.route('/images/<filename>/')
def get_image(filename):
    return send_from_directory(UPLOAD_PATH,filename)
```


### 对上传文件使用表单验证：
1. 定义表单的时候，对文件的字段，需要采用`FileField`这个类型。
2. 验证器应该从`flask_wtf.file`中导入。`flask_wtf.file.FileRequired`是用来验证文件上传是否为空。`flask_wtf.file.FileAllowed`用来验证上传的文件的后缀名。
3. 在视图文件中，使用`from werkzeug.datastructures import CombinedMultiDict`来把`request.form`与`request.files`来进行合并。再传给表单来验证。
示例代码如下：
```python
from werkzeug.datastructures import CombinedMultiDict
form = UploadForm(CombinedMultiDict([request.form,request.files]))
```


## 上下文：

### Local对象：
在`Flask`中，类似于`request`的对象，其实是绑定到了一个`werkzeug.local.Local`对象上。这样，即使是同一个对象，那么在多个线程中都是隔离的。类似的对象还有`session`以及`g`对象。

### Thread Local对象：
只要满足绑定到这个对象上的属性，在每个线程中都是隔离的，那么他就叫做`Thread Local`对象。


### 应用上下文和请求上下文：
应用上下文和请求上下文都是存放到一个`LocalStack`的栈中。和应用app相关的操作就必须要用到应用上下文，比如通过`current_app`获取当前的这个`app`。和请求相关的操作就必须用到请求上下文，比如使用`url_for`反转视图函数。
1. 在视图函数中，不用担心上下文的问题。因为视图函数要执行，那么肯定是通过访问url的方式执行的，那么这种情况下，Flask底层就已经自动的帮我们把请求上下文和应用上下文都推入到了相应的栈中。
2. 如果想要在视图函数外面执行相关的操作，比如获取当前的app(current_app)，或者是反转url，那么就必须要手动推入相关的上下文：
    * 手动推入app上下文：
   
        ```python
        # 第一种方式：
        app_context = app.app_context()
        app_context.push()
        # 第二种方式：
        with app.app_context():
            print(current_app)
        ```
    * 手动推入请求上下文：推入请求上下文到栈中，会首先判断有没有应用上下文，如果没有那么就会先推入应用上下文到栈中，然后再推入请求上下文到栈中：
        ```python
        with app.test_request_context():
            print(url_for('my_list'))
        ```

### 为什么上下文需要放在栈中：
1. 应用上下文：Flask底层是基于werkzeug，werkzeug是可以包含多个app的，所以这时候用一个栈来保存。如果你在使用app1，那么app1应该是要在栈的顶部，如果用完了app1，那么app1应该从栈中删除。方便其他代码使用下面的app。
2. 如果在写测试代码，或者离线脚本的时候，我们有时候可能需要创建多个请求上下文，这时候就需要存放到一个栈中了。使用哪个请求上下文的时候，就把对应的请求上下文放到栈的顶部，用完了就要把这个请求上下文从栈中移除掉。


### 保存全局对象的g对象：
g对象是在整个Flask应用运行期间都是可以使用的。并且他也是跟request一样，是线程隔离的。这个对象是专门用来存储开发者自己定义的一些数据，方便在整个Flask程序中都可以使用。一般使用就是，将一些经常会用到的数据绑定到上面，以后就直接从g上面取就可以了，而不需要通过传参的形式，这样更加方便。


### 常用的钩子函数：
在Flask中钩子函数是使用特定的装饰器装饰的函数。为什么叫做钩子函数呢，是因为钩子函数可以在正常执行的代码中，插入一段自己想要执行的代码。那么这种函数就叫做钩子函数。（hook）
1. `before_first_request`：Flask项目第一次部署后会执行的钩子函数。
2. `before_request`：请求已经到达了Flask，但是还没有进入到具体的视图函数之前调用。一般这个就是在视图函数之前，我们可以把一些后面需要用到的数据先处理好，方便视图函数使用。
3. `context_processor`：使用这个钩子函数，必须返回一个字典。这个字典中的值在所有模版中都可以使用。这个钩子函数的函数是，如果一些在很多模版中都要用到的变量，那么就可以使用这个钩子函数来返回，而不用在每个视图函数中的`render_template`中去写，这样可以让代码更加简洁和好维护。
4. `errorhandler`：在发生一些异常的时候，比如404错误，比如500错误。那么如果想要优雅的处理这些错误，就可以使用`errorhandler`来出来。需要注意几点：
    * 在errorhandler装饰的钩子函数下，记得要返回相应的状态码。
    * 在errorhandler装饰的钩子函数中，必须要写一个参数，来接收错误的信息，如果没有参数，就会直接报错。
    * 使用`flask.abort`可以手动的抛出相应的错误，比如开发者在发现参数不正确的时候可以自己手动的抛出一个400错误。
示例代码如下：
```python
from flask import Flask,request,session,url_for,current_app,g,render_template,abort
from werkzeug.local import Local,LocalStack
from utils import log_a,log_b,log_c
from threading import local
import os

# 只要绑定在Local对象上的属性
# 在每个线程中都是隔离的
# Thread Local


# flask=werkzeug+sqlalchemy+jinja

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)

# 栈

# with app.app_context():
#     print(current_app.name)

@app.route('/')
def index():
    # print(current_app.name)
    # print(url_for('my_list'))
    username = request.args.get('username')
    g.username = username
    # log_a()
    # log_b()
    # log_c()
    print(g.user)
    if hasattr(g,'user'):
        print(g.user)
    return render_template('index.html')

@app.route('/list/')
def my_list():
    session['user_id'] = 1
    user_id = request.args.get('user_id')
    if user_id == '1':
        return 'hello'
    else:
        # 如果user_id在数据库中不存在，这时候我就让他跳转到400错误
        abort(400)
    return render_template('list.html')

with app.test_request_context():
    # 手动推入一个请求上下文到请求上下文栈中
    # 如果当前应用上下文栈中没有应用上下文
    # 那么会首先推入一个应用上下文到栈中
    print(url_for('my_list'))


# @app.before_first_request
# def first_request():
#     print('hello world')

@app.before_request
def before_request():
    # print('在视图函数执行之前执行的钩子函数')
    user_id = session.get('user_id')
    if user_id:
        g.user = 'zhiliao'

@app.context_processor
def context_processor():
    # return {"current_user":'zhiliao'}
    if hasattr(g,'user'):
        return {"current_user":g.user}
    else:
        return {}


@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'),500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'),404

@app.errorhandler(400)
def args_error(error):
    return '您的参数不正确'

if __name__ == '__main__':
    app.run(debug=True)

```


## 信号笔记：
使用信号分为3步，第一是定义一个信号，第二是监听一个信号，第三是发送一个信号。以下将对这三步进行讲解：

1. 定义信号：定义信号需要使用到blinker这个包的Namespace类来创建一个命名空间。比如定义一个在访问了某个视图函数的时候的信号。示例代码如下：
    ```python
    # Namespace的作用：为了防止多人开发的时候，信号名字冲突的问题
    from blinker import Namespace

    mysignal = Namespace()
    visit_signal = mysignal.signal('visit-signal')
    ```
2. 监听信号：监听信号使用singal对象的connect方法，在这个方法中需要传递一个函数，用来接收以后监听到这个信号该做的事情。示例代码如下：
    ```python
    def visit_func(sender,username):
        print(sender)
        print(username)
    mysignal.connect(visit_func)
    ```
3. 发送信号：发送信号使用singal对象的send方法，这个方法可以传递一些其他参数过去。示例代码如下：
  ```python
  mysignal.send(username='zhiliao')
  ```

### Flask内置的信号：
1. template_rendered：模版渲染完成后的信号。
2. before_render_template：模版渲染之前的信号。
3. request_started：模版开始渲染。
4. request_finished：模版渲染完成。
5. request_tearing_down：request对象被销毁的信号。
6. got_request_exception：视图函数发生异常的信号。一般可以监听这个信号，来记录网站异常信息。
7. appcontext_tearing_down：app上下文被销毁的信号。
8. appcontext_pushed：app上下文被推入到栈上的信号。
9. appcontext_popped：app上下文被推出栈中的信号
10. message_flashed：调用了Flask的`flashed`方法的信号。

## Flask-Restful笔记：

### 安装：
Flask-Restful需要在Flask 0.8以上的版本，在Python2.6或者Python3.3上运行。通过pip install flask-restful即可安装。

### 基本使用：
1. 从`flask_restful`中导入`Api`，来创建一个`api`对象。
2. 写一个视图函数，让他继承自`Resource`，然后在这个里面，使用你想要的请求方式来定义相应的方法，比如你想要将这个视图只能采用`post`请求，那么就定义一个`post`方法。
3. 使用`api.add_resource`来添加视图与`url`。
示例代码如下：

```python
class LoginView(Resource):
    def post(self,username=None):
        return {"username":"zhiliao"}

api.add_resource(LoginView,'/login/<username>/','/regist/')
```

注意事项：
* 如果你想返回json数据，那么就使用flask_restful，如果你是想渲染模版，那么还是采用之前的方式，就是`app.route`的方式。
* url还是跟之前的一样，可以传递参数。也跟之前的不一样，可以指定多个url。
* endpoint是用来给url_for反转url的时候指定的。如果不写endpoint，那么将会使用视图的名字的小写来作为endpoint。

#### 对类方法添加装饰器
```python
class Home(Resource):

    method_decorator = {'get':['login_required']
    def get(self):
        pass

    def post(self):
        pass
```

### 参数验证：
Flask-Restful插件提供了类似WTForms来验证提交的数据是否合法的包，叫做reqparse。以下是基本用法：
    ```python
    parser = reqparse.RequestParser()
    parser.add_argument('username',type=str,help='请输入用户名')
    args = parser.parse_args()
    ```
add_argument可以指定这个字段的名字，这个字段的数据类型等。以下将对这个方法的一些参数做详细讲解： 
1. default：默认值，如果这个参数没有值，那么将使用这个参数指定的值。 
2. required：是否必须。默认为False，如果设置为True，那么这个参数就必须提交上来。 3. type：这个参数的数据类型，如果指定，那么将使用指定的数据类型来强制转换提交上来的值。 
4. choices：选项。提交上来的值只有满足这个选项中的值才符合验证通过，否则验证不通过。 
5. help：错误信息。如果验证失败后，将会使用这个参数指定的值作为错误信息。 
6. trim：是否要去掉前后的空格。

其中的type，可以使用python自带的一些数据类型，也可以使用flask_restful.inputs下的一些特定的数据类型来强制转换。比如一些常用的： 
1. url：会判断这个参数的值是否是一个url，如果不是，那么就会抛出异常。 
2. regex：正则表达式。 
3. date：将这个字符串转换为datetime.date数据类型。如果转换不成功，则会抛出一个异常。


#### 对于定义的字段格式：以格式的字段为主
- 当格式与model对应的字段一致时，即返回预期的格式化的数据。
- 当格式比model字段多时，不存在的字段为默认值None
- 当格式比model字段少，多余的字段不会显示。

对于一个视图函数，你可以指定好一些字段用于返回。以后可以使用ORM模型或者自定义的模型的时候，他会自动的获取模型中的相应的字段，生成json数据，然后再返回给客户端。这其中需要导入flask_restful.marshal_with装饰器,如果函数使用marsha(data,fields)。并且需要写一个字典，来指示需要返回的字段，以及该字段的数据类型。示例代码如下：

```python
class ProfileView(Resource):
    resource_fields = {
        'username': fields.String,
        'age': fields.Integer,
        'school': fields.String
    }

    @marshal_with(resource_fields)
    def get(self,user_id):
        user = User.query.get(user_id)
        return user
```

#### ListField
```python
user_fields = {
    "username":fields.String,
    "age":fields.Integer,
    }
    
dest_data = {
    'status':200,
    'message':'ok',
    'data':[{'u1':1,'age':18},{'u2':2,'age':19}]
}

resource_fields = {
    "status": fields.String,
    "message":fields.String,
    "data":fields.List(fields.Nested(user_fields))
    }
```

在get方法中，返回user的时候，flask_restful会自动的读取user模型上的username以及age还有school属性。组装成一个json格式的字符串返回给客户端。

### 重命名属性：

很多时候你面向公众的字段名称是不同于内部的属性名。使用 attribute可以配置这种映射。比如现在想要返回user.school中的值，但是在返回给外面的时候，想以education返回回去，那么可以这样写：
```python
resource_fields = {
    'education': fields.String(attribute='school')
}
```

### 默认值：
在返回一些字段的时候，有时候可能没有值，那么这时候可以在指定fields的时候给定一个默认值，示例代码如下：
```python
resource_fields = {
    'age': fields.Integer(default=18)
}
```

### 复杂结构：
有时候想要在返回的数据格式中，形成比较复杂的结构。那么可以使用一些特殊的字段来实现。比如要在一个字段中放置一个列表，那么可以使用fields.List，比如在一个字段下面又是一个字典，那么可以使用fields.Nested。以下将讲解下复杂结构的用法：
```python
class ArticleView(Resource):

    resource_fields = {
        'aritlce_title':fields.String(attribute='title'),
        'content':fields.String,
        'author': fields.Nested({
            'username': fields.String,
            'email': fields.String
        }),
        'tags': fields.List(fields.Nested({
            'id': fields.Integer,
            'name': fields.String
        })),
        'read_count': fields.Integer(default=80)
    }

    @marshal_with(resource_fields)
    def get(self,article_id):
        article = Article.query.get(article_id)
        return article
```


### Flask-restful注意事项：
1. 在蓝图中，如果使用`flask-restful`，那么在创建`Api`对象的时候，就不要再使用`app`了，而是使用蓝图。
2. 如果在`flask-restful`的视图中想要返回`html`代码，或者是模版，那么就应该使用`api.representation`这个装饰器来定义一个函数，在这个函数中，应该对`html`代码进行一个封装，再返回。示例代码如下：

```python
@api.representation('text/html')
def output_html(data,code,headers):
    print(data)
    # 在representation装饰的函数中，必须返回一个Response对象
    resp = make_response(data)
    return resp

class ListView(Resource):
    def get(self):
        return render_template('index.html')
api.add_resource(ListView,'/list/',endpoint='list')
```


### 返回值的规范：
```json
{
    "code":200,
    "message": "",
    "data":{
        "name":'xxx',
        "age":'xxx'
    }
}
```

### 状态码的规范：
1. 200：成功。
2. 401：没有授权。
3. 400：参数错误。
4. 500：服务器错误。

## flask-admin
### 安装
```shell
pip install Flask-Admin
pip install flask-babelex # 国际化
```
汉化设置
```python
from flask_babelex import Babel

app = Flask(__name__)
babel = Babel(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'zh_CN'
```
### BaseView
```python
from flask_admin import Admin,BaseView, expose
flask_admin = Admin()
def create_app(object_name):
    """Create the app instance via `Factory Method`"""
    flask_admin.init_app(app)
    flask_admin.add_view(CustomView(name='Custom'))

class CustomView(BaseView):
    @expose('/')  # 类似route
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    def second_page(self):
        return self.render('admin/second_page.html')
# BaseView 子类必须定义一个路由 URL 为 / 的视图函数, 在 Admin 界面中只会默认显示该视图函数, 其他的视图函数是通过 / 中的链接来实现跳转的
```
html
```html
{% extends 'admin/master.html' %}
{% block body %}
  This is the custom view!
  <a href="{{ url_for('customview.second_page') }}">Link</a>
{% endblock %}
```

### modelView
```python
from flask.ext.admin.contrib.sqla import ModelView

class CustomModelView(ModelView):
    """View function of Flask-Admin for Models page."""
    pass

def create_app(object_name):
    flask_admin.init_app(app)
    # Register view function `CustomView` into Flask-Admin
    flask_admin.add_view(CustomView(name='Custom'))
    # Register view function `CustomModelView` into Flask-Admin
    models = [Role, Tag, Reminder, BrowseVolume]
    for model in models:
        flask_admin.add_view(
            CustomModelView(model, db.session, category='Models'))  
```

### ModelView
**常见参数**
```python
can_create
can_edit
can_delete
column_list
column_labels
form_columns
form_excluded_columns
form_args,可以指定对某个字段进行过滤
form_args=dict(
status=dict(label='状态',filters=(filter_status))) # filter_status为自定义函数，self即值。
```


## flask_migrate笔记：
在实际的开发环境中，经常会发生数据库修改的行为。一般我们修改数据库不会直接手动的去修改，而是去修改ORM对应的模型，然后再把模型映射到数据库中。这时候如果有一个工具能专门做这种事情，就显得非常有用了，而flask-migrate就是做这个事情的。flask-migrate是基于Alembic进行的一个封装，并集成到Flask中，而所有的迁移操作其实都是Alembic做的，他能跟踪模型的变化，并将变化映射到数据库中。

### 安装：
pip install flask-migrate


### 在manage.py中的代码：
```python
from flask_script import Manager
from zhiliao import app
from exts import db
from flask_migrate import Migrate,MigrateCommand

manager = Manager(app)

# 用来绑定app和db到flask_migrate的
Migrate(app,db)
# 添加Migrate的所有子命令到db下
manager.add_command("db",MigrateCommand)


if __name__ == '__main__':
    manager.run()
```

### flask_migrate常用命令：
1. 初始化一个环境：python manage.py db init
2. 自动检测模型，生成迁移脚本：python manage.py db migrate
3. 将迁移脚本映射到数据库中：python manage.py db upgrade
4. 更多命令：python manage.py db --help

### 实例

#### config.py
```python
#encoding: utf-8

DB_USERNAME = 'root'
DB_PASSWORD = 'password'
DB_HOST = '192.168.16.8'
DB_PORT = '3306'
DB_NAME = 'flask_migrate_demo'

DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % (DB_USERNAME,DB_PASSWORD,DB_HOST,DB_PORT,DB_NAME)

SQLALCHEMY_DATABASE_URI = DB_URI
```

#### exts.py
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
```

#### manage.py
```python
from flask_script import Manager
from demo import app
from exts import db
from flask_migrate import Migrate, MigrateCommand


manager = Manager(app)
Migrate(app,db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
```

#### models.py
```python

from exts import db

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=True)


if __name__ == '__main__':
    pass
```

#### demo.py
```python
from flask import Flask
from exts import db
import config

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/index')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
```


## flask-apscheduler
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


 sqlalchemy中单例模式,它是通过` try, execept` 来关闭锁的，而不是通过 `with ` 语句

```python
# sqlalchemy\util\langhelpers.py
_symbol.__name__ = "symbol"  
  
  
class symbol(object):
	symbols = {}  
	_lock = compat.threading.Lock()  
	  
	def __new__(cls, name, doc=None, canonical=None):  
	    cls._lock.acquire()  
	    try:  
	        sym = cls.symbols.get(name)  
	        if sym is None:  
	            cls.symbols[name] = sym = _symbol(name, doc, canonical)  
	        return sym  
	    finally:  
	        symbol._lock.release()
```