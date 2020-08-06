本篇主要讲一下`__getattribute__, __getattr__,__get__`的执行顺序

```python
#!/usr/bin/env python
# coding:utf-8


class Account:
    user_name = 'andy'

    def __get__(self, instance, owner):
        print('作为类属性时被访问时，无条件经过我')
        print(instance, owner)
        return self

    def __getattribute__(self, item):
        print('访问属性时，无条件经过我')
        return object.__getattribute__(self, item)

    def __getattr__(self, item):
        print('当__getattribute__失败时经过我')


class UserAccount(Account):
    account = Account()


if __name__ == '__main__':
    u = UserAccount()
    # print(u.user_name)
    print(u.account)
"""    
访问属性时，无条件经过我
作为类属性时被访问时，无条件经过我
<__main__.UserAccount object at 0x7f641ee7ff60> <class '__main__.UserAccount'>
<__main__.Account object at 0x7f641eef4630>
"""
```
总结就是：
当获取属性时，无条件走`__getattribute__`,当属性获取失败，异常时，会尝试走`__getattr__`,相当于后备手段（不知是不是通常所说的防御型编程）。而`__get__`则针对当前类作为另一个类的类属性时调用，但注意：因为`__getattribute__`在获取属性(包括类属性)时无条件执行，所以会先走`__getattribte__`,从它执行的结果可以看到，先执行了`__getattribute__`,再是`__get__`