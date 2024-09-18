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


## 自定义URL转换器

### 自定义URL转换器的方式：
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

## url_for, to_python, to_url

### `url_for`的基本使用：
`url_for`第一个参数，应该是视图函数的名字的字符串。后面的参数就是传递给`url`。如果传递的参数之前在`url`中已经定义了，比如Page,那么这个参数就会被当成`path`的形式给`url`。如果
这个参数之前没有在`url`中定义，那么将变成查询字符串的形式放到`url`中,即`？count=2`的形式。
```python
@app.route('/post/list/<page>/')
def my_list(page):
    return 'my list'

print(url_for('my_list',page=1,count=2))
# 构建出来的url：/my_list/1/?count=2
```

### 为什么需要`url_for`：
1. 将来如果修改了`URL`，但没有修改该URL对应的函数名，就不用到处去替换URL了。
2. `url_for`会自动的处理那些特殊的字符，不需要手动去处理。
    ```python
    url = url_for('login',next='/')
    # 会自动的将/编码，不需要手动去处理。
    # url=/login/?next=%2F
    ```


### `to_python`的作用：
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

### `to_url`的作用：
这个方法的返回值，将会在调用url_for函数的时候生成符合要求的URL形式。
比如：我在传入参数时是['a','b'],我希望在url中是/post/a+b/的形式，那么在to_url中对它进行拼接，上面代码中value即传进来的列表['a','b'],然后通过join来处理。

## redirect
重定向分为永久性重定向和暂时性重定向，在页面上体现的操作就是浏览器会从一个页面自动跳转到另外一个页面。比如用户访问了一个需要权限的页面，但是该用户当前并没有登录，因此我们应该给他重定向到登录页面。

* 永久性重定向：`http`的状态码是`301`，多用于旧网址被废弃了要转到一个新的网址确保用户的访问，最经典的就是京东网站，你输入`www.jingdong.com`的时候，会被重定向到`www.jd.com`，因为`jingdong.com`这个网址已经被废弃了，被改成`jd.com`，所以这种情况下应该用永久重定向。

* 暂时性重定向：`http`的状态码是`302`，表示页面的暂时性跳转。比如访问一个需要权限的网址，如果当前用户没有登录，应该重定向到登录页面，这种情况下，应该用暂时性重定向。

```python

from flask import Flask,request,redirect,url_for

app = Flask(__name__)

@app.route('/login/')
def login():
    return '这是登录页面'

@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '个人中心页面'
    else:
        # redirect 重定向
        return redirect(url_for('login'))
```

### `GET`请求和`POST`请求：
在网络请求中有许多请求方式，比如：GET、POST、DELETE、PUT请求等。那么最常用的就是`GET`和`POST`请求了。
1. `GET`请求：只会在服务器上获取资源，不会更改服务器的状态。这种请求方式推荐使用`GET`请求。
2. `POST`请求：会给服务器提交一些数据或者文件。一般POST请求是会对服务器的状态产生影响，那么这种请求推荐使用POST请求。
3. 关于参数传递：
    * `GET`请求：把参数放到`url`中，通过`?xx=xxx`的形式传递的。因为会把参数放到url中，所以如果视力好，一眼就能看到你传递给服务器的参数。这样不太安全。
    * `POST`请求：把参数放到`Form Data`中。会把参数放到`Form Data`中，避免了被偷瞄的风险，但是如果别人想要偷看你的密码，那么其实可以通过抓包的形式。因为POST请求可以提交一些数据给服务器，比如可以发送文件，那么这就增加了很大的风险。所以POST请求，对于那些有经验的黑客来讲，其实是更不安全的。

4. 在`Flask`中，`route`方法，默认将只能使用`GET`的方式请求这个url，如果想要设置自己的请求方式，那么应该传递一个`methods`参数。

## 其它
### 在局域网中让其他电脑访问我的网站：
如果想在同一个局域网下的其他电脑访问自己电脑上的Flask网站，
那么可以设置`host='0.0.0.0'`才能访问得到。

 指定端口号：
Flask项目，默认使用`5000`端口。如果想更换端口，那么可以设置`port=9000`。

### url唯一：
在定义url的时候，一定要记得在最后加一个斜杠。
1. 如果不加斜杠，那么在浏览器中访问这个url的时候，如果最后加了斜杠，那么就访问不到。这样用户体验不太好。
2. 搜索引擎会将不加斜杠的和加斜杠的视为两个不同的url。而其实加和不加斜杠的都是同一个url，那么就会给搜索引擎造成一个误解。加了斜杠，就不会出现没有斜杠的情况。

对于app.route('/hello/'),如果不带反斜线，flask为了兼容会让浏览器重定向到带反斜线的url.


### 获取所有url
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


这个简化的实现展示了 Flask 如何在 session 中存储和检索 flash messages。实际的 Flask 实现更加复杂和健壮，但基本原理是相似的。

总之，flash messages 只能获取一次的机制主要依赖于 get_flashed_messages() 函数在读取消息后立即从 session 中删除这些消息，结合 Flask 的请求-响应周期和 session 管理，实现了这种一次性的行为。

From claude-3-5-sonnet@20240620, input:29, output: 837
```


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

### template_folder
1. 在渲染模版的时候，默认会从项目根目录下的`templates`目录下查找模版。
2. 如果不想把模版文件放在`templates`目录下，那么可以在`Flask`初始化的时候指定`template_folder`来指定模版的路径。

在使用`render_template`渲染模版的时候，可以传递关键字参数。以后直接在模版中使用就可以了。
 如果你的参数过多，那么可以将所有的参数放到一个字典中，然后在传这个字典参数的时候，使用两个星号，将字典打散成关键参数。


### url_for

模版中的`url_for`跟我们后台视图函数中的`url_for`   使用起来基本是一模一样的。也是传递视图函数的名字，也可以传递参数。
使用的时候，需要在`url_for`左右两边加上一个`{{ url_for('func') }}`, 
传参数：`<p><a href="{{ url_for('login',ref='/',id='1') }}">登录</a></p>`


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


### if
`if`条件判断语句必须放在`{% if statement %}`中间，并且还必须有结束的标签`{% endif %}`。和`python`中的类似，可以使用`>，<，<=，>=，==，!=`来进行判断，也可以通过`and，or，not，()`来进行逻辑合并操作。

### for
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

### 宏：
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

### include标签：
1. 这个标签相当于是直接将指定的模版中的代码复制粘贴到当前位置。
2. `include`标签，如果想要使用父模版中的变量，直接用就可以了，不需要使用`with context`。
3. `include`的路径，也是跟`import`一样，直接从`templates`根目录下去找，不要以相对路径去找。

### set/with 

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

### flash
flash 即flask中的闪现
使用：
在视图函数中调用 flash(message, category)
在模板中使用get_flashed_messages()
```jinja2

{% set message = get_flash_message() %} # 此时message变量的范围是当前block,如果又定义了另一个block，则无法使用

{% with message = get_flash_message() %}
  message 的有效范围为with语句内部
{% endwith %}
```


### 自动加载模板
`app.config['TEMPLATES_AUTO_RELOAD']=True`
