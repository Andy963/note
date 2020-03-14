
## module

### 列举常用的模块。
```
os,datatime,date,time, hashlib,math,re,urlib,random,json
```

### 如何安装第三方模块？
```
pip install
easy_install
```

### re 的match 和search 区别？
```
match（）函数只检测RE是不是在string的开始位置匹配，

search()会扫描整个string查找匹配；
```

### 什么是正则的贪婪匹配？或 正则匹配中的贪婪模式与非贪婪模式的区别？
```
贪婪匹配:正则表达式一般趋向于最大长度匹配，也就是所谓的贪婪匹配。

非贪婪匹配：就是匹配到结果就好，就少的匹配字符。
```

### 如何生成一个随机数？
```
import random
 
print(random.random())          # 用于生成一个0到1的随机符点数: 0 <= n < 1.0
print(random.randint(1, 1000))  # 用于生成一个指定范围内的整数
```

### 如何使用python 删除一个文件？
```
import os
file = r'D:\test.txt'
if os.path.exists(file):
    os.remove(file)
    print('delete success')
else:
    print('no such file:%s' % file)
```

### logging 模块的作用？以及应用场景？
```
logging模块定义的函数和类为应用程序和库的开发实现了一个灵活的事件日志系统。logging模块是Python的一个标准库模块，由标准库模块提供日志记录API的关键好处是所有Python模块都可以使用这个日志记录功能。所以，你的应用日志可以将你自己的日志信息与来自第三方模块的信息整合起来
```

### json 序列化时，可以处理的数据类型有哪些？如何定制支持datetime 类型？
```
integer, string, dict, array, boolean,null,object

import json
from json import JSONEncoder
from datetime import datetime

class ComplexEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return super(ComplexEncoder,self).default(obj)
d = { 'name':'alex','data':datetime.now()}
print(json.dumps(d,cls=ComplexEncoder))
# {"name": "alex", "data": "2018-05-18 19:52:05"}

json序列化时遇到中文会默认转换成unicode  ，如何让他保留中文形式
import json
a=json.dumps({"ddf":"你好"},ensure_ascii=False)
print(a) #{"ddf": "你好"}
```

### 写代码实现查看一个目录下的所有文件
```
if os.path.exists(folder):
    for root, dirs, files in os.walk(folder, topdown=True):
        for file in files:
            file_path = os.path.join(folder, file)
            file_names.append(file_path)
```

### 用Python 匹配HTML tag 的时候,<.>和<.?>有什么区别?
```
前面为贪婪匹配，会茶杯尽可能多的内容
后者为非贪婪匹配，会匹配一个（如果有匹配）
```
### 如何判断一个邮箱合法
```
import re
text = input("Please input your Email address：\n")
if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$',text):
#if re.match(r'[0-9a-zA-Z_]{0,19}@163.com',text):
    print('Email address is Right!')
else:
    print('Please reset your right Email address!')
 
```
### 请写出以字母或下划线开始, 以数字结束的正则表达式
```
import re
pattern = r'^[a-zA-z_]*[0-9]$'
```

### 写Python 爬虫都用到了那些模块, 分别是做什么用的?
```
urlib
xpath
scrapy

```
### sys.path.append("/root/mods")的作用？
```
将模块路径加到当前模块扫描的路径里
```

### 列举出Python 中比较熟知的爬虫框架
```
scrapy
requests
urlib
seliume
bs4
xpath
```

### 输入某年某日, 判断这是这一年的第几天?(可以用Python 的内置模块)
```
import datetime

y = int(input('请输入4位数字的年份：'))  # 获取年份
m = int(input('请输入月份：'))  # 获取月份
d = int(input('请输入是哪一天：'))  # 获取“日”

targetDay = datetime.date(y, m, d)  # 将输入的日期格式化成标准的日期
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  # 减去上一年最后一天
print('%s是%s年的第%s天。' % (targetDay, y, dayCount.days))
```

### 使用过Python 那些第三方组件
```
gevent
paramiko
mptt
```