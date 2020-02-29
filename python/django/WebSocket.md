# Django WebSocket

websocket是一种协议，2008年诞生，2011年成为国际标准。它的特点是服务器可以主动向客户端推送信息，客户端也可以主动向服务器发送信息，是真正的双向平等对话。它是建立在 TCP 协议之上的协议，即握手阶段仍然是http协议。

这里讲的是Django中的channels, channels运行于ASGI协议上，ASGI的全名是Asynchronous Server Gateway Interface。它是区别于Django使用的WSGI协议 的一种异步服务网关接口协议，正是因为它才实现了websocket

在django中请求处理逻辑是：url ---> view, 在channels中也是一样，只是叫的名字不同罢了。它的处理逻辑是：routing ---> consumer. 所以在django中完成前后端的双向通信，需要用url--->view这套逻辑来渲染页面，而用routing--->consumer这套逻辑来进行双向的信息发送。


## 使用的基本流程

### 配置
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

### 路由

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

### 处理请求

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

## 路由

分析channels源码，我们会发现它支持多种路由方式：
>ProtocolTypeRouter  # 根据协议类型映射（分发）
>URLRouter  # 根据url路径路由，可以使用django.conf.url来解析路径，支持url()或者path()
>ChannelNameRouter  # 根据channel的名字路由，channel可以理解 为广播的频道

```python
application = ProtocolTypeRouter({
    'websocket': URLRouter([
        url(r'^chat/$', consumers.ChatConsumer),
    ])
})
```
可以看到这段代码是先将 websocket协议分配给后面的URLRouter来处理了，而我们的URLRouter则是基于url路径的路由。最终达到websocket协议的 url路径的路由。

而上面的路由又将chat的url全部交给了ChatConsumer这个类来处理了。

## 视图

这里说的视图，即是django的视图，因为它们的功能一样，所以我便叫它视图：


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

## web端：
据说大多数浏览器都支持websocket，WebSocket 对象作为一个构造函数，用于新建 WebSocket 实例

ref: https://developer.mozilla.org/en-US/docs/Web/API/WebSocket
```js
var ws = new WebSocket('ws://localhost:8000');
```

### readyState属性
webSocket.readyState
readyState 属性返回实例对象的当前状态，共有四种

>CONNECTING：值为0，表示正在连接。
OPEN：值为1，表示连接成功，可以通信了。
CLOSING：值为2，表示连接正在关闭。
CLOSED：值为3，表示连接已经关闭，或者打开连接失败。


### 回调函数
主要是三个函数：
>webSocket.onopen  #  实例对象的onopen属性，用于指定连接成功后的回调函数
>webSocket.onclose  #  实例对象的onclose属性，用于指定连接关闭后的回调函数
>webSocket.onmessage  #  实例对象的onmessage属性，用于指定收到服务器数据后的回调函数
>webSocket.onerror  #  实例对象的onerror属性，用于指定报错时的回调函数
>webSocket.send  #  用于向服务器发送数据

#### onopen

```js
ws.onopen = function () {
  ws.send('Hello Server!');
}

// 也可以这样,同样的道理，其它几个方法也可以通过这种方式来达到各自的目的，或者指定多个回调函数
ws.addEventListener("onopen", function(event) {
  // do sth
});
```

#### onclose

```js
ws.onclose = function(event) {
  // do sth
};


```

#### onmessage

```js
ws.onmessage = function(event) {
   var data = event.data;
  // do sth
  // 处理数据
};
```

#### send

```js
ws.send('your message');

// 文件（二进制）
var file = document.querySelector('input[type="file"]').files[0];
ws.send(file);
```

#### onerror

```js
socket.onerror = function(event) {
  // handle error event
};

```

#### bufferedAmount

实例对象的bufferedAmount属性，表示还有多少字节的二进制数据没有发送出去。它可以用来判断发送是否结束。
```js
var data = new ArrayBuffer(10000000);
socket.send(data);

if (socket.bufferedAmount === 0) {
  // 发送完毕
} else {
  // 发送还没结束
}
```

## channels-layer

channel类比于广播的频道，当一个频道发送了消息，只要收听这个频道的所有人都能收到广播消息。

Channels引入了一个layer的概念，channel layer是一种通信系统，允许多个consumer实例之间互相通信，以及与外部Django程序实现互通。

channel layer主要实现了两种概念抽象：

channel name： channel实际上就是一个发送消息的通道，每个Channel都有一个名称，每一个拥有这个名称的人都可以往Channel里边发送消息

group： 多个channel可以组成一个Group，每个Group都有一个名称，每一个拥有这个名称的人都可以往Group里添加/删除Channel，也可以往Group里发送消息，Group内的所有channel都可以收到，但是无法发送给Group内的具体某个Channel


### 配置
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


###  处理请求
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

## 认证

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