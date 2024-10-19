## 源

### 创建文件目录
linu在用户home目录下，win下为：C:\\Users\\Andy Andy即我的用户名

```shell
mkdir .pip # window中不需要加"."
cd .pip
vim pip.conf # window中为pip.ini
```

### 添加源
```python
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
proxy = http://127.0.0.1:51837
extra-index-url=
        https://pypi.org/simple

[install]
trusted-host=
        mirrors.aliyun.com
        pypi.org

```

## 运算符（operator）

海象运算符：
```python

my_list = [1,2,3]

# 这里说的能避免两次操作：
if len(my_list) > 3:
	print(f"Error {len(my_list)} is too long")

# 这里可以减少一条语句
count = len(my_list)
if count > 3:
   print(f"Error, {count} is too many items")

# 当转换为海象运算符时...
if (count := len(my_list)) > 3:
   print(f"Error, {count} is too many items")

line = f.readLine()
while line:
   print(line)
   line = f.readLine()

# 转换为海象运算符时
while line := f.readLine():
   print(line)
```
学了go之后 发现这不是一样的吗？就是简化了赋值操作而已，之前还不是很理解这个所谓的海象运算符

### 位运算符

![位运算符](https://raw.githubusercontent.com/Andy963/notePic/main/1605365202_20201114224632712_18078.png =986x)

应用：

判断一个数是否是2的整数次方
```python
def is_power_of_two(n):
    return n != 0 and (n & (n-1) == 0)
```

在后台设计权限管理，一种思路是通过位运算。之前写flask 项目有使用这种方式，还是比较好理解的。

### 运算符优先级

![](https://raw.githubusercontent.com/Andy963/notePic/main/1605366605_20201114230958337_31816.png)

## 数字（number）

### 数学函数

ceil: 返回数字的上入整数，即上向取整. 如 math.ceil(4.1) = 5 与之对应的，floor向下取整
exp(x): 返回e的x次幂
log(x,base): 返回以base为底的x的对数，以10为底还有log10(x)
modf(x): 返回x的整数部分与小数部分，整数部分也以浮点数表示
pow(x,y): 返回 x的y次方
round(x): 四舍五入
sqrt(x): 返回x的平方根


## 字符串
### 字符串格式化

![](https://raw.githubusercontent.com/Andy963/notePic/main/1605537528_20201116223843190_3343.png)

格式化操作符辅助指令:
![](https://raw.githubusercontent.com/Andy963/notePic/main/1605537606_20201116223958736_20108.png)

python三引号允许一个字符串跨多行，字符串中可以包含换行符、制表符以及其他特殊字符

### f-string
f-string 是 python3.6 之后版本添加的，称之为字面量格式化字符串，是新的格式化字符串的语法

```python
In [1]: name = "andy"

In [2]: f'hello {name}'
Out[2]: 'hello andy'
```

在 Python 3.8 的版本中可以使用 = 符号来拼接运算表达式与结果：

```python
>>> x = 1
>>> print(f'{x+1}')   # Python 3.6
2

>>> x = 1
>>> print(f'{x+1=}')   # Python 3.8
'x+1=2'
```


find(str, b, e) 查检str是否包含在目标字符串中，返回在则返回索引，如果不在则返回-1,与index类似，但如果元素不在目标字符串中，index函数会报错。并且还有对应的rfind,rindex从右边开始。
ljust(width, fillchar), 左对齐并使用fillchar填充到指定宽度，与之对应的有rjust

## 列表（list）
列表都可以进行的操作包括索引，切片，加，乘，检查成员。

需要注意乘法运算时，是在列表内部对元素进行重复(元组也是如此)

```python
ls = ["a", "b"]  
print(ls * 3)

# ['a', 'b', 'a', 'b', 'a', 'b']
```

注意，列表也有clear方法，可以将整个列表清空（与集合相同）

## 元组（tuple）

元组是不可变类型，另外，当元组中只有一个元素时，就在元素后面添加逗号，否则括号会被当作运算符使用。

### 修改元组

元组可以相加，相乘

```python
In [1]: t1 = (12,34,5)

In [2]: t2 = ('ab','cd')

In [3]: t3=t1+t2

In [4]: t3
Out[4]: (12, 34, 5, 'ab', 'cd')
```

### 删除整个元组

因元组是不可变类型，所以无法删除元组中元素，但可以删除整个元组

```python
In [5]: del t1[0]
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-5-8940bcde932e> in <module>
----> 1 del t1[0]

TypeError: 'tuple' object doesn't support item deletion

In [6]: del t1

In [7]: t1
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-7-5db19043943a> in <module>
----> 1 t1

NameError: name 't1' is not defined
```

元组也是序列，所以可以通过下标访问元素，截取，与序列方法一致。


## 集合（set）
集合（set）是一个无序的不重复元素序列。可以使用大括号 { } 或者 set() 函数创建集合，创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。

初始化：
```python
my_set = {1, 2, 3, 4}
my_set = set([1, 2, 3, 4])
```

### 添加元素

add 添加一个元素，如果该元素已经存在于集合中，则集合不会发生变化。
update 可以添加多个元素，
```python
s.add( x )
s.update( x )
In [1]: s = set()

In [2]: s.update('a','b')

In [3]: s
Out[3]: {'a', 'b'}
```
### 移除元素

```python
s.remove( x ) # 如果 不存在，报错
s.discard( x ) # 如果不存在，不报错
In [4]: s.remove('d')
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-4-3e5f395d32ae> in <module>
----> 1 s.remove('d')

KeyError: 'd'

In [5]: s.discard('d')
s.pop()  #随机删除一个元素
In [6]: s.pop()
Out[6]: 'b'

In [7]: s
Out[7]: {'a'}
```

### 清空集合

```python
s.clear()
```

### 内置方法
difference() 返回集合的差集
intersection 返回集合的交集
isdisjoint() 判断是否有相同的元素
issubset 判断是否为子集
issuperset 判断是否为超集
symmetric_difference 返回两个集合中不重复的元素集合
union 返回并集


## 字典（dict）

字典是另一种可变容器模型，且可存储任意类型对象
dict()
```python
In [1]: dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
Out[1]: {'sape': 4139, 'guido': 4127, 'jack': 4098}

In [2]:  dict(sape=4139, guido=4127, jack=4098)
Out[2]: {'sape': 4139, 'guido': 4127, 'jack': 4098}

#列表 推导式
In [3]: {x: x**2 for x in (2, 4, 6)}
Out[3]: {2: 4, 4: 16, 6: 36}
```
### 方法
items() 键值对
keys() 所有的键
values() 所有的值

copy() 浅复制字典
fromkeys()  这个方法用得少，特意试了一下：

```python
In [17]: d = {}

In [18]: d.fromkeys('a','b')
Out[18]: {'a': 'b'}

In [19]: d.fromkeys(['a','b'],[1])
Out[19]: {'a': [1], 'b': [1]}

In [20]: d.fromkeys(['a','b'],1)
Out[20]: {'a': 1, 'b': 1}
```
get(key,default=None),从字典中获取key对应的值，如果不存在，则返回默认值
update(dict) 将dict更新到字典中
setdefault(key,default=None) 将某个键设置默认值，如果不存在则会添加
pop(key) 删除指定键对应的值，返回的为该值，必须指定key，删除后该对应的键也从字典中消失了
popitem() 随机删除字典中的最后一对键值



## 可迭代对象

从代码角度来说，对象内部实现了__iter__()方法或者实现了__getitem__()的方法,主要包括:列表、元组、字典、集合字符串和open()打开的文件

enumerate的一个优点：

```python
fruits = ['apple', 'banana', 'cherry']

for index, fruit in enumerate(fruits):
    if fruit == 'banana':
        fruits.remove(fruit)

print(fruits)

# 下面的边迭代边删除会超出边界
fruits = ['apple', 'banana', 'cherry']

for i in range(len(fruits)):
    if fruits[i] == 'banana':
        fruits.remove(fruit)

1. 使用 enumerate() 的方法：

enumerate() 函数在 Python 中创建了一个迭代器对象。这个迭代器在循环开始时就生成了，它包含了原始列表中所有元素的引用（不是副本）。

当循环开始时，迭代器指向第一个元素。每次迭代，它就移动到下一个元素。即使原始列表被修改了，迭代器仍然保持着对原始元素的引用。

具体过程如下：
⦁ 迭代器指向 'apple'，不删除，移到下一个
⦁ 迭代器指向 'banana'，删除它，移到下一个
⦁ 迭代器指向 'cherry'，不删除，循环结束

所以，即使 'banana' 被删除，迭代器仍然能够找到并指向 'cherry'，因为它持有的是对原始元素的引用，而不是列表索引。

2. 从后向前遍历：
fruits = ['apple', 'banana', 'cherry']

for i in range(len(fruits) - 1, -1, -1):
    if fruits[i] == 'banana':
        fruits.remove(fruits[i])

print(fruits)

从后向前遍历不会出现索引越界，因为我们是从最大索引开始，逐渐减小到0。即使删除了元素，也不会影响到我们还没有处理的元素的索引。

具体过程如下：
⦁ i = 2，检查 'cherry'，不删除
⦁ i = 1，检查 'banana'，删除它
⦁ i = 0，检查 'apple'，不删除

即使在删除 'banana' 后列表长度变为2，这也不会影响到索引0的访问，因为我们已经处理完了所有大于0的索引。

底层原理：
⦁ 在 Python 中，列表是动态数组实现的。当我们删除一个元素时，后面的所有元素都会向前移动一位。
⦁ 从前向后遍历时，如果删除了当前元素，后面的元素会前移，导致下一次迭代时跳过了一个元素。
⦁ 从后向前遍历时，即使删除了当前元素，它也不会影响到我们还没有处理的元素的位置。

或者使用列表推导式：
fruits = ['apple', 'banana', 'cherry']
fruits = [fruit for fruit in fruits if fruit != 'banana']
print(fruits)

```

### 迭代器

迭代器是一个实现了迭代器协议的对象。在 Python 中,迭代器协议包括两个方法:

- **__iter__**(): 返回迭代器对象本身
- **__next__**(): 返回容器中的下一个元素,如果没有更多元素则抛出 StopIteration 异常

 迭代器的特点:

- 惰性计算: 只有在需要时才会计算下一个元素,节省内存
- 单向遍历: 只能向前遍历,不能后退
- 状态保持: 记住当前遍历的位置

迭代器是一个可以记住遍历的位置的对象，它会从第一个元素遍历，一直向前，无法后退，到遍历完所有元素，它有两个基本方法：`__iter__, __next__`

```python
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
```

### 生成器
使用了yield的函数被称为生成器。即生成器是使用函数语法定义的迭代器

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个特殊的迭代器。

在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

```python
import sys

def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
```

   生成器的本质就是迭代器，在python社区中，大多数时候都把迭代器和生成器是做同一个概念。唯一的不同就是：迭代器都是Python给你提供的已经写好的工具或者通过数据转化得来的，比如文件句柄，iter([1,2,3])。生成器是需要我们自己用python代码构建的工具。

生成器的构建方式： 通过生成器函数 通过生成器推导式

### 生成器函数

在生成器中，我们可以通过yield返回数据，而不是return, return会结束程序，而yield只是生成一个对象，等待你来取。但你可以理解为return.

```python
def fun():
    print('one')
    yield 11
    yield 22

ret = fun()
print(ret.__next__())
```

当代码执行时，首先会打印one,然后将第一个yield的值交给ret（可以理解为return）,此时它会保留状态，下次再取则从第一个yield之后取。如果再次执行`print(ret.__next__())`则会取到第二个yield之后 的值，即 22。

总结：yield与return的区别：
        return一般在函数中只设置一个，他的作用是终止函数，并且给函数的执行者返回值。
        yield在生成器函数中可设置多个，他并不会终止函数，next会获取对应yield生成的元素

### send
send用来向生成器中传值，它本身包含next方法，看下面的例子：

```python
def gen(name):
    print(f'{name} ready to eat')
    while 1:
        food = yield
        print(f'{name} start to eat {food}')

dog = gen('alex')
next(dog)
# 还可以给上一个yield发送值
dog.send('骨头')
dog.send('狗粮')
dog.send('香肠')
"""
alex ready to eat
alex start to eat 骨头
alex start to eat 狗粮
alex start to eat 香肠
"""
```

首先，next会将程序执行到yield，但上面next并不会打印出什么，(把yield理解为return,即即程序执行到yield返回了，没有赋值，但保留了状态，等待下一次从赋值开始)。随后的send将值传入，而程序从上次的状态接着执行，即赋值操作：food='骨头', 所以我们看到的是："alex start to eat 骨头"

**send() vs next()**

我们看下官方文档：
> generator.send(value)
恢复执行并向生成器函数“发送”一个值。<u>**value 参数将成为当前 yield 表达式的结果**</u>。 send() 方法会返回生成器所产生的下一个值，或者如果生成器没有产生下一个值就退出则会引发 StopIteration。 

当直接调用 send() 来启动生成器时，它必须以 None 作为调用参数，因为这时没有可以接收值的 yield 表达式，即还没有走到yield,可以通过调用一次next()达到走到yield的目的。

相同：
1.  生成器对应的yield向下执行一次
2. 获取yield生成的值

不同：
1.  第一次取yield的值时只能用next，如果非要用send,必须要send(none) 因为没有yield语句来接收这个值

### yield from

当使用 ` yield from <expr>` 时，它会将所提供的表达式视为一个子迭代器。 这个子迭代器产生的所有值都直接被传递给当前生成器方法的调用者。 通过 send() 传入的任何值以及通过 throw() 传入的任何异常如果有适当的方法则会被传给下层迭代器。 如果不是这种情况，那么 send() 将引发 AttributeError 或 TypeError，而 throw() 将立即引发所传入的异常。

```python
def fun():
    yield ['a', 'b', 'c']


f = fun()
print(f.__next__())
```

这种情况下，会直接返回整个列表，但如果使用`yield from` 就会返回列表中单个元素。


推导式
```python

gen = (i**2 for i in range(10))
```

### 生成器应用
一个保存了400W条分词后的中文文本数据的文件，每条数据大概200-400个词，电脑内存32G，现在需要统计词频，用做后续算法的处理。

```python
def get_sentence_words(path):
    files = os.listdir(path)
    for file in files:
        file_path = os.path.join(path, file)
        with open(file_path, 'r') as f:
            for line in tqdm(f, desc='read sentence_cuts'):
                line = line.strip().split(' ')
                for word in line:
                    yield word
 
if __name__ == '__main__':
    words_gen = get_sentence_words('data_set/sentence_cut')
    weight_dict = Counter(words_gen)
    print('len(weight_dict)',len(weight_dict))
    total = 0
    for v in weight_dict.values():
        total += v
    print('total words is %d'% total)

```

ref:https://blog.csdn.net/HUSTHY/article/details/106882669


## 函数

定义在函数内部的函数，该函数引用外部作用域而不是全局作用域的变量，该函数称为闭包函数。该函数可以在其定义环境外执行。
闭包函数私有化了变量,完成了数据的封装,类似于面向对象. 闭包因为保存了变量,如果大量使用,对内存是有消耗的.

 高阶函数：
高阶函数在Python中是指可以接受函数作为参数，或者将函数作为返回值的函数¹²。这种能够处理函数的函数就被称为高阶函数¹。简而言之，高阶函数就是能够接受函数作为参数或者返回函数的函数。

高阶函数主要有：filter, map, reduce, sorted
#### enumerate
enumerate 是python中的内置函数，返回一个enumerate对象（可迭代对象），可以在获取每个元素的同时获取到它的索引，且它可以指定索引的起始值，例如有时需要索引从1开始，而不是编程语言中默认的从0开始。且enumerate 是延迟计算的

```python
# 如果直接在遍历列表时会导致问题，但如果通过enumerate 则可以解决问题
arr = [3, 2, 0]  
for i, _ in enumerate(arr):  
    if i == 2:  
        arr.remove(i)  
  
print(arr)
# 另一个解决此问题的办法是倒序遍历
```


#### filter

python中filter 是一个内置的高阶函数（能够以函数作为参数或者作为返回值的函数），用于过滤序列的值.它有两个参数，第一个为过滤函数，第二个为序列。返回值为一个迭代器对象。

```python
b = filter(lambda x: x % 2 == 1, a)
print(list(b))  # 输出：[1, 3, 5]
```

短路返回相关ref:
[boolean logic - Does Python support short-circuiting? - Stack Overflow](https://stackoverflow.com/questions/2580136/does-python-support-short-circuiting)

#### map

它接受一个函数和一个或多个迭代器作为输入，并返回一个将函数应用于每个迭代器元素的新迭代器

```python
numbers = [1, 2, 3, 4]
squares = map(lambda x: x**2, numbers)
print(list(squares))  # 输出 "[1, 4, 9, 16]"
```

#### reduce

```python
from functools import reduce

numbers = [1, 2, 3, 4]
sum = reduce(lambda total, num: total + num, numbers)
print(sum)  # 输出 "10"

```

即使我们没有给`total`赋初始值，`reduce()`函数仍然可以正确地计算出数字列表的和。
但是，请注意，如果序列为空，并且没有提供初始值，`reduce()`函数会抛出一个`TypeError`

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda total, num: total * num, numbers, 1)
print(product)  # 输出 "24"
```
### 装饰器:

本质是一个函数或一个类，它接受一个函数作为输入，并返回另一个函数.装饰器通常使用闭包来记住原始函数，并在新函数中调用它.

不影响原有函数的功能（不修改源码）,还能添加新的功能(开闭原则)

#### 函数装饰器

```python

def func1(func):
	def func2():
		print('aaa')
		return func()
	return func2

@func1
def my_print():
	print("hello I'm print")

if __name__ == '__main__':
		# my_print = func1(my_print) = func2
		my_print()


# 不带参数
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time of {func.__name__}: {end - start:.2f} seconds")
        return result
    return wrapper

@time_it
def some_function():
    time.sleep(1)

some_function()


# 带参数
def log(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} - Start function {func.__name__}")
            result = func(*args, **kwargs)
            print(f"{prefix} - End function {func.__name__}")
            return result
        return wrapper
    return decorator

@log("INFO")
def some_function():
    print("Function is running...")

some_function()


# 多个装饰器时，执行顺序从外到内
def my_decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def my_decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@my_decorator1
@my_decorator2
def my_function():
    print("Hello, world!")

my_function()

#output 
Decorator 1
Decorator 2
Hello, world!
```

#### 类装饰器

使用类作为装饰器本质上还是使用的函数，只不过形式上是类

```python
class ClsDecorator:
    def __init__(self, fun):
        print('__init__')
        self.f = fun

    def __call__(self, *args, **kwargs):
        print('enter', self.f.__name__)
        self.f()
        print('exit', self.f.__name__)


@ClsDecorator
def fun():
    print('this is my func')


fun()
# 输出
__init__
enter fun
this is my func
exit fun
```

之所以说本质上还是函数，是因为在类中我们定义了`__call__`方法，因为`__call__`允许我们像调用函数一样调用类，我们将函数传入，并在
`__init__`中初始化，随便在`__call__`方法中使用我们可以在使用真正的函数之前或者之后 做一些操作，和我们的函数装饰器一样。

在此基础上我们可以通过对象来进行装饰：

```python
class ClsDecorator:
    def __init__(self, name,age):
        print('__init__')
        self.name = name
        self.age = age

    def __call__(self,func):
        def wrap(*args):
            print('enter', func.__name__)
            print(self.name,self.age)
            func(*args)
            print('exit')
        return wrap


@ClsDecorator('andy',30)
def fun():
    print('this is my func')

fun = ClsDecorator('andy',30)(fun)

fun()
# 输出
__init__
enter fun
andy 30
this is my func
exit
```

我们在装饰时是使用的实例化对象，这样有一点好处是方便传入参数。当有参数时：`ClsDecorator('andy',30)` 已经完成了类的实例化，此时将 `fun` 参数 传给 ClsDecorator的实例对外，此时 `call` 方法就不能是简单的函数，而应该是闭包，否则就直接执行了。


#### 应用场景

1. 类装饰器可以用于计算函数的运行时间，示例代码如下

```python

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"{self.func.__name__} took {end_time - start_time:.2f} seconds")
        return result

@Timer
def some_function():
    time.sleep(2)

some_function()

```


2.  缓存器

```python
class Cache:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        result = self.func(*args)
        self.cache[args] = result
        return result

@Cache
def some_function(x, y):
    return x + y

print(some_function(1, 2)) # 3
print(some_function(1, 2)) # 3 (from cache)

```

3.  权限验证
类装饰器还可以用于实现一个权限验证功能，用于检查用户是否有访问某个页面或执行某个操作的权限

```python
class Permission:
    def __init__(self, role):
        self.role = role

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.role in get_user_roles(): # get_user_roles() 为获取用户角色的函数
                return func(*args, **kwargs)
            else:
                raise Exception("Access denied")
        return wrapper

@Permission("admin")
def some_function():
    pass

```


## 类

### 创建类的方式 
 #### 常见方式 class

```python
class Person:
	age = 0
	def run(self):
		pass
```

#### 通过type

```python
def run(self):
	print('---',self)

# xxx是引用名,Human则是类名，()表示基类的元组，所以外部无法直接访问Human
xxx = type("Human",(),{"age":0,"run":run})
print(xxx.__dict__)
xxx.run('10km')

{'age': 0, 'run': <function run at 0x7fafdb457ca0>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None}
--- 10km
```

#### 通过metaclass

```python
class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['method'] = lambda self: self.x + self.y
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj = MyClass(1, 2)
print(obj.method()) # Output: 3

```

### 属性

#### 受保护的属性:
以单下划线` _ `开头定义。
   ⦁ 表示该属性不应该被外部直接访问，主要用于内部使用，子类可以访问。
   ⦁ 这并不是强制性的保护，只是一种约定，告诉其他程序员这个属性是“受保护的”。
   
    - 类内部可以访问
    - 子类内部可以 访问
    - 模块内其他位置访问 : 类,实例均无法访问
    - 跨模块访问: import 导入可以访问,但会提示,  from module import * 导入则无法访问,会报错(如果指定在__all__中则可以导入,如果没有在__all___列表中则报错).

#### 私有化属性

以双下划线`__`开头定义。
   ⦁ Python会对双下划线的属性进行名称改编（name mangling），以确保其在类外部无法直接访问。
   ⦁ 通常情况下，私有属性仅仅通过类的实例方法访问
#### 只读属性

通过使用 @property 装饰器来定义一个只读属性。
也可以通过重写setattr实现
   ⦁ 只读属性只能被获取，无法被设置。

```python
class Person:
	def __setattr__(self,key,value):
		if key == "age" and key in self.__dict__.keys():
			print("this attr can not set!")
		else:
			# self.key = value 这样会导致无限循环
			self.__dict__[key] = value

p = Person()
# 第一次设置时,p中不含有age属性,所以可以设置
p.age = 18
print(p.age)
# 此时p 中已经有属性age,所以不能修改
p.age = 28
print(p.age)

```


### 方法
在python中类有三种不同方法：实例方法，类方法，静态方法。这三种方法通过第一个参数的类型来进行区分，实例方法的第一个参数为为的实例对象，类方法的第一个参数为类对象，而静态方法不要求参数，与普通函数无异。
静态方法,类方法,普通实例方法都是存储在类中,而不会存储在对象中

#### 实例方法
实例方法，要求第一个方法为实例对象，当我们通过实例调用时，会自动将实例作为第一个参数传递给实例方法。下面是通过类来调用实例方法，虽然不会出错，但没有多大意义。

```python
class Person:
    def eat(self):
        print('eat', self)


p = Person()
p.eat()
Person.eat('123')
#输出
eat <__main__.Person object at 0x7fb915e54c18>
eat 123
```

#### 类方法
类方法的第一个参数是类对象，而非实例对象，但仍可能通过实例对象调用，且不用明确传类

提供了一种在不需要实例的情况下操作类的方式，非常适合用于一些与类相关但不依赖于特定实例的操作。

```python
class Man:
    @classmethod
    def eat(cls):
        print('eat',cls)

#输出
eat <class '__main__.Man'>
eat <class '__main__.Man'>


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)

# 使用类方法创建实例
date1 = Date.from_string('11-09-2023')

```

#### 静态方法
静态方法与普通函数无异，只是存放在类命名空间中而已，静态方法（@staticmethod）不能访问类的状态，但类方法可以访问和修改类的状态。

```python
class Person:
    @staticmethod
    def eat():
        print('eat')

Person.eat()
p = Person()
p.eat()
f = Person.eat
f()
# 输出
eat
eat
eat
```

### 属性访问及顺序

针对三种方法，对实例属性，类属性的访问问题：

```python
class Person:
    age = 1

    def show_age(self):
        print('age', self.age)


print(Person.age)
p = Person()
print(p.age)
p.show_age()
# 输出
1
1
age 1
```

可以看到，对于类属性，不管是类本身，还是实例都可以访问到。
那我们添加一个实例属性

```python
class Person:
    age = 1

    def show_age(self):
        print('age', self.age)


print(Person.age)
p = Person()
print(p.age)
p.show_age()
p.height = 170
print(p.height)
print(Person.height)
# 输出
1
1
age 1
170
AttributeError: type object 'Person' has no attribute 'height'
```
可以看到，类是无法找到实例属性的。你可以通过子女找到父母，但你却无法通过父母确定它的孩子，父母可能有很多个孩子，而某个具体的孩子，他的父母是唯一确定的。

~~至于静态方法，因为它既无cls,也无self,所以它唯一的办法是只能通过类访问~~
可以通过类名访问：ClassName.static_method()
也可以通过类的实例访问：instance.static_method()

```python
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

# 通过类名调用
MyClass.static_method()

# 通过实例调用
obj = MyClass()
obj.static_method()

```

访问属性所用方法顺序

当获取属性时，无条件走`__getattribute__`,当属性获取失败，异常时，会尝试走`__getattr__`,相当于后备手段（不知是不是通常所说的防御型编程）。而`__get__`则针对当前类作为另一个类的类属性时调用，但注意：因为`__getattribute__`在获取属性(包括类属性)时无条件执行，所以会先走`__getattribte__`,从它执行的结果可以看到，先执行了`__getattribute__`,再是`__get__`

```python
# answer from gpt
"""
1.  首先查找实例的 `__dict__` 属性，如果找到了就返回该属性的值。
2.  如果没找到，就会查找类的 `__dict__` 属性，如果找到了就返回该属性的值。
3.  如果还没找到，就会递归地调用类的 `__getattribute__` 方法来查找属性。
4.  如果 `__getattribute__` 方法中调用了 `object.__getattribute__` 方法，则会再次查找实例的 `__dict__` 属性和类的 `__dict__` 属性。
5.  如果还是没找到，就会调用类的 `__getattr__` 方法，如果该方法存在的话。
6.  如果该属性是一个描述符（descriptor），那么就会调用描述符的 `__get__` 方法，获取描述符的值。
7.  最后如果还是没有找到该属性，就会抛出 `AttributeError` 异常。

 需要注意的是，当 `__getattribute__` 方法中调用实例的属性时，需要使用 `object.__getattribute__(self, name)` 方法，否则会导致递归调用，出现无限循环的错误。
"""

class Foo:
    class_var = "class var"

    def __init__(self):
        self.instance_var = "instance var"

    def __getattribute__(self, name):
        print(f"__getattribute__({name}) called")
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print(f"__getattr__({name}) called")

    class Descriptor:
        def __get__(self, instance, owner):
            print("__get__ called")
            return "descriptor value"

    descriptor = Descriptor()

foo = Foo()

# 查找实例属性，首先在 __dict__ 中查找
print(foo.instance_var)

# 查找类属性，首先在 __dict__ 中查找
print(foo.class_var)

# 查找不存在的实例属性，先调用 __getattribute__ 方法，再调用 __getattr__ 方法
print(foo.nonexistent_instance_var)

# 查找不存在的类属性，先调用 __getattribute__ 方法，再调用 __getattr__ 方法
print(foo.nonexistent_class_var)

# 查找描述符的值，先调用 __getattribute__ 方法，再调用 __get__ 方法
print(foo.descriptor)

```

### 描述器

```python

"""
描述一个属性的**增，改，删，查**操作，这个属性指向一个特殊的对象，如果实现了`__get__,__set__,__delete__`,那么将被解释器识别为一个描述器，此时如果你在外部试图对该属性进行增删改查，解释器将自动将这些动作进行转移，交给它的三个助手（__get__,__set__,__delete__）来处理。比如你想将一个人的年龄设置为负值，这显示不合情理，那在__set__中就可以对这种情况进行拦截（这是起验证的作用）
但为了进行设置，获取，删除下面这种方式也可以做到，为什么要描述器呢？
"""

class Person:
    def __init__(self):
        self.__age = 0
        
    def get_age(self):
        return self.__age
    
    def set_age(self,value):
        self.__age = value
        
    def del_age(self):
        del self.__age
```

这里可以看到，如果我要设置时必须显式的调用set_age方法，这样操作起来比较麻烦，而我们的习惯通过p.age=1这种方式进行设置操作。

##### 方式一
property

```python
class Person:
    def __init__(self):
        self.__age = 0

    def get_age(self):
        return self.__age

    def set_age(self, value):
        self.__age = value

    def del_age(self):
        del self.__age

    age = property(get_age, set_age, del_age)
```

##### 方式二

```python
class Person:
    def __init__(self):
        self.__age = 0

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            value = 0
        self.__age = value

    @age.deleter
    def age(self):
        del self.__age
```

##### 方式三
用另一个类来保存属性，下面我们看看调用方法中的instance, owner分别是什么

```python

class Age:

    def __set__(self, instance, value):
        print('__set__', instance, value)

    def __get__(self, instance, owner):
        print('__get__',instance,owner)

    def __delete__(self, instance):
        print('__del__')


class Person:
    age = Age()


p = Person()
p.age = -1
print(p.age)
# 输出
__set__ <__main__.Person object at 0x7f2d8cae2a90> -1
__get__ <__main__.Person object at 0x7f2d8cae2a90> <class '__main__.Person'>
None
```

稍加改进：

```python
class Age:

    def __set__(self, instance, value):
        print('__set__', instance, value)
        if value < 0:
            value = 0
        instance.__age = value

    def __get__(self, instance, owner):
        print('__get__',instance,owner)
        return instance.__age

    def __delete__(self, instance):
        print('__del__')
        del instance.__age


class Person:
    age = Age()


p = Person()
print(p)
p.age = -1
print(p.age)
# 输出
<__main__.Person object at 0x7fca538e2ac8>
__set__ <__main__.Person object at 0x7fca538e2ac8> -1
__get__ <__main__.Person object at 0x7fca538e2ac8> <class '__main__.Person'>
0
```

我们在设置值时进行了拦截，当值小于0，将被设置为0。
这里有一点需要注意，因为age是对所有Person了实例共享的，在Age类中，我们不能将值绑定给self,如果绑定给self,那么所有的实例都在修改同一份age,而通过内存地址我们可以看到Instance表示是p实例，我们应该将age绑定给p,这样每个实例对象有自己的age

一种常见的用法是，我们通过描述器将属性作为保护属性存储在类的内部，而将普通变量暴露给外部：

```python
class Age:

    def __set__(self, instance, value):
        print('__set__', instance, value)
        if value < 0:
            value = 0
        instance._age = value

    def __get__(self, instance, owner):
        print('__get__', instance, owner)
        return instance._age

    def __delete__(self, instance):
        print('__del__')
        del instance._age


class Person:
    age = Age()

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('Andy', 30)
print(p.__dict__)
# 输出
__set__ <__main__.Person object at 0x7f1673ce2ac8> 30
{'name': 'Andy', '_age': 30}
```

可以看到，在实例化时`self.age=age`调用了`__set__`方法，而且类内部保存的是`_age`属性。甚至你可以使用私有变量来保存。这里的age相当于暴露给外部的接口，用来访问，设置，删除。

如果一个对象定义了 __set__() 或 __delete__()，则它会被视为数据描述器。 仅定义了 __get__() 的描述器称为非数据描述器（它们经常被用于方法，但也可以有其他用途）



## 模块导入

 第一次导入时
- 在自己当下的命名空间中，执行所有的代码
- 创建一个模块对象，并将模块内所有的顶级变量每个属性的形式绑定到模块对象上
- 在import的位置，引入import后面的变量名称到当前 命名空间

 第二次导入时：
  只执行第一步导入时的第三步

**从哪个位置导入**
 

当Python代码导入模块时，会发生以下步骤：

1.  搜索模块：首先，Python会在sys.path变量中定义的目录中搜索要导入的模块。sys.path变量是一个包含要搜索的目录列表的字符串列表。如果找到了匹配的模块，Python就会停止搜索并继续执行下一步。如果找不到匹配的模块，Python会引发一个ImportError。
    
2.  编译模块：Python会将找到的模块的源代码编译为字节码。编译后的字节码会被缓存到__pycache__目录中，以便于下次导入时快速加载。
    
3.  执行模块：Python会执行编译后的字节码，这将导入模块的全局变量和函数。如果模块定义了__name__变量，Python会将该变量设置为模块的名称。模块的执行过程也可能会导入其他模块，这些模块会遵循相同的导入过程。
    
4.  创建模块对象：Python会创建一个模块对象，并将其添加到sys.modules缓存中。该模块对象包含了模块的全局命名空间和其他元数据。
    
5.  返回模块对象：导入完成后，Python会返回模块对象，这样我们就可以在我们的代码中使用模块中定义的变量和函数。
    

需要注意的是，当模块被导入时，它的代码会被执行。这意味着模块中的全局变量、函数、类等都会在导入时定义，而不是在第一次访问时才定义。因此，在编写模块时，需要注意不要编写会产生副作用的代码，例如修改全局状态或执行耗时的操作。


**从哪个位置导入**
- 内置模块
- 当前目录 （注意sys.path的第一个值也是当前目录）
- sys.path
- 环境变量（`PYTHONPATH` 环境变量）
- 安装路径的lib库
- 追加路径（修改sys.path, 环境变量等，添加.pth文件）

对于.pth文件的优先级，安装路径下的.pth文件>site-package>site-packge路径中的.pth文件

### 覆盖导入

当自定义的模块与内置模块同名时，我们导入的是内置模块，因为内置模块优先级最高上。
当自定义的模块与与非内置标准模块同名，这种两种情况都可能，两者路径都在sys.path中，谁在前就会导入谁，并覆盖后者。这种情况下，我们可以使用`from my_module import my_func`这种指定从哪个模块导入的方式，如果你写过celery可能会遇到这种情况，在celery中的一种解决方式是`from __future__ import absolute_import`

### 局部导入
在某个局部范围内导入,因为模块，函数，类等都会产生自己的命名空间，当我们在某个局部才导入模块，那么此模块的生命周期也仅仅在此范围
另一方面，导入模块也会消耗内存，耗时，有些模块只有某种特定情况下才需要，那么只要当那种情况发生时需要导入。

```python
def main():
    import module1
    pass
```

### 循环导入
循环导入要把握的要点：当遇到import时，会跳转到要导入的文件，然后把该文件内容全部执行一遍，并在导入的地方产生对应的命名空间，绑定导入的模块中的所有对象。这咱遇到import跳转的情况不仅仅发生在第一次导入时，当在要导入的文件中又遇到import时会再次跳转，当完成该次导入后再跳转回来，继续执行剩下的代码。如果已经有该模块的命名空间，则不会重复导入，但会绑定该模块中的还没有绑定的对象。

### 延迟导入
q.py
```python
def bar():
    print('bar in a.py')

def foo():
    from b import bar
    print('foo in a.py')
    bar()

```

b.py

```python
def foo():
    from a import bar
    print('foo in b.py')
    bar()
```

此时在b中执行foo则没有问题

### 可选导入
当两个模块api相同，我们想优先导入m1,如果m1导入失败再导入m2时，可以考虑可选导入的方式
```python
try:
    import m1 as m
except ModuleNotFoundError:
    import m2 as m
    
m1.run()
```
我们导入后，将两个模块都取相同的别名，因为api一样，这样我们就可以在导入后使用统一的调用

### 包内导入

```
├── mod1
│   ├── __init__.py
│   ├── lib1.py
│   └── lib2.py
├── test.py

```
lib1.py
```python
name = 'lib1'
```

lib2.py
```python
from . import lib1

name = 'lib2'
print(lib1.name)
```

test.py
```python
from mod1 import lib1 ,lib2

print(lib1.name)
print(lib2.name)
```

包内导入，在python3中，默认是绝对导入，当我们使用`.`导入时，是按照包的路径来导的，在外部的test.py中导入lib1,lib2，并使用其中的变量。此时无法使用相对导入，但lib1,lib2是在Mod1包内，可以使用相对导入，在lib2中我们使用相对导入，mod1.lib, mod1.lib2, 在lib2中使用相对导入即从“点”查找，即从lib2,找到mod1,而mod1中是能找到lib1的，所以能正常导入，**但是** 如果我们直接运行lib1.py则会报错，因为直接运行的话，当前`__name__ == '__main__'` 而它没有`.`路径，所以无法找到，同样的原理，如果我们想在lib1,或者lib2中导入外层的test同级的文件，则无法导入，因为mod只到了mod1,再上一层没有mod，（不能简单的将相对导入理解为路径的上一层 ）


## 错误与异常

主要的异常类：
ZeroDevisionError
NameError
TypeError
IndexError
KeyError
ValueError
AttributeError
StopIteration

异常继承
BaseException:
    - SystemExit
    - KeyboardInterrupt
    - GeneratorExit
    - Exception


### 解决方案
#### 方案一：try except

```python
try:
    pass
except (except1,except2) as e:
    pass
except except3 as e:
    pass
else:
    pass
finally:
    pass
```

#### 方案二：with 

with语句
```python 
with open('f','r',encoding='utf-8') as fp:
    fp.read()

# 转换成上下文管理器
class Test:
    def __enter__(self):
        return self
    def __exit__(self,exc_type,exc_val,exc_tb):
        pass
```

#### 方案三：contextlib

contextlib

```python
import contextlib

@contextlib.contextmanager
def test():
	print(1)
	yield
	print(2)

with test() as t:
	print(3)
```

在yield之前的相当于在`__enter__`执行， yield之后 的则在`__exit__`执行， 使用时的`print(3)`则在yeild处执行

处理错误
```python
import contextlib.contextmanager

@contextlib.contextmanager
def ze():
	try:
		yield
	except ZeroDevisionError as e:
		print('error',e)
```

代码会走到try,然后执行，然后是捕获except 这样在需要使用的地方变成了：

```python
with ze():
    a/b
```
这样就能捕获异常

#### contextlib.closing
contextlib.closing会默认调用对象内部的close方法：
```python
import contextlib


class Test(object):

    def close(self):
        print('close')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

with Test() as t:
	t.run()

# 使用contextlib.closing就不需要实现__enter__, __exit__方法
with contextlib.closing(Test()) as t:
    t.run()
```

#### contextlib嵌套使用

with 可以嵌套使用，也可以转化成contextlib
```python
with open('src.txt','r') as source:
	with open('tar.txt', 'w') as target:
		src_content = source.read()
		target.write(src_content)

# 使用contextlib写法
import contextlib

with open('src.txt', 'r') as source, open('tar.txt','w') as target:
	src_content = source.read()
	target.write(src_content)
```

## 进程线程协程
### 进程

进程是计算机中的程序执行实例，是操作系统分配资源的和调度基本单位。

#### 进程创建的方式

**multiprocessing**(推荐)

```python
from multiprocessing import Process

def func():
    print(12345)

if __name__ == '__main__': 
    p = Process(target=func,) 
    p.start() 
    print('*' * 10) 
#########################################################
def worker(num):
    return f"Result: {num * num}"

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(worker, range(10))
        print(results)
```

也可以继承Process类

**concurrent.futures**
concurrent.futures 提供了一个高层次的接口，可方便地启动和管理多进程及多线程。使用 ProcessPoolExecutor 可以快速创建多个进程

```python
from concurrent.futures import ProcessPoolExecutor

def worker(name):
   return f'Worker: {name}'

if __name__ == '__main__':
   with ProcessPoolExecutor() as executor:
	   futures = [executor.submit(worker, f'Alice-{i}') for i in range(5)]
	   for future in futures:
		   print(future.result())
   
```


**subprocess**

```python
import subprocess

result = subprocess.run(['ls', '-l'], capture_output=True, text=True)
print(result.stdout)
   
```

#### 守护进程

前面我们讲的子进程是不会随着主进程的结束而结束，子进程全部执行完之后，程序才结束，那么如果有一天我们的需求是我的主进程结束了，由我主进程创建的那些子进程必须跟着结束，怎么办？守护进程就来了！

主进程创建守护进程
其一：守护进程会在主进程代码执行结束后就终止
其二：守护进程内无法再开启子进程,否则抛出异常：AssertionError: daemonic processes are not allowed to have children

**注意**：

```python
import os
import time
from multiprocessing import Process

class Myprocess(Process):
    def __init__(self,person):
        super().__init__()
        self.person = person
        
    def run(self):
        print(os.getpid(),self.name)
        print('%s正在和女主播聊天' %self.person)
        time.sleep(3)
        
if __name__ == '__main__':
    p=Myprocess('太白')
    p.daemon=True #一定要在p.start()前设置,设置p为守护进程,禁止p创建子进程,并且父进程代码执行结束,p即终止运行
    p.start()
    # time.sleep(1) # 在sleep时linux下查看进程id对应的进程ps -ef|grep id
    # p.join()
    print('主')
```

#### 进程同步

实现了程序的异步，让多个任务可以同时在几个进程中并发处理，他们之间的运行没有顺序，一旦开启也不受我们控制。尽管并发编程让我们能更加充分的利用IO资源，但是也给我们带来了新的问题：进程之间数据不共享,但是共享同一套文件系统,所以访问同一个文件,或同一个打印终端,是没有问题的，而共享带来的是竞争，竞争带来的结果就是错乱，如何控制，就是加锁处理。

```python
import os
import time
import random
from multiprocessing import Process

def work(n):
    print('%s: %s is running' %(n,os.getpid()))
    time.sleep(random.random())
    print('%s:%s is done' %(n,os.getpid()))

if __name__ == '__main__':
    for i in range(5):
        p=Process(target=work,args=(i,))
        p.start()
```
结果

```
# 看结果：通过结果可以看出两个问题：问题一：每个进程中work函数的第一个打印就不是按照我们for循环的0-4的顺序来打印的
#问题二：我们发现，每个work进程中有两个打印，但是我们看到所有进程中第一个打印的顺序为0-2-1-4-3，但是第二个打印没有按照这个顺序，变成了2-1-0-3-4，说明我们一个进程中的程序的执行顺序都混乱了。
# 问题的解决方法，第二个问题加锁来解决，第一个问题是没有办法解决的，因为进程开到了内核，有操作系统来决定进程的调度，我们自己控制不了
# 0: 9560 is running
# 2: 13824 is running
# 1: 7476 is running
# 4: 11296 is running
# 3: 14364 is running

# 2:13824 is done
# 1:7476 is done
# 0:9560 is done
# 3:14364 is done
# 4:11296 is done
```
解决办法，加锁

上述示例加锁

```python
#由并发变成了串行,牺牲了运行效率,但避免了竞争
from multiprocessing import Process,Lock
import os,time
def work(n,lock):
    #加锁，保证每次只有一个进程在执行锁里面的程序，这一段程序对于所有写上这个锁的进程，大家都变成了串行
    lock.acquire()
    print('%s: %s is running' %(n,os.getpid()))
    time.sleep(1)
    print('%s:%s is done' %(n,os.getpid()))
    #解锁，解锁之后其他进程才能去执行自己的程序
    lock.release()
if __name__ == '__main__':
    lock=Lock()
    for i in range(5):
        p=Process(target=work,args=(i,lock))
        p.start()
```

 条件变量

```python
!/usr/bin/python  
# coding:utf-8  
import time  
from multiprocessing import Process, Condition  
  
  
def worker(condition):  
    print('inside worker')  
    with condition:  
        print("Worker is waiting")  
        condition.wait()  
        print("Worker is done waiting")  
  
  
def main():  
    condition = Condition()  
    p = Process(target=worker, args=(condition,))  
    p.start()  
    time.sleep(4) # 如果不等待，主线程执行到notify,而子线程还没起来，会导致子线
    # 一直卡在那里等待 
    with condition:  
        print("Main is notifying worker")  
        condition.notify()  
    p.join()  
  
  
if __name__ == '__main__':  
    main()
inside worker
Worker is waiting
Main is notifying worker
Worker is done waiting
```

#### 进程通信

 队列

进程彼此之间互相隔离，要实现进程间通信（IPC），multiprocessing模块支持两种形式：队列和管道，这两种方式都是使用消息传递的。队列就像一个特殊的列表，但是可以设置固定长度，并且从前面插入数据，从后面取出数据，先进先出。

**队列的方法介绍**

```
q = Queue([maxsize]) 
创建共享的进程队列。maxsize是队列中允许的最大项数。如果省略此参数，则无大小限制。底层队列使用管道和锁定实现。另外，还需要运行支持线程以便队列中的数据传输到底层管道中。 
Queue的实例q具有以下方法：

q.get( [ block [ ,timeout ] ] ) 
返回q中的一个项目。如果q为空，此方法将阻塞，......项目可用为止。block用于控制阻塞行为，默认为True. 如果设置为False，将引发Queue.Empty异常（定义在Queue模块中）。timeout是可选超时时间，用在阻塞模式中。如果在制定的时间间隔内没有项目变为可用，将引发Queue.Empty异常。

q.get_nowait( ) 
同q.get(False)方法。

q.put(item [, block [,timeout ] ] ) 
将item放入队列。如果队列已满，此方法将阻塞至有空间可用为止。block控制阻塞行为，默认为True。如果设置为False，将引发Queue.Empty异常（定义在Queue库模块中）。timeout指定在阻塞模式中等待可用空间的时间长短。超时后将引发Queue.Full异常。

q.qsize() 
返回队列中目前项目的正确数量。此函数的结果并不可靠，因为在返回结果和在稍后程序中使用结果之间，队列中可能添加或删除了项目。在某些系统上，此方法可能引发NotImplementedError异常。


q.empty() 
如果调用此方法时 q为空，返回True。如果其他进程或线程正在往队列中添加项目，结果是不可靠的。也就是说，在返回和使用结果之间，队列中可能已经加入新的项目。

q.full() 
如果q已满，返回为True. 由于线程的存在，结果也可能是不可靠的（参考q.empty（）方法）。
```

队列的简单使用

```python
from multiprocessing import Queue
q=Queue(3) #创建一个队列对象，队列长度为3

#put ,get ,put_nowait,get_nowait,full,empty
q.put(3)   #往队列中添加数据
q.put(2)
q.qsize  查看当前队列中已使用的长度 -- 2
q.put(1)
# q.put(4)   # 如果队列已经满了，程序就会停在这里，等待数据被别人取走，再将数据放入队列。
           # 如果队列中的数据一直不被取走，程序就会永远停在这里。
try:
    q.put_nowait(4) # 可以使用put_nowait，如果队列满了不会阻塞，但是会因为队列满了而报错。
except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去，但是会丢掉这个消息。
    print('队列已经满了')

# 因此，我们再放入数据之前，可以先看一下队列的状态，如果已经满了，就不继续put了。
print(q.full()) #查看是否满了，满了返回True，不满返回False
print(q.get())  #取出数据
print(q.get())
print(q.get())
# print(q.get()) # 同put方法一样，如果队列已经空了，那么继续取就会出现阻塞。
try:
    q.get_nowait(3) # 可以使用get_nowait，如果队列满了不会阻塞，但是会因为没取到值而报错。
except: # 因此我们可以用一个try语句来处理这个错误。这样程序不会一直阻塞下去。
    print('队列已经空了')

print(q.empty()) #空了
```

子/主进程通过队列进行通信

```python
#看下面的队列的时候，按照编号看注释
import time
from multiprocessing import Process, Queue

def f(q):
    q.put('姑娘，多少钱~')  
    # print(q.qsize()) #查看队列中有多少条数据了

def f2(q):
    print('》》》》》》》》')
    print(q.get())  
    
if __name__ == '__main__':
    q = Queue() 
    q.put('小鬼')

    p = Process(target=f, args=(q,)) 
    p2 = Process(target=f2, args=(q,)) 
    p.start()
    p2.start()
    time.sleep(1) 
    print(q.get()) #结果：姑娘，多少钱~
    p.join()
```
输出:
```
》》》》》》》》
小鬼
姑娘，多少钱~
```


#### 进程间共享数据

documentations: [multiprocessing --- 基于进程的并行 — Python 3.11.1 文档](https://docs.python.org/zh-cn/3/library/multiprocessing.html)

 1、共享内存：
  共享内存有局限，只有Value, Array

最近刚写了爬bing壁纸的个小脚本，但一直使用的单进程，比较慢，然后在尝试使用多进程，但为了计数count,一直没找到比较好的方法，最后还尝试使用了aiohttp，都没能解决这个问题。只好翻官方文档：

```python
import random  
import time  
from multiprocessing import Value, Process, Lock  
  
  
def f1(n, lock):  
    time.sleep(2)  
    lock.acquire()  
    n.value += 1  
    lock.release()  
    # 这里不能直接用n.value += 1而不加锁
    # 但可以通过
    with n.get_lock():
        n.value += 1
  
def main():  
    lock = Lock()  
    num = Value('i', 0)  
    ps = []  
    for i in range(2):  
        p = Process(target=f1, args=(num, lock))  
        p.start()  
        ps.append(p)  
  
    for i in ps:  
        i.join()  
    print(num.value)  
  
  
if __name__ == '__main__':  
    main()
```

这里在两个不同的里程里修改同一个变量num,开始使用的是`time.sleep(2,5)` 然后每次数字都能正常返回2，让我产生了进程安全的错觉，当我将其改成`time.sleep(2)` 之后 就只返回1了，很明显，同时修改数据不安全。只能通过上锁的方式保证。

Ref: value 对象的 types类型：
[array --- 高效的数值数组 — Python 3.11.1 文档](https://docs.python.org/zh-cn/3/library/array.html#module-array)

Manager 代理
Manager的优势是可以存任意pickelable的数据，即支持所有python数据类型

```python
import time  
from multiprocessing import Value, Process, Lock, Manager  
  
  
def f1(n, lock):  
    time.sleep(2)  
    lock.acquire()  
    n['value'] += 1  
    lock.release()  
  
  
def main():  
    lock = Lock()  
    with Manager() as manager:  
        d = manager.dict()  # count = manager.Value('i',0)
        d['value'] = 0   
        ps = []  
        for i in range(10):  
            p = Process(target=f1, args=(d, lock))  
            p.start()  
            ps.append(p)  
  
        for i in ps:  
            i.join()  
        # 注意要在内部打印，否则是取不到值
        print(d['value'])  
  
  
if __name__ == '__main__':  
    main()
```

同样的，Manager 并不能保证数据安全，也需要用锁。

### 线程

线程是进程内的执行单元，是操作系统调度的最小单位

threading模块的完全模仿了multiprocess模块的接口，二者在使用层面，有很大的相似性，因而不再详细介绍（[官方链接](https://docs.python.org/3/library/threading.html?highlight=threading#)）

#### 线程创建的方式

**threading**

```python
import time
from threading import Thread

def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('太白',))
    t.start()
    print('主线程')
```

也可以继承Thread类

**concurrent.futures**
concurrent.futures模块提供了一个更高级的接口，可以方便地管理线程池
   
```python
   from concurrent.futures import ThreadPoolExecutor

   def task(n):
       print(f"Task {n} running")

   with ThreadPoolExecutor(max_workers=5) as executor:
       for i in range(5):
           executor.submit(task, i)
   
```

同一进程中的线程是资源共享的

```python
import os

from  threading import Thread

n=100

def work():
    global n  #修改全局变量的值
    n += 1 
    print(n) # 101

if __name__ == '__main__':

    n=1
    t=Thread(target=work)
    t.start()
    t.join()   #必须加join，因为主线程和子线程不一定谁快，一般都是主线程快一些，所有我们要等子线程执行完毕才能看出效果
    print('主',n) #查看结果为101,因为同一进程内的线程之间共享进程内的数据
# 通过一个global就实现了全局变量的使用，不需要进程的IPC通信方法
```

**进程和线程的区别**
```
进程是最小的内存分配单位
线程是操作系统调度的最小单位

线程被CPU执行了

进程内至少含有一个线程
进程中可以开启多个线程　

开启一个线程所需要的时间要远小于开启一个进程　

全局变量在多个线程之间是共享的
```

#### 其他常用方法

```
Thread实例对象的方法
  # getName(): 返回线程名。
  # setName(): 设置线程名。

threading模块提供的一些方法：
  # threading.currentThread(): 返回当前的线程对象。
  # threading.get_ident():  获取线程id
```

**简单示例**

```python
import threading, time

def run(n):
    print('-'*30)
    print("Pid is :%s" % threading.get_ident())  # 返回线程pid

if __name__ == '__main__':
    threading.main_thread().setName('Chengd---python')    #自定义线程名
    for i in range(3):
        thread_alive = threading.Thread(target=run, args=(i,))
        thread_alive.start()
    thread_alive.join()
    print('\n%s thread is done...'% threading.current_thread().getName())    #获取线程名
```

**结果**

```
Pid is :140410400802560
------------------------------
------------------------------
Pid is :140410392348416
Pid is :140410383894272

Chengd---python thread is done...
```


join方法

用来等待子线程运行结束。
```python
import time
from threading import Thread

def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('太白',))
    t2=Thread(target=sayhi,args=('alex',))
    t.start()
    t2.start()
    t.join()  #因为这个线程用了join方法，主线程等待子线程的运行结束

    print('主线程')
    print(t.is_alive())  #所以t这个线程肯定是执行结束了，结果为False
    print(t2.is_alive()) #有可能是True，有可能是False，看子线程和主线程谁执行的快
```

**结果**

```
第一次：
太白 say hello
alex say hello
主线程
False
False
第二次
太白 say hello
主线程
False
True
alex say hello
```

join会让主线程等待子线程结束，才继续执行主线程的代码，可能全程序变成线性执行。如果主线程中有死循环或者阻塞会等待（即确定不会比子线程更早结束，例如阻塞等待子线程的结果）的情况，则无需join.

#### 守护线程

**无论是进程还是线程，都遵循：守护xx会等待主xx运行完毕后被销毁。需要强调的是：运行完毕并非终止运行**

#1.对主进程来说，运行完毕指的是主进程代码运行完毕
#2.对主线程来说，运行完毕指的是主线程所在的进程内所有非守护线程统统运行完毕，主线程才算运行完毕

**详细解释**

```
主进程在其代码结束后就已经算运行完毕了（守护进程在此时就被回收）,然后主进程会一直等非守护的子进程都运行完毕后回收子进程的资源(否则会产生僵尸进程)，才会结束，

主线程在其他非守护线程运行完毕后才算运行完毕（守护线程在此时就被回收）。因为主线程的结束意味着进程的结束，进程整体的资源都将被回收，而进程必须保证非守护线程都运行完毕后才能结束，因为进程执行结束是要回收资源的，所有必须你里面的非守护子线程全部执行完毕。
```

**守护线程使用示例**

```python
from threading import Thread
import time
def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('taibai',))
    t.setDaemon(True) #必须在t.start()之前设置
    t.start()

    print('主线程')
    print(t.is_alive())
    '''
    主线程
    True
    '''
```


#### 线程队列

线程之间的通信我们列表行不行呢，当然行，那么队列和列表有什么区别呢？

​queue队列 ：使用import queue，用法与进程Queue一样

​queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.

**先进先出**
```python
import queue #不需要通过threading模块里面导入，直接import queue就可以了，这是python自带的
#用法基本和我们进程multiprocess中的queue是一样的
q=queue.Queue()
q.put('first')
q.put('second')
q.put('third')

# q.put_nowait() #数据多了就报错，可以通过try来搞
print(q.get())
print(q.get())
print(q.get())
# q.get_nowait() #没有数据就报错，可以通过try来搞
'''
结果(先进先出):
first
second
third
'''
```

队列是线程安全的，不会出现多个线程抢占同一个资源或数据的情况。

```python
import queue  
from threading import Thread, Lock  
  
  
def f1(q, ):  
    time.sleep(2)  
    x = q.get()  
    x += 1  
    q.put(x)  
  
  
q = queue.Queue()  
q.put(0)  
  
  
def main():  
    ps = []  
    for i in range(15):  
        p = Thread(target=f1, args=(q,))  
        p.start()  
        ps.append(p)  
  
    for i in ps:  
        i.join()  
    print(q.get())  
  
  
if __name__ == '__main__':  
    main()
```
#### 数量级导致不同的线程表现

```python
import threading  
  
  
a = 0  
  
  
def func(index):  
    global a  
    # with threading.Lock():  
    #     for i in range(10000):    #         a+=1    
    for i in range(1000000):  
        a = a+1  
    print(index, a)  
  
  
t_1 = threading.Thread(target=func, args=[1])  
t_1.start()  
  
  
t_2 = threading.Thread(target=func, args=[2])  
t_2.start()  
  
  
t_3 = threading.Thread(target=func, args=[3])  
t_3.start()  
  
t_1.join()  
t_2.join()  
t_3.join()  
print('全局', a)
```

下面看另一种情况，通过循环来创建线程：

```python
from threading import Thread, Lock  
  
a = 0  
  
  
def f1(x, ):  
    global a  
    for i in range(100000):  
        a += 1  
    print(x, a)  
  
  
def main():  
    ps = []  
    for i in range(3):  
        p = Thread(target=f1, args=(i,))  
        p.start()  
        ps.append(p)  
  
    for i in ps:  
        i.join()  
    print(a)
```

刚开始，上面第一段代码会导致线程安全问题，而下面的代码则“表现出线程安全”

这里有个坑就是，上面的代码从逻辑上讲与下面的代码完全是一样的，
这里不管使用：`a +=1  a=a+x` 效果一样，实际的影响因素是： 100000 与1000000 
的区别，当将100000逐渐调大，就会出现线程抢占导致的数据安全问题（不同电脑可能有不同表现）

但是下面这个链接有个不同的情况：所说python 3.10已经解决了这个问题，是因为中断的问题，不过太深，没有仔细研究。

[python - Python3.10 下为什么没有多线程自增安全问题了？ - SegmentFault 思否](https://segmentfault.com/q/1010000041987131)


### 协程

**协程介绍**

协程的目的是基于单线程来实现并发，即只用一个主线程（很明显可利用的cpu只有一个）情况下实现并发，为此我们需要先回顾下并发的本质：切换+保存状态

cpu正在运行一个任务，会在两种情况下切走去执行其他的任务（切换由操作系统强制控制），一种情况是该任务发生了阻塞，另外一种情况是该任务计算的时间过长或有一个优先级更高的程序替代了它

协程本质上就是一个线程，以前线程任务的切换是由操作系统控制的，遇到I/O自动切换，现在我们用协程的目的就是较少操作系统切换的开销（开关线程，创建寄存器、堆栈等，在他们之间进行切换等），在我们自己的程序里面来控制任务的切换。

协程：是单线程下的并发，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：**协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。**

**协程就是告诉Cpython解释器，不是搞了个GIL锁吗，那好，我就自己搞成一个线程让你去执行，省去你切换线程的时间，我自己切换比你切换要快很多，避免了很多的开销，对于单线程下，我们不可避免程序中出现io操作，但如果我们能在自己的程序中（即用户程序级别，而非操作系统级别）控制单线程下的多个任务能在一个任务遇到io阻塞时就切换到另外一个任务去计算，这样就保证了该线程能够最大限度地处于就绪态，即随时都可以被cpu执行的状态，相当于我们在用户程序级别将自己的io操作最大限度地隐藏起来，从而可以迷惑操作系统，让其看到：该线程好像是一直在计算，io比较少，从而更多的将cpu的执行权限分配给我们的线程。**

#### yield | async 实现协程

上述的情况并不能提升效率，只是为了让cpu能够雨露均沾，实现看起来所有任务都被“同时”执行的效果，如果多个任务都是纯计算的，这种切换反而会降低效率。为此我们可以基于yield来验证。yield本身就是一种在单线程下可以保存任务运行状态的方法。

任务切换+保存状态 = 并发

```python
import time

def func1():
    for i in range(11):
        #yield
        print('这是我第%s次打印啦' % i)
        time.sleep(1)

def func2():
    g = func1()
    #next(g)
    for k in range(10):
        print('哈哈，我第%s次打印了' % k)
        time.sleep(1)
        #next(g)

#不写yield，下面两个任务是执行完func1里面所有的程序才会执行func2里面的程序，有了yield，我们实现了两个任务的切换+保存状态
func1()
func2()

######################################################################

import asyncio

# 定义一个协程
async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # 模拟耗时操作
    print("World!")

# 运行协程
async def main():
    await say_hello()

# 执行主协程
if __name__ == "__main__":
    asyncio.run(main())

```

总结协程特点：

1. **必须在只有一个单线程里实现并发**
2. **修改共享数据不需加锁**  (非抢占式的并发)
3. **用户程序里自己保存多个控制流的上下文栈**
4. **附加：一个协程遇到IO操作自动切换到其它协程(gevent模块来实现)**

#### gevent模块
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是**Greenlet**, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

**常用方法**

```python
#用法
g1=gevent.spawn(func,1,2,3,x=4,y=5)创建一个协程对象g1，spawn括号内第一个参数是函数名，如eat，后面可以有多个参数，可以是位置实参或关键字实参，都是传给函数eat的，spawn是异步提交任务

g2=gevent.spawn(func2)

g1.join() #等待g1结束

g2.join() #等待g2结束  有人测试的时候会发现，不写第二个join也能执行g2，是的，协程帮你切换执行了，但是你会发现，如果g2里面的任务执行的时间长，但是不写join的话，就不会执行完等到g2剩下的任务了

#或者上述两步合作一步：gevent.joinall([g1,g2])

g1.value#拿到func1的返回值
```

**遇到IO阻塞时会自动切换任务**

看示例：

```python
import gevent

def eat(name):
    print('%s eat 1' %name)
    gevent.sleep(2)
    print('%s eat 2' %name)

def play(name):
    print('%s play 1' %name)
    gevent.sleep(1)
    print('%s play 2' %name)

g1=gevent.spawn(eat,'egon')
g2=gevent.spawn(play,name='egon')
g1.join()
g2.join()
#或者gevent.joinall([g1,g2])
print('主')
```
**结果**
egon eat 1
egon play 1
egon play 2
egon eat 2
主

**上例gevent.sleep(2)模拟的是gevent可以识别的io阻塞,**
**而time.sleep(2)或其他的阻塞,gevent是不能直接识别的需要用下面一行代码,打补丁,就可以识别了**

**或者我们干脆记忆成：要用gevent，需要将from gevent import monkey;monkey.patch_all()放到文件的开头**

**看示例**

```python
from gevent import monkey;
monkey.patch_all() #必须写在最上面，这句话后面的所有阻塞全部能够识别了

import gevent  #直接导入即可
import time

def eat():
    #print()　　
    print('eat food 1')
    time.sleep(2)  #加上mokey就能够识别到time模块的sleep了
    print('eat food 2')

def play():
    print('play 1')
    time.sleep(1)  #来回切换，直到一个I/O的时间结束，这里都是我们个gevent做得，不再是控制不了的操作系统了。
    print('play 2')

g1=gevent.spawn(eat)
g2=gevent.spawn(play_phone)
gevent.joinall([g1,g2])
print('主')
```

#### gevent模块的应用示例

**示例1：爬虫**

```python
from gevent import monkey;monkey.patch_all()
import gevent
import requests
import time

def get_page(url):
    print('GET: %s' %url)
    response=requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' %(len(response.text),url))


start_time=time.time()
gevent.joinall([
    gevent.spawn(get_page,'https://www.python.org/'),
    gevent.spawn(get_page,'https://www.yahoo.com/'),
    gevent.spawn(get_page,'https://github.com/'),
])

stop_time=time.time()
print('run time is %s' %(stop_time-start_time))
```

**示例2**
通过gevent实现单线程下的socket并发（from gevent import monkey;monkey.patch_all()一定要放到导入socket模块之前，否则gevent无法识别socket的阻塞）

一个网络请求里面经过多个时间延迟time

**服务端代码**

```python
from gevent import monkey;monkey.patch_all()
from socket import *
import gevent

#如果不想用money.patch_all()打补丁,可以用gevent自带的socket
# from gevent import socket
# s=socket.socket()

def server(server_ip,port):
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((server_ip,port))
    s.listen(5)
    while True:
        conn,addr=s.accept()
        gevent.spawn(talk,conn,addr)

def talk(conn,addr):
    try:
        while True:
            res=conn.recv(1024)
            print('client %s:%s msg: %s' %(addr[0],addr[1],res))
            conn.send(res.upper())
    except Exception as e:
        print(e)
    finally:
        conn.close()

if __name__ == '__main__':
    server('127.0.0.1',8080)
```

**客户端代码**

```python
from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))


while True:
    msg=input('>>: ').strip()
    if not msg:continue

    client.send(msg.encode('utf-8'))
    msg=client.recv(1024)
```


