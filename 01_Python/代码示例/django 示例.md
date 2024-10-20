### 多app管理 （apps && extra_apps）
当项目中因为app较多而将所有app添加到apps包目录下时，通过下面的方法将路径添加进环境中
```python
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))
```


#### drf中文件上时重新选择文件
```py
from django.core.files.uploadedfile import InMemoryUploadedFile #这个是更改了
from django.db.models.fields.files import FieldFile #这个是没更改
```


### 自定义标签过,滤器

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

