# design_pattern


### 单例模式

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