## 配置

### from_object
使用`app.config.from_object`的方式加载配置文件：
将配置写在config文件中

1. 导入`import config`。
2. 使用`app.config.from_object(config)`。
当在config中设置：
```python
Debug=True 
```
此时获取config['DEBUG']得到是False,默认值
而如果conifg['Debug']来获取，则会报错，小写的配置被忽略，导致找不到变量。
**所有的配置文件中的变量都必须大写**。

### from_pyfile
使用`app.config.from_pyfile`的方式加载配置文件：
这种方式不需要`import`，直接使用`app.config.from_pyfile('config.py')`就可以了。
注意这个地方，必须要写文件的全名，后缀名不能少。

1. 这种方式，加载配置文件，不局限于只能使用`py`文件，普通的`txt`文件同样也适合。
2. 这种方式，可以传递`silent=True`，那么这个静态文件没有找到的时候，不会抛出异常。

本地服务器启用多线程或者多进程：
```python
app.run(threaded=True) # process
```