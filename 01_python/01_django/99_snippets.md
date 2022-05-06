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