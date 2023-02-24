## cors_setting

### install django-cors-headers
```shell
pip install django-cors-headers
```

### change settings
```python
INSTALLED_APPS = [
    ......
    'corsheaders',
    ......
]

MIDDLEWARE = [
    ......
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ......
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
```

## offline script
```python

import os
import sys
import django
from api import models

# 获取项目的根目录
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(base_dir)	# 添加到系统环境变量
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "demos.settings")	# 加载项目的配置文件，demos是项目
django.setup()	# 启动django

# now we can use model to add data
```

### visit media
how to visiti media like pic,video
```python

#settings.py
MEDIA_URL = "/media/"
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# url
from shop.ettings import MEDIA_ROOT
from django.views.static import serve

url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}
```

### django reverse with query string
there isn't a way to rever query string but only args or kwargs. this snippets is from github
refs: https://gist.github.com/benbacardi/227f924ec1d9bedd242b
```python
from django.utils.http import urlencode

def reverse_querystring(view, urlconf=None, args=None, kwargs=None, current_app=None, query_kwargs=None):
    '''Custom reverse to handle query strings.
    Usage:
        reverse('app.views.my_view', kwargs={'pk': 123}, query_kwargs={'search': 'Bob'})
    '''
    base_url = reverse(view, urlconf=urlconf, args=args, kwargs=kwargs, current_app=current_app)
    if query_kwargs:
        return '{}?{}'.format(base_url, urlencode(query_kwargs))
    return base_url
```


## 保存搜索条件

默认情况下request中的参数是不能修改的，我们先拷贝一份，再修改
```python

def gen_url(request,id):
    params = request.GET.copy()
    params._matable=True
    params['id] = id
    return params.urlencode()
```



## CBV加装饰器的三种方式

>  对类使用method_decorator(装饰器名, name='方法名')
>  对dispathc使用 method_decorator(装饰器名）
>  对类中的某个方法使用 method_decorator(装饰器名）


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


## 自定义标签过,滤器

#### 在app中新建一个templatetags包


#### 创建文件
> 在settings中注册当前app
> 如：cus_tags.py 那么在页面中引用 为`{% load cus_tags %}`

#### 编写标签，过滤器
```python
from django import template
from django.utils.safestring import mark_safe

register = template.Library()   #register的名字是固定的,不可改变


@register.filter
def filter_multi(v1,v2):
    return  v1 * v2

@register.simple_tag  #和自定义filter类似，只不过接收更灵活的参数，没有个数限制。
def simple_tag_multi(v1,v2):
    return  v1 * v2

@register.simple_tag
def my_input(id,arg):
    result = "<input type='text' id='%s' class='%s' />" %(id,arg,)
    return mark_safe(result)
```

```python
from django import template

register = template.Library()


@register.inclusion_tag('result.html')  #将result.html里面的内容用下面函数的返回值渲染，然后作为一个组件一样，加载到使用这个函数的html文件里面
def show_results(n): #参数可以传多个进来
    n = 1 if n < 1 else int(n)
    data = ["第{}项".format(i) for i in range(1, n+1)]
    return {"data": data}#这里可以穿多个值，和render的感觉是一样的{'data1':data1,'data2':data2....}
```

####  页面中使用
` {% simple_tag_multi 1 2 %}`


## 表单批量添加bootstrap样式
```python

from django import forms

from auc import models as auc_models


class BootstrapModelForm(forms.ModelForm):
    """为form表单批量添加bootstrap样式"""
    exclude_bootstrap_field = []  # 排除的字段

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            if field in self.exclude_bootstrap_field:
                continue
            old_class = self.fields[field].widget.attrs.get('class', '')
            self.fields[field].widget.attrs["class"] = old_class + ' form-control'


class AuctionModelForm(BootstrapModelForm):
    exclude_bootstrap_field = ['cover', ]

    class Meta:
        model = auc_models.Vendue
        fields = ['title', 'cover', 'start_time', 'cash_deposit']

```
