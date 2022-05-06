
## 上下文管理器

### 一般的上下文管理器
通常情况下，上下文管理器是这样的
```python
class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('close resource connection')

    def query(self):
        print('query data')

with MyResource() as r:
    r.query()
```
它的执行流程是：enter,返回实例对象，即我们的r,然后执行r.query(), 最后退出 执行exit方法。用一种函数表示就是这种样的：(显然这是行不通的)
```python
def make_myresource():
    print('connect to resource')
    return MyResource()# 跳出去执行查找方法
    print('close resource connection')

with make_myresource() as r
    r.query()
```
原因是return会中止程序，不再执行后面的代码，那么，如果我们使用的是yield呢？因为yield会保存状态，并且再下一次执行时接着从上一次执行的地方继续执行，我们改造一下：

### contextmanager
```python
# encoding:utf-8
from contextlib import contextmanager


class MyResource:
    def query(self):
        print('query data')


@contextmanager
def make_myresource():
    print('connect to resource')
    yield MyResource()
    print('close resource connection')
    
with make_myresource() as r:
    r.query()
```
执行
```python
connect to resource
query data
close resource connection
```

### 应用

#### 改造print
假设我们在打印一本书名是，想自动给书名前后加上书名号《》,类似这样的，即输出的结果是：《活着》
```python
with book_mark():
    print("《")
    print("活着")
    print("》")
```
我们先用一般的上下文管理的方式实现：
```python
class BookMark:
    def __enter__(self):
        print("《", end='')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("》", end='')

with BookMark():
    print('活着',end='')
```
现在我们来改造它：
```python
from contextlib import contextmanager
@contextmanager
def make_mark():
    print("《",end='')
    yield
    print("》",end='')

with make_mark():
    print('活着', end='')
```
简单总结一下：我们要编写的这个需要contextmanager装饰的函数中yield之前会执行enter中的操作，而yield之后 则是执行exit中的操作。而真正的动作则是在with语句中执行即可。

伪代码：
```python
@contextmanager
def func():
    enter (进入时的操作)
    yield  （跳出，执行我们的核心动作）
    exit (退出前的操作）

with func as f:
     核心动作
```
#### 数据库提交
下面看更实际的例子：在数据据库提交数据使用事务来保证它原子性操作，要怎么改造呢
未修改前：
```python
try:
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    db.session.add(gift)
    db.session.commit()
except Exception as e:
    db.session.rollback()
```
改造后：
```python
from contextlib import contextmanager

@contextmanager
def auto_commit():
    try: #进入前的操作
        yield # 跳出执行核心动作
        self.session.commit() # 返回后要接着执行的动作
    except Exception as e:
        self.session.rollback()
        raise e

with db.auto_commit():
    # 核心动作
    gift = Gift()
    gift.isbn = isbn
    gift.uid = current_user.id
    db.session.add(gift)
```
总结：
在我们定定义的需要contextmanager装饰的函数中我们只需要写，前戏和事后回味两部分内容。这两部分内容用yield分隔开。
而在我们调用with语句中则是执行真正的战斗部分。

