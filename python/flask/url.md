## URL与视图函数的映射：

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

## url_for

### `url_for`的基本使用：
`url_for`第一个参数，应该是视图函数的名字的字符串。后面的参数就是传递给`url`。如果传递的参数之前在`url`中已经定义了，比如Page,那么这个参数就会被当成`path`的形式给`url`。如果这个参数之前没有在`url`中定义，那么将变成查询字符串的形式放到`url`中,即`？count=2`的形式。
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

### `to_python`的作用：
这个方法的返回值，将会传递到view函数中作为参数。
比如：如果传的url中是/post/a+b/,我希望到视图函数中时已经转成a,b两个参数，就可以在to_python中做split，如下
```py
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

```py
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
5. 
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

### 视图函数中可以返回哪些值：
1. 可以返回字符串：返回的字符串其实底层将这个字符串包装成了一个`Response`对象。
2. 可以返回元组：元组的形式是(响应体,状态码,头部信息)，也不一定三个都要写，写两个也是可以的。返回的元组，其实在底层也是包装成了一个`Response`对象。
3. 可以返回`Response`及其子类。


### 实现一个自定义的`Response`对象：
1. 继承自`Response`类。
2. 实现方法`force_type(cls,rv,environ=None)`。
3. 指定`app.response_class`为你自定义的`Response`对象。
4. 如果视图函数返回的数据，不是字符串，也不是元组，也不是Response对象，那么就会将返回值传给`force_type`，然后再将`force_type`的返回值返回给前端。

```py
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

### 获取所有url
flask中所有的url都保存在url_map中，`app.url_map`即可查看所有路由

### 前端显示flash信息
在前端显示flash信息，`get_flashed_messages()`