# DRF parser

## 解析器的作用
解析器的作用就是服务端接收客户端传过来的数据，把数据解析成自己可以处理的数据。本质就是对请求体中的数据进行解析
这就与请求数据中的请求头有关：

>Accept是告诉对方我能解析什么样的数据，通常也可以表示我想要什么样的数据。
ContentType是告诉对方我给你的是什么样的数据类型

## 确定解析器
一组视图的有效解析器总是被定义为一个类的列表。当访问request.data时，REST框架将检查传入请求中的Content-Type头，并确定用于解析请求内容的解析器。

注意：
>开发客户端应用程序时应该始终记住在HTTP请求中发送数据时确保设置Content-Type头。如果你不设置内容类型，大多数客户端将默认使用'application/x-www-form-urlencoded'，而这可能并不是你想要的。举个例子，如果你使用jQuery的.ajax() 方法发送json编码数据，你应该确保包含contentType：'application / json'设置。

## 设置解析器

### 单个视图

```python
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    """
    可以接收JSON内容POST请求的视图。
    """
    parser_classes = (JSONParser,)

    def post(self, request, format=None):
        return Response({'received data': request.data})
```

### 全局

```python
REST_FRAMEWORK = {
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
    )
}
```
当你的项目中只配置了 JSONParser 解析器时，你的项目现在就只能解析JSON格式的数据了，客户端如果使用浏览器提交，那么你将无法解析。

注意，在视图类中定义的配置项的优先级要高于全局配置中的配置项

## 其它parser

* FormParser
* MultiPartParser
* FileUploadParser

### FormParser
解析 HTML 表单内容。request.data将被填充一个QueryDict的数据。
通常，你需要使用FormParser和MultiPartParser两者，以便完全支持HTML表单数据。
.media_type: application/x-www-form-urlencoded

### MultiPartParser
解析多部分HTML表单内容，支持文件上传。request.data 都将被一个 QueryDict填充。
你通常会同时使用FormParser和MultiPartParser两者，以便完全支持HTML表单数据。
.media_type: multipart/form-data

### FileUploadParser
解析原始文件上传内容。 request.data 属性将是有单个key 'file'的包含上传文件的字典。
如果与FileUploadParser一起使用的视图使用filename URL关键字参数调用，则该参数将用作文件名。
如果没有filename URL关键字参数调用，那么客户端必须在Content-Disposition HTTP头中设置文件名。例如 Content-Disposition: attachment; filename=upload.jpg.
.media_type: */*

FileUploadParser 用于与原始数据请求一起上传文件的本机客户端。对于基于Web的上传，或者对于具有多部分上传支持的本机客户端，您应该使用MultiPartParser解析器。
由于该解析器的media_type与任何内容类型匹配，所以FileUploadParser通常应该是API视图中唯一的解析器。
FileUploadParser 遵循 Django 的标准 FILE_UPLOAD_HANDLERS 设置，和 request.upload_handlers 属性。参见 Django 文档 获取更多细节。

```python
# views.py
class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        # ...
        # do some stuff with uploaded file
        # ...
        return Response(status=204)

# urls.py
urlpatterns = [
    # ...
    url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())
]
```