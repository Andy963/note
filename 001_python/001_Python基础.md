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

自带venv的使用：

```shell
python -m venv "venv_name"
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

### 删除元组

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

### 添加元素
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


## 栈 Stack
栈的一个常见应用就是浏览器的前进后退,每访问一个网页,这条记录就被放在一个栈中,当前页在最栈顶,最早访问的URL则放在栈底. 后退一次,取出一个,前进一次加入一个.

```python

from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(sysmbolString) and balanced:
        symbol = symbolString[index]
        # 左括号入栈
        if symbol == "(":
            s.push(symbol)
        else:
            # 如果是右括号，且栈是空的，则返回False
            if s.isEmpty():
                balanced = False
            else:
            # 是右括号，且栈不为空，那么栈顶一定是左括号，所以将栈顶元素出栈
                s.pop()
        index = index + 1
   if balanced and s.isEmpty():
       return True
   else:
       return False
       
```

为实现对不同括号的匹配，我们修改上面的函数：

```python

from pythonds.basic import Stack


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
                if not match(symbol, s.peek()):
                    balanced = False
        index = index + 1


    if balanced and s.isEmpty():
        return True
    else:
        return False

def match(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)
```

进制转换：

```python

from pythonds.basic import Stack

def divideBy2(decNumber):
    remstack = Stack()
    
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber // 2
    binString = ""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString
```

当换成其它进制时，比如16进制，表示时有一点问题，那么就需要考虑加入其它字符串来表示，否则余数就有两位会出错

```python

from pythonds.basic import Stack

def divideBy2(decNumber, base=2):
    digits = "0123456789ABCDEF"
    remstack = Stack()

    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    binString = ""
    while not remstack.isEmpty():
        binString = binString +  digits[remstack.pop()]
    return binString
```

## 流程控制

python中没有三元运算，但可用if else 代替

```python
rs = 'yes' if True else 'no'
rs
Out[4]: 'yes'
```

注意这种简化版与js中三目运算 [[001_Basic#^376bba]]是有区别的,与golang中[[04_流程控制#^znroy7]]也是有区别的
### 循环
while循环，当条件成立，就会一直执行，即死循环。

```python
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
print("1 到 %d 之和为: %d" % (n,sum))
```
while 循环中可以使用else,即条件不成立，循环无法继续时会执行：
> 1. while循环的else子句会在循环正常结束时执行。
2. "正常结束"指的是循环条件变为False，而不是通过break语句跳出循环。
3. 如果循环是因为break语句而终止的，else子句不会执行。
4. 如果while循环的条件一开始就是False，else子句仍然会执行。

```python
count = 0
while count < 5:
   print (count, " 小于 5")
   count = count + 1
else:
   print (count, " 大于或等于 5")
```


### 可迭代对象
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

- **iter**(): 返回迭代器对象本身
- **next**(): 返回容器中的下一个元素,如果没有更多元素则抛出 StopIteration 异常

2. 迭代器的特点:

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

####send
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

## 函数与类

### 函数
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
本质是一个函数，它接受一个函数作为输入，并返回另一个函数.装饰器通常使用闭包来记住原始函数，并在新函数中调用它.
不影响原有函数的功能,还能添加新的功能

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

上面是使用函数作为装饰器的情形，下面看看使用类作为装饰器的情形：
使用为作为装饰器本质上还是使用的函数，只不过形式上是类

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

我们在装饰时是使用的实例化对象，这样有一点好处是方便传入参数

#### 案例

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


### 类

#### 创建类的方式 
- 常见方式

```python
class Person:
	age = 0
	def run(self):
		pass
```
- 通过type创建

```python
def run(self):
	print('---',self)

# xxx是类名,Human则是类属性 name的值,所以外部无法直接访问Human
xxx = type("Human",(),{"age":0,"run":run})
print(xxx.__dict__)
xxx.run('10km')

{'age': 0, 'run': <function run at 0x7fafdb457ca0>, '__module__': '__main__', '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None}
--- 10km
```

通过metaclass 创建

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

#### 属性

##### 私有化属性
_var 受保护的属性:
    - 类内部可以访问
    - 子类内部可以 访问
    - 模块内其他位置访问 : 类,实例均无法访问
    - 跨模块访问: import 导入可以访问,但会提示,  from module import * 导入则无法访问,会报错(如果指定在__all__中则可以导入,如果没有在__all___列表中则报错).

__var 私有属性

##### 只读属性

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

##### 内置属性

```python
__dict__ # 类的属性
__bases__ # 类的父类所构成的元组
__doc__ # 文档
__name__ # 类名
__module__ # 定义所在的模块 
```


#### 方法
在python中类有三种不同方法：实例方法，类方法，静态方法.这三种方法通过第一个参数的类型来进行区分，实例方法的第一个参数为为的实例对象，类方法的第一个参数为类对象，而静态方法不要求参数，与变通函数无异。
静态方法,类方法,普通实例方法都是存储在类中,而不会存储在对象中

##### 实例方法
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

##### 类方法
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

##### 静态方法
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

##### 内置方法 

###### __call__ 
让对象具备被调用的能力

```python
class Person:
	def __call__(self):
		print("run")

p = Person()
p()
run
```

flask orm中的 sessionmaker 就用到了__call__ [[005_SqlAlchemy#用session做数据的增删改查操作：]]  源码如下：

```python
class sessionmaker(_SessionClassMethods):
    

	def __call__(self, **local_kw):  
	    """Produce a new :class:`.Session` object using the configuration  
	    established in this :class:`.sessionmaker`.  
	    In Python, the ``__call__`` method is invoked on an object when    it is "called" in the same way as a function::  
	        Session = sessionmaker()        session = Session()  # invokes sessionmaker.__call__()  
	    """    for k, v in self.kw.items():  
	        if k == "info" and "info" in local_kw:  
	            d = v.copy()  
	            d.update(local_kw["info"])  
	            local_kw["info"] = d  
	        else:  
	            local_kw.setdefault(k, v)  
	    return self.class_(**local_kw)
```

应用场景:类似偏函数

```python
def create_pen(p_type,p_color):
	print(f"create a {p_color}-{p_type}")


create_pen('钢笔','红色')
create_pen('钢笔','黑色')

from functools import partial

def create_pen(p_color,p_type):
	print(f"create a {p_color}-{p_type}")


# create_pen('钢笔','红色')
# create_pen('钢笔','黑色')

# 这种情况会导致出错,可以将p_type参数换到后面的位置
# gangPen = partial(create_pen,p_type="钢笔")
# gangPen('黄色')
# gangPen('绿色')


# 针对上面的偏函数,可以通过面向对象的方式实现
class PenFactory:
	def __init__(self,p_type):
		self.p_type = p_type

	def __call__(self,p_color):
		print(f"create a {p_color} - {self.p_type}")

pencilFac = PenFactory('铅笔')
pencilFac('红色')
pencilFac('黄色')
#create a 红色 - 铅笔
#create a 黄色 - 铅笔
```

###### 切片

```python

class Person:
	def __init__(self):
		self.items = [1,2,3,4,5,5,6,7]

	def __setitem__(self,key,value):
		# print(key.start)
		# print(key.stop)
		# print(key.step)
		# print(value)
		# 防止传入的key为字符串类型的情况
		# slice为内置类,直接用即可
		if isinstance(key,slice):
			self.items[key.start:key.stop:key.step] = value

	def __getitem__(self,item):
		print("getitem",item)

	def __delitem__(self,key):
		print("delete item",key)

p = Person()
p[0:3:1] = ['a','b']
print(p.items)
# 只能修改,否则为空,无法修改
# ['a', 'b', 4, 5, 5, 6, 7]
```

###### 遍历操作

1. __iter__() 方法：
   ⦁ 这是实现迭代的首选方法。
   ⦁ 如果一个类定义了 __iter__() 方法，Python 会优先使用它来进行遍历。
   ⦁ __iter__() 方法应该返回一个迭代器对象。

2. __getitem__() 方法：
   ⦁ 如果一个类没有定义 __iter__() 方法，但定义了 __getitem__() 方法，Python 会尝试使用 __getitem__() 来进行遍历。
   ⦁ Python 会从索引 0 开始，连续调用 __getitem__() 方法，直到抛出 IndexError 异常。

3. 遍历的优先顺序：
   ⦁ Python 首先查找 __iter__() 方法。
   ⦁ 如果 __iter__() 不存在，则查找 __getitem__() 方法。
   ⦁ 如果两者都不存在，则该对象被认为是不可迭代的。

```python
class Person:
    def __init__(self, age):
        self.age = age

    def __getitem__(self, item):
        self.age += 1
        if self.age > 18:
            raise StopIteration("成年了")
        return self.age


p = Person(1)
for i in p:
    print(i)


class Person:
    def __init__(self, age):
        self.age = age

    def __getitem__(self, item):
        self.age += 1
        if self.age > 18:
            raise StopIteration("成年了")
        return self.age

    def __iter__(self):
        # 如果定义了本方法,本方法优先级比__getitem__高
        # 在遍历时,本方法返回一个迭代器对象,并不断调用 __next__方法来获取下一个值
        print('iter')
        # return iter([1,2,3])
        return self

    def __next__(self):
        self.age += 1
        if self.age > 18:
            raise StopIteration("成年了")
        return self.age


p = Person(1)
for i in p:
    print(i)

```

###### 属性访问及顺序

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

#### 描述器

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
这里有一点需要注意，因为age是对所有Person了实例共享的，在Age类中，我们不能将值绑定给self,如果绑定给self,那么所有的实例都在修改同一份age,而通过内存地址我们可以看到Instance表示 是p实例，我们应该将age绑定给p,这样每个实例对象有自己的age

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


#### 调用类对象

要想达到调用函数一样调用类对象，应得在类中实现__call__方法。这类可以当作函数来调用的对象，称为可调用对象。

```python
#!/usr/bin/env python
# coding: utf-8 
# Create by Andy963 @2020-07-12 13:37:23

class A:
    def go(self):
        return object()
    
class B:
    def run(self):
        return object()
    
def func():
    return object()

def main(params:
    params()
    # a.go
    # b.run
    # fun()
    pass

#在上面的情况中，如果是传入的A的对象，在main中我得调用a.go方法，而如果是B的对象，则需要调用run方法，对于不同的类，要调用不同的方法，显示在main函数中我们
#无法知道这个具体方法，而__call__方法让这一切成为可能。只要类实现了__call__方法。


class Person:
    def __init__(self,name):
        self.name = name

    def __call__(self):
        print(self.name,'hello,world')

if __name__ == '__main__':
    andy = Person('andy')
    andy() # 可调用对象


#因为实现了__call__方法，我只需要调用类对象（就像调用函数一样）
```


#### 描述器

只要是定义了__get__()、__set()__  、 __delete()__中任意一个方法的对象都叫描述符
通常情况下，类P的属性x,我们获取时obj.x 是从 p.__dict__中取值，而如果定义了相应的描述符，就可以改变这种行为.

如果我们要对类的某种行为做一定的限制，下面的方式可以达到目的，但这种方式显然是不合适的。

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        if not isinstance(age, int):
            raise TypeError('Expected an int!')
        self.age = age


p = Person('andy', 10)
print(p.name, p.age)
p1 = Person('andy', '10')
print(p1.name, p1.age)

```

下面用property装饰器来实现：

```python
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a str!')
        self.__name = value

    @name.deleter
    def name(self):
        del self.__name


p = Person('andy')
print(p.name)
p.name = 10 # TypeError: Expected a str!
print(p.name)
```

假如我们想在对类属性进行操作时，对它做一定的限制，比如类型检查，可以用上面的方式实现。
但通常情况下，类有多个属性，不太合适每个属性都这么写一遍，那有没有更好的方法呢？

```python
class String:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string')

        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Integers:
    def __init__(self, age):
        self.age = age

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self.age]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.age] = value

    def __delete__(self, instance):
        del instance.__dict__[self.age]


class Person:
    name = String('name')
    age = Integers('age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person('andy', 10)
print(p.name, p.age)
p.name = 10 # TypeError: Expected a string
print(p.name)
```

表面看，上面这种做法更麻烦了。但考虑到重用性，这种方式更合适。
针对属性定一个类，这样类可以重用，且不同属性可以定制不同的验证规则。



## 模块
一组特定功能的类，函数的打包

模块内的`__init__.py` 在python3.3之后的版本非必须，但仍建议加上。当导入一个包时，会自动执行`__init__.py`中的代码，例如，在django项目中使用pymysql模块时需要在配置文件所在包的`__init__.py`中添加如下语句：

```python
import pymysql
pymysql.install_as_MySQLdb() 
```

### 导入模块后发生了什么？

 第一次导入时
- 在自己当下的命名空间中，执行所有的代码
- 创建一个模块对象，并将模块内所有的顶级变量每个属性的形式绑定到模块对象上
- 在import的位置，引入import后面的变量名称到当前 命名空间

 第二次导入时：
  只执行第一步导入时的第三步

**从哪个位置导入**

```from chat gpt
当Python代码导入模块时，会发生以下步骤：

1.  搜索模块：首先，Python会在sys.path变量中定义的目录中搜索要导入的模块。sys.path变量是一个包含要搜索的目录列表的字符串列表。如果找到了匹配的模块，Python就会停止搜索并继续执行下一步。如果找不到匹配的模块，Python会引发一个ImportError。
    
2.  编译模块：Python会将找到的模块的源代码编译为字节码。编译后的字节码会被缓存到__pycache__目录中，以便于下次导入时快速加载。
    
3.  执行模块：Python会执行编译后的字节码，这将导入模块的全局变量和函数。如果模块定义了__name__变量，Python会将该变量设置为模块的名称。模块的执行过程也可能会导入其他模块，这些模块会遵循相同的导入过程。
    
4.  创建模块对象：Python会创建一个模块对象，并将其添加到sys.modules缓存中。该模块对象包含了模块的全局命名空间和其他元数据。
    
5.  返回模块对象：导入完成后，Python会返回模块对象，这样我们就可以在我们的代码中使用模块中定义的变量和函数。
    

需要注意的是，当模块被导入时，它的代码会被执行。这意味着模块中的全局变量、函数、类等都会在导入时定义，而不是在第一次访问时才定义。因此，在编写模块时，需要注意不要编写会产生副作用的代码，例如修改全局状态或执行耗时的操作。
```

**从哪个位置导入**
- 内置模块
- 当前目录 （注意sys.path的第一个值也是当前目录）
- sys.path
- 环境变量（`PYTHONPATH` 环境变量）
- 安装路径的lib库
- 追加路径（修改sys.path, 环境变量等，添加.pth文件）

对于.pth文件的优先级，安装路径下的.pth文件>site-package>site-packge路径中的.pth文件

##### 覆盖导入

当自定义的模块与内置模块同名时，我们导入的是内置模块，因为内置模块优先级最高上。
当自定义的模块与与非内置标准模块同名，这种两种情况都可能，两者路径都在sys.path中，谁在前就会导入谁，并覆盖后者。这种情况下，我们可以使用`from my_module import my_func`这种指定从哪个模块导入的方式，如果你写过celery可能会遇到这种情况，在celery中的一种解决方式是`from __future__ import absolute_import`

##### 局部导入
在某个局部范围内导入,因为模块，函数，类等都会产生自己的命名空间，当我们在某个局部才导入模块，那么此模块的生命周期也仅仅在此范围
另一方面，导入模块也会消耗内存，耗时，有些模块只有某种特定情况下才需要，那么只要当那种情况发生时需要导入。

```python
def main():
    import module1
    pass
```

##### 循环导入
循环导入要把握的要点：当遇到import时，会跳转到要导入的文件，然后把该文件内容全部执行一遍，并在导入的地方产生对应的命名空间，绑定导入的模块中的所有对象。这咱遇到import跳转的情况不仅仅发生在第一次导入时，当在要导入的文件中又遇到import时会再次跳转，当完成该次导入后再跳转回来，继续执行剩下的代码。如果已经有该模块的命名空间，则不会重复导入，但会绑定该模块中的还没有绑定的对象。

延迟导入
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

##### 可选导入
当两个模块api相同，我们想优先导入m1,如果m1导入失败再导入m2时，可以考虑可选导入的方式
```python
try:
    import m1 as m
except ModuleNotFoundError:
    import m2 as m
    
m1.run()
```
我们导入后，将两个模块都取相同的别名，因为api一样，这样我们就可以在导入后使用统一的调用

##### 包内导入
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

### 反射导入模块

反射可以用来获取类的方法，也可以用来导入模块，并从模块中导入方法。

```python
import importlib

PLUGIN_DICT = {
    "board": "lib.plugins.board.Board",
    "disk": "lib.plugins.disk.Disk",
    "memory": "lib.plugins.memory.Memory",
    "network":"lib.plugins.network.Network",
    "cpu":"lib.plugins.cpu.Cpu",
}

def get_server_info(hostname, ssh_func):
    """
    :param hostname: 要远程操作的主机名
    :param ssh_func: 执行远程操作的方法
    :return: 执行命令后得到的信息
    """

    info_dict = {}
    for key, path in PLUGIN_DICT.items():
        module_path, class_name = path.rsplit('.', maxsplit=1)
        # 根据字符串的形式去导入模块 “lib.plugins.board"
        module = importlib.import_module(module_path)
        # 去模块找到类
        try:
            cls = getattr(module, class_name)
        except Exception:
            raise ImportError('模块获取失败')
        # 对类型实例化
        obj = cls()
        # 执行对象的process方法
        result = obj.process(hostname, ssh_func)
        info_dict[key] = result

    return info_dict
```
```python
In [1]: s = 'lib.plugin.board'

In [2]: s.rsplit('.', maxsplit=1)
Out[2]: ['lib.plugin', 'board']
```

我们将所有的模块都放在lib.plugin包下，这样module_path = lib.plugin, class_name=board, 这样通过importlib.import_module就获取到了对象。接着去模块中找类：getattr(module, class_name). 得到类，通过加括号的方式实例化类对象，此时执行类对象的处理方法。

### 时间（time）

#### asctime

```python
time.asctime() // 'Fri Sep 15 14:46:37 2023' 
```

它不接受任何参数，也就是它只能返回上面样式的字符串，比较鸡肋

#### ctime

将一个指定的秒数转成上面的asctime 样式的字符串格式，如果没有指定秒数，默认使用time.time() 返回值。

```python
>>> time.ctime()
'Fri Sep 15 14:53:17 2023'
```
#### gmtime
将一个指定秒数转成结构化时间

```python
>>> time.gmtime()
time.struct_time(tm_year=2023, tm_mon=9, tm_mday=15, tm_hour=6, tm_min=54, tm_sec=44, tm_wday=4, tm_yday=258, tm_isdst=0)

- `tm_year`：年份，例如2023
- `tm_mon`：月份，范围从1（一月）到12（十二月）
- `tm_mday`：一个月中的第几天，范围从1到31
- `tm_hour`：小时，范围从0（午夜）到23
- `tm_min`：分钟，范围从0到59
- `tm_sec`：秒，范围从0到61（60和61用于闰秒）
- `tm_wday`：一周中的第几天，范围从0（星期一）到6（星期日）
- `tm_yday`：一年中的第几天，范围从1到366
- `tm_isdst`：夏令时标志，值为0表示标准时间，为1表示夏令时。如果信息不可用，则为-1
```

#### localtime
与上面的gmtime 一样，但是会转为本地时间，目前就发现小时显示不一样，对于gmtime 会显示6， 而localtime则显示14


### socket
wrap_socket 旧的接口不能用，改为使用context

```python
cert_file = str('')
key_file = str('')
context = ssl.SSLContext(ssl.ProTocol_SSLv23)
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE
context.load_cert_chain(cert,key)
_socket = context.wrap_socket()
```

### datetime to timezone
```python
import pytz
from datetime import datetime
unware_time = datetime.strptime(time_str,'%Y-%d-%d %H:%M:%s')
unware_time.replace(tzinfo=pytz.UTC)
```

### re模块

#### look around:

- look forward

```python

In [12]: txt = "i love python, i love regex"
# 后面是python的Love
In [13]: pattern = re.compile("love\s(?=python)")
# 所以这里只能匹配出第一个love, 因为第二个love后面接的regex
In [14]: pattern.search(txt)
Out[14]: <re.Match object; span=(2, 7), match='love '>
# 后面不是python的Love
In [15]: pattern = re.compile("love\s(?!python)")
# 通过索引可以看到，匹配的是第二个love, 因为第一个Love后面接的是python
In [16]: pattern.search(txt)
Out[16]: <re.Match object; span=(17, 22), match='love '>
# 后面既不能是python也不能是love
In [17]: pattern = re.compile("love\s(?!python|regex)")

In [18]: pattern.search(txt)
```

the word after "?=" or "?!" will not consuming characters. the first one `love\s(?=python)` means only match the word love which is followed by python.
if i change the "?=" to "?!" means not match, so the result is the "love" folled by regex

- look back/behind

```python
# 肯定型后视断言，这里的<= 可以理解为在当前位置回退几个字符，看是否能匹配上内部的模式
# 这里的内部的模式即pattern in the brackets, but remmber the pattern lenght is
# accurate, but not variable(a.*, a{3,4} is not allowed)
In [72]: text = "love regex or hate regex, can't ignore regex"

In [73]: pattern = re.compile("(?<=(love|hate)\s)regex")

In [74]: pattern.findall(text)
Out[74]: ['love', 'hate']

# negetive look back, which is oppoiste to the up one
In [94]: pattern = re.compile("(?<!love\s)regex")

In [95]: pattern.findall(text)
Out[95]: ['regex', 'regex']

# i don't known why this negetive lookbehind not work even if i change the 
# the inside mode to a or anything else.
In [96]: pattern = re.compile("(?<!(love|hate)\s)regex")
In [97]: pattern.findall(text)
Out[97]: ['']

```

the word after ?<= will only match the word  has hate or love before regex.  and ?<! not match. but there is sth confusing: when i use "love|hate" why it return "" ? 

### argparse
 argparse example
```python
#!/usr/bin/env python
# coding: utf-8 
# Create by Andy963 @2021-01-10 10:50:27


import argparse


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quite", action="store_true")

    parser.add_argument("num", help="The fibonacci number you wish to calculate.", type=int)
    parser.add_argument('-o', "--output", help="Output result to a file", action="store_true")
    args = parser.parse_args()

    result = fib(args.num)
    if args.verbose:
        print("The " + str(args.num) + "th fib number is " + str(result))
    elif args.quite:
        print(result)
    else:
        print("fib(" + str(args.num) + ") =" + str(result))

    if args.output:
        f = open("fib.txt", "a")
        f.write(str(result) + "\n")


if __name__ == '__main__':
    main()
```




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
contextlib.closing会默认调用对象内部的closing方法：
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

#### 进程创建的两种方式

**方式1**(推荐)
```python
from multiprocessing import Process

def func():
    print(12345)

if __name__ == '__main__': 
    p = Process(target=func,) 
    p.start() 
    print('*' * 10) 
```

**方式2**
```python
class MyProcess(Process): 
    def __init__(self,person):
        super().__init__()
        self.person=person
    def run(self):
        print(os.getpid())
        print(self.pid)
        print(self.pid)
        print('%s 正在和女主播聊天' %self.person)

if __name__ == '__main__':
    p1=MyProcess('Jedan')
    p2=MyProcess('太白')
    p3=MyProcess('alexDSB')

    p1.start() 
    p2.start()
    # p2.run()
    p3.start()
```

 方式3 进程池
 
```python
import multiprocessing

def worker(num):
    return f"Result: {num * num}"

if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        results = pool.map(worker, range(10))
        print(results)

```

#### 子进程和主进程

我们通过主进程创建的子进程是异步执行的，那么我们就验证一下，并且看一下子进程和主进程(也就是父进程)的ID号，来看看是否是父子关系。

```python
import time
import os

#os.getpid()  获取自己进程的ID号
#os.getppid() 获取自己进程的父进程的ID号

from multiprocessing import Process

def func():
    print('aaaa')
    time.sleep(1)
    print('子进程>>',os.getpid())
    print('该子进程的父进程>>',os.getppid())
    print(12345)

if __name__ == '__main__': 
    #首先我运行当前这个文件，运行的这个文件的程序，那么就产生了主进程

    p = Process(target=func,) 
    p.start() 
    print('*' * 10) 
    print('父进程>>',os.getpid())
    print('父进程的父进程>>',os.getppid())
```

结果
```
#********** 首先打印出来了出进程的程序，然后打印的是子进程的，也就是子进程是异步执行的，相当于主进程和子进程同时运行着，如果是同步的话，我们先执行的是func()，然后再打印主进程最后的10个*号。
#父进程>> 3308
#父进程的父进程>> 5916 #我运行的test.py文件的父进程号，它是pycharm的进程号，看下面的截图

#aaaa
#子进程>> 4536
#该子进程的父进程>> 3308 #是我主进程的ID号，说明主进程为它的父进程

#12345
```

####  进程之间是空间隔离的
进程之间的数据是隔离的，也就是数据不共享

```python

from multiprocessing import Process

n=100 #全局变量
def work():
    global n
    n += 1
    print('子进程内: ',n)

if __name__ == '__main__':
    p=Process(target=work)
    p.start()
    p.join() 
    print('主进程内: ',n)
```
**结果**
```
#看结果：
# 子进程内:  101
# 主进程内:  100
```

原因是子进程在创建时会复杂父进程的整个内存空间，然后两个内存空间是独立的，所以子进程中修改了n的值并不会影响父进程中
####  进程对象的其他方法

name和pid的用法

```python
import time
import random
from multiprocessing import Process

class Piao(Process):
    def __init__(self,name):
        #为我们开启的进程设置名字的做法
        super().__init__()
        self.name=name

    def run(self):
        print('%s is piaoing' %self.name)
        time.sleep(random.randrange(1,3))
        print('%s is piao end' %self.name)

p=Piao('egon')
p.start()
print('开始')
print(p.pid) #查看pid
```
**结果 **
```
开始
934
egon is piaoing
egon is piao end
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

#### 生产者和消费者模型

在并发编程中使用生产者和消费者模式能够解决绝大多数并发问题。该模式通过平衡生产线程和消费线程的工作能力来提高程序的整体处理数据的速度。

**为什么要使用生产者和消费者模式**
在线程世界里，生产者就是生产数据的线程，消费者就是消费数据的线程。在多线程开发当中，如果生产者处理速度很快，而消费者处理速度很慢，那么生产者就必须等待消费者处理完，才能继续生产数据。同样的道理，如果消费者的处理能力大于生产者，那么消费者就必须等待生产者。为了解决这个问题于是引入了生产者和消费者模式。

**什么是生产者消费者模式**

​	生产者消费者模式是通过一个容器来解决生产者和消费者的强耦合问题。生产者和消费者彼此之间不直接通讯，而通过阻塞队列来进行通讯，所以生产者生产完数据之后不用等待消费者处理，直接扔给阻塞队列，消费者不找生产者要数据，而是直接从阻塞队列里取，阻塞队列就相当于一个缓冲区，平衡了生产者和消费者的处理能力，并且我可以根据生产速度和消费速度来均衡一下多少个生产者可以为多少个消费者提供足够的服务，就可以开多进程等等，而这些进程都是到阻塞队列或者说是缓冲区中去获取或者添加数据。


**通过队列实现一个生产者和消费者模型**

```python
import time,random,os
from multiprocessing import Process,Queue

def consumer(q):
    while True:
        res=q.get()
        time.sleep(random.randint(1,3))
        print('\033[45m%s 吃 %s\033[0m' %(os.getpid(),res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res='包子%s' %i
        q.put(res)
        print('\033[44m%s 生产了 %s\033[0m' %(os.getpid(),res))

if __name__ == '__main__':
    q=Queue()
    #生产者们:即厨师们
    p1=Process(target=producer,args=(q,))

    #消费者们:即吃货们
    c1=Process(target=consumer,args=(q,))

    #开始
    p1.start()
    c1.start()
    print('主')
```

上述模型解释
```
#生产者消费者模型总结

    #程序中有两类角色
        一类负责生产数据（生产者）
        一类负责处理数据（消费者）
        
    #引入生产者消费者模型为了解决的问题是：
        平衡生产者与消费者之间的工作能力，从而提高程序整体处理数据的速度
        
    #如何实现：
        生产者<-->队列<——>消费者
    #生产者消费者模型实现类程序的解耦和
    
缓冲和解耦
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

#### 进程管理

多个进程之间的管理是操作系统和分布式系统中的重要话题。以下是一些常用的进程管理方法和技术：

1. 进程调度

操作系统的进程调度器负责决定哪个进程在某一时刻运行。常见的调度算法包括：

⦁ 先来先服务（FCFS）
⦁ 最短作业优先（SJF）
⦁ 优先级调度
⦁ 轮转调度（Round Robin）
⦁ 多级队列调度

2. 进程间通信（IPC）

进程间通信允许进程相互交换数据和信息。常见的IPC方法包括：

⦁ 管道（Pipes）
⦁ 消息队列
⦁ 共享内存
⦁ 信号量
⦁ 套接字（Sockets）

3. 同步机制

为了协调进程间的活动，可以使用以下同步机制：

⦁ 互斥锁（Mutex）
⦁ 信号量（Semaphores）
⦁ 条件变量（Condition Variables）
⦁ 读写锁（Read-Write Locks）

4. 资源管理

操作系统负责管理和分配系统资源，如CPU时间、内存、I/O设备等。这包括：

⦁ 内存管理（如分页、分段）
⦁ CPU时间片分配
⦁ I/O设备分配

### 线程

线程是进程内的执行单元，是操作系统调度的最小单位

threading模块的完全模仿了multiprocess模块的接口，二者在使用层面，有很大的相似性，因而不再详细介绍（[官方链接](https://docs.python.org/3/library/threading.html?highlight=threading#)）

#### 线程创建的两种方式

**方式1**

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

**方式2**
```python
import time
from threading import Thread

class Sayhi(Thread):
    def __init__(self,name):
        super().__init__()
        self.name=name
        
    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)

if __name__ == '__main__':
    t = Sayhi('太白')
    t.start()
    print('主线程')
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

守护线程

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

#### 线程同步

互斥锁(同步锁)

多个线程抢占资源时会造成数据混乱的问题，可以通过加锁来解决，看代码：

```python
import os,time

from threading import Thread,Lock

def work():
    global n
    lock.acquire() #加锁
    temp=n
    time.sleep(0.1)
    n=temp-1
    lock.release()
    
    with lock:
        temp=n
        time.sleep(0.1)
        n=temp-1
if __name__ == '__main__':
    lock=Lock()
    n=100
    l=[]
    for i in range(100):
        t=Thread(target=work)
        l.append(t)
        t.start()
    for t in l:
        t.join()

    print(n) #结果肯定为0，由原来的并发执行变成串行，牺牲了执行效率保证了数据安全
```
加锁之后，数据不会出现混乱的问题了，这种情况称之为线程安全。

锁的单例模式

创建锁的时候，我们还可以采用单例模式，看下面的示例：

```python
from threading import Thread,Lock

class SingleTon:
    __instance = None
    lock = Lock()

    def __new__(cls, *args, **kwargs):
        if cls.__instance:
            return cls.__instance
        with cls.lock:
            if not cls.__instance:
                cls.__instance = super().__new__(cls)
            return cls.__instance

def fun():
    s = SingleTon()
    print(id(s))

for i in range(20):
    t1 = Thread(target=fun,)
    t1.start()
```

#### 死锁

​	进程也有死锁与递归锁，进程的死锁和线程的是一样的，而且一般情况下进程之间是数据不共享的，不需要加锁，由于线程是对全局的数据共享的，所以对于全局的数据进行操作的时候，要加锁。

​	所谓死锁： 是指两个或两个以上的进程或线程在执行过程中，因争夺资源而造成的一种互相等待的现象，若无外力作用，它们都将无法推进下去。此时称系统处于死锁状态或系统产生了死锁，这些永远在互相等待的进程称为死锁进程，如下就是死锁：

**现象1：将自己锁死**
```python

import time
from threading import Lock

mutexA=Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()
```

**现象2：锁嵌套引起的死锁**

``` python
import time
from threading import Thread,Lock

mutexA=Lock()
mutexB=Lock()

class MyThread(Thread):
    def run(self):
        self.func1()
        self.func2()
        
    def func1(self):
        mutexA.acquire()
        print('\033[41m%s 拿到A锁>>>\033[0m' %self.name)
        mutexB.acquire()
        print('\033[42m%s 拿到B锁>>>\033[0m' %self.name)
        mutexB.release()
        mutexA.release()

    def func2(self):
        mutexB.acquire()  
        print('\033[43m%s 拿到B锁???\033[0m' %self.name)
        time.sleep(2)
        #分析：当线程1执行完func1，然后执行到这里的时候，拿到了B锁，线程2执行func1的时候拿到了A锁，那么线程2还要继续执行func1里面的代码，再去拿B锁的时候，发现B锁被人拿了，那么就一直等着别人把B锁释放，那么就一直等着，等到线程1的sleep时间用完之后，线程1继续执行func2，需要拿A锁了，但是A锁被线程2拿着呢，还没有释放，因为他在等着B锁被释放，那么这俩人就尴尬了，你拿着我的老A，我拿着你的B，这就尴尬了，俩人就停在了原地

        mutexA.acquire()
        print('\033[44m%s 拿到A锁???\033[0m' %self.name)
        mutexA.release()

        mutexB.release()

if __name__ == '__main__':
    for i in range(10):
        t=MyThread()
        t.start()
```

#### 递归锁

死锁的解决方法：递归锁，在Python中为了支持在同一线程中多次请求同一资源，python提供了可重入锁RLock。
这个RLock内部维护着一个Lock和一个counter变量，counter记录了acquire的次数，从而使得资源可以被多次require。直到一个线程所有的acquire都被release，其他的线程才能获得资源。上面的例子如果使用RLock代替Lock，则不会发生死锁：

**现象1的解决**

```python
import time
from threading import RLock as Lock

mutexA=Lock()
mutexA.acquire()
mutexA.acquire()
print(123)
mutexA.release()
mutexA.release()
```

**现象2的解决**

```python
import time
from threading import Thread,RLock
fork_lock = noodle_lock = RLock()

def eat1(name):
    noodle_lock.acquire()
    print('%s 抢到了面条'%name)
    fork_lock.acquire()
    print('%s 抢到了叉子'%name)
    print('%s 吃面'%name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    fork_lock.acquire()
    print('%s 抢到了叉子' % name)
    time.sleep(1) 
    noodle_lock.acquire()
    print('%s 抢到了面条' % name)
    print('%s 吃面' % name)
    noodle_lock.release()
    fork_lock.release()

for name in ['taibai','wulaoban']:
    t1 = Thread(target=eat1,args=(name,))
    t1.start()
for name in ['alex','peiqi']:
    t2 = Thread(target=eat2,args=(name,))
    t2.start()
```

#### GIL锁和锁的区别

```
GIL VS Lock

  机智的同学可能会问到这个问题，就是既然你之前说过了，Python已经有一个GIL来保证同一时间只能有一个线程来执行了，为什么这里还需要lock? 

  首先我们需要达成共识：锁的目的是为了保护共享的数据，同一时间只能有一个线程来修改共享的数据

  然后，我们可以得出结论：保护不同的数据就应该加不同的锁。

  最后，问题就很明朗了，GIL 与Lock是两把锁，保护的数据不一样，前者是解释器级别的（当然保护的就是解释器级别的数据，比如垃圾回收的数据），后者是保护用户自己开发的应用程序的数据，很明显GIL不负责这件事，只能用户自定义加锁处理，即Lock

  过程分析：所有线程抢的是GIL锁，或者说所有线程抢的是执行权限

  线程1抢到GIL锁，拿到执行权限，开始执行，然后加了一把Lock，还没有执行完毕，即线程1还未释放Lock，有可能线程2抢到GIL锁，开始执行，执行过程中发现Lock还没有被线程1释放，于是线程2进入阻塞，被夺走执行权限，有可能线程1拿到GIL，然后正常执行到释放Lock。。。这就导致了串行运行的效果

　　既然是串行，那我们执行

　　t1.start()

　　t1.join

　　t2.start()

　　t2.join()

  这也是串行执行啊，为何还要加Lock呢，需知join是等待t1所有的代码执行完，相当于锁住了t1的所有代码，而Lock只是锁住一部分操作共享数据的代码。
```

#### 线程队列

线程之间的通信我们列表行不行呢，当然行，那么队列和列表有什么区别呢？

​	queue队列 ：使用import queue，用法与进程Queue一样

​	queue is especially useful in threaded programming when information must be exchanged safely between multiple threads.

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

#### 锁，条件变量，信号量

```from chatgpt
1.  锁（Lock）：一种基本的同步原语，用于在多个线程之间提供独占访问。只有获取锁的线程可以修改共享资源，其他线程必须等待锁被释放后才能获取锁。Python 中常用的锁包括 `RLock` 和 `Semaphore`。
2.  条件变量（Condition）：一种高级同步原语，用于在线程之间共享复杂状态的情况下进行同步。条件变量提供了一个线程等待的机制，可以等待某个状态变为满足条件时才继续执行。Python 中的条件变量通过 `threading.Condition` 类实现。
3.  信号量（Semaphore）：一种计数器，用于在多个线程之间控制并发访问的数量。当一个线程需要访问某个共享资源时，它需要先获取一个信号量，如果没有可用的信号量，则线程会被阻塞。Python 中的信号量通过 `threading.Semaphore` 类实现。

锁、条件变量和信号量都是线程同步的工具，但是它们的使用场景不同，需要根据具体的情况进行选择。例如，当多个线程需要互斥访问某个共享资源时，可以使用锁来实现；当线程需要等待某个事件或条件时，可以使用条件变量；当需要控制并发访问数量时，可以使用信号量。
```

Ref: 

[Threading Semaphore in Python](https://superfastpython.com/thread-semaphore/)


### 协程

**协程介绍**

协程的目的是基于单线程来实现并发，即只用一个主线程（很明显可利用的cpu只有一个）情况下实现并发，为此我们需要先回顾下并发的本质：切换+保存状态

cpu正在运行一个任务，会在两种情况下切走去执行其他的任务（切换由操作系统强制控制），一种情况是该任务发生了阻塞，另外一种情况是该任务计算的时间过长或有一个优先级更高的程序替代了它

协程本质上就是一个线程，以前线程任务的切换是由操作系统控制的，遇到I/O自动切换，现在我们用协程的目的就是较少操作系统切换的开销（开关线程，创建寄存器、堆栈等，在他们之间进行切换等），在我们自己的程序里面来控制任务的切换。

协程：是单线程下的并发，又称微线程，纤程。英文名Coroutine。一句话说明什么是线程：**协程是一种用户态的轻量级线程，即协程是由用户程序自己控制调度的。**

**协程就是告诉Cpython解释器，不是搞了个GIL锁吗，那好，我就自己搞成一个线程让你去执行，省去你切换线程的时间，我自己切换比你切换要快很多，避免了很多的开销，对于单线程下，我们不可避免程序中出现io操作，但如果我们能在自己的程序中（即用户程序级别，而非操作系统级别）控制单线程下的多个任务能在一个任务遇到io阻塞时就切换到另外一个任务去计算，这样就保证了该线程能够最大限度地处于就绪态，即随时都可以被cpu执行的状态，相当于我们在用户程序级别将自己的io操作最大限度地隐藏起来，从而可以迷惑操作系统，让其看到：该线程好像是一直在计算，io比较少，从而更多的将cpu的执行权限分配给我们的线程。**

#### yield实现协程

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
```

总结协程特点：

1. **必须在只有一个单线程里实现并发**
2. **修改共享数据不需加锁**  (非抢占式的并发)
3. **用户程序里自己保存多个控制流的上下文栈**
4. **附加：一个协程遇到IO操作自动切换到其它协程(gevent模块来实现)**

#### gevent模块
Gevent 是一个第三方库，可以轻松通过gevent实现并发同步或异步编程，在gevent中用到的主要模式是**Greenlet**, 它是以C扩展模块形式接入Python的轻量级协程。 Greenlet全部运行在主程序操作系统进程的内部，但它们被协作式地调度。

**安装**

```python
pip3 install gevent
```
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
from gevent import monkey;monkey.patch_all() #必须写在最上面，这句话后面的所有阻塞全部能够识别了

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
class DB:  
    def __init__(self, url="sqlite:///db.sqlite3"):  
        self.engine = create_engine(  
            url=url,  
            connect_args={"check_same_thread": False},  
            pool_size=10,  
            max_overflow=20,  
            pool_recycle=3600,  # 连接在连接池中的回收时间  
            pool_pre_ping=True,  # 在使用前检查连接是否有效  
        )  
        self.Session = scoped_session(sessionmaker(bind=self.engine))  
  
    @contextmanager  
    def get_session(self, method_name=None):  # autocommit=True  
        session = self.Session()  
        try:  
            yield session  # enter 处理的逻辑
            session.commit()  # exit 时处理的逻辑， 提交事务  
        except Exception as e:  
            session.rollback()  # 回滚事务  
            if method_name:  
                db_logger.error(f"Error in method {method_name}: {e}", exc_info=True)  
            raise e  
        finally:  
            session.close()  # 关闭会话
```


总结：
在我们定定义的需要contextmanager装饰的函数中我们只需要写，前戏和事后回味两部分内容。这两部分内容用yield分隔开。
而在我们调用with语句中则是执行真正的战斗部分。



## 内存管理机制
 python中垃圾回收机制主要有三方面:引用记数为主,标记清除,分代回收为辅

### 引用计数(没有人记得你时,才是真正的死亡)

在python中一切皆为对象,每个对象都维护一个引用次数,如果次数为零,即没有任何引用,它将被回收机制无情的收割(没有人赢得你时,才是真正的死亡.鲁迅也曾说:有的人死了,但他仍活着,我想也有此意思).下面看看具体代码:

```python
import sys


class Person:
    pass


p = Person() # p被创建,指向Person对象,记数 +1

print("p ref count:", sys.getrefcount(p)) # p作为实参传给函数,记数 +1,总次数为 2
p1 = p  # p1引用 ,记数 +1 总次数为 3
print("p ref count", sys.getrefcount(p)) 
del p1 # 删除 p1对p的引用,次数-1, 总次数为2
print("p ref count", sys.getrefcount(p)) # 2

#输出:
p ref count: 2
p ref count 3
p ref count 2
```

#### 第一次打印为什么是2?
我们来看源码
```python
def getrefcount(): # real signature unknown; restored from __doc__
    """
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().
    """
    pass
```

可以清楚的看到,结果比我们预想的要高一个,是因为变量本身作为getrefcount的临时引用,所以会+1,所以结果为2

#### 函数为什么会引用+2?
我们先看看下面这种情况:
- 创建 +1
- getrefcount +1
那也只有2才对,可是结果为什么是4呢?

```python
import sys


class Person:
    pass

def log_ref(var):
    print(sys.getrefcount(var))

p = Person()
# 输出:
4
```

在对象传给函数时,函数内部有两个属性`func_globals, __globals__`都会引用该参数,所以此时该对象的引用计数会 +2. 需要注意的是在python3中我们通过dir无法查看到 `func_globals`.
在python2中,函数包含两个属性:`func_globals, __globals__`,在python3中前者的命名发生了改变,具体可以参考: https://docs.python.org/3.1/whatsnew/3.0.html
Operators And Special Methods:
> The function attributes named func_X have been renamed to use the __X__ form, freeing up these names in the function attribute namespace for user-defined attributes. To wit, func_closure, func_code, func_defaults, func_dict, func_doc, func_globals, func_name were renamed to __closure__, __code__, __defaults__, __dict__, __doc__, __globals__, __name__, respectively.


#### 既然对象作为参数传递给函数引用会+2,那么下面这段代码为结果为什么是2?
很明显 getrefcount也是函数,那打印结果应该是3才对,这是因为getrefcount会自动处理这种情况
```python
import sys


class Person:
    pass


p = Person()
print("p ref count:", sys.getrefcount(p))
```

#### 作为容器的元素的场景
这里的容器以列表为例:

```python
import sys


class Person:
    pass


p = Person()

l = [p, ]

print(sys.getrefcount(p))
# 输出3
```

#### +1场景总结:
引用记数+1场景:
- 对象被创建
- 对象被引用
- 对象作为参数,传入函数中
- 对象作为对象存储在容器中

#### 对象被显式销毁
主动将你忘记.但此时你已经不存在,无法通过`getrefcount()`来测试引用数量

#### 对象的引用被指新的对象
没错,你被绿了.你对象移情别恋了,她心里只有另一个人了,记得你的人就少了一个

```python
import sys


class Person:
    pass


you = Person()
your_gf = you
print(sys.getrefcount(you))  # 你对象还爱你的时候
another_handsome_boy = Person()
your_gf = another_handsome_boy
print(sys.getrefcount(you))  # 你对象爱上高富帅的时候
#输出:
3
2
```

#### 离开作用域
在getrefcount函数中,记数会+1,那如果这样,我不停打印不会就不断增加吗?但离开了getrefcount的世界,它就把你忘记了
```python
import sys


class Person:
    pass


you = Person()
print(sys.getrefcount(you))
print(sys.getrefcount(you))
#输出
2
2
```
#### 销毁容器
当你的世界被销毁时:
```python
import sys


class Person:
    pass


p = Person()

l = [p, ]
del l
print(sys.getrefcount(p))
# 输出2
```

#### -1场景总结
- 显式销毁
- 引用被指向新的对象
- 离开作用域
- 容器被销毁

### 标记清除
引用记数无法解决的问题:
```python
import sys


class Person:
    pass


you = Person()
your_gf = Person()
you.gf = your_gf
your_gf.bf = you
print(sys.getrefcount(you))
print(sys.getrefcount(your_gf))
# 输出
3
3
```
除去你getrefcount引用,你和你对象相亲相爱,所以每人有两个引用.此时即出现了循环引用.
我们看官方文档: 只有容器类型,会存在这种循环引用,而对于简单原子数据类型如 数字,字符串不支持垃圾回收,或者不存储对其它对象引用的容器也不支持.

> Python’s support for detecting and collecting garbage which involves circular references requires support from object types which are “containers” for other objects which may also be containers. Types which do not store references to other objects, or which only store references to atomic types (such as numbers or strings), do not need to provide any explicit support for garbage collection.

ref: https://docs.python.org/3.1/c-api/gcsupport.html?highlight=circular%20reference

如果我们显式删除,会导致无法查看getrefcount, 我们借助第三方库来查看对对象的引用数,注意count的参数为字符串:
```python
pip install objgraph

import sys
import objgraph


class Person:
    pass


you = Person()
your_gf = Person()
print(objgraph.count("Person"))


del your_gf
print(objgraph.count("Person"))
# 输出
2
1
```

#### 循环引用
彼此相爱的两人,任谁也分不开

```python
import sys
import objgraph


class Person:
    pass


you = Person()
your_gf = Person()
print(objgraph.count("Person"))

you.gf = your_gf
your_gf.bf = you

del you
del your_gf
print(objgraph.count("Person"))

# 输出
2
2
```

借助objgraph 打印出这种节点图:

```python
import sys
import objgraph


class Boy:
    pass


class Girl:
    pass


you = Boy()
your_gf = Girl()
print(objgraph.count("Boy"))
print(objgraph.count("Girl"))
you.gf = your_gf
your_gf.bf = you
# del you
# del your_gf
print(objgraph.count("Boy"))
print(objgraph.count("Girl"))
objgraph.show_backrefs([you,your_gf])
```
上面的代码中虽然在最后的print语句时仍能打印,但如果我们删除了`you, your_gf`则也无法打印出图形,会报错
我们通过引用图:

![](https://github.com/Andy963/notePic/blob/main/circular_ref.png?raw=true)
![](https://github.com/Andy963/notePic/blob/main/circular_ref.png)

#### python的解决办法
python会收集所有的容器对象,放在一个双向链表中,将一个对象和它引用的对象的引用数都-1,如果它们的引用数变成0,则说明它们之间存在循环引用,那么这两个对象将标记出来,并被无情清除. 如果你和你的对象私定终生,他们总有办法发现的,尤其是他们不同意的时候.

### 分代回收
Python解释器在垃圾回收时，会遍历链表中的每个对象，如果存在循环引用，就将存在循环引用的对象的引用计数器 -1，同时Python解释器也会将计数器等于0（可回收）和不等于0（不可回收）的一分为二，把计数器等于0的所有对象进行回收，把计数器不为0的对象放到另外一个双向链表表（即：分代回收的下一代）
分代回收的代，有三代，按年轻到老的顺序为：0代，1代，2代 
门限，有三个门限 ，门限0，门限1，门限2，默认情况下为700，10，10 

```python
import gc

print(gc.get_threshold())
# (700, 10, 10)
```
第一个参数表示:垃圾回收器中新增的对象个数-消亡的对象个数,当这个值达到700以上时,会触发检测机制.
简单点讲:当新生儿出生数,减去死亡人数大于700,将导致这种检测(这时候就该计划生育了),然后开始检测,当0代的检测10次后(你只生了一胎,不信,检测10次,确定你只生了一胎),才会检测1代(此时0代的检测到第11次了),然后1代检测10次后才会检测2代(此时0代已经检测到101次).

> The GC classifies objects into three generations depending on how many collection sweeps they have survived. New objects are placed in the youngest generation (generation 0). If an object survives a collection it is moved into the next older generation. Since generation 2 is the oldest generation, objects in that generation remain there after a collection. In order to decide when to run, the collector keeps track of the number object allocations and deallocations since the last collection. When the number of allocations minus the number of deallocations exceeds threshold0, collection starts. Initially only generation 0 is examined. If generation 0 has been examined more than threshold1 times since generation 1 has been examined, then generation 1 is examined as well. Similarly, threshold2 controls the number of collections of generation 1 before collecting generation 2. 

如果要修改这些门限: 调用`set_threshold()`即可

#### 启用回收
垃圾回收机制默认是开启的:
```python
import gc

print(gc.isenabled()) # True
gc.disable()
```

#### 手动回收
我们以前面的循环引用为例:
```python
import gc
import objgraph


class Boy:
    pass


class Girl:
    pass


you = Boy()
your_gf = Girl()
print(objgraph.count("Boy"))
print(objgraph.count("Girl"))
you.gf = your_gf
your_gf.bf = you
del you
del your_gf
gc.collect()
print(objgraph.count("Boy"))
print(objgraph.count("Girl"))
```
在未手动触发垃圾回收时,两次都输出
```
1
1
1
1
```
启用后则是:
```python
1
1
0
0
```


## 测试（unittest）

```python
import unittest

class MyTestCase(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('andy'.upper(), 'ANDY')

    def test_is_upper(self):
        self.assertTrue('ANDY'.isupper())
        self.assertFalse('Andy'.isupper())

if __name__ == '__main__':
    unittest.main()
```

通过继承unittest.TestCase来实现一个测试用例，在这个类中，定义的以test开关的方法，测试框架将把它当作独立的测试来执行。

如果我们希望在测试前做一些准备工作，在测试之后做一些清理工作，我们就用到了fixtures(固定装置)，指的测试开始前的准备工作setUp和测试完成后的清理工作tearDown
#### 方法级别的fixtures

```python
class MyTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_sth(self):
        pass

    def tearDown(self):
        pass
```

#### 类级别的fixtures

```python
class MyTestCase(unittest.TestCase):
    def setUpClass(self):
        pass

    def tearDownClass(self):
        pass
```
#### 模块级别的fixtures
```python
def setUpModule():
    pass

def tearDownModule():
    pass
```

### 跳过测试和预计失败
unittest 支持直接跳过或按条件跳过测试，也支持预计测试失败：

通过 skip 装饰器或 SkipTest 直接跳过测试
通过 skipIf 或 skipUnless 按条件跳过或不跳过测试
通过 expectedFailure 预计测试失败
```python
class MyTestCase(unittest.TestCase):

    @unittest.skip("直接跳过")
    def test_nothing(self):
        self.fail("shouldn't happen")

    @unittest.skipIf(mylib.__version__ < (1, 3),"满足条件跳过")
    def test_format(self):
        # Tests that work for only a certain version of the library.
        pass

    @unittest.skipUnless(sys.platform.startswith("win"), "满足条件不跳过")
    def test_windows_support(self):
        # windows specific testing code
        pass

    def test_maybe_skipped(self):
        if not external_resource_available():
            self.skipTest("跳过")
        # test code that depends on the external resource
        pass

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "这个目前是失败的")

```

### 子测试
用不同的参数来测试同一段逻辑，但又不希望被视作同一个测试。就可以使用子测试
示例中使用了 with self.subTest(i=i) 的方式定义子测试，这种情况下，即使单个子测试执行失败，也不会影响后续子测试的执行。这样，我们就能看到输出中有三个子测试不通过
```python
class NumbersTest(unittest.TestCase):

    def test_even(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in range(0, 6):
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

```

## 异步
### asyncIo使用

我们先看下面的例子：

```python
import time
from datetime import datetime


def print_message_periodical(interval_seconds, message='keep alive'):
    while True:
        print(f'{datetime.now()} - {message}')
        start = time.time()
        end = start + interval_seconds
        while True:
            yield
            now = time.time()
            if now >= end:
                break


if __name__ == "__main__":
    a = print_message_periodical(3, 'three')
    b = print_message_periodical(10, 'ten')
    stack = [a, b]
    while True:
        for task in stack:
            next(task)
```
因为yield的存在，当print_message_periodical函数执行到这里时会中断，返回yield的值（yield类似return但不会结束函数)， 这样再次执行next时，就会执行另一个task，达到了切换的目的。中断，切换即异步的核心。

那么asyncIo是怎么做的呢？
```python
import asyncio
import time
from math import sqrt
from datetime import datetime

async def print_message_periodical(interval_seconds, message='keep alive'): # p定义函数时使用async
    while True:
        print(f'{datetime.now()} - {message}')
        start = time.time()
        end = start + interval_seconds
        while True:
            await asyncio.sleep(0) # 需要中断的地方使用await
            now = time.time()
            if now >= end:
                break

if __name__ == "__main__":
    scheduler = asyncio.get_event_loop() # 获取 event_loop对象
    scheduler.create_task(
        print_message_periodical(3, 'three')
    )
    scheduler.create_task(
        print_message_periodical(10, 'ten')
    )
    scheduler.run_forever()
```

### 事件循环

伪代码：
```
任务列表 = [任务1，任务2，任务3]

while True:
    可执行任务列表，已完成任务列表 = 去任务列表中检查所有任务，将可执行/已完成的返回

    for 就绪任务 in 可执行任务列表：
        执行已经就绪任务

    for 已经完成任务 in 已经完成任务列表
        在任务列表中移除已经完成任务

    如果 任务列表 中的任务都已经完成  终止循环
```
import asyncio
#去生成或者获取一个事件循环
loop = asyncio.get_evnet_loop()

#将任务添加到 '任务列表'
loop.run_until_complete(任务)

### 使用流程
- 定义协程函数
- 得到协程对象
- 执行

```python
import asyncio

async def func():  # 使用async def 来定义协程函数
    print('来了，来了')

result = func()  # 返回是一个协程对象

# 执行
loop = asyncio.get_event_loop()
loop.run_until_complete(result)

# asyncio.run(result) python3.7才有
```



### await

**示例1**
```python
await + 可等待对象 (协程对象，Future对象,Task对象 -> IO等待)

import asyncio

async def func():
    print('hello')
    result = await asyncio.sleep(2)
    print('finish', result)

asyncio.run(func())

执行流程： 
func添加到列表中后，先执行print, 此时遇到IO,如果有其他任务，就会切换到其他任务，当其他任务完成或者也遇到IO,切换回来，如果有返回值，交给result,再执行
print语句
```

**示例2**
```python
import asyncio

async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def func():
    print('执行协程函数内部代码')
    #遇到IO操作，挂起当前协程(任务）等IO操作完成之后再继续往下执行
    # 当前协程挂起时，事件循环就会去执行其他协程任务

    result = await others()

    print('IO操作完成，结果为：',result)
# asyncio.run(func())
loop = asyncio.get_event_loop()
loop.run_until_complete(func())
```
**执行结果**
执行协程函数内部代码
start
end
IO操作完成，结果为： 返回值

**示例3**
多个await对象
```python
import asyncio

async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def func():
    print('执行协程函数内部代码')
    #遇到IO操作，挂起当前协程(任务）等IO操作完成之后再继续往下执行
    # 当前协程挂起时，事件循环就会去执行其他协程任务

    result = await others()

    print('IO操作完成，结果为：',result)

    result1 = await others()

    print('IO操作完成，结果为：',result1)
# asyncio.run(func())
loop = asyncio.get_event_loop()
loop.run_until_complete(func())

```

### Task对象
task对象在事件循环中添加多个任务，用于并发调度协程，通过asyncio.create_task(协程对象)的方式创建task对象，这样可以让协程加入事件循环中等待被调度执行，除了使用asyncio.create_task(),函数以外，还可以用低层级的loop.create_task(),ensure_future()函数，不建议手动实例化Task对象。
**示例1**
```python
import asyncio

async def fun():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def main():
    print('执行协程函数内部代码')
    #遇到IO操作，挂起当前协程(任务）等IO操作完成之后再继续往下执行
    # 当前协程挂起时，事件循环就会去执行其他协程任务

    # task1 = asyncio.create_task(fun())
    # task2 = asyncio.create_task(fun())
    task1 = asyncio.ensure_future(fun())
    task2 = asyncio.ensure_future(fun())

    print('main finish')

    result1 = await task1
    result2 = await task2

    print('IO操作完成，结果为：',result1,result2)
# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

```
**结果**
执行协程函数内部代码
main finish
start
start
end
end
IO操作完成，结果为： 返回值 返回值

**示例2**
```python
import asyncio

async def fun():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

async def main():
    print('执行协程函数内部代码')
    #遇到IO操作，挂起当前协程(任务）等IO操作完成之后再继续往下执行
    # 当前协程挂起时，事件循环就会去执行其他协程任务

    # task1 = asyncio.create_task(fun()) create_task可以添加name参数指定名字
    # task2 = asyncio.create_task(fun())
    task1 = asyncio.ensure_future(fun())
    task2 = asyncio.ensure_future(fun())

    task_list = [task1,task2] # 定义一个task对象列表

    print('main finish')

    done,pending = await asyncio.wait(task_list,timeout=2) #timeout参数为可选，如果超出时间那么就没执行完，此时done为空，pending为未执行完的对象


    print('IO操作完成，结果为：',done)
# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

**结果**
执行协程函数内部代码
main finish
start
start
IO操作完成，结果为： set()
end

可以看到done为一个集合。

**示例3**
```python
import asyncio

async def fun():
    print('start')
    await asyncio.sleep(2)
    print('end')
    return '返回值'

task_list = [fun(),fun()] # 定义一个task对象列表

done,pending = asyncio.run(asyncio.wait(task_list,timeout=2))
print(done)
```

### future对象
Task继承Future,Task对象内部await 结果的处理基于Future对象来的
**示例1**
```python
import asyncio

async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（future对象） 这个任务什么也不干
    fut = loop.create_future()

    # 等待任务最终结果（Future对象）没有结果会一直等下去
    await fut

asyncio.run(main())
```

**示例2**
```python
import asyncio

async def set_after(fut):
    await asyncio.sleep(2)
    fut.set_result('0')

async def main():
    # 获取当前事件循环
    loop = asyncio.get_running_loop()

    # 创建一个任务（future对象） 没绑定任何行为，则这个任务永远不知道什么时候结束 
    fut = loop.create_future()

    # 创建一个任务（Task对象）绑定了set after函数，函数内部在2s后给fut赋值
    # 即手动设置future任务的结果，那么fut就结束了
    await loop.create_task(set_after(fut))
    data = await fut
    
asyncio.run(main())
```

### concurrent.futures.Future对象

```python
import time
from concurrent.futures import future 
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import processPoolExecutor


def func(value):
    time.sleep(1)
    print(value)
    return
pool = ThreadPoolExecutor(max_workers=5)

# pool = processPoolExecutor(max_workers=5)

for i in range(10):
    fut = pool.submit(func,i)
    print(fut)
    
```
线程池一次只能创建5个连接，但实际它创建了10个，后面的一个只是在等待前面的执行完成。
可能会存在交叉使用的情况：如异步编程+mysql(不支持异步）这时就可能使用Concurrent.futures

```python
import time
from concurrent.futures import future 
from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import processPoolExecutor


def func1(value):
    time.sleep(1)
    print(value)
    return


async def main():
    loop = asyncio.get_runing_loop()

    # run in the deafult executor(ThreadPoolExecutor)
    # 第一步先调用ThreadPoolExecutor的submit方法去线程池中申请一个线程 执行func1函数 
    # 并返回一个concurrent.futures.Future对象
    # 第二步 调用asyncio.wrap_future将concurrent.futures.Future对象包装成asyncio.Future对象
    # 因为concurrent.futures.Future对象不支持await语法，所以需要包装为asyncio.Future对象才能使用
    fut = loop.run_in_executor(None,func1)
    result = await fut
    print('default thread pool', result)

    # 2 run in custom thread pool
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, func1)
        print('custom thread pool',result)
    # 3 run in a custom process pool
    with concurrent.futures.processPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, func1)
        print('custom process pool',result)

asyncio.run(main())
```

**实例**
```python
import asyncio
import requests

async def download_images(url):
    # 发送网络请求，下载图片，遇到网络IO,自动切换到其它任务
    print('开始下载', url)
    loop = asyncio.get_event_loop()

    # requests 默认不支持异步操作，所以使用线程池来配合实现
    future = loop.run_in_executor(None, requests.get, url)

    response = await future
    print('下载完成')
    file_name = url.rsplit('-')[-1]

    with open(file_name, mode='wb') as file_obj:
        file_obj.write(response.content)


if __name__ == '__main__':
    url_list = []
    tasks = [download_images(url) for url in url_list]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
```

### 异步迭代器
```python
import asyncio


class Reader:
    def __init__(self):
        self.count = 0

    async def read_count(self):
        # await asyncio.sleep(1)
        self.count += 1
        if self.count == 100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        val = await self.read_count()
        if val == None:
            raise StopAsyncIteration
        return val


async def func():
    obj = Reader()
    # async for 必须写在一个协程函数中
    async for item in obj:
        print(item)


asyncio.run(func())

```

### 异步上下文管理器
```python
import asyncio


class AsyncContextManager:
    def __int__(self):
        self.conn = conn

    async def do_something(self):
        # 异步操作
        return

    async def __aenter__(self):
        # 异步
        self.conn = await asyncio.sleep(1)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        # 异步关闭
        await asyncio.sleep(1)


obj = AsyncContextManager()


async def func():
    # async with 必须放在协程函数中
    async with obj as f:
        result = await f.do_something()
        pass
```

### 异步redis
pip install aioredis
```python
import asyncio
import aioredis

async def execute(address,password):
    print('开始执行',address)
    # 网络io操作，创建redis连接
    redis=await aioredis.create_redis(address,password=password)
    # 网络IO操作，在redis中设置哈希值
    await = redis.hmset_dict('car',key=1,key2=2,key3=3)
    # 网络IO操作，去redis中获取值
    result = await redis.hgetall('car',encoding='utf-8')

    print(result)
    # 网络IO操作，关闭redis连接
    redis.close()
    print('结束')

asyncio.run(func)
```

### 异步mysql
```python
import asyncio
import aiomysql

async def execute():  
    conn = await aiomysql.connct(host='127.0.0.1',port=3306,usr='root',password='123',db='mysql')

    # 网络IO 创建cursor
    cur = await conn.cursor
    # 网络IO 执行sql
    await cur.execute('Select * from user')
    # 网络IO 获取结果 
    result = await cur.fetchall()
    print(result)
    # 网络IO 关闭连接
    await cur.close()
    conn.close()

asyncio.run(execute)

```

**多个连接**
```python
import asyncio
import aiomysql

async def execute():  
    conn = await aiomysql.connct(host='127.0.0.1',port=3306,usr='root',password='123',db='mysql')

    # 网络IO 创建cursor
    cur = await conn.cursor
    # 网络IO 执行sql
    await cur.execute('Select * from user')
    # 网络IO 获取结果 
    result = await cur.fetchall()
    print(result)
    # 网络IO 关闭连接
    await cur.close()
    conn.close()
task_list = [
 execute('1.1.1.1','password1'),
 execute('1.2.3.4','password2')
]
asyncio.run(asyncio.wait(task_list))

```

### FastAPi
```shell
pip install fastapi
pip install uvicorn
```

**示例**
```python
import asyncio

import uvicorn
from fastapi import FastAPI 

app = FastAPI()

REDIS_POOL = aioredis.ConnectionsPool('redis://ip:port',password='password',minsize=1,maxsize=10)

@app.get('/')
def index():
    # 普通接口
    return {"msg":'hello world'}

async def read():
    # 异步接口
    print('请求来了')
    await asyncio.sleep(3)
    # 连接
    conn = await REDIS_POOL.acquire()
    redis = redis(conn)

    # 设置值
    await redis.hmset_dict('car',key1=1,key2=2)

    # 取值
    result = await redis.hgetall('car',encoding='utf-8')

    # REDIS_POOL.release(conn)
    return result

if __name__ == '__main__':
    uvicorn.run('code:app',host='127.0.0.1',port=5000,log_level='info')

```

### 爬虫
```shell
pip install aiohttp
```

```python
import aiohttp
import asyncio


async def fetch(session,url):
    print('发送请求',url)
    async with session.get(url, verify_ssl=False) as response:
        text = await response.text
        print('得到结果',url,len(text))

async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
        'https://python.org',
        'https://www.baidu.com'
        ]
        tasks = [asyncio.create_task(fetch(session,url) for url in url_list)]

        await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
```

### 同步与阻塞的关系

#### 状态
在程序运行的过程中，由于被操作系统的调度算法控制，程序会进入几个状态：就绪，运行和阻塞。

（1）就绪(Ready)状态
当进程已分配到除CPU以外的所有必要的资源，只要获得处理机便可立即执行，这时的进程状态称为就绪状态。
（2）执行/运行（Running）状态当进程已获得处理机，其程序正在处理机上执行，此时的进程状态称为执行状态。
（3）阻塞(Blocked)状态正在执行的进程，由于等待某个事件发生而无法执行时，便放弃处理机而处于阻塞状态。引起进程阻塞的事件可有多种，例如，等待I/O完成、申请缓冲区不能满足、等待信件(信号)等。

#### 同步与异步
所谓同步就是一个任务的完成需要依赖另外一个任务时，只有等待被依赖的任务完成后，依赖的任务才能算完成，这是一种可靠的任务序列其实就是一个程序结束才执行另外一个程序，串行的，不一定两个程序就有依赖关系。

所谓异步是不需要等待被依赖的任务完成，只是通知被依赖的任务要完成什么工作，依赖的任务也立即执行，只要自己完成了整个任务就算完成了。至于被依赖的任务最终是否真正完成，依赖它的任务无法确定，所以它是不可靠的任务序列。

举例
> 比如我们去楼下的老家肉饼吃饭，饭点好了，取餐的时候发生了一些同步异步的事情。同步：我们都站在队里等着取餐，前面有个人点了一份肉饼，后厨做了很久，但是由于同步机制，我们   还是要站在队里等着前面那个人的肉饼做好取走，我们才往前走一步。

> 异步：我们点完餐之后，点餐员给了我们一个取餐号码，跟你说，你不用在这里排队等着，去找个地方坐着玩手机去吧，等饭做好了，我叫你。这种机制(等待别人通知)就是异步等待消息通知。在异步消息处理中，等待消息通知者(在这个例子中等着取餐的你)往往注册一个回调机制，在所等待的事件被触发时由触发机制(点餐员)通过某种机制(喊号，‘250号你的包子好了‘)找到等待该事件的人。
> 
#### 阻塞和非阻塞

阻塞和非阻塞这两个概念与程序（线程）等待消息通知(无所谓同步或者异步)时的状态有关。也就是说阻塞与非阻塞主要是程序（线程）等待消息通知时的状态角度来说的

**阻塞和非阻塞举例**

> 继续上面的那个例子，不论是排队还是使用号码等待通知，如果在这个等待的过程中，等待者除了等待消息通知之外不能做其它的事情，那么该机制就是阻塞的，表现在程序中,也就是该程序一直阻塞在该函数调用处不能继续往下执行。相反，有的人喜欢在等待取餐的时候一边打游戏一边等待，这样的状态就是非阻塞的，因为他(等待者)没有阻塞在这个消息通知上，而是一边做自己的事情一边等待。阻塞的方法：input、time.sleep，socket中的recv、accept等等。

#### 比较
**同步阻塞形式**
效率最低。拿上面的例子来说，就是你专心排队，什么别的事都不做。

**异步阻塞形式**
如果在排队取餐的人`采用的是异步的方式去等待消息被触发（通知）`，也就是领了一张小纸条，假如在这段时间里他不能做其它的事情，就在那坐着等着，不能玩游戏等，那么很显然，这个人被阻塞在了这个等待的操作上面；
**异步操作是可以被阻塞住的，只不过它不是在处理消息时阻塞，而是在等待消息通知时被阻塞。**

**同步非阻塞形式**
实际上是效率低下的。
想象一下你一边打着电话一边还需要抬头看到底队伍排到你了没有，如果把打电话和观察排队的位置看成是程序的两个操作的话，`这个程序需要在这两种不同的行为之间来回的切换`，效率可想而知是低下的。

**异步非阻塞形式**
效率更高，
因为打电话是你(等待者)的事情，而通知你则是柜台(消息触发机制)的事情，`程序没有在两种不同的操作中来回切换`。
比如说，这个人突然发觉自己烟瘾犯了，需要出去抽根烟，于是他告诉点餐员说，排到我这个号码的时候麻烦到外面通知我一下，那么他就没有被阻塞在这个等待的操作上面，自然这个就是异步+非阻塞的方式了。

很多人会把同步和阻塞混淆，是`因为很多时候同步操作会以阻塞的形式表现出来`，同样的，很多人也会把异步和非阻塞混淆，`因为异步操作一般都不会在真正的IO操作处被阻塞`。


## 算法时间复杂度

- 找出基本操作
- 计算基本操作执行的次数
- 去掉低阶项，常数项

基本操作：常数 用加法
顺序结构：常数 用加法
循环结构：乘法 
分支结构：取最大值


### 举例说明：

```python
def bubble(arr):
    n = len(arr)	 # 基本操作 1次
	for i in range(n): # 循环结构 用乘法  n 
		for j in range(n-i-1):  # 循环结构 用乘法 n
			if arr[j] < arr[j+1]: # 分支结构 取最大值 ：
				arr[j],arr[j+1] = arr[j+1], arr[j] # 基本操作1次
	return arr
```

最坏的情况下，内层循环会执行n-1，n-2,n-3 .... 1次
计算过程 ： n  * （n-1+1)*(n-1)/2 * 3   在这里的3属于常数项，去掉，剩下结果为n*n

### 常见算法复杂度：

#### 常数复杂度：O(1)

```python
def f(item):
	return item[0]
```

#### 线性时间复杂度O(n)

```python
def f(arr, target):
	for i in range(len(arr)): # 循环结构 n
		if arr[i] == target:  # 分支结构 最坏的情况下，每次循环都会执行这个判断 
			return i
```

计算过程：n * 2  , 去掉常数项，O(n)

#### 二次时间复杂度

[[001_Python基础#举例说明：]]

#### 对数时间复杂度

```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

```

这里主体部分是while 循环，即循环结构，其它的都是常数项，那么循环执行多少次呢？
第一次执行时后，需要查找的数组长度为n/2, 依次为：
- n
- n/2
- n/ 2 * 2
- n/ 2 * 2 * 2
- n/ 2 * (k-1)

假如第k次找到了目标，那么 n/ 2 * (k-1) = 1, k = 1 + log2n, 去掉常数项，则复杂度为 O(log2n)

#### 线性对数时间

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

```