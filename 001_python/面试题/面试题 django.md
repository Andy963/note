
## django
### 简述http 协议及常用请求头。
```
具体：
　　Http协议是建立在tcp之上的，是一种规范，它规定了发送的数据的数据格式，这个数据格式是通过\r\n 进行分割的，请求头与请求体也是通过2个\r\n分割的，响应的时候，响应头与响应体也是通过\r\n分割，并且还规定已请求已响应就会断开链接
浏览器本质,socket客户端遵循Http协议
　　HTTP协议本质：通过\r\n分割的规范+ 请求响应之后断开链接   ==  >  无状态、 短连接
常用请求头：
User-Agent，Referer，Host，Content-Type，Cookie，connection,accept,Accept-Language
```
### 列举常见的请求方法。
```
get,post, head,put,delete,option,trace,connect
```
### 列举常见的状态码。
```
200
300 301
404
500
```
### http 和https 的区别？
```
http:

超文本传输协议,明文传输
80端口
连接简单且是无状态的
https:

需要到ca申请证书,要费用
具有安全性的ssl加密传输协议
端口是443
https协议是有ssl+http协议构建的可进行加密传输,身份认证的网络协议,安全
```
### 简述websocket 协议及实现原理

```
websocket是给浏览器新建的一套（类似与http，基于Html5）协议，协议规定：（\r\n分割）浏览器和服务器连接之后不断开，以此完成：服务端向客户端主动推送消息。
全双工：可以同时双向发送数据

websocket协议额外做的一些操作
握手  ---->  连接线进行校验
加密  ----> payload_len=127/126/<=125   --> mask key 

传统socket是单相思，websocket是两情相悦
##本质
创建一个连接后不断开的socket
当连接成功之后：
    客户端（浏览器）会自动向服务端发送消息，包含： Sec-WebSocket-Key: iyRe1KMHi4S4QXzcoboMmw==
    服务端接收之后，会对于该数据进行加密：base64(sha1(swk + magic_string))
    构造响应头：
            HTTP/1.1 101 Switching Protocols\r\n
            Upgrade:websocket\r\n
            Connection: Upgrade\r\n
            Sec-WebSocket-Accept: 加密后的值\r\n
            WebSocket-Location: ws://127.0.0.1:8002\r\n\r\n        
    发给客户端（浏览器）
建立：双工通道，接下来就可以进行收发数据
    发送数据是加密，解密，根据payload_len的值进行处理
        payload_len <= 125
        payload_len == 126
        payload_len == 127
    获取内容：
        mask_key
        数据
        根据mask_key和数据进行位运算，就可以把值解析出来。

什么是魔法字符串：
客户端向服务端发送消息时，会有一个'sec-websocket-key'和'magic string'的随机字符串(魔法字符串)
#服务端接收到消息后会把他们连接成一个新的key串，进行编码、加密，确保信息的安全性
```
### django 中如何实现websocket？
```
django 中使用channels
```
### Python web 开发中, 跨域问题的解决思路是?
```
跨域指由于浏览器同源策略的限制，不同端口，域名，协议的请求会被拦截响应。
解决办法是：服务器设置响应头
jsonp是json用来跨域的一个东西。原理是通过script标签的跨域特性来绕过同源策略
```

### 请简述http 缓存机制。
```
强制缓存，服务器通知浏览器一个缓存时间，在缓存时间内，下次请求，直接用缓存，不在时间内，执行比较缓存策略。
比较缓存，将缓存信息中的Etag和Last-Modified通过请求发送给服务器，由服务器校验，返回304状态码时，浏览器直接使用缓存。
```
### 谈谈你所知道的Python web 框架。
```
django, flask,
```
### django、flask、tornado 框架的比较？
```
django 大而全，flask 小而轻
```

### 什么是wsgi？
```
web server gateway interface. web服务器与web应用程序（框架）之间通信的一种通用接口
```
### 列举django 的内置组件？
```
paginator, form, model, admin, cookie,session, contentType,middleware, signal, orm
```

### 简述django 下的(內建的)缓存机制
```
缓存是将一些常用的数据保存内存或者memcache中,在一定的时间内有人来访问这些数据时,则不再去执行数据库及渲染等操作,而是直接从内存或memcache的缓存中去取得数据,然后返回给用户.django提供了6中内存缓存机制，分别为：

开发调试缓存（为开发调试使用，实际上不使用任何操作）；

内存缓存（将缓存内容缓存到内存中）；

文件缓存（将缓存内容写到文件 ）；

数据库缓存（将缓存内容存到数据库）；

memcache缓存（包含两种模块，python-memcached或pylibmc.）。

以上缓存均提供了三种粒度的应用。
```
### django 中model 的SlugField 类型字段有什么用途
```
url中不能有空格，会被转化成%20，这样比较难看，slugfield用来保存语义化的url：全部转小写，空格转下划线
```

### django 常见的线上部署方式有哪几种？
```
Nginx + uWSGI 
Nginx + Gunicorn 
```

16 django 对数据查询结果排序怎么做, 降序怎么做？
```python
order_by() 降序在字段前面加 -
```
### django 中使用memcached 作为缓存的具体方法? 优缺点说明?
```
在settings中的CACHES中设置缓存，是Django目前原生支持的最快最有效的缓存系统。
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}
由于Memcached是基于内存的缓存，数据只存储在内存中，如果服务器死机的话数据会丢失，所以不要把内存缓存作为唯一的数据存储方法
```

### django 的orm 中如何查询 id 不等于5 的元素？
```
from django.db.models import Q
filter(~Q(id=5))
```

### 使用Django 中model filter 条件过滤方法,把下边sql 语句转化成python
```
select * from company where title like "%abc%" or mecount>999 order by createtime desc;

from django.db.models import Q
company.objects.filter(Q(title.icontains='abc')|Q(mecount__gt=999).order_by(-'createtime')
```

### 从输入http://www.baidu.com/到页面返回, 中间都是发生了什么？
```
浏览器的地址栏输入URL并按下回车。
DNS解析URL对应的IP。
HTTP发起请求。
根据IP建立TCP连接（三次握手）。
HTTP发起请求。
服务器处理请求。
浏览器接收HTTP响应。
渲染页面，构建DOM树。
关闭TCP连接（四次挥手）
```

### django 请求的生命周期？
```
1. 当用户在浏览器中输入url时,浏览器会生成请求头和请求体发给服务端
请求头和请求体中会包含浏览器的动作(action),这个动作通常为get或者post,体现在url之中.

2. url经过Django中的wsgi,再经过Django的中间件,最后url到路由映射表,在路由中一条一条进行匹配,
一旦其中一条匹配成功就执行对应的视图函数,后面的路由就不再继续匹配了.
3. 视图函数根据客户端的请求查询相应的数据.返回给Django,然后Django把客户端想要的数据做为一个字符串返回给客户端.
4. 客户端浏览器接收到返回的数据,经过渲染后显示给用户.
```

### django 中如何在model 保存前做一定的固定操作,比如写一句日志？
```
利用Django的Model的Signal Dispatcher,通过django.db.models.signals.pre_save()方法，在事件发生前，发射触发信号，这一切都被调度中的receiver方法深藏功与名的保存了。
信号的处理一般都写在Model中，举个例子
import logging
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
class Order(models.Model):
    logger = logging.getLogger(__name__)

    @receiver(pre_save, sender=Order)
    def pre_save_handler(sender, **kwargs):
     logger.debug("{},{}".format(sender, **kwargs))
```

### 简述django 中间件及其应用场景？
```
Django项目中默认启用了csrf保护,每次请求时通过CSRF中间件检查请求中是否有正确token值
当用户在页面上发送请求时，通过自定义的认证中间件，判断用户是否已经登陆，未登陆就去登陆。
当有用户请求过来时，判断用户是否在白名单或者在黑名单里
```

### 简述django FBV 和CBV？
```
FBV—function base view 函数处理请求
CBV—class base view 类处理请求
```
### 如何给django CBV 的函数设置添加装饰器？
```
# @method_decorator(wrapper,name='get')#CBV版装饰器方式一
class BookList(View):
    @method_decorator(wrapper) #CBV版装饰器方式二
    def dispatch(self, request, *args, **kwargs):
        print('请求内容处理开始')
        res = super().dispatch(request, *args, **kwargs)
        print('处理结束')
        return res
    def get(self,request):
        print('get内容')
        # all_books = models.Book.objects.all()
        return render(request,'login.html')
    @method_decorator(wrapper) #CBV版装饰器方式三
    def post(self,request):
        print('post内容')
        return redirect(reverse('book_list'))
```
### django 如何连接多个数据库并实现读写分离
```
在settings中指定多个数据库
1 通过using指定使用哪个数据库
2在项目的app中创建db_router.py文件,并在该文件中定义一个数据库路由类,用来进行读写分离，这个类最多提供四个方法，分别是：db_for_read、db_for_write、allow_relation、allow_migrate，以下只写了三个。
class MasterSlaveDBRouter(object):
    """数据库主从读写分离路由"""
    def db_for_read(self, model, **hints):
        """读数据库"""
        return "slave"

    def db_for_write(self, model, **hints):
        """写数据库"""
        return "default"

    def allow_relation(self, obj1, obj2, **hints):
        """是否运行关联操作"""
        return True
```

### django 中的F/Q 的作用？
```
  F:主要用来获取原数据进行计算。
  Django 支持 F() 对象之间以及 F() 对象和常数之间的加减乘除和取模的操作。
  修改操作也可以使用F函数,比如将每件商品的价格都在原价格的基础上增加10
from django.db.models import F
from app01.models import Goods
 
Goods.objects.update(price=F("price")+10)  # 对于goods表中每件商品的价格都在原价格的基础上增加10元
F查询专门对对象中某列值的操作，不可使用__双下划线！

Q:用来进行复杂查询
    Q查询可以组合使用 “&”, “|” 操作符，当一个操作符是用于两个Q的对象,它产生一个新的Q对象，
　　Q对象可以用 “~” 操作符放在前面表示否定，也可允许否定与不否定形式的组合。
　　Q对象可以与关键字参数查询一起使用，不过一定要把Q对象放在关键字参数查询的前面。

  Q(条件1) | Q(条件2) 或
  Q(条件1) & Q(条件2) 且
  Q(条件1) & ~Q(条件2) 非
```
### django 中如何执行原生SQL？
```
在Django中使用原生Sql主要有以下几种方式:
extra:结果集修改器，一种提供额外查询参数的机制(依赖model)
raw:执行原始sql并返回模型实例(依赖model)
直接执行自定义sql(不依赖model)
```

### only 和defer 的区别？
```
1.只取id/name/age字段
models.User.objects.all().only("id", "name", "age")

2.除了name字段
models.User.objects.all().defer("name")
```

### selectrelated 和prefetchrelated 的区别？
```
# 他俩都用于连表查询，减少SQL查询次数
select_related
select_related主要针一对一和多对一关系进行优化，通过多表join关联查询，一次性获得所有数据，存放在内存中，但如果关联的表太多，会严重影响数据库性能。
def index(request):
    obj = Book.objects.all().select_related("publisher")
    return render(request, "index.html", locals())
prefetch_related
prefetch_related是通过分表，先获取各个表的数据，存放在内存中，然后通过Python处理他们之间的关联。
def index(request):
    obj = Book.objects.all().prefetch_related("publisher")
    return render(request, "index.html", locals())
```
### django 中filter 和exclude 的区别
```
  def filter(self, *args, **kwargs)
      # 条件查询(符合条件)
       # 查出符合条件
      # 条件可以是：参数，字典，Q

  def exclude(self, *args, **kwargs)
      # 条件查询(排除条件)
      # 排除不想要的
      # 条件可以是：参数，字典，Q
```

### django 中values 和values_list 的区别？
```
values 字典列表,ValuesQuerySet查询集
<QuerySet [{'id': 2, 'name': '作者2', 'age': 24}, {'id': 3, 'name': '作者3', 'age': 35}]>

values_list 返回元祖列表,字段值
<QuerySet [(2, '作者2', 24), (3, '作者3', 35)]>
```
### 如何使用django orm 批量创建数据？
```
def bulk_create(self, objs, batch_size=None):
    # 批量插入
    # batch_size表示一次插入的个数
    objs = [
        models.DDD(name='r11'),
        models.DDD(name='r22')
    ]
    models.DDD.objects.bulk_create(objs, 10)
    
objs_list = []
for i in range(100):
    obj = People('name%s'%i,18)  #models里面的People表
    objs_list.append(obj)  #添加对象到列表

People.objects.bulk_create(objs_list,100)  #更新操作
```
### django 的Form 和ModeForm 的作用？
```
 - 作用：
      - 对用户请求数据格式进行校验
      - 自动生成HTML标签
  - 区别：
      - Form，字段需要自己手写。
          class Form(Form):
              xx = fields.CharField(.)
              xx = fields.CharField(.)
              xx = fields.CharField(.)
              xx = fields.CharField(.)
      - ModelForm，可以通过Meta进行定义
          class MForm(ModelForm):
              class Meta:
                  fields = "__all__"
                  model = UserInfo
  - 应用：只要是客户端向服务端发送表单数据时，都可以进行使用，如：用户登录注册
```
### django 的Form 组件中，如果字段中包含choices 参数，请使用两种方式实现数据源实时更新。
```
方式一:重写构造方法，在构造方法中重新去数据库获取值
  class UserForm(Form):
      name = fields.CharField(label='用户名',max_length=32)
      email = fields.EmailField(label='邮箱')
      ut_id = fields.ChoiceField(
          # choices=[(1,'普通用户'),(2,'IP用户')]
          choices=[]
      )

      def __init__(self,*args,**kwargs):
          super(UserForm,self).__init__(*args,**kwargs)

          self.fields['ut_id'].choices = models.UserType.objects.all().values_list('id','title')

方式二: ModelChoiceField字段,指定queryset
  from django.forms import Form
  from django.forms import fields
  from django.forms.models import ModelChoiceField
  class UserForm(Form):
      name = fields.CharField(label='用户名',max_length=32)
      email = fields.EmailField(label='邮箱')
      ut_id = ModelChoiceField(queryset=models.UserType.objects.all())

  依赖：
      class UserType(models.Model):
          title = models.CharField(max_length=32)

          def __str__(self):
              return self.title
```

### django 的Model 中的ForeignKey 字段中的on_delete 参数有什么作用？
```
CASCADE：删除作者信息一并删除作者名下的所有书的信息；
PROTECT：删除作者的信息时，采取保护机制，抛出错误：即不删除Books的内容；
SET_NULL：只有当null=True才将关联的内容置空；
SET_DEFAULT：设置为默认值；
SET( )：括号里可以是函数，设置为自己定义的东西；
DO_NOTHING：字面的意思，啥也不干，你删除你的干我毛线
```
### django 中csrf 的实现机制？
```
目的：防止用户直接向服务端发起POST请求

- 用户先发送GET获取csrf token: Form表单中一个隐藏的标签 + token
- 发起POST请求时，需要携带之前发送给用户的csrf token；
- 在中间件的process_view方法中进行校验。

在html中添加{%csrf_token%}标签

第一步：django第一次响应来自某个客户端的请求时,后端随机产生一个token值，把这个token保存在SESSION状态中;同时,后端把这个token放到cookie中交给前端页面；
第二步：下次前端需要发起请求（比如发帖）的时候把这个token值加入到请求数据或者头信息中,一起传给后端；Cookies:{csrftoken:xxxxx}
第三步：后端校验前端请求带过来的token和SESSION里的token是否一致。

```
### django 如何实现websocket？
```
channels, 早期是dewebsocket
```

### 基于django 使用ajax 发送post 请求时，有哪种方法携带csrf token？
```
1.后端将csrftoken传到前端，发送post请求时携带这个值发送
data: {
        csrfmiddlewaretoken: '{{ csrf_token }}'
  },
2.获取form中隐藏标签的csrftoken值，加入到请求数据中传给后端
data: {
          csrfmiddlewaretoken:$('[name="csrfmiddlewaretoken"]').val()
     },
3 cookie中存在csrftoken,将csrftoken值放到请求头中,需要先下载jQuery-cookie
headers:{ "X-CSRFtoken":$.cookie("csrftoken")}
```
### django 的缓存能使用redis 吗？如果可以的话，如何配置？
```
准备软件：redis数据库、django-redis模块
settings
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
           "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

from django.shortcuts import render,HttpResponse
from django_redis import get_redis_connection
  
def index(request):
# 根据名字去连接池中获取连接
conn = get_redis_connection("default")
    conn.hset('n1','k1','v1') # 存数据
    return HttpResponse('...')
```
### django 路由系统中name 的作用？
```
反向解析url路径用
在模板中使用：{ % url 'home' %}
在视图中使用：reverse(“home”）
```

### django 的模板中filter、simpletag、inclusiontag 的区别？
```
filter:自定义过滤器只是带有一个或两个参数的Python函数 可以在if、for语句中使用
simpletag:和自定义filter类似，只不过接收更灵活的参数。不能在if for中使用
inclusiontag:多用于返回html代码片段，可以使用后端数据
```

### django-debug-toolbar 的作用？
```
一、查看访问的速度、数据库的行为、cache命中等信息。 
二、尤其在Mysql访问等的分析上大有用处(sql查询速度)
```
### django 中如何实现单元测试？
```
对于每一个测试方法都会将setUp()和tearDown()方法执行一遍
会单独新建一个测试数据库来进行数据库的操作方面的测试，默认在测试完成后销毁。
在测试方法中对数据库进行增删操作，最后都会被清除。也就是说，在test_add中插入的数据，在test_add测试结束后插入的数据会被清除。
django单元测试时为了模拟生产环境，会修改settings中的变量，例如, 把DEBUG变量修改为True, 把ALLOWED_HOSTS修改为[*]。
from django.test import TestCase
from app01.models import People  #导入people Model类
# Create your tests here.


#创建测试类
class PeopleTestCase(TestCase):
    def setUp(self):  #setUp 固定写法
        People.objects.create(name='name1',age=12)  #创建一条数据
    def test_people_models(self):  #函数名非固定写法
        res = People.objects.get(name='name1')  #查询数据库
        self.assertEqual(res.age,12)  #断言查询结果是否是12

执行测试
python manage.py test
```
### 解释orm 中 db first 和 code first 的含义？
```
db first: 先创建数据库，再更新表模型
code first：先写表模型，再更新数据库
```
### django 中如何根据数据库表生成model 类？
```
1、修改seting文件，在setting里面设置要连接的数据库类型和名称、地址
2、运行下面代码可以自动生成models模型文件
       - python manage.py inspectdb
3、创建一个app执行下下面代码：
       - python manage.py inspectdb > app/models.py 
```
### 使用orm 和原生sql 的优缺点？
```
SQL：
# 优点：
执行速度快
# 缺点：
编写复杂，开发效率不高
----------------------------------------------------------------
ORM：
# 优点：
让用户不再写SQL语句，提高开发效率
可以很方便地引入数据缓存之类的附加功能
# 缺点：
在处理多表联查、where条件复杂查询时，ORM的语法会变得复杂。
没有原生SQL速度快
```
### 简述MVC 和MTV
```
MVC：model、view(模块)、controller(视图)
MTV：model、tempalte、view
```
### django 的contenttype 组件的作用？
```
contenttype是django的一个组件(app)，它可以将django下所有app下的表记录下来
可以使用他再加上表中的两个字段,实现一张表和N张表动态创建FK关系。
   - 字段：表名称
   - 字段：数据行ID
应用：路飞表结构优惠券和专题课和学位课关联
```
## falsk
请手写一个flask 的 Hello World。
```py
from flask import Flask

app = Flask(__name__)

@app.route('/index', endpoint='index')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run()
```

