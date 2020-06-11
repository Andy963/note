

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