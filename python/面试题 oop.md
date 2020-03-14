## 面向对象

### 简述面向对象的三大特性
```
封装、继承、多态
封装：把对象的属性私有化，同时提供可以被外界访问这些属性的方法。
继承：是使用已存在的类的定义，作为建立新类的基础技术，新类可以增加新的属性或新的方法，也可以用父类的功能，但不能选择性地继承。通过使用继承，能够非常方便地复用这些代码。
多态：(事物有多种形态)表现为程序中定义的引用变量，所指向的具体类型和具体调用的方法，在编译期并不能确定，而是在程序运行期确定
```

### 什么是鸭子模型？
```
一个对象有效的语义，不是由继承自特定的类或实现特定的接口，而是由"当前方法和属性的集合"决定
在鸭子类型中，关注的不是对象的类型本身，而是它是如何使用的
```
### super 的作用？
```
用于子类继承父类的方法，并按照mro的顺序查找父类的方法
```

### mro 是什么？
```
Python的方法解析顺序(Method Resoluthion Order, 或MRO)。
```

### 什么是c3 算法？
```
多重继承时计算继承顺序的看法
```

### 列举面向对象中带双下划线的特殊方法
```
__doc__
__call__
__dict__
__str__
__repr__
__getitem__
__setitem__
__delitem__
__new__
__metaclass__
__enter__ __exit__
```
### 双下划线和单下划线的区别？
```
1、前后都有双下划线-特殊变量
变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名

2、前面双下划线-私有变量
在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问。
双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_${classname}__name，所以，仍然可以通过_${classname}__name来访问__name变量。但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名

3、前面单下划线-口头私有变量
以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”
```

### 实例变量和类变量的区别？
```
类变量也叫静态变量，
实例变量也叫对象变量，
区别在于：
   类变量和实例变量的区别在于：类变量是所有对象共有，其中一个对象将它值改变，其他对象得到的就是改变后的结果；而实例变量则属对象私有，某一个对象将其值改变，不影响其他对象；
```

### 静态方法和类方法区别？
```
staticmethod主要用途是限定namespace，也就是说这个函数虽然是个普通的function，但是它只有这个class会用到，不适合作为module level的function。这时候就把它作为staticmethod

                类调用           实例化对象调用   需要传入类
classmethod     可以	  可以	需要
staticmethod	可以	可以	不需要
classonlymethod	可以	不可以	需要

```

### isinstance 和type 的作用？
```
共同点：两者都可以判断对象类型
不同点：对于一个 class 类的子类对象类型判断，type就不行了，而 isinstance 可以。
```

### 有用过with statement（语句）吗？它的好处是什么？
```
with语句的作用是通过某种方式简化异常处理，它是所谓的上下文管理器的一种
比如文件操作时能在操作结束 后自动关闭文件处理
```

### 请􁧿述with 的用法, 如果自己的类需要支持with 语句, 应该如何书写?

```
通过类型去判断python对象是否可调用，需要同时判断的是函数还是方法，或者类是否实现__call__方法，如果一个类实现了__call__方法，那么其实例也会成为一个可调用对象

```

### 请用两个队列来实现一个栈(给出伪代码即可)
```

```

### 已知如下链表类, 请实现单链表逆置
```
class Node:
2. def __init__(self, value, next):
3. self.value = value
4. self.next = next
```

### 类的加载顺序(类中有继承有构造有静态)
```

```

### 参考下面代码片段
请在Context 类下添加代码完成该类的实现
```
class Context:
   pass

with Content() as ctx:
    ctx.do_something()

class Content:
    def __enter__(self):
        return self
​
    def __exit__(self, type, value, trace):
        print("type:", type)
        print("value:", value)
        print("trace:", trace)
        print(sample)
​
​
    def do_something(self):
        bar = 1
        return bar + 10
```
### 函数del_node(self,data)的功能
: 在根节点指针为root 的二叉树(又称二叉=排序树)上排除数值为K 的节点,若删除成功,返回0,否则返回-1, 概述节点的定义类型为

```
class Node(object):
    def __init__(self,data):
    self.data = data # 节点的数值
    self.left_child = Node # 指向左右子树的指针
    self.right_child = Node

    def set_data(self,data):
    self.data = data
```

