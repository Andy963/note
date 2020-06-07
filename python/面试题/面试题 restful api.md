## api

### 什么是webservice？
```
通过网络调用其他网站的资源
```
### 什么是rpc？
```
remote Procedure  call
远程过程调用，简单的理解是一个节点请求另一个节点提供的服务

```

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

### django rest framework 框架如何对Queryset 进行序列化？
```
指定serializer_class
```

### 简述 django rest framework 框架的认证流程。
```
- 如何编写？写类并实现authenticators
　　请求进来认证需要编写一个类，类里面有一个authenticators方法，我们可以自定义这个方法，可以定制3类返值。
　　成功返回元组，返回none为匿名用户，抛出异常为认证失败。

源码流程：请求进来先走dispatch方法，然后封装的request对象会执行user方法，由user触发authenticators认证流程
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