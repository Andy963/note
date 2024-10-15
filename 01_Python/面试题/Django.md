
## django

### django 的生命周期：

```
- **请求 (Request)**：
    
    - 用户在浏览器中发出一个 HTTP 请求，例如通过访问一个 URL。
    - 请求通过网络传输到 Django 服务器。
- **WSGI/ASGI 服务器处理**：
    
    - Django 通过 WSGI (Web Server Gateway Interface) 或 ASGI (Asynchronous Server Gateway Interface) 服务器接收请求。常见的服务器是 Gunicorn、uWSGI 等。
    - WSGI/ASGI 服务器将请求转交给 Django 应用。
- **中间件 (Middleware)**：
    
    - 请求首先经过中间件层。中间件是处理请求和响应的钩子，允许你在请求到达视图之前、或者在响应发送回用户之前对其进行处理。
    - 常见的中间件包括认证、会话管理、缓存、CSRF 保护等。
- **URL 路由系统 (URL Routing)**：
    
    - Django 将请求发送到 `urls.py` 文件中的 URL 路由系统。
    - 路由系统通过 URL 模式匹配，确定哪个视图函数或类应该处理这个请求。如果找到匹配的 URL，Django 将请求传递给相应的视图；如果没有找到匹配的 URL，Django 返回一个 404 错误响应。
- **视图处理 (View Processing)**：
    
    - 视图是 Django 中处理请求的核心部分。视图可以是函数视图（function-based view，FBV）或者类视图（class-based view，CBV）。
    - 视图会执行相关的业务逻辑，例如从数据库中获取数据、验证用户输入等。
    - 视图可以返回不同的响应类型，如 HTML 模板、JSON 数据、重定向等。
- **模型和数据库交互 (Model & ORM)**：
    
    - 如果视图需要从数据库获取或保存数据，它会通过 Django 的 ORM（对象关系映射）系统与数据库进行交互。
    - ORM 会将 Python 对象和数据库表映射起来，使得查询和操作数据库变得更加直观和简单。
- **模板渲染 (Template Rendering)**：
    
    - 如果视图返回 HTML 页面，通常会使用 Django 的模板系统来渲染响应。
    - 视图将数据上下文传递给模板，模板根据上下文数据生成最终的 HTML 页面。
- **响应 (Response)**：
    
    - 视图将生成的响应返回给 Django 框架，响应可以是 HTML、JSON、XML 或文件等。
    - 在响应返回之前，响应会再次经过中间件层，允许对响应进行处理或修改。
- **发送响应给 WSGI/ASGI 服务器**：
    
    - Django 将响应发送回 WSGI/ASGI 服务器。
    - WSGI/ASGI 服务器将响应传递给客户端（通常是用户的浏览器），从而完成整个请求-响应周期。

用户请求  --->  WSGI/ASGI 服务器  --->  中间件  --->  URL 路由  --->  视图
                                                             ↓
                                                         数据库/模板
                                                             ↓
             用户响应  <---  WSGI/ASGI 服务器  <---  中间件  <---  响应

```

### django drf中视图有哪几种类型

```python
APIView, 到GenericAPIView,再到ViewSet.
```

APIView是drf中所有view的父类，本身继承于Django的View. 。最直接封装的是对request,response都进行了封装，response里面做了一些认证，权限，限流之类处理。而response返回的结果是经过系列化的json.

GenericAPIView这里都是通用的APIView,所谓通用就是常用的增删改查，也就是restframework已经帮你封装好了。比如django的GenericView封装了ListView, DetailView，CreateView, UpdateView, DeleteView等通用视图类。drf中则封装得更多。

ViewSet其实是对前面内容的更高层的封装，但我们可以看到在ViewSet类中并没有实现任何特殊的内容，它只是继承了两个类ViewSetMixin, APIView. VIewSet常常配合router使用，router可以自动将常用的 get绑定list，post绑定create这些操作完成，而不需要你在as_view中指定对应的关系了，连这个都省去了。

### django 给类视图加装饰器的方法有哪些

```python
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View

def wrapper(fn):
    def inner(request,*args,**kwargs):
        ret = fn(request)
        print('xsssss')
        return ret
    return inner

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
# @wrapper
def book_list(request):
    return HttpResponse('aaa')
```
ref： https://www.cnblogs.com/clschao/articles/10409764.html

总结：1.给整个视图函数指定装饰器，但是需要指定请求方法。2.给dispatch使用装饰器，会对所有请求方法生效。3.对某个指定请求方法使用装饰器。

### django认证的流程

中间件认证处理
视图函数中authenticate_classes中的认证类依次处理（类似责任链）
authenticate(每个认识类都有)，返回结果有三种：
- （user,auth)  --> request.user = user, request.auth = auth
- None
- AuthenticationFailed
权限检查
视图函数执行

```python
#!/usr/bin/env python
# -*- coding:utf-8 -*-
from rest_framework.authentication import BaseAuthentication
from rest_framework.authentication import get_authorization_header
from apps.api import models
from rest_framework import exceptions


class GeneralAuthentication(BaseAuthentication):
    """ 通用认证（所有页面都可以应用）
    如果用户已登录，则在request.user和request.auth中赋值；未登录则做任何操作。
    用户需要在请求头Authorization中传递token，格式如下：
        Authorization: token 401f7ac837da42b97f613d789819ff93537bee6a

    建议：配合和配置文件一起使用，未认证的用户request.user和request.auth的值为None

    REST_FRAMEWORK = {
        "UNAUTHENTICATED_USER":None,
        "UNAUTHENTICATED_TOKEN":None
    }
    """
    keyword = "token"

    def authenticate(self, request):
        auth_tuple = get_authorization_header(request).split()

        # 1.如果没有传token，则通过本次认证，进行之后的认证
        if not auth_tuple:
            return None

        # 2.如果传递token，格式不符，则通过本次认证，进行之后的认证
        if len(auth_tuple) != 2:
            return None

        # 3.如果传递了token，但token的名称不符，则通过本次认证，进行之后的认证
        if auth_tuple[0].lower() != self.keyword.lower().encode():
            return None

        # 4.对token进行认证，如果通过了则给request.user和request.auth赋值，否则返回None
        try:
            token = auth_tuple[1].decode()
            user_object = models.UserInfo.objects.get(token=token)
            return (user_object, token)
        except Exception as e:
            return None

class UserAuthentication(BaseAuthentication):
    keyword = "token"

    def authenticate(self, request):
        auth_tuple = get_authorization_header(request).split()

        if not auth_tuple:
            raise exceptions.AuthenticationFailed('认证失败')

        if len(auth_tuple) != 2:
            raise exceptions.AuthenticationFailed('认证失败')

        if auth_tuple[0].lower() != self.keyword.lower().encode():
            raise exceptions.AuthenticationFailed('认证失败')
        try:
            token = auth_tuple[1].decode()
            user_object = models.UserInfo.objects.get(token=token)
            return (user_object, token)
        except Exception as e:
            raise exceptions.AuthenticationFailed('认证失败')
```

### 什么是 RESTful API

* API与用户的通信协议，总是使用HTTPs协议。
* 域名 
    * https://api.example.com                         尽量将API部署在专用域名（会存在跨域问题）
    * https://example.org/api/                        API很简单
* 版本
    * URL，如：https://api.example.com/v1/
    * 请求头                                                  跨域时，引发发送多次请求
* 路径，视网络上任何东西都是资源，均使用名词表示（可复数）
    * https://api.example.com/v1/zoos
    * https://api.example.com/v1/animals
    * https://api.example.com/v1/employees
* method
    * GET      ：从服务器取出资源（一项或多项）
    * POST    ：在服务器新建一个资源
    * PUT      ：在服务器更新资源（客户端提供改变后的完整资源）
    * PATCH  ：在服务器更新资源（客户端提供改变的属性）
    * DELETE ：从服务器删除资源
* 过滤，通过在url上传参的形式传递搜索条件
    * https://api.example.com/v1/zoos?limit=10：指定返回记录的数量
    * https://api.example.com/v1/zoos?offset=10：指定返回记录的开始位置
    * https://api.example.com/v1/zoos?page=2&per_page=100：指定第几页，以及每页的记录数
    * https://api.example.com/v1/zoos?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序
    * https://api.example.com/v1/zoos?animal_type_id=1：指定筛选条件
* 状态码

```python
200 OK - [GET]：服务器成功返回用户请求的数据，该操作是幂等的（Idempotent）。
201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
204 NO CONTENT - [DELETE]：用户删除数据成功。
400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
500 INTERNAL SERVER ERROR - [*]：服务器发生错误，用户将无法判断发出的请求是否成功。

#更多看这里：http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
```


### django drf中序列化时外键有哪几种方式获取外键字段

PrimaryKeyRelatedField,默认行为，即显示外键对象的主键，通常是它的id
StringRelatedField: 会调用外键对象的__str__方法
```python
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()  # 使用模型的 __str__ 方法
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']

```

Nested Representation
```python
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'age']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # 嵌套序列化器
    
    class Meta:
        model = Book
        fields = ['id', 'title', 'author']
```

source:
```python
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    # 指定外键显示的字段来源
    category = serializers.CharField(source='category.name')
    tag = TagSerializer(many=True)

    class Meta:
        model = Article
        fields = "__all__"
```

```python
class ArticleSerializer(serializers.ModelSerializer):
    # 只能获取到id
    category = serializers.CharField(source='category.name')
    tag = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = "__all__"

    def get_tag(self, obj):
        return obj.tag.values('id', 'title')
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

### django 中如何在model 保存前做一定的固定操作,比如写一句日志？

```python
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


### 如何给django CBV 的函数设置添加装饰器？

```python
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

### 中间件的主要用途（应用场景）

django中中间件可以是函数，也可以是类。如果是类必须要实现的是__init__,__call__方法，其中__init__方法需要接收get_response(指向下一个中间件的处理函数即__call__，最后一个指向社图函数),而__call__中就是具体要求的逻辑，可以选择性的实现process_view(在视图之前执行),process_exception(视图异常时调用), process_template_response(响应返回之前)。
```
process_request(request)
process_view()
process_exception()

process_response()
1. 身份验证
2. 安全检查
3. 会话管理
4. 压缩响应
5. 日志记录
6. 性能监控
7. 错误处理(异常处理)
```

### uwsgi、uWSGI和WSGI的区别
[[01_Python/面试题/概念#uwsgi]]
[[01_Python/面试题/概念#uWSGI]] 
[[01_Python/面试题/概念#WSGI (Web Server Gateway Interface)]]

```
 WSGI是一种通信协议规范。uWSGI是实现了这个WSGI协议的Web服务器。uwsgi是uWSGI服务器实现的自有传输协议。

⦁ WSGI是抽象的通信规范。uWSGI是具体的软件实现。uwsgi是具体的协议实现。

⦁ WSGI规定了Web服务器和Python应用的通信方式。uWSGI除了WSGI,还实现了uwsgi、http等多种协议。uwsgi协议则专用于uWSGI服务器与其他服务器的通信。

⦁ 任何遵循WSGI规范的Python Web应用都可以在任何兼容WSGI的服务器上运行。而uwsgi协议则是uWSGI服务器特有的。

⦁ WSGI是Python特有的规范。uWSGI虽然最初是为Python设计,但现在也支持其他语言。uwsgi协议理论上可用于任何语言。

总的来说,WSGI是规范,uWSGI是实现,uwsgi是具体协议。它们在层次和用途上有所不同,但都致力于提高Python Web应用的部署和服务效率。

```

### Django的HttpRequest对象是在什么时候创建的？

```
⦁ 当一个请求到达时，WSGI服务器调用Django的application对象（通常是一个WSGIHandler实例）。
   ⦁ WSGIHandler的__call__方法被调用，它接收environ和start_response参数。
   ⦁ 在__call__方法内，会调用get_response()方法。
   ⦁ get_response()方法会创建一个WSGIRequest对象，这个对象就是我们通常所说的request。
   ⦁ WSGIRequest在初始化时使用environ来填充它的各个属性。

所以，总的来说，您的理解是正确的主要方向。请求确实经过WSGIHandler，environ确实被用来创建request对象。只是具体的创建过程是由WSGIRequest类完成的，而不是直接在WSGIHandler的__call__方法中完成。
```

### 什么是中间件并简述其作用

```
它是一个轻量、低级别的插件系统，用于在全局范围内改变Django的输入和输出。每个中间件组件都负责做一些特定的功能。

1. 请求预处理：
   ⦁ 在视图处理请求之前执行某些操作
   ⦁ 例如：添加一些通用数据到请求对象中

2. 响应后处理：
   ⦁ 在视图返回响应后修改或处理响应
   ⦁ 例如：添加额外的HTTP头

3. 异常处理：
   ⦁ 捕获处理过程中的异常并进行相应处理
   ⦁ 例如：记录错误日志或返回自定义错误页面

4. 安全相关：
   ⦁ 实现安全检查或认证
   ⦁ 例如：CSRF保护、用户认证等

5. 会话管理：
   ⦁ 处理用户会话
   ⦁ 例如：添加自定义会话处理逻辑

6. 缓存：
   ⦁ 实现缓存机制
   ⦁ 例如：对某些请求结果进行缓存

7. 压缩响应：
   ⦁ 对响应内容进行压缩以减少传输数据量

8. 日志记录：
   ⦁ 记录请求和响应的详细信息

9. 性能监控：
   ⦁ 记录请求处理时间等性能指标

10. 国际化和本地化：
    ⦁ 根据用户的语言偏好设置来处理内容

中间件的工作流程：

1. 在请求阶段，中间件按照MIDDLEWARE设置中的顺序从上到下执行。
2. 在响应阶段，中间件按照相反的顺序从下到上执行。

使用中间件的优点：

1. 可重用性：中间件可以在多个项目中重复使用。
2. 灵活性：可以轻松添加或移除中间件，而不影响其他部分的代码。
3. 全局性：中间件作用于所有的请求/响应，无需在每个视图中重复编写相同的代码。

总之，中间件是Django中一个强大的特性，它提供了一种优雅的方式来全局性地处理请求和响应，使得代码更加模块化和可维护。
```


### 列举django中间件的5个方法，以及django中间件的应用场景

```
1. process_request(self, request)
   ⦁ 在Django决定使用哪个视图之前被调用
   ⦁ 返回None或HttpResponse对象

2. process_view(self, request, view_func, view_args, view_kwargs)
   ⦁ 在Django调用视图之前被调用
   ⦁ 返回None或HttpResponse对象

3. process_template_response(self, request, response)
   ⦁ 在视图函数执行完毕后被调用
   ⦁ 必须返回一个实现了render方法的响应对象

4. process_response(self, request, response)
   ⦁ 在Django执行视图函数并生成响应之后被调用
   ⦁ 必须返回HttpResponse对象

5. process_exception(self, request, exception)
   ⦁ 当视图抛出异常时调用
   ⦁ 返回None或HttpResponse对象

Django中间件的应用场景：

1. 身份认证和授权
   ⦁ 实现用户认证，检查用户是否已登录
   ⦁ 基于用户角色或权限控制访问
   通常使用: process_request
   原因: 这个方法在视图处理之前被调用,可以早早地检查用户身份,如果未授权可以立即返回响应,避免不必要的处理。
   

2. 安全增强
   ⦁ 实现CSRF保护
   ⦁ 添加安全headers（如X-Frame-Options）
   ⦁ 实现IP黑名单/白名单
   通常使用: process_response
   原因: 安全headers通常需要添加到响应中,process_response 可以在返回响应之前修改或添加这些headers。


3. 性能优化
   ⦁ 压缩响应内容
   ⦁ 实现缓存机制
   压缩: process_response
   缓存: process_request 和 process_response
   原因: 压缩需要在响应生成后进行。而缓存可能需要在请求开始时检查缓存(process_request),在响应生成后保存缓存(process_response)。

4. 日志和监控
   ⦁ 记录请求和响应信息
   ⦁ 性能监控和统计
   通常使用: process_request 和 process_response
   原因: 可以在请求开始和结束时记录信息,从而计算处理时间等指标。

5. 跨域资源共享(CORS)
   ⦁ 添加必要的CORS headers
   通常使用: process_response
   原因: CORS headers需要添加到响应中,这在响应生成后、返回客户端前完成。

6. 会话管理
   ⦁ 自定义会话处理逻辑
   通常使用: process_request 和 process_response
   原因: 在请求开始时读取会话,在响应返回前保存会话变更。

7. 多语言支持
   ⦁ 根据用户偏好或请求头设置语言
   通常使用: process_request
   原因: 需要在视图处理之前设置语言,以便整个请求过程使用正确的语言设置。

8. URL重写或重定向
   ⦁ 实现URL重写规则
   ⦁ 处理旧URL到新URL的重定向
    通常使用: process_request
   原因: 在决定使用哪个视图之前,可以检查并修改URL或进行重定向。

9. 异常处理
   ⦁ 自定义错误页面
   ⦁ 记录异常信息
   通常使用: process_exception
   原因: 这个方法专门用于处理视图中抛出的异常。

10. 请求/响应修改
    ⦁ 修改请求或响应的内容
    ⦁ 添加自定义headers
    请求修改: process_request
    响应修改: process_response
    原因: 分别在处理开始前修改请求,在返回响应前修改响应。
```

### 简述Django对http请求的执行流程

```
在接受一个Http请求之前的准备，需要先配置Django项目，包括设置URLs、安装应用等。然后启动一个支持WSGI网关协议的服务器（如uWSGI或Gunicorn）来监听端口，等待外界的Http请求。Django自带的开发者服务器也可以用于开发环境。

当一个http请求到达服务器时，WSGI服务器会根据WSGI协议从Http请求中提取出必要的参数，组成一个字典（environ），并调用Django的application对象（通常在wsgi.py中定义）。

Django的application对象负责处理请求，其流程如下：
1. 创建请求对象（HttpRequest）
2. 应用请求中间件
3. 通过URL配置进行路由分发
4. 调用匹配的视图函数
5. 视图函数返回响应对象（HttpResponse）
6. 应用响应中间件
7. 返回最终的HttpResponse对象

在这个过程中，Django会加载配置的中间件，进行URL路由匹配，调用相应的视图函数等。最后，Django返回一个可以被浏览器解析的、符合Http协议的HttpResponse对象。

WSGI服务器接收到这个响应后，将其发送回客户端，完成整个请求-响应周期。
```

### 请简述Django下的（内建）缓存机制

```
当浏览器首次请求时,Django会处理请求并生成响应,然后将响应内容缓存到配置的存储介质中,同时设置响应头包含缓存控制信息。在后续请求中,浏览器会带上"If-Modified-Since"头部,Django接收到请求后会检查这个头部,并与缓存中内容的最后修改时间进行比较。如果缓存内容已过期,Django会重新获取并处理数据,更新缓存,然后返回新的响应;如果缓存内容未过期,Django会直接从缓存中获取数据,返回304 Not Modified响应,告诉浏览器使用本地缓存。这种机制能有效减少服务器负载,提高响应速度,同时确保客户端获取最新数据。
```

### 什么是ASGI，简述WSGI和ASGI的关系与区别

```
1. ASGI 是 WSGI 的精神继承者，旨在解决 WSGI 的一些限制。
2. ASGI 保留了 WSGI 的许多设计理念，但进行了扩展以支持异步操作和更多协议。

WSGI 和 ASGI 的主要区别：

1. 同步 vs 异步：
   ⦁ WSGI 是同步的，一次只能处理一个请求。
   ⦁ ASGI 是异步的，可以同时处理多个请求，提高并发性能。

2. 协议支持：
   ⦁ WSGI 主要支持 HTTP 协议。
   ⦁ ASGI 支持多种协议，包括 HTTP、WebSocket、HTTP/2 等。

3. 性能：
   ⦁ ASGI 通常在处理大量并发连接时表现更好，特别是对于长连接和实时应用。
   ⦁ WSGI 在处理简单的 HTTP 请求时可能更轻量级。

4. 编程模型：
   ⦁ WSGI 使用同步编程模型，更简单直观。
   ⦁ ASGI 使用异步编程模型，需要使用 async/await 语法。

5. 兼容性：
   ⦁ 许多现有的 WSGI 应用可以在 ASGI 服务器上运行（通过适配器）。
   ⦁ ASGI 应用通常不能直接在 WSGI 服务器上运行。

6. 生态系统：
   ⦁ WSGI 有更成熟的生态系统，许多传统 Web 框架都基于 WSGI。
   ⦁ ASGI 生态系统正在快速发展，新的异步框架和工具不断涌现。

7. 使用场景：
   ⦁ WSGI 适合传统的 Web 应用和 REST API。
   ⦁ ASGI 更适合需要实时功能、WebSocket 或高并发的应用。

```

### Django本身提供了runserver，为什么不能用来部署

```
Django本身提供了runserver,但它不适合用来部署生产环境。runserver是Django自带的WSGI Server,主要用于测试和开发。它以单进程方式运行,性能有限,缺乏安全性和稳定性考虑,不支持高并发,也不具备静态文件服务等生产环境所需的功能。

相比之下,uWSGI是一个功能强大的Web服务器,它实现了WSGI、uwsgi、http等多种协议。需要注意的是,uwsgi是一种通信协议,而uWSGI是实现该协议的Web服务器。uWSGI具有超快的性能、低内存占用和多app管理等优点。它支持多进程、多线程,能够更好地发挥多核优势,提升性能和并发处理能力。

在生产环境中,uWSGI通常与Nginx配合使用,形成一个强大的部署方案。这种组合能够将用户访问请求与应用程序隔离,提供更好的安全性和可靠性。uWSGI还提供了缓存、负载均衡等高级特性,使其更适合处理生产环境的复杂需求。

此外,uWSGI提供了更强大的配置选项和更可靠的进程管理,使得它在可扩展性和稳定性方面都优于runserver。值得一提的是,Gunicorn是另一个常用的WSGI服务器选择,也适用于生产环境部署。

总的来说,使用uWSGI(或类似的专业WSGI服务器)而不是runserver进行部署,可以获得更高的并发处理能力、更好的性能、更强的安全性和更灵活的配置选项,这些都是生产环境所必需的。

安全性：

1. 请求处理：
   ⦁ runserver: 所有请求都由 Django 直接处理，包括静态文件。这可能导致不必要的资源消耗和潜在的安全风险。
   ⦁ 生产环境：Nginx 可以处理静态文件请求，仅将动态请求传递给 Django，减少了暴露面。

2. 缓冲和请求大小限制：
   ⦁ runserver: 缺乏对请求大小的严格控制。
   ⦁ 生产环境：Nginx 可以设置请求大小限制，防止大量数据导致的 DoS 攻击。

3. 错误处理：
   ⦁ runserver: 可能暴露详细的错误信息。
   ⦁ 生产环境：可以配置自定义错误页面，避免泄露敏感信息。

4. 安全头部：
   ⦁ runserver: 不提供额外的安全头部。
   ⦁ 生产环境：Nginx 可以添加各种安全头部，如 X-XSS-Protection, X-Frame-Options 等。

5. SSL/TLS 配置：
   ⦁ runserver: 虽然可以配置 SSL，但选项有限。
   ⦁ 生产环境：Nginx 提供更灵活、更安全的 SSL/TLS 配置选项。

稳定性：

1. 并发处理：
   ⦁ runserver: 单线程，一次只能处理一个请求。
   ⦁ 生产环境：可以处理大量并发连接，uWSGI 可以配置多进程和多线程。

2. 资源管理：
   ⦁ runserver: 不会自动重启失败的进程。
   ⦁ 生产环境：uWSGI 可以监控并自动重启失败的工作进程。

3. 负载均衡：
   ⦁ runserver: 不支持负载均衡。
   ⦁ 生产环境：Nginx 可以实现负载均衡，分发流量到多个后端服务器。

4. 内存泄漏处理：
   ⦁ runserver: 长时间运行可能导致内存泄漏。
   ⦁ 生产环境：可以配置定期重启工作进程，避免长时间运行导致的问题。

5. 优雅关闭：
   ⦁ runserver: 关闭时可能直接中断正在处理的请求。
   ⦁ 生产环境：uWSGI 支持优雅关闭，确保正在处理的请求完成。

6. 静态文件服务：
   ⦁ runserver: 效率较低，可能影响应用性能。
   ⦁ 生产环境：Nginx 高效处理静态文件，减轻 Django 负担。

```

### urlpatterns中的name与namespace的区别

```
name:给路由起一个别名  
  
namespace:防止多个应用之间的路由重复
```


### 外键有什么用，什么时候合适使用外接，外键一定需要索引吗？

```
- 程序很难100％保证数据的完整性,而用外键即使在数据库服务器宕机或异常的时候,也能够最大限度的保证数据的一致性和完整性。
- 如果项目性能要求不高,安全要求高,建议使用外键，如果项目性能要求高,安全自己控制，不用外键，因为外键查询比较慢。
- 加入外键的主要问题就是影响性能,因此加入索引能加快关联查询的速度。

   class Book(models.Model):
       author = models.ForeignKey(Author, on_delete=models.CASCADE, db_index=True)
   
   class Book(models.Model):
       author = models.ForeignKey(Author, on_delete=models.CASCADE)

       class Meta:
           indexes = [
               models.Index(fields=['author']),
           ]
   

```

### `Primary Key`和`Unique Key`的区别

```
- Primary key与Unique Key都是唯一性约束。
- Primary key是主键，一个表只能由一个，Unique key是唯一键，一个表可以有多个唯一键字段。
- Primary key 必须不能为空，Unique Key 可为空。
```

### django中怎么写原生SQL

```
1. 使用extra
# 查询人民邮电出版社出版并且价格大于50元的书籍  
Book.objects.filter(publisher__name='人民邮电出版社').extra(where=['price>50'])

2. 使用raw
books=Book.objects.raw('select * from hello_book')    
  
for book in books:    
   print book

3. 使用游标
from django.db import connection    
cursor = connection.cursor()   
cursor.execute("insert into hello_author(name) values ('特朗普')"）  
cursor.execute("update hello_author set name='普京' WHERE name='特朗普'")    
cursor.execute("delete from hello_author where name='普京'")    
cursor.execute("select * from hello_author")    
cursor.fetchone()    
cursor.fetchall()
```


### 谈一谈你对ORM的理解
[[01_Python/面试题/概念#ORM]]

```
**ORM**是“对象-关系-映射”的简称。

ORM是MVC或者MVC框架中包括一个重要的部分，它实现了数据模型与数据库的解耦，即数据模型的设计不需要依赖于特定的数据库，通过简单的配置就可以轻松更换数据库，这极大的减轻了开发人员的工作量，不需要面对因数据库变更而导致的无效劳动。
```

### Django ORM如何取消级联

```
1. 使用 on_delete=models.DO_NOTHING

这个选项会完全取消级联操作。当关联的对象被删除时，不会对当前模型的实例做任何操作。

from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING)


2. 使用 on_delete=models.SET_NULL

这个选项会在关联对象被删除时，将外键字段设置为NULL。注意，你需要将外键字段设置为可空（null=True）。

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)


3. 使用 on_delete=models.SET_DEFAULT

这个选项会在关联对象被删除时，将外键字段设置为一个默认值。你需要指定一个默认值。

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_DEFAULT, default=1)


4. 使用 on_delete=models.SET()

这个选项允许你指定一个函数，在关联对象被删除时调用该函数来设置新的值。

def get_default_author():
    return Author.objects.get_or_create(name='Unknown')[0].id

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET(get_default_author))


5. 使用 on_delete=models.PROTECT

这个选项会阻止删除操作，如果尝试删除被引用的对象，会引发 ProtectedError。

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)


注意事项：

1. 更改 on_delete 选项可能需要数据库迁移。

2. 取消级联可能会导致数据一致性问题，请确保你的应用程序能够正确处理这些情况。

3. 如果你使用 SET_NULL 或 SET_DEFAULT，确保相关字段允许为空或有合适的默认值。

4. 在某些情况下，你可能需要手动处理关联数据的清理，以避免出现孤立数据。
```

### Django 查询集的2大特性？什么是惰性执行

```
1. 惰性执行(Lazy Evaluation)
2. 缓存机制(Caching)

惰性执行是指 Django 查询集在创建、过滤、切片等操作时不会立即执行实际的数据库查询。只有当你真正需要结果时，Django 才会访问数据库。

惰性执行的主要特点:

1. 创建查询集不会触发数据库查询。
2. 对查询集进行过滤、排序等操作也不会立即执行查询。
3. 查询集可以被重复使用，每次使用时都会重新生成 SQL。
4. 只有在实际需要结果时才执行查询，如:
   ⦁ 迭代查询集
   ⦁ 对查询集进行切片
   ⦁ 调用 len() 或 list() 等方法

5. 一旦查询执行后，结果会被缓存，后续使用相同查询集不会重复查询数据库。
惰性执行的优势:

1. 性能优化: 避免不必要的数据库查询，减少数据库负载。
2. 灵活性: 可以构建复杂的查询，而不用担心性能问题。
3. 链式操作: 可以方便地组合多个过滤条件。
示例:

# 这行代码不会执行查询
queryset = Book.objects.filter(author="John")

# 这行也不会执行查询
queryset = queryset.filter(published_date__year=2021)

# 此时才会执行实际的数据库查询
for book in queryset:
    print(book.title)


总之，惰性执行是 Django ORM 的一个重要特性，它通过延迟执行数据库查询来优化性能，同时提供了构建复杂查询的灵活性。理解并善用这一特性可以帮助开发者编写更高效的 Django 应用。
```

### Django查询集返回的列表过滤器有哪些

```
all()：返回所有数据  
filter()：返回满足条件的数据  
exclude()：返回满足条件之外的数据，相当于sql语句中where部分的not关键字  
order_by()：排序
```


### selected_related与prefetch_related有什么区别

```
在查询对象集合的时候，把指定的外键对象也一并完整查询加载，避免后续的重复查询。使用 select_related() 和 prefetch_related() 可以很好的减少数据库请求的次数，从而提高性能。

1. **select_related**适用于一对一字段（OneToOneField）和外键字段（ForeignKey）查询；
2. **prefetch_related**适用多对多字段（ManyToManyField）和一对多字段的查询。（或许你会有疑问，没有一个叫OneToManyField的东西啊。实际上 ，ForeignKey就是一个多对一的字段，而被ForeignKey关联的字段就是一对多字段了）

1. select_related:

   ⦁ 用于处理一对一(OneToOne)和多对一(ForeignKey)的关系。
   ⦁ 通过JOIN操作在单个数据库查询中获取相关对象。
   ⦁ 减少数据库查询的次数，适合于"正向"关系查询。
   ⦁ 直接将关联的对象数据加载到内存中。

   示例：
   
   # 不使用select_related
   book = Book.objects.get(id=1)
   author = book.author  # 这里会触发额外的数据库查询

   # 使用select_related
   book = Book.objects.select_related('author').get(id=1)
   author = book.author  # 不会触发额外的查询，因为author已经被预先加载
   

2. prefetch_related:

   ⦁ 用于处理多对多(ManyToMany)和一对多(反向ForeignKey)的关系。
   ⦁ 执行单独的查询来获取相关对象，然后在Python中进行连接。
   ⦁ 可以减少数据库查询的次数，适合于"反向"关系和多对多关系查询。
   ⦁ 允许对预取的对象进行过滤和自定义。

   示例：
   
   # 不使用prefetch_related
   books = Book.objects.all()
   for book in books:
       print(book.authors.all())  # 每本书都会触发一次额外的查询

   # 使用prefetch_related
   books = Book.objects.prefetch_related('authors').all()
   for book in books:
       print(book.authors.all())  # 不会触发额外的查询
   

主要区别：

1. 查询方式：
   ⦁ select_related 使用SQL的JOIN操作。
   ⦁ prefetch_related 执行单独的查询，然后在Python中进行连接。

2. 适用关系：
   ⦁ select_related 适用于一对一和多对一关系。
   ⦁ prefetch_related 适用于多对多和一对多（反向）关系。

3. 数据加载：
   ⦁ select_related 在单个查询中加载所有相关数据。
   ⦁ prefetch_related 执行额外的查询来加载相关数据。

4. 灵活性：
   ⦁ select_related 不太灵活，因为它依赖于数据库的JOIN操作。
   ⦁ prefetch_related 更灵活，允许对预取的对象进行过滤和自定义。

5. 性能影响：
   ⦁ select_related 可能会导致大量数据被一次性加载，特别是在多层级关系中。
   ⦁ prefetch_related 可能会执行多个查询，但每个查询通常更小更快。

1. select_related（使用 JOIN）：

假设我们有 Book 和 Author 两个模型，它们是多对一的关系（一本书有一个作者，一个作者可以写多本书）。

class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)


使用 select_related 的查询：

books = Book.objects.select_related('author').all()


这将生成类似下面的 SQL 查询：

SELECT book.id, book.title, author.id, author.name
FROM book
INNER JOIN author ON book.author_id = author.id;


这是一个单一的查询，通过 JOIN 操作一次性获取了书籍和作者的信息。

2. prefetch_related（单独查询）：

现在假设我们有一个多对多的关系，比如一本书可以有多个类别，一个类别可以包含多本书：

class Category(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)


使用 prefetch_related 的查询：

books = Book.objects.prefetch_related('categories').all()


这将生成两个单独的查询：

第一个查询获取所有书籍：
SELECT id, title FROM book;


第二个查询获取相关的类别：
SELECT book_categories.book_id, category.id, category.name
FROM category
INNER JOIN book_categories ON category.id = book_categories.category_id
WHERE book_categories.book_id IN (1, 2, 3, ...);


这里的 "IN (1, 2, 3, ...)" 包含了第一次查询中获取的所有书籍的 ID。

prefetch_related 的"单独查询"就是指它会执行额外的查询来获取相关对象，而不是在一个查询中通过 JOIN 获取所有数据。这种方法在处理多对多关系或者可能返回大量数据的查询时特别有用，因为它可以更好地控制查询的规模和复杂度。

在 Python 中，Django ORM 会自动将这两个查询的结果组合在一起，使得你可以轻松地访问每本书的类别，而不会触发额外的数据库查询。
```

### Django QueryDict和dict区别

```

Django的QueryDict和Python的普通dict虽然都是字典类型的数据结构,但它们有一些重要的区别:

1. 多值支持:

   ⦁ QueryDict可以存储同一个key对应多个value。
   ⦁ 普通dict一个key只能对应一个value。

2. 不可变性:

   ⦁ QueryDict默认是不可变的(immutable)。
   ⦁ 普通dict是可变的(mutable)。

3. 获取值的方法:

   ⦁ QueryDict使用get()方法获取单个值,getlist()获取多个值。
   ⦁ 普通dict只用get()或[]来获取值。

4. 创建方式:

   ⦁ QueryDict通常由Django自动创建(如request.GET, request.POST)。
   ⦁ 普通dict由Python直接创建。

5. 特殊方法:

   ⦁ QueryDict有一些特殊方法如urlencode()。
   ⦁ 普通dict没有这些特殊方法。

6. 复制:

   ⦁ QueryDict的copy()方法返回一个可变的副本。
   ⦁ 普通dict的copy()返回一个浅拷贝。

7. 数据来源:

   ⦁ QueryDict通常用于处理HTTP请求参数。
   ⦁ 普通dict用途更加广泛。

8. 默认值行为:

   ⦁ QueryDict的get()方法在key不存在时默认返回None。
   ⦁ 普通dict的get()可以指定默认值,不指定则返回None。

9. 类型:

   ⦁ QueryDict是django.http.QueryDict类的实例。
   ⦁ 普通dict是Python内置的dict类的实例。

示例:

# QueryDict
from django.http import QueryDict
q = QueryDict('a=1&a=2&b=3')
print(q.getlist('a'))  # ['1', '2']
print(q.get('a'))      # '1'

# 普通dict
d = {'a': 1, 'b': 3}
print(d.get('a'))      # 1
print(d.get('c', 'default'))  # 'default'


了解这些区别可以帮助你在Django开发中更好地处理请求参数和其他字典类型的数据。

From claude-3-5-sonnet@20240620, input:15, output: 630
```


### Django中查询Q和F的区别

```
Q对象:
1. 用途: 用于构建复杂的查询条件,特别是涉及OR操作或者嵌套条件的查询。
2. 功能: 允许你组合多个查询条件,使用&(AND)、|(OR)、~(NOT)等操作符。
3. 使用场景: 当你需要执行复杂的过滤操作,如多条件组合查询时。
4. 示例:
   from django.db.models import Q

   # 查找名字为'John'或年龄大于30的用户
   User.objects.filter(Q(name='John') | Q(age__gt=30))
   

F对象:
1. 用途: 用于直接引用数据库字段的值,进行字段值的比较或运算。
2. 功能: 允许你在不实际获取对象的情况下,直接在数据库层面进行字段操作。
3. 使用场景: 当你需要比较同一个模型的不同字段,或者进行字段值的计算时。
4. 示例:
   from django.db.models import F

   # 查找价格大于折扣价的商品
   Product.objects.filter(price__gt=F('discounted_price'))

   # 将所有商品的价格增加10%
   Product.objects.update(price=F('price') * 1.1)
   

主要区别:
1. Q主要用于构建复杂的查询条件,而F用于引用和操作数据库字段。
2. Q对象更多地用于过滤(filter)操作,F对象既可用于过滤,也常用于更新(update)操作。
3. Q对象可以组合多个条件,F对象主要用于单个字段的操作或比较。
4. Q对象可以处理跨关系的复杂查询,F对象通常用于同一个模型内的字段操作。
```


### 如何给CBV添加装饰器

```
1. 使用method_decorator装饰器

这是最常用的方法。你可以在类上使用method_decorator来装饰特定的方法:

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class MyView(View):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

2. 在urls.py中使用

你可以在URL配置中直接应用装饰器:

from django.contrib.auth.decorators import login_required
from .views import MyView

urlpatterns = [
    path('my-view/', login_required(MyView.as_view())),
]

```

### 在视图函数中，常用的验证装饰器有哪些？

| 装饰器                   | 用途                           |
| --------------------- | ---------------------------- |
| @login_required()     | 检查用户是否通过身份验证                 |
| @group_required()     | 检查用户是否属于有权限的用户组访问            |
| @anonymous_required() | 检验用户是否已经登录                   |
| @superuser_only()     | 它只允许超级用户才能访问视图               |
| @ajax_required        | 用于检查请求是否是AJAX请求              |
| @timeit               | 用于改进某个视图的响应时间，或者只想知道运行需要多长时间 |


### 如何提高Django应用程序的性能

```
**前端优化：**

1. 减少 http 请求，减少数据库的访问量，比如使用雪碧图。
2. 使用浏览器缓存，将一些常用的 css，js，logo 图标，这些静态资源缓存到本地浏览器，通过设置 http 头中的 cache-control 和 expires 的属性，可设定浏览器缓存，缓存时间可以自定义。
3. 对 html，css，javascript 文件进行压缩，减少网络的通信量。

**后端优化：**

1. 合理的使用缓存技术，对一些常用到的动态数据，比如首页做一个缓存，或者某些常用的数据做个缓存，设置一定得过期时间，这样减少了对数据库的压力，提升网站性能。
2. 使用 celery 消息队列，将耗时的操作扔到队列里，让 worker 去监听队列里的任务，实现异步操作，比如发邮件，发短信。
3. 就是代码上的一些优化，补充：nginx 部署项目也是项目优化，可以配置合适的配置参数，提升效率，增加并发量。
4. 如果太多考虑安全因素，服务器磁盘用固态硬盘读写，远远大于机械硬盘，这个技术现在没有普及，主要是固态硬盘技术上还不是完全成熟， 相信以后会大量普及。
5. 服务器横向扩展
```


### 谈谈对Celery的理解,有哪些应用场景

```
Celery是一个用Python开发的分布式任务队列系统，基于生产者-消费者模型。它允许生产者将任务发送到消息队列，由消费者处理这些任务.

1. 简单：配置和使用相对简单。
2. 可靠：具有任务重试机制，能够处理执行失败或连接中断的情况。
3. 高性能：单进程可以每分钟处理大量任务。
4. 灵活：支持多种消息代理和结果后端，组件可扩展和自定义。
5. 实时处理：主要用于实时操作，但也支持任务调度。


1. 异步任务：当用户在网站进行某个操作需要很长时间完成时，我们可以将这种操作交给Celery执行，直接返回给用户，等到Celery执行完成以后通知用户，大大提好网站的并发以及用户的体验感。例如：发送验证邮件
2. 定时任务：向定时清除沉余数据或批量在几百台机器执行某些命令或者任务，此时Celery可以轻松搞定。
```
## DRF

### 谈谈你对restfull 规范的认识？
```
1 建议用https代替http
2 在URL中体现API,添加api标识
3 在url中体现版本
https://www.cnblog/api/v2/userinfo/
4 一般情况下对于apI接口用名词不用动词
5 如果有条件 在URL后面进行参数传递
https://www.cnblogs.com/api/v1/userinfo/?page=1&category=2
6 根据 method 不同做不同操作
get/post/put/patch/delete
7.返回状态码给用户
8.返回值 
9操作异常时返回错误信息
10 对下一个请求返回一些接口 hypermedia api
```
### 什么是接口的幂等性？
```
一个接口通过1次相同的访问，再对该接口进行N次相同的访问时，对资源不造影响就认为接口具有幂等性。'
    GET，  #第一次获取结果、第二次也是获取结果对资源都不会造成影响，幂等。
    POST， #第一次新增数据，第二次也会再次新增，非幂等。
    PUT，  #第一次更新数据，第二次不会再次更新，幂等。
    PATCH，#第一次更新数据，第二次不会再次更新，非幂等。
    DELTE，#第一次删除数据，第二次不在再删除，幂等。
```

### 为什么要使用django rest framework 框架？

```
# 在编写接口时可以不使用django rest framework框架，
# 不使用：也可以做，可以用django的CBV来实现，开发者编写的代码会更多一些。
# 使用：内部帮助我们提供了很多方便的组件，我们通过配置就可以完成相应操作，如：
    '序列化'可以做用户请求数据校验+queryset对象的序列化称为json
    '解析器'获取用户请求数据request.data，会自动根据content-type请求头的不能对数据进行解析
    '分页'将从数据库获取到的数据在页面进行分页显示。
     # 还有其他组件：
     '认证'、'权限'、'访问频率控制 
```

### django rest framework 框架中都有那些组件？
```
#- 路由，自动帮助开发者快速为一个视图创建4个url

#- 版本处理
    - 问题：版本都可以放在那里？
            - url
            - GET 
            - 请求头 
#- 认证 
    - 问题：认证流程？
#- 权限 
    - 权限是否可以放在中间件中？以及为什么？
#- 访问频率的控制
    匿名用户可以真正的防止？无法做到真正的访问频率控制，只能把小白拒之门外。
    如果要封IP，使用防火墙来做。
    登录用户可以通过用户名作为唯一标示进行控制，如果有人注册很多账号，则无法防止。
#- 视图
#- 解析器 ，根据Content-Type请求头对请求体中的数据格式进行处理。request.data 
#- 分页
#- 序列化
    - 序列化
        - source
        - 定义方法
    - 请求数据格式校验
#- 渲染器 
```

### 使用django rest framework 框架编写视图时都继承过哪些类？

```
a. 继承APIView（最原始）但定制性比较强
    这个类属于rest framework中的顶层类，内部帮助我们实现了只是基本功能：认证、权限、频率控制，
但凡是数据库、分页等操作都需要手动去完成，比较原始。
    class GenericAPIView(APIView)
    def post(...):
          pass 

b.继承GenericViewSet（ViewSetMixin，generics.GenericAPIView）
　　首先他的路由就发生变化
    如果继承它之后，路由中的as_view需要填写对应关系
　　在内部也帮助我们提供了一些方便的方法：
　　get_queryset
　　get_object
　　get_serializer
　　get_serializer_class
　　get_serializer_context
　　filter_queryset
注意：要设置queryset字段，否则会抛出断言的异常。

代码
只提供增加功能 只继承GenericViewSet

class TestView(GenericViewSet):
　　serialazer_class = xxx
　　def creat(self,*args,**kwargs):
　　　　pass  # 获取数据并对数据

c. 继承  modelviewset  --> 快速快发
　　　　-ModelViewSet(增删改查全有+数据库操作)
　　　　-mixins.CreateModelMixin（只有增）,GenericViewSet
　　　　-mixins.CreateModelMixin,DestroyModelMixin,GenericViewSet
　　对数据库和分页等操作不用我们在编写，只需要继承相关类即可。
　　
示例：只提供增加功能
class TestView(mixins.CreateModelMixin,GenericViewSet):
　　　　serializer_class = XXXXXXX
*** 
　　modelviewset --> 快速开发，复杂点的genericview、apiview
```


### 简述 django rest framework 框架的认证流程。

```
- 如何编写？写类并实现authenticators
　　请求进来认证需要编写一个类，类里面有一个authenticators方法，我们可以自定义这个方法，可以定制3类返值。
　　成功返回元组，返回none为匿名用户，抛出异常为认证失败。

源码流程：
请求进来先走dispatch方法，然后封装的request对象会执行user方法，由user触发authenticators认证流程
- 方法中可以定义三种返回值：
    - （user,auth），认证成功
    - None , 匿名用户
    - 异常 ，认证失败
- 流程：
    - dispatch 
    - 再去request中进行认证处理
```
### django rest framework 如何实现的用户访问频率控制？（匿名用户和注册用户）

```
# 对匿名用户，根据用户IP或代理IP作为标识进行记录，为每个用户在redis中建一个列表
    {
        throttle_1.1.1.1:[1526868876.497521,152686885.497521...]，
        throttle_1.1.1.2:[1526868876.497521,152686885.497521...]，
        throttle_1.1.1.3:[1526868876.497521,152686885.497521...]，
    } 
 每个用户再来访问时，需先去记录中剔除过期记录，再根据列表的长度判断是否可以继续访问。
 '如何封IP'：在防火墙中进行设置
--------------------------------------------------------------------------
# 对注册用户，根据用户名或邮箱进行判断。
    {
        throttle_xxxx1:[1526868876.497521,152686885.497521...]，
        throttle_xxxx2:[1526868876.497521,152686885.497521...]，
        throttle_xxxx3:[1526868876.497521,152686885.497521...]，
    }
每个用户再来访问时，需先去记录中剔除过期记录，再根据列表的长度判断是否可以继续访问。
\如1分钟：40次，列表长度限制在40，超过40则不可访问
```