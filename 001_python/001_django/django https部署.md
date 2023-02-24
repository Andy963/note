# django https部署


## 安装Nginx




## nginx 支持https

### 申请ssl证书

### 下载证书

### 在nginx配置证书


### 域名解析

### 访问nginx(测试）


### 部署django项目

### settings

#### 本地准备两个settings:
>local_settings.py
>prod_settings.py

在prod_settings.py最后面添加：
```python
try:
    from .local_settings import *
except ImportError:
    pass
```

#### .gitignore
.gitignore中 添加 local_settings.py


#### 提交本地代码到github

#### 服务器拉取代码

#### 线上创建local_settings.py 
添加内容：
```python
debug=False
allow_hosts = ['*']
#这样在线上的local_settings.py中的配置会覆盖前面的设置
```

