## gevent模块

并发，一个cpu执行多个任务，看起来像是同时发生（运行）。核心是：切换并保存状态。



### 什么是同步，异步？

同步指在发生一个功能调用时在没有得到结果之前不返回该调用，一旦调用返回就得到了返回值。
异步指是一个功能调用后立即返回，没有返回结果，但可以执行另外的功能。当该功能执行完成后，可以通过状态，通知等方式来告知调用者取回返回值。

### 什么是阻塞，非阻塞
阻塞调用是指调用结果返回之前，当前线程会被挂起（如遇到io操作）。调用线程只有在得到结果之后才会返回。函数只有在得到结果之后才会将阻塞的线程激活

非阻塞和阻塞的概念相对应，非阻塞调用指在不能立刻得到结果之前也会立刻返回，同时该函数不会阻塞当前线程

### 同步异步，阻塞与非阻塞

同步与异步针对的是函数/任务的调用方式：同步就是当一个进程发起一个函数（任务）调用的时候，一直等到函数（任务）完成，而进程继续处于激活（非阻塞）状态。而异步情况下是当一个进程发起一个函数（任务）调用的时候，不会等函数返回，而是继续往下执行，当函数返回的时候通过状态、通知、事件等方式通知进程任务完成。

阻塞与非阻塞针对的是进程或线程：阻塞是当请求不能满足（得到结果）的时候就将进程挂起，而非阻塞则不会阻塞当前进程

### Gevent是什么？
一个第三方模块，用来实现并发。

### greenlet的作用，有什么缺点？
grennlet实现了任务切换，但遇到IO时会阻塞，不能自动切换。gevent遇到I/O阻塞时会自动切换来提高效率。

asynchronous/synchronous  #   异步与同步

### gevent使用流程是？

*spawn(task)  #  起任务
*join/joinall()  #  阻塞主线程


### 实例

```python
import gevent
import requests
import time

from gevent import monkey;

monkey.patch_all()

def get_page(url):
    print('GET: %s' % url)
    response = requests.get(url)
    if response.status_code == 200:
        print('%d bytes received from %s' % (len(response.text), url))

start_time = time.time()
gevent.joinall([
    gevent.spawn(get_page, 'https://www.python.org/'),
    gevent.spawn(get_page, 'https://www.yahoo.com/'),
    gevent.spawn(get_page, 'https://github.com/'),
])
stop_time = time.time()
print('run time is %s' % (stop_time - start_time))
```



