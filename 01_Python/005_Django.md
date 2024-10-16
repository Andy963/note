## 模型（Model）

- Fields
	- fields types
	- field options
	- relationship
- Meta
- Model attribute
- Model method
- Model instance
	- proxy model

```python

from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
```
### proxy model

```python
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    is_published = models.BooleanField(default=False)

class PublishedBook(Book):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.is_published = True
        super().save(*args, **kwargs)

# 定制管理功能
class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_active = models.BooleanField(default=True)

class ProductActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ProductActive(Product):
    class Meta:
        proxy = True
    objects = ProductActiveManager()

# active_products = ProductActive.objects.all()
```

flask 中有view model [[10_flask-sqlalchemy#view model]]


table_name 通过meta 设置，而flask 则是通过 __tablename__指定 [[005_SqlAlchemy#将ORM模型映射到数据库中：]]

```python

class MyModel(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = 'my_table'
```

### OneToOne

```python

from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

```

#### add

```python
user = User.objects.create(username='johndoe')
user_profile = UserProfile.objects.create(user=user, bio='I am John Doe', location='New York')

```
#### del

```python
user_profile = UserProfile.objects.get(user__username='johndoe')
user_profile.delete()

```
#### query

```python
user_profile = UserProfile.objects.get(user__username='johndoe')
print(user_profile.bio)

```
#### update

```python
user_profile = UserProfile.objects.get(user__username='johndoe')
user_profile.bio = 'New bio'
user_profile.save()


# 方法二
obj = MyModel.objects.get(id=1)
obj.field_name = new_value
obj.save(update_fields=['field_name'])

# 方法三
from django.db.models import F

obj = MyModel.objects.get(id=1)
obj.count = F('count') + 1
obj.save()

# 方法四
obj, created = MyModel.objects.update_or_create(
    id=1,
    defaults={'field_name': new_value}
)

MyModel.objects.filter(id=1).update(field_name=new_value)

```

update方法是针对 orm中的queryset，如果本身是单个对象（如通过get获取到的对象）则没有update方法。
### ForeignKey

#### add 

```python
from myapp.models import Book, Author

author = Author.objects.create(name='Tom')
book = Book.objects.create(name='Django', author=author)

# 添加新的Author实例，并将其关联到book上
new_author = Author.objects.create(name='Lucy')
book.author = new_author
book.save()
```

#### del

```python
book.delete()

book = Book.objects.get(id=1)
author.book_set.remove(book)

# 删除所有
author.book_set.clear()

```


#### query

```python
# 查询关联的Author实例
author = book.author

# 查询关联到某个Author实例的所有Book实例，模型名小写_set 作为反向关系的名称
books = author.book_set.all()

如果指定了related_name,related_query_name，则：
class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', related_query_name='book')

使用 author.books.all() 获取作者的所有书籍
# 这里django 默认使用模型小写即book, 所以这里通过related_query_name与默认的book一致
Author.objects.filter(book__publish_year=2020)


```

#### update

```python
new_author = Author.objects.create(name='Jerry')
book.author = new_author
book.save()

```

### ManyToMany

 添加
#### add

```python
# 假设；book, tag外键
# tag为Tag对象
book1.tags.add(tag1)
book1.tags.add([tag1,tag2])

tag3 = Tag(name='python')
tag3.book_set.add(tag3)
```

#### create
```python
book1.tag.create(name='go')
tag3.book_set.create(name='python')

```

#### set
```python
book2.tag.set([tag1])

book1.tag.all()
Book.objects.filter(tag=1)

tag1.book_set.all()
Tag.objects.filter(book__name='python')
```

#### delete
```python
book1.tag.all()
tag1.delete()
```

#### remove
```python
book1.tag.remove(tag1)
```

#### clear
clear解除关联关系
```python
tag1.book_set.clear()
```

## 模板（Template）

### 对象循环
```html
<table class="table table-bordered">
    <thead>
    <tr>
        <th>封面</th>
        <th>专场</th>
        <th>预展时间</th>
        <th>拍卖时间</th>
        <th>状态</th>
        <th>操作</th>
    </tr>
    </thead>
    <tbody>
    {% for item in queryset %}
        <tr>
            <td>
                <img style="height: 60px;" src="{{ item.cover }}">
            </td>
            <td><a href="{% url 'auction_item_list' item.id %}">{{ item.title }}</a></td>
            <td>{{ item.preview_start_time|date:"Y-m-d H:i" }}</td>
            <td>{{ item.auction_start_time|date:"Y-m-d H:i" }}</td>
            <td>{{ item.get_status_display }}</td>
            <td>
                <div class="btn-group btn-group-xs" role="group" aria-label="Small button group">
                    <a class="btn btn-default" href="{% url 'auction_edit' pk=item.id %}">编辑</a>
                    <a class="btn btn-danger"
                       onclick="removeRow(this,'{% url 'auction_delete' pk=item.id %}')">删除</a>
                </div>
            </td>
        </tr>
    {% endfor %}
    </tbody>
</table>
```

###  form循环的模板

```html
{% for field in auction_form %}
    <div class="col-sm-6">
        <div class="form-group">
            <label for="{{ field.id_for_label }}"
                   class="col-sm-3 control-label">{{ field.label }}</label>
            <div class="col-sm-9">
                {{ field }}
                <span style="color: red;">{{ field.errors.0 }}</span>
            </div>
        </div>
    </div>
{% endfor %}
```


## 视图函数（View）

```python
from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
```



```python
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def my_view(request):
    # I can assume now that only GET or POST requests make it this far
    # ...
    pass
```

### 事务(Atomic)

```python
from django.db import transaction
def perform_create(self, serializer):
    with transaction.atomic():
        coupon_obj = Coupon.objects.filter(id=serializer.validated_data['coupon'].id).select_for_update().first()
        if coupon_obj.left_count<= 0:
            raise exceptions.ValidationError('优惠券已领完')
        serializer.save(user=self.request.user)

        # 优惠分发数量加1
        coupon_obj.dispatch_count+= 1
        coupon_obj.save()
```

## 序列化器（Serializer)

#### 日期序列化器

```py
import json
from datetime import datetime
from datetime import date

#对含有日期格式数据的json数据进行转换
class JsonCustomEncoder(json.JSONEncoder):
    def default(self, field):
        if isinstance(field,datetime):
            return field.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(field,date):
            return field.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self,field)


d1 = datetime.now()

dd = json.dumps(d1,cls=JsonCustomEncoder)
print(dd)
```


### to_internal_value
to_internal_value是在外部数据传进来时进行处理的函数，通常情况下，状态码在数据库中只保存一个数字即可，在查看时我们要看后面对应的文字。对于传入的数据，我们可以 在此验证。如果是数字类型，那么它必须只能是0,1,如果是文字，那么对它进行转换，最后存入数据库的仍为数字。最后返回 data，它的处理在validate之前。
```python
STATES_CODE = (
	(0,'失败'),
	(1,'成功'),
	)

def to_internal_value(self,data):
	"""
	传入的data是个字典类型
	最后一定要返回data
	"""

	states = data.get('states')
	if states not in [i[1] for i in STATES_CODE]:
		raise ValueError('states的选项不正确')
		
	if not isinstance(states,int):
		for item in STATES_CODE:
			if item[1] == states:
				data['states'] = item[0]
	return data

```
### to_representation
to_presentation控制数据的输出时的形式，比如，字段如果设置为blank=True,null=True,最后数据可能为Null,这样就会导致输出的数据为Null,此时我们可以对它进行处理。
指定这种情况下显示的值。

```python
def to_presentation(self,instance):
	if not data['ver']:
		data['ver'] = ''

	if not data['status']:
		data['status'] = '状态未知'

	return data
```


### 选择（choice）
方法一：
```python
status = Serializer.SerializerMethodField()


def get_status(self,obj):
    if obj.status == 'd':
        return "草稿"
    elif obj.status == 'p':
        return "发布"
```
方法二：
```python
class BlogSerializer(serializers.Serializer):
    STATUS_CHOICES = {
        'd': 'draft',
        'p': 'published'
    }

    def to_representation(self, obj):
        data = super().to_representation(obj)
        data["status"] = self.STATUS_CHOICES[obj.status]
        return data
```


### 验证（validate)
我们先看看serializer中的核心参数：

> read_only：True表示不允许用户自己上传，只能用于api的输出。如果某个字段设置了read_only=True，那么就不需要进行数据验证，只会在返回时，将这个字段序列化后返回
write_only: 与read_only对应
required: 顾名思义，就是这个字段是否必填。
allow_null/allow_blank：是否允许为NULL/空 。
error_messages：出错时，信息提示,与form表单一样。
label: 字段显示设置，如 label=’验证码’
help_text: 在指定字段增加一些提示文字，这两个字段作用于api页面比较有用
style: 说明字段的类型，这样看可能比较抽象，如：
> `password = serializers.CharField(style={'input_type': 'password'})`
> validators:指定验证器。

#### validators
如果对django的form表单比较了解，可以很容易理解这些字段的意思。比如这里的validators,在form中也是存在的。
```python
class UserSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11)
```
这里的serializer虽然能提供简单的长度验证，但远远不够，此时我们就需要指定Validators:
```python
def phone_validator(value):
    pattern = r"^1[3|4|5|6|7|8|9]\d{9}$"
    if not re.match(pattern, value):
        raise ValidationError('手机号格式错误')
    return value

class UserSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=11, min_length=11, validators=[phone_validator, ])
```

#### UniqueValidator

指定某一个对象是唯一的，如，电话号只能存在且唯一

```python
phone = serializers.CharField(
    max_length=11,
    min_length=11,
    validators=[UniqueValidator(queryset=UserProfile.objects.all())
    )
```

#### UniqueTogetherValidator

queryset：required，用于明确验证唯一性集合，必须设置
fields: required，字段列表或者元组，字段必须是序列化类中存在的字段
message：当验证失败时的提示信息

UniqueTogetherValidator有一个隐性要求就是验证的字段必须要提供值，除非设置了一个默认值,并且它需要在Meta中设置：

比如要求用户昵称与邮箱联合唯一：

```python
class UserSerializer(serializers.Serializer):
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset=UserProfile.objects.all(),
                fields=('username', 'email')
            )
        ]

```


#### 局部钩子validate_phone

这里以短信验证码登陆时的验证为例，我们在给用户发送短信验证码后会将它存入redis，当我们验证时，就需要与redis中进行对比，在form中我们获取初始数据是通过self.cleaned_data, 这里是通过self.initial_data,获取到phone然后去redis根据电话号取验证码，与用户传过来的进行对比。
```python
def message_code_validator(value):
    if not value.isdecimal() or len(value) != 4:
        raise ValidationError('短信验证码格式错误')

class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(label='手机号', validators=[phone_validator, ])
    code = serializers.CharField(label="验证码", validators=[message_code_validator, ])

    def validate_code(self, value):
        phone = self.initial_data.get('phone')
        conn = get_redis_connection()
        code = conn.get(phone)
        if not code:
            raise ValidationError('短信验证码已失效')
        if value != code.decode('utf-8'):
            raise ValidationError('短信验证码错误')
        return value
```

#### 全局钩子validate

```python
class LoginSerializer(serializers.Serializer):
    password = serializers.CharField(label='密码', validators=[password_validator, ])
    password2 = serializers.CharField(label="验证密码", validators=[password_validator, ])

    def validate(self, value):
        password = self.initial_data.get('password')
        password2 = self.initial_data.get('password2')

        if password != password2:
            raise ValidationError('两次密码不一致')
        return value
```


## Django WebSocket

websocket是一种协议，2008年诞生，2011年成为国际标准。它的特点是服务器可以主动向客户端推送信息，客户端也可以主动向服务器发送信息，是真正的双向平等对话。它是建立在 TCP 协议之上的协议，即握手阶段仍然是http协议。

这里讲的是Django中的channels, channels运行于ASGI协议上，ASGI的全名是Asynchronous Server Gateway Interface。它是区别于Django使用的WSGI协议 的一种异步服务网关接口协议，正是因为它才实现了websocket

在django中请求处理逻辑是：url ---> view, 在channels中也是一样，只是叫的名字不同罢了。它的处理逻辑是：routing ---> consumer. 所以在django中完成前后端的双向通信，需要用url--->view这套逻辑来渲染页面，而用routing--->consumer这套逻辑来进行双向的信息发送。

### 配置App
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'channels',
]

#  指定路由位置
ASGI_APPLICATION = "django_channels_demo.routing.application"
```

### 路由(router)

分析channels源码，我们会发现它支持多种路由方式：
>ProtocolTypeRouter  # 根据协议类型映射（分发）
>URLRouter  # 根据url路径路由，可以使用django.conf.url来解析路径，支持url()或者path()
>ChannelNameRouter  # 根据channel的名字路由，channel可以理解 为广播的频道

```python
from channels.routing import ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from demo import consumers


application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url(r'^chat/$', consumers.ChatConsumer),
    ])
})
```
可以看到这段代码是先将 websocket协议分配给后面的URLRouter来处理了，而我们的URLRouter则是基于url路径的路由。最终达到websocket协议的 url路径的路由。
而上面的路由又将chat的url全部交给了ChatConsumer这个类来处理了。

### 消费者（Consumer)

这里说的视图，即是django的视图，因为它们的功能一样，所以我便叫它视图：

```python
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(WebsocketConsumer):

    def websocket_connect(self, message):
        self.accept()

    def websocket_receive(self, message):
        print('接收到消息', message)
        self.send(text_data='收到了')

    def websocket_disconnect(self, message):
        print('客户端断开连接了')
        raise StopConsumer()
```

我们看源码的websocket模块，发现只有四个类：
>WebsocketConsumer
>JsonWebsocketConsumer
>AsyncWebsocketConsumer
>AsyncJsonWebsocketConsumer

这么一看，实际只有两个类，因为后面两个是异步版本。

### WebsocketConsumer

```python
class WebsocketConsumer(SyncConsumer):
    """
    Base WebSocket consumer. Provides a general encapsulation for the
    WebSocket handling model that other applications can build on.
    """

    groups = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.groups is None:
            self.groups = []

    def websocket_connect(self, message):
        """
        Called when a WebSocket connection is opened.
        """
        try:
            for group in self.groups:
                async_to_sync(self.channel_layer.group_add)(group, self.channel_name)
        except AttributeError:
            raise InvalidChannelLayerError(
                "BACKEND is unconfigured or doesn't support groups"
            )
        try:
            self.connect()
        except AcceptConnection:
            self.accept()
        except DenyConnection:
            self.close()

    def connect(self):
        self.accept()

    def accept(self, subprotocol=None):
        """
        Accepts an incoming socket
        """
        super().send({"type": "websocket.accept", "subprotocol": subprotocol})

    def websocket_receive(self, message):
        """
        Called when a WebSocket frame is received. Decodes it and passes it
        to receive().
        """
        if "text" in message:
            self.receive(text_data=message["text"])
        else:
            self.receive(bytes_data=message["bytes"])

    def receive(self, text_data=None, bytes_data=None):
        """
        Called with a decoded WebSocket frame.
        """
        pass

    def send(self, text_data=None, bytes_data=None, close=False):
        """
        Sends a reply back down the WebSocket
        """
        if text_data is not None:
            super().send({"type": "websocket.send", "text": text_data})
        elif bytes_data is not None:
            super().send({"type": "websocket.send", "bytes": bytes_data})
        else:
            raise ValueError("You must pass one of bytes_data or text_data")
        if close:
            self.close(close)

    def close(self, code=None):
        """
        Closes the WebSocket from the server end
        """
        if code is not None and code is not True:
            super().send({"type": "websocket.close", "code": code})
        else:
            super().send({"type": "websocket.close"})

    def websocket_disconnect(self, message):
        """
        Called when a WebSocket connection is closed. Base level so you don't
        need to call super() all the time.
        """
        try:
            for group in self.groups:
                async_to_sync(self.channel_layer.group_discard)(
                    group, self.channel_name
                )
        except AttributeError:
            raise InvalidChannelLayerError(
                "BACKEND is unconfigured or doesn't support groups"
            )
        self.disconnect(message["code"])
        raise StopConsumer()

    def disconnect(self, code):
        """
        Called when a WebSocket connection is closed.
        """
        pass

```

这里定义的方法可以分成四类来看：连接， 发送消息，接收消息，断开连接。

当建立连接时，需要定制点功能我们就可以重写：websocket_connect
同样的道理，我们可以重写：websocket_receive, websocket_disconnect,而在这些函数内部我们可以调用send方法，比如上面的当我们收到消息时，给发送者回消息，就可以调用send.显然 我们可以看到这里可以发送两种类型的数据：
bytes, text即二进制和文本数据。

### JsonWebsocketConsumer

而另一个类JsonWebsocketConsumer是WebsocketConsumer的子类，所以很好理解它改送json格式的数据，只不过对文本数据转化为json格式而已。没什么特别，下面是源码：

```python
class JsonWebsocketConsumer(WebsocketConsumer):
    """
    Variant of WebsocketConsumer that automatically JSON-encodes and decodes
    messages as they come in and go out. Expects everything to be text; will
    error on binary data.
    """

    def receive(self, text_data=None, bytes_data=None, **kwargs):
        if text_data:
            self.receive_json(self.decode_json(text_data), **kwargs)
        else:
            raise ValueError("No text section for incoming WebSocket frame!")

    def receive_json(self, content, **kwargs):
        """
        Called with decoded JSON content.
        """
        pass

    def send_json(self, content, close=False):
        """
        Encode the given content as JSON and send it to the client.
        """
        super().send(text_data=self.encode_json(content), close=close)

    @classmethod
    def decode_json(cls, text_data):
        return json.loads(text_data)

    @classmethod
    def encode_json(cls, content):
        return json.dumps(content)
```



### channels-layer

channel类比于广播的频道，当一个频道发送了消息，只要收听这个频道的所有人都能收到广播消息。

Channels引入了一个layer的概念，channel layer是一种通信系统，允许多个consumer实例之间互相通信，以及与外部Django程序实现互通。

channel layer主要实现了两种概念抽象：

channel name： channel实际上就是一个发送消息的通道，每个Channel都有一个名称，每一个拥有这个名称的人都可以往Channel里边发送消息

group： 多个channel可以组成一个Group，每个Group都有一个名称，每一个拥有这个名称的人都可以往Group里添加/删除Channel，也可以往Group里发送消息，Group内的所有channel都可以收到，但是无法发送给Group内的具体某个Channel


#### 配置
官方推荐redis作为layer

`pip3 install channels-redis`

```python
CHANNEL_LAYERS = {
    'default': {
    'BACKEND': 'channels_redis.core.RedisChannelLayer',
    'CONFIG': {"hosts": ["redis://10.211.55.25:6379/1"],},
    },
}
```

基于内存

```python
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",
    }
}
```

将channels-layer配置添加到settings中


####  消费者（consumer)
在consumer中

```python
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class ChatGroupConsumer(WebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)('f1', self.channel_name)
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        async_to_sync(self.channel_layer.group_send)('f1', {
            'type': 'call.back',
            'message': text_data
        })

    def call_back(self, event):
        message = event['message']
        self.send(message)

    def disconnect(self, code):
        async_to_sync(self.channel_layer.group_discard)('f1', self.channel_name)
```

self.channel_name的生成方式：
```python
    async def new_channel(self, prefix="specific."):
        """
        Returns a new channel name that can be used by something in our
        process as a specific channel.
        """
        return "%s.inmemory!%s" % (
            prefix,
            "".join(random.choice(string.ascii_letters) for i in range(12)),
        )
```
这里有几点需要注意，group_add，f1相当于群名，而每个进来的的连接通过self.channel_name（随机字符串），即将这些连接加到这个群里，同样当断开连接里通过group_discard将人从群里踢除。

注意async_to_sync中的type参数，我们写的是call.back但在我们定义这个函数里要写成call_back, 因为源码中将“."转换成了 ”_":

```python
def get_handler_name(message):
    """
    Looks at a message, checks it has a sensible type, and returns the
    handler name for that type.
    """
    # Check message looks OK
    if "type" not in message:
        raise ValueError("Incoming message has no 'type' attribute")
    if message["type"].startswith("_"):
        raise ValueError("Malformed type in message (leading underscore)")
    # Extract type and replace . with _
    return message["type"].replace(".", "_")
```

### 认证(authenticate)

django channels 基于cookie, session实现了认证：
```python
from channels.auth import AuthMiddlewareStack

@database_sync_to_async
def get_user(scope):
    pass

@database_sync_to_async
def login(scope, user, backend=None):
    pass

@database_sync_to_async
def logout(scope):
    pass

def _get_user_session_key(session):
    # This value in the session is always serialized to a string, so we need
    # to convert it back to Python whenever we access it.
    return get_user_model()._meta.pk.to_python(session[SESSION_KEY])




class AuthMiddleware(BaseMiddleware):
    """
    Middleware which populates scope["user"] from a Django session.
    Requires SessionMiddleware to function.
    """

    def populate_scope(self, scope):
        # Make sure we have a session
        if "session" not in scope:
            raise ValueError(
                "AuthMiddleware cannot find session in scope. SessionMiddleware must be above it."
            )
        # Add it to the scope if it's not there already
        if "user" not in scope:
            scope["user"] = UserLazyObject()

    async def resolve_scope(self, scope):
        scope["user"]._wrapped = await get_user(scope)


# Handy shortcut for applying all three layers at once
AuthMiddlewareStack = lambda inner: CookieMiddleware(
    SessionMiddleware(AuthMiddleware(inner))
)
```

在最后部分我们拿到的AuthMiddlewareStack是基于cookie,session的认证。需要说明的是在channel中的scope类似于django中的request,`user = scope.get("user", None)` 我们可以这样获取 user.
具体使用只用等后面再更新了......
