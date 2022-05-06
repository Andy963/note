## Django Rest Framework


### RESTful API设计

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



## 序列化器



### 外键

方式一：
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

方式二：
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



### serializer中验证字段

```python
class ReceiveCouponSerializer(serializers.ModelSerializer):
    rest_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.UserCoupon
        fields = ['coupon', 'rest_count']

    def get_rest_count(self, obj):
        return obj.init_count - obj.dispatch_count - 1

    def validate_coupon(self, value):
        # value 为coupon object
        # 此处获取request对象的方法： self.context['request']
        # 如果使用了authenticate 组件，就可以获取user: self.context['request'].user
        user_obj = self.context['request'].user

        # 如果优惠券对象不存在，或者已经删除状态
        if not value or value.deleted:
            raise exceptions.ValidationError('优惠券不存在')
        # 如果不是可领取状态
        if value.status != 2:
            raise exceptions.ValidationError('优惠券不可领取')
        # 判断个数
        if (value.dispatch_count + 1) > value.init_count:
            raise exceptions.ValidationError('优惠券已经领完')

        # 判断是否已经领取
        is_exists = models.UserCoupon.objects.filter(user=user_obj, coupon=value).exists()
        if is_exists:
            raise exceptions.ValidationError('已经领取此优惠券')

        return value
```


## FileField处理

当model中定义了filefield时，在serializer中处理时会出现取到的数据是添加了本地路径的数据，例如：
>c://user/andy//http://www.jingang.ga/v.jpg
>http://127.0.0.1:8000/www.jinagng.ga/v.jpg

### 在serializer中的处理：

有两种情况需要处理，
> 一个是cover字段本身，可以将它定义为CharField
> Queryset对象中使用 ".name"

```python
class AuctionModelSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()
    cover = serializers.CharField()  # 这里定义为charField

    class Meta:
        model = models.Auction
        fields = ['id', 'title', 'status', 'cover', 'total_price', 'look_count', 'goods_count', 'items']

    def get_items(self, obj):
        queryset = models.AuctionItem.objects.filter(auction=obj)[0:5]
        return [row.cover.name for row in queryset]  # 这里使用.cover.name
```


## 认证组件


### python

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


### js
js中设置header携带
```javascript
// 这是三元表达式，如果存在userInfo,则Authorization为 token userInfo.token,否则为空
header: {
        Authorization: userInfo ? "token " + userInfo.token : ""
      }
```


