新开个笔记读读flask 的源码，这里用来记录一些比较有意思的发现，或者任何其它想记录的东西


sqlalchemy中单例模式,它是通过` try, execept` 来关闭锁的，而不是通过 `with ` 语句

```python
# sqlalchemy\util\langhelpers.py
_symbol.__name__ = "symbol"  
  
  
class symbol(object):
	symbols = {}  
	_lock = compat.threading.Lock()  
	  
	def __new__(cls, name, doc=None, canonical=None):  
	    cls._lock.acquire()  
	    try:  
	        sym = cls.symbols.get(name)  
	        if sym is None:  
	            cls.symbols[name] = sym = _symbol(name, doc, canonical)  
	        return sym  
	    finally:  
	        symbol._lock.release()
```