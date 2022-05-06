# asyncIo使用

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