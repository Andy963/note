# design_pattern


### 单例模式
第一种
```py
class Singleton:
    __instance = None
    __is_first_init = False
    
    def __new__(cls, name):
        if not cls.__instance:
            Singleton.__instance = super().__new__(cls)
        return cls.__instance
        
    def __init__(self, name):
        if not self.__is_first_init:
            Singleton.__is_first_init = True
```
第二种
```py
class Singleton(type):
    def __init__(cls,what,bases=None,dict=None):
        super().__init__(what,bases,dict)
        cls.__instacne = None
        
    def __call__(cls,*args,**kwargs):
        if cls.__instance = super().__call__(*args,**kwargs)
       return cls.__instance
       

class NewClass(metaclass=Singleton):
    def __init__(self):
        pass
        
```

第三种
```py
def singletonDecorator(cls,*args, **kwargs):
    instance = {}
    
    def wrapperSingleton(*args,**kwargs):
        if cls not in instance:
            instance(cls) = cls(*args, **kwargs)
        return instance(cls)
        
    return wrapperSingleton
    

@singletonDecorator
class NewClass:
    def __init__(self):
        pass
```