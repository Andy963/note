
- Fields
	- fields types
	- field options
	- relationship
- Meta
- Model attribute
- Model method
- Model instance
	- proxy model


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

### Model

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

```

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

# 查询关联到某个Author实例的所有Book实例
books = author.book_set.all()

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


## 表单模板

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

## 事务

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



## 缓存

python提供了六种缓存方式：
经常使用的有文件缓存和Mencache缓存

> 开发调试缓存
内存缓存
文件缓存
数据库缓存
Memcache缓存(使用python-memcached模块)
Memcache缓存(使用pylibmc模块)

### 内存缓存
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',     # 指定缓存使用的引擎
        'LOCATION': 'unique-snowflake',                                 # 写在内存中的变量的唯一值 
        'TIMEOUT':300,     # 缓存超时时间(默认为300秒,None表示永不过期)
        'OPTIONS':{
            'MAX_ENTRIES': 300,   # 最大缓存记录的数量（默认300）
            'CULL_FREQUENCY': 3,# 缓存到达最大个数之后,剔除缓存个数的比例，即1/CULL_FREQUENCY（默认3）
        }
    }
}
```

### memcache缓存
```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',   # 指定缓存使用的引擎
        'LOCATION': '192.168.10.100:11211',   # 指定Memcache缓存服务器的IP地址和端口
        'OPTIONS':{
            'MAX_ENTRIES': 300,
            'CULL_FREQUENCY': 3,
        }
    }
}
#location也可以这样配置
'LOCATION': 'unix:/tmp/memcached.sock',  # 指定局域网内的主机名加socket套接字为Memcache缓存服务器
'LOCATION': [                            # 指定一台或多台其他主机ip地址加端口为Memcache缓存服务器
    '192.168.10.100:11211',
    '192.168.10.101:11211',
    '192.168.10.102:11211',
]
```

### 其它缓存的引擎：
```python
'BACKEND': 'django.core.cache.backends.db.DatabaseCache', # 数据库
'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache', # 文件缓存
#使用数据库缓存时需要创建缓存数据库表：python manage.py createcachetable
```

## 多app的管理

当使用apps文件夹时创建app时应指定创建app的目标文件夹：
例如要创建的app叫web, 在apps文件夹下创建web文件夹

```shell
python manage.py startapp web apps/web
```

## 其他
### session
如果在settings中设置
```python
SESSION_COOKIE_AGE=60*30 30分钟。
SESSION_EXPIRE_AT_BROWSER_CLOSE False：
SESSION_SAVE_EVERY_REQUEST=True # 这个必须设置，前面的超时失效和关闭浏览器失效二选一。
```
在视图函数中
```python
request.session.set_expiry(value) 
当value为整数时，在value秒后失效，value=0,关闭浏览器失效，value=None,依赖全局session失败策略，value为datetime对象时在该时间后失效。
```