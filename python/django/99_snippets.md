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