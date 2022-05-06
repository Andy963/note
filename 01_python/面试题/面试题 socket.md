## 网络

### python 的底层网络交互模块有哪些？
```
socket, urllib,urllib3 , requests, grab, pycurl
```

### 简述 OSI 七层协议。
```
应表会传网数物

应用层：HTTP，FTP，NFS

表示层：Telnet，SNMP

会话层：SMTP，DNS

传输层：TCP，UDP

网络层：IP，ICMP，ARP，

数据链路层：Ethernet，PPP，PDN，SLIP，FDDI

物理层：IEEE 802.1A，IEEE 802.11
```

### 什么是C/S和B/S架构？
```
软件系统体系结构:
C/S体系结构:client/server
指的是客户端/服务端    例如;QQ，微信

B(browser)/S体系结构:browser/server
指的是浏览器/服务端      例如12306(网站);购物网站,微信小程序


两者区别:
C/S :优点:交互性好,对服务器压力小,安全 ;缺点:服务器更新时需要同步更新客户端
B/S:优点:不需要更新客户端   缺点:交互性差,安全性低
```

### 简述 TCP 三次握手、四次挥手的流程。
```

```

### 什么是arp 协议？
```
ARP协议，全称“Address Resolution Protocol”,中文名是地址解析协议，使用ARP协议可实现通过IP地址获得对应主机的物理地址（MAC地址）
```

### TCP 和UDP 的区别？为何基于tcp 协议的通信比基于udp 协议的通信更可靠？
```
TCP类似于：打电话（反馈机制,有回复）
UDP类似于：发短信（只管往一个地址发送，没有反馈机制）
'''
1、TCP面向连接（如打电话要先拨号建立连接）;UDP是无连接的，即发送数据之前不需要建立连接
2、TCP提供可靠的服务。也就是说，通过TCP连接传送的数据，无差错，不丢失，不重复，且按序到达;UDP尽最大努力交付，即不保证可靠交付
3、TCP面向字节流，实际上是TCP把数据看成一连串无结构的字节流;UDP是面向报文的
UDP没有拥塞控制，因此网络出现拥塞不会使源主机的发送速率降低（对实时应用很有用，如IP电话，实时视频会议等）
4、每一条TCP连接只能是点到点的;UDP支持一对一，一对多，多对一和多对多的交互通信
5、TCP首部开销20字节;UDP的首部开销小，只有8个字节
6、TCP的逻辑通信信道是全双工的可靠信道，UDP则是不可靠信道
'''

# 为何基于tcp协议的通信比基于udp协议的通信更可靠？
'''
tcp:可靠 对方给了确认收到信息，才发下一个，如果没收到确认信息就重发
udp:不可靠 一直发数据，不需要对方回应
'''
```

### 什么是局域网和广域网？
```
两者范围不一样:
        局域网就是在固定的一个地理区域内由2台以上的电脑用网线和其他网络设备搭建而成的一个封闭的计算机组，范围在几千米以内；
        广域网是一种地域跨度非常大的网络集合，范围在几十公里到几千公里。

两者的IP地址设置不一样:
        局域网里面，必须在网络上有一个唯一的IP地址，这个IP地址是唯一的，在另外一个局域网，这个IP地址仍然能够使用。
        广域网上的每一台电脑（或其他网络设备）都有一个或多个广域网IP地址，而且不能重复
```

### 什么是socket?简述基于tcp协议的套接字通信流程？
```
Socket是应用层与TCP/IP协议族通信的中间软件抽象层，它是一组接口。在设计模式中，Socket其实就是一个门面模式，它把复杂的TCP/IP协议族隐藏在Socket接口后面，对用户来说，一组简单的接口就是全部。

服务端:
创建socket对象，绑定ip端口bind(),  设置最大链接数listen(),  accept()与客户端的connect()创建双向管道， send(), recv(),close()

客户端:
创建socket对象，connect()与服务端accept()创建双向管道, send(),recv(),close()
```

### 什么是粘包？ socket 中造成粘包的原因是什么？ 哪些情况会发生粘包现象？
```
粘包:
数据粘在一起，主要因为：接收方不知道消息之间的界限，不知道一次性提取多少字节的数据，造成的数据量比较小，时间间隔比较短，就合并成了一个包，这是底层的一个优化算法（Nagle算法）

只有TCP有粘包现象，UDP永远不会粘包
粘包：在获取数据时,出现数据的内容不是本应该接收的数据,如:对方第一次发送hello,第二次发送world,
　　我方接收时,应该收两次,一次是hello,一次是world,但事实上是一次收到helloworld,一次收到空,这种现象叫粘包
原因
粘包问题主要还是因为接收方不知道消息之间的界限，不知道一次性提取多少字节的数据所造成的。

什么情况会发生：
1、发送端需要等缓冲区满才发送出去，造成粘包（发送数据时间间隔很短，数据包很小，会合到一起，产生粘包）

2、接收方不及时接收缓冲区的包，造成多个包接收（客户端发送了一段数据，服务端只收了一小部分，服务端下次再收的时候还是从缓冲区拿上次遗留的数据，产生粘包）
```

### IO 多路复用的作用？
```
socketserver，多个客户端连接，单线程下实现并发效果，就叫多路复用。

与多进程和多线程技术相比，I/O多路复用技术的最大优势是系统开销小，系统不必创建进程/线程，也不必维护这些进程/线程，从而大大减小了系统的开销。
```

### 什么是防火墙以及作用
```
  在互联网上防火墙是一种非常有效的网络安全模型，通过它可以隔离风险区域(即Internet或有一定风险的网络)与安全区域(局域网)的连接，同时不会妨碍人们对风险区域的访问。所以它一般连接在核心交换机与外网之间。
    作用：
        1.过滤进出网络的数据 
        2.管理进出访问网络的行为 
        3.封堵某些禁止业务 
        4.记录通过防火墙信息内容和活动 
        5.对网络攻击检测和告警
```
### select、poll、epoll 模型的区别？
```
都是i/o多路复用的机制，监视多个socket是否发生变化，本质上都是同步i/o
    select,poll实现需要自己不断轮询所有监测对象，直到对象发生变化，在这个阶段中，
可能要睡眠和唤醒多次交替，而epoll也需要调用epoll_wait不断轮询就绪链表，但是当对象发生变化时，
会调用回调函数，将变化的对象放入就绪链接表中，并唤醒在epoll_wait中进入睡眠的进程。
虽然都会睡眠和唤醒，但是select和poll在被唤醒的时候要遍历整个监测对象集合，
而epoll只要判断就绪链表是否为空即可，节省了大量cpu的时间
```

### 简述 进程、线程、协程的区别 以及应用场景？
```
进程最小的资源单位
线程是指进程内的一个执行单元，
# 进程
进程拥有自己独立的堆和栈，既不共享堆，亦不共享栈，进程由操作系统调度。
# 线程
线程拥有自己独立的栈和共享的堆，共享堆，不共享栈，线程亦由操作系统调度
# 协程和线程
协程避免了无意义的调度，由此可以提高性能；但同时协程也失去了线程使用多CPU的能力

进程与线程的区别
（1）地址空间：线程是进程内的一个执行单位，进程内至少有一个线程，他们共享进程的地址空间，而进程有自己独立的地址空间
（2）资源拥有：进程是资源分配和拥有的单位，同一个进程内线程共享进程的资源
（3）线程是处理器调度的基本单位，但进程不是
（4）二者均可并发执行
（5）每个独立的线程有一个程序运行的入口

协程与线程
（1）一个线程可以有多个协程，一个进程也可以单独拥有多个协程，这样Python中则能使用多核CPU
（2）线程进程都是同步机制，而协程是异步
（3）协程能保留上一次调用时的状态
```

### 什么是GIL 锁？
```
GIL本质就是一把互斥锁，既然是互斥锁，所有互斥锁的本质都一样，都是将并发运行变成串行，以此来控制同一时间内共享数据只能被一个任务所修改，进而保证数据安全。

GIL保护的是解释器级的数据，保护用户自己的数据则需要自己加锁处理
应用（总结）：
多线程用于IO密集型，如socket，爬虫，web
多进程用于计算密集型，如金融分析
  1. 每个cpython进程内都有一个GIL
  2. GIL导致同一进程内多个进程同一时间只能有一个运行
  3. 之所以有GIL，是因为Cpython的内存管理不是线程安全的
  4. 对于计算密集型用多进程，多IO密集型用多线程
```

### Python 中如何使用线程池和进程池？
```
import threadpool, time
 
with open(r'../uoko_house_id.txt', 'r', encoding='utf-8') as f:    # with open语句表示通用的打开文件的方式，此处用来获取需要爬取参数的列表
    roomIdLi = f.readlines()
    roomIdList =[x.replace('\n','').replace(' ','') for x in roomIdLi]
    print(roomIdList)
    li = [[i, item] for i, item in enumerate(roomIdList)]    # enumerate()将列表中元素和其下标重新组合输出
 
def run(roomId):
    """对传入参数进行处理"""
    print('传入参数为：', roomId)
    time.sleep(1)
  
def main():
    roomList = li       # 房间信息
    start_time = time.time()
    print('启动时间为：', start_time)
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(run, roomList)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    print("共用时:", time.time()-start_time)
 
if __name__ == '__main__':
    main()
    
    

# 进程池
from multiprocessing.pool import Pool
from time import sleep
 
def fun(a):
    sleep(5)
    print(a)
 
if __name__ == '__main__':
    p = Pool()             
    for i in range(10):
        p.apply_async(fun, args= (i, ))
    p.close()
    p.join()      
```

### threading.local 的作用？
```
实现线程局部变量的传递。

ThreadLocal 最常用的地方：
为每个线程绑定一个资源（数据库连接，HTTP请求，用户身份信息等），这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资源。

为每个线程创建一个独立的空间，使得线程对自己的空间中的数据进行操作（数据隔离）。
import threading
from threading import local
import time
 
obj = local()
 
 
def task(i):
    obj.xxxxx = i
    time.sleep(2)
    print(obj.xxxxx,i)
 
for i in range(10):  #开启了10个线程
    t = threading.Thread(target=task,args=(i,))
    t.start()

flask g
```

### 进程之间如何进行通信？
```
python提供了多种进程通信的方式，主要Queue和Pipe这两种方式，Queue用于多个进程间实现通信，Pipe是两个进程的通信。

from multiprocessing import Process,Queue

"""
创建两个子进程，让一个子进程放数据，另一个子进程拿数据
"""
def producer(q):
    q.put('hello jeff')


def consumer(q):
    print(q.get())


if __name__ == '__main__':
    q = Queue()  # 生成一个队列
    p = Process(target=producer, args=(q,))  # 创建一个生产进程对象
    c = Process(target=consumer, args=(q,))  # 创建一个消费进程对象
    p.start()  # 创建进程，启动
    c.start()  # 创建进程，启动
    
# 结果：
hello jeff
```
### 什么是并发和并行？
```
并发：看起来像同时运行，内部：服务器来回切换者服务，速度很快，用户感觉不到

并行：真正意义上的同时运行
```
### 解释什么是异步非阻塞？
```
非阻塞：不等待
即：遇到IO阻塞不等待(setblooking=False),（可能会报错->捕捉异常）
        - sk=socket.socket()
        - sk.setblooking(False)
异步：回调，当达到某个指定的状态之后，自动调用特定函数

实例
nb_async.py   实现异步非阻塞的模块
```

### 路由器和交换机的区别？
```
1：交换机：是负责内网里面的数据传递（arp协议）根据MAC地址寻址
   路由器：在网络层，路由器根据路由表，寻找该ip的网段
2：路由器可以处理TCP/IP协议
3：路由器可以把一个IP分配给很多个主机使用，这些主机对外只表现出一个IP。
   交换机可以把很多主机连起来，这些主机对外各有各的IP。
4：交换机是做端口扩展的，也就是让局域网可以连进来更多的电脑。
  路由器是用来做网络连接，也就是；连接不同的网络
```

### 什么是域名解析？
```
在互联网上，所有的地址都是ip地址，现阶段主要是IPv4（比如：110.110.110.110）。
但是这些ip地址太难记了，所以就出现了域名（比如http://baidu.com）。
域名解析就是将域名，转换为ip地址的这样一种行为。
```

### 如何修改本地hosts 文件？
```
Hosts是一个没有扩展名的系统文件，可以用记事本等工具打开，其作用就是将一些常用的网址域名与其对应的IP地址建立一个关联“数据库”，
当用户在浏览器中输入一个需要登录的网址时，系统会首先自动从Hosts文件中寻找对应的IP地址，
一旦找到，系统会立即打开对应网页，如果没有找到，则系统会再将网址提交给DNS域名解析服务器进行IP地址的解析。

文件路径：C:\WINDOWS\system32\drivers\etc。
将127.0.0.1   www.163.com  添加在最下面
修改后用浏览器访问“www.163.com”会被解析到127.0.0.1，导致无法显示该网页
```

### 生产者消费者模型应用场景？
```
生产者与消费者模式是通过一个容器来解决生产者与消费者的强耦合关系，生产者与消费者之间不直接进行通讯，
而是利用阻塞队列来进行通讯，生产者生成数据后直接丢给阻塞队列，消费者需要数据则从阻塞队列获取，
实际应用中，生产者与消费者模式则主要解决生产者与消费者生产与消费的速率不一致的问题，达到平衡生产者与消费者的处理能力，而阻塞队列则相当于缓冲区。

应用场景：用户提交订单，订单进入引擎的阻塞队列中，由专门的线程从阻塞队列中获取数据并处理

优势：
1；解耦
假设生产者和消费者分别是两个类。如果让生产者直接调用消费者的某个方法，那么生产者对于消费者就会产生依赖（也就是耦合）。
将来如果消费者的代码发生变化，可能会影响到生产者。而如果两者都依赖于某个缓冲区，两者之间不直接依赖，耦合也就相应降低了。
2：支持并发
生产者直接调用消费者的某个方法，还有另一个弊端。由于函数调用是同步的（或者叫阻塞的），在消费者的方法没有返回之前，生产者只能一直等着
而使用这个模型，生产者把制造出来的数据只需要放在缓冲区即可，不需要等待消费者来取

3：支持忙闲不均
缓冲区还有另一个好处。如果制造数据的速度时快时慢，缓冲区的好处就体现出来了。
当数据制造快的时候，消费者来不及处理，未处理的数据可以暂时存在缓冲区中。等生产者的制造速度慢下来，消费者再慢慢处理掉。
```

### 什么是cdn？
```
目的是使用户可以就近到服务器取得所需内容，解决 Internet网络拥挤的状况，提高用户访问网站的响应速度。
cdn 即内容分发网络
```

### 程序从Flag A 执行到Flag B 的时间大致为多少秒
```
import threading
import time
def _wait():
    time.sleep(60)
    print('a')
#FlagA
t = threading.Thread(target=_wait, daemon=False)
t.start()
#FlagB
```

### 有A.txt 和B.txt 两个文件, 使用多进程和进程池的方式分别读取这两个文件
```
# 多进程
"""通过多进程加速读取excel的测试"""
__author__ = "hanyaning@deri.energy"
import os.path
import time
from service import logger
import pandas as pd
from multiprocessing import Process, Manager
startTime = time.time()

logger = logger.MyLogger("multi_process").getLogger()


def getExcelData(path, return_data=None, file_name=""):
    global startTime
    logger.info("开始读取Excel文件，当前进程pid：" + str(os.getpid()))
    if not os.path.exists(path):
        raise FileNotFoundError()
    if os.path.isfile(path):
        return_data[file_name] = pd.read_excel(path, skiprows=1, skipfooter=1)
        logger.info("读取Excel文件完毕，当前进程pid：" + str(os.getpid()))

if __name__ == "__main__":
    excel_path = os.path.join(os.getcwd(), "../excels")
    xls_names = [x for x in os.listdir(excel_path) if x.endswith(".xls")]
    first = str(time.time() - startTime)
    logger.info("进入程序用时：" + first)
    p_list = []
    # Manager类似于同步数据管理工具，可在多进程时实现各进程操作同一个数据，比如这里通过它组织返回值
    manager = Manager()
    # Manager.dict()类似于共享变量，各个进程可以修改它，通过每次添加不同的key值，可以实现方法返回值的获取
    return_data = manager.dict()
    first = time.time() - startTime
    # 手动创建多个进程读取，可能存在创建进程过多导致系统崩溃的情况
    for file_name in xls_names:
        p = Process(target=getExcelData, args=(os.path.join(excel_path, file_name), return_data, file_name))
        p.start()
        p_list.append(p)
    print(p_list)

    """
    经测试，直到这里都还会延迟数秒才执行进程的target方法，尽管前面已经调用了start(),但进程并没有立即执行
    寡人认为是系统创建进程需要时间，并且是创建好所有进程后才各进程才开始工作，这里要创建120个进程花费了大多数的时间
    后面在采用进程池时，当设置最大进程数为120时，依然花费了大把的时间，而设置为10时，大大缩小了创建进程到执行target方法所要等待的时间
    这也证明了寡人的观点，至于正确与否，寡人先跟代码去了，且等下回分解
    """
    for p in p_list:
        # 如果有子进程没有执行完，需要先阻塞主进程
        p.join()
    logger.info("各进程执行完毕")
    # 获取返回值字典为列表
    data_frames = return_data.values()
    # 合并列表为一个dataFrame
    data = pd.DataFrame()

    for da in data_frames:
        data = data.append(da)

    endTime = time.time()
    print(endTime - startTime)
    print(len(data))


# 进程池
"""通过多进程加速读取excel的测试"""
__author__ = "hanyaning@deri.energy"
import os.path
import time
from service import logger
import pandas as pd
from multiprocessing import Pool

logger = logger.MyLogger("multi_process").getLogger()


def getExcelData(path):
    logger.info("开始读取excel，当前进程pid：" + str(os.getpid()))
    data = pd.DataFrame()
    if not os.path.exists(path):
        raise FileNotFoundError()
    if os.path.isfile(path):
        logger.info("读取Excel文件完毕，当前进程pid：" + str(os.getpid()))
    return data.append(pd.read_excel(path, skiprows=1, skipfooter=1), sort=False)


if __name__ == "__main__":
    excel_path = os.path.join(os.getcwd(), "../excels")
    xls_names = [x for x in os.listdir(excel_path) if x.endswith(".xls")]
    startTime = time.time()

    p_list = []
    # 使用进程池Pool
    pool = Pool(processes=10)
    pool_data_list = []
    data = pd.DataFrame()
    for file_name in xls_names:
        # 需要注意不能直接在这里调用get方法获取数据,原因是apply_async后面 get()等待线程运行结束才会下一个,这里多进程会变成阻塞执行
        pool_data_list.append(pool.apply_async(getExcelData, (os.path.join(excel_path, file_name),)))
    pool.close()
    # 需要阻塞以下，等所有子进程执行完毕后主线程才继续执行
    pool.join()
    for pool_data in pool_data_list:
        # 这里再使用get()方法可以获取返回值
        data = data.append(pool_data.get())
    endTime = time.time()
    print(endTime - startTime)
    print(len(data))
```

### 那些是常见的TCPFlags?
```
SYN：表示建立连接
FIN:表示关闭连接
RST：表示连接重置
ACK：表示响应，三次握手，四次挥手
URG：
PSH：表示有DATA数据传输
```
### 下面关于网络七层和四层的􁧿述, 那条是错误的?
A. ~~SNMP 工作在四层~~  2层
B. 四层是指网络的传输层, 主要包括IP 和端口信息
C. 七层是指网络的应用层(协议层), 比如http 协议就工作在七层
D. 四层主要应用于TCP 和UDP 的代理, 七层主要应用于HTTP 等协议的代理

### tracerroute 一般使用的是那种网络层协议
ICMP

### iptables 知识考察, 根据要求写出防火墙规则?
```

A. 屏蔽192.168.1.5 访问本机dns 服务端口
B. 允许10.1.1.0/24 访问本机的udp 8888 9999 端口
iptables -A INPUT -p tcp --dport 53 -s 192.168.1.5 -j DROP
iptables -A INPUT -p udp --dport 8888 9999 -s 10.1.1.0/24 -j ACCEPT

iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT

针对这2条命令进行一些讲解吧
-A 参数就看成是添加一条 INPUT 的规则
-p 指定是什么协议 我们常用的tcp 协议，当然也有udp 例如53端口的DNS
到时我们要配置DNS用到53端口 大家就会发现使用udp协议的
而 --dport 就是目标端口 当数据从外部进入服务器为目标端口
反之 数据从服务器出去 则为数据源端口 使用 --sport
-j 就是指定是 ACCEPT 接收 或者 DROP 不接收
```

### 业务服务器192.168.1.2 访问192.168.1.3 数据接口, 无法正常返回数据, 请根据以上信息写出排查思路
```

```
### 请实现一个简单的socket 编程, 要求
```
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('', 8888))
server.listen(5)

#等待客户端连接
while True:
    (client, address) = server.accept()
    data = client.recv(4096)
    print data
    client.send("hello")                                                    
    client.close()


# 客户端
import socket                
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8888))
client.send("My name is client")
message = client.recv(4096)                                                      
print message                
client.close()
```

### 谈一下对于多线程编程的理解, 对于CPU 密集型怎样使用多线程, 说说线程池, 线程锁的用法, 有没有用过multiprocessing 或concurrent.future？
```
CPU密集型使用多进程
IO密集型使用多线程
加锁
锁定
释放
```

### 关于守护线程的说法, 正确的是 c
A. 所有非守护线程终止, 即使存在守护线程, 进程运行终止
B. 所有守护线程终止, 即使存在非守护线程, 进程运行终止
C. 只要有守护线程或者非守护线程其中之一存在, 进程就不会终止
D. 只要所有的守护线程和非守护线程中终止运行之后, 进程才会终止

### 描述多进程开发中join 与deamon 的区别
```
p.join([timeout]):主线程等待p终止（强调：是主线程处于等的状态，而p是处于运行的状态）
p.daemon：默认值为False，如果设为True，代表p为后台运行的守护进程，当p的父进程终止时，p也随之终止，并且设定为True后，p不能创建自己的新进程，必须在p.start之前设置
```

### 请简述GIL 对Python 性能的影响
```
GIL：全局解释器锁。每个线程在执行的过程都需要先获取GIL，保证同一时刻只有一个线程可以执行字节码。
线程释放GIL锁的情况：
在IO操作等可能会引起阻塞的system call之前,可以暂时释放GIL,但在执行完毕后,必须重新获取GIL
Python 3.x使用计时器（执行时间达到阈值后，当前线程释放GIL）或Python 2.x，tickets计数达到100
Python使用多进程是可以利用多核的CPU资源的。
多线程爬取比单线程性能有提升，因为遇到IO阻塞会自动释放GIL锁
```

### 曾经在哪里使用过：线程、进程、协程？
```
在写高并发的服务端代码时
在写高性能爬虫的时候。
```

### 请使用yield 实现一个协程？
```
import time

import queue
def consumer(name):
    print("--->starting eating baozi...")
    while True:
        new_baozi = yield
        print("[%s] is eating baozi %s" % (name,new_baozi))
        #time.sleep(1)
 
def producer():
 
    r = con.__next__()
    r = con2.__next__()
    n = 0
    while n < 5:
        n +=1
        con.send(n)
        con2.send(n)
        print("\033[32;1m[producer]\033[0m is making baozi %s" %n )

if __name__ == '__main__':
    con = consumer("c1")
    con2 = consumer("c2")
    p = producer()
```

### 请使用python 内置async 语法实现一个协程？
```
from datetime import datetime
import asyncio

async def add(n):
    print(datetime.now().strftime('%H:%M:%S.%f'))
    count = 0
    for i in range(n):
        count += i
    print(datetime.now().strftime('%H:%M:%S.%f'))
    return count

async def fun(n):
    res = await add(n)
    print(f'res = {res}')

loop = asyncio.get_event_loop()
tasks = [fun(20000000), fun(30000000)]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
```

### 简述线程死锁是如何造成的？如何避免？
```
若干子线程在系统资源竞争时，都在等待对方对某部分资源解除占用状态，结果是谁也不愿先解锁，互相干等着，程序无法执行下去，这就是死锁。
GIL锁（有时候，面试官不问，你自己要主动说，增加b格，尽量别一问一答的尬聊，不然最后等到的一句话就是：你还有什么想问的么？）
GIL锁 全局解释器锁（只在cpython里才有）
作用：限制多线程同时执行，保证同一时间只有一个线程执行，所以cpython里的多线程其实是伪多线程!
所以Python里常常使用协程技术来代替多线程，协程是一种更轻量级的线程，
进程和线程的切换时由系统决定，而协程由我们程序员自己决定，而模块gevent下切换是遇到了耗时操作才会切换。
三者的关系：进程里有线程，线程里有协程。
```

### asynio 是什么？
```
python高并发模块
```

### gevent 模块是什么？
```
from gevent import monkey;monkey.patch_all()  # 由于该模块经常被使用 所以建议写成一行
from gevent import spawn
实现协程
gevent是第三方库，通过greenlet实现协程，其基本思想是：

当一个greenlet遇到IO操作时，比如访问网络，就自动切换到其他的greenlet，等到IO操作完成，再在适当的时候切换回来继续执行。由于IO操作非常耗时，经常使程序处于等待状态，有了gevent为我们自动切换协程，就保证总有greenlet在运行，而不是等待IO。
```

### 什么是twisted 框架？
```
twisted是异步非阻塞框架。爬虫框架Scrapy依赖twisted。
```

### 什么是LVS
```
LVS ：Linux虚拟服务器
作用：LVS主要用于多服务器的负载均衡。
它工作在网络层，可以实现高性能，高可用的服务器集群技术。
它廉价，可把许多低性能的服务器组合在一起形成一个超级服务器。
它易用，配置非常简单，且有多种负载均衡的方法。
它稳定可靠，即使在集群的服务器中某台服务器无法正常工作，也不影响整体效果。另外可扩展性也非常好。
```

### 什么是Nginx？
```
Nginx是一款自由的、开源的、高性能的HTTP服务器和反向代理服务器，同时也是一个IMAP、POP3、SMTP代理服务器。可以用作HTTP服务器、方向代理服务器、负载均衡。
```

### 什么是keepalived?
```
Keepalived起初是为LVS设计的，专门用来监控集群系统中各个服务节点的状态，它根据TCP/IP参考模型的第三、第四层、第五层交换机制检测每个服务节点的状态，如果某个服务器节点出现异常，或者工作出现故障，Keepalived将检测到，并将出现的故障的服务器节点从集群系统中剔除，这些工作全部是自动完成的，不需要人工干涉，需要人工完成的只是修复出现故障的服务节点。

后来Keepalived又加入了VRRP的功能，VRRP（Vritrual Router Redundancy Protocol,虚拟路由冗余协议)出现的目的是解决静态路由出现的单点故障问题，通过VRRP可以实现网络不间断稳定运行，因此Keepalvied 一方面具有服务器状态检测和故障隔离功能，另外一方面也有HA cluster功能，下面介绍一下VRRP协议实现的过程。
```

### 什么是haproxy
```
- TCP 代理：可从监听 socket 接受 TCP 连接，然后自己连接到 server，HAProxy 将这些 sockets attach 到一起，使通信流量可双向流动。

- HTTP 反向代理（在 HTTP 专用术语中，称为 gateway）：HAProxy 自身表现得就像一个 server，通过监听 socket 接受 HTTP 请求，然后与后端服务器建立连接，通过连接将请求转发给后端服务器。

- SSL terminator / initiator / offloader: 客户端 -> HAProxy 的连接，以及 HAProxy -> server 端的连接都可以使用 SSL/TLS

- TCP normalizer: 因为连接在本地操作系统处终结，client 和 server 端没有关联，所以不正常的 traffic 如 invalid packets, flag combinations, window advertisements, sequence numbers, incomplete connections(SYN floods) 不会传递给 server 端。这种机制可以保护脆弱的 TCP stacks 免遭协议上的攻击，也使得我们不必修改 server 端的 TCP 协议栈设置就可以优化与 client 的连接参数。


- HTTP normalizer: HAProxy 配置为 HTTP 模式时，只允许有效的完整的请求转发给后端。这样可以使得后端免遭 protocol-based 攻击。一些不规范的定义也被修改，以免在 server 端造成问题（eg: multiple-line headers，会被合并为一行）

- HTTP 修正工具：HAProxy 可以 modify / fix / add / remove / rewrite URL 及任何 request or response header。

- a content-based switch: 可基于内容进行转发。可基于请求中的任何元素转发请求或连接。因此可基于一个端口处理多种协议（http,https, ssh）

- a server load balancer: 可对 TCP 连接 和 HTTP 请求进行负载均衡调度。工作于 TCP 模式时，可对整个连接进行负载均衡调度；工作于 HTTP 模式时，可对 HTTP 请求进行调度。

- a traffic regulator: 可在不同的方面对流量进行限制，保护 server ，使其不超负荷，基于内容调整 traffic 优先级，甚至可以通过 marking packets 将这些信息传递给下层以及网络组件。

- 防御 DDos 攻击及 service abuse: HAProxy 可为每个 IP地址，URL，cookie 等维护大量的统计信息，并对其进行检测，当发生服务滥用的情况，采取一定的措施如：slow down the offenders, block them, send them to outdated contents, etc

- 是 network 的诊断的一个观察节点：根据精确记录细节丰富的日志，对网络诊断很有帮助

- an HTTP compression offloader：可自行对响应进行压缩，而不是让 server 进行压缩，因此对于连接性能较差的 client，或使用高延迟移动网络的 client，可减少页面加载时间
```

### 什么是负载均衡？
```
系统的扩展可分为纵向（垂直）扩展和横向（水平）扩展。纵向扩展，是从单机的角度通过增加硬件处理能力，比如CPU处理能力，内存容量，磁盘等方面，实现服务器处理能力的提升，不能满足大型分布式系统（网站），大流量，高并发，海量数据的问题。因此需要采用横向扩展的方式，通过添加机器来满足大型网站服务的处理能力。比如：一台机器不能满足，则增加两台或者多台机器，共同承担访问压力。这就是典型的集群和负载均衡架构
```

### 什么是rpc 及应用场景？
```
RPC主要用于公司内部的服务调用，性能消耗低，传输效率高，服务治理方便。HTTP主要用于对外的异构环境，浏览器接口调用，APP接口调用，第三方接口调用等...
```

### 什么是反向代理？
```
反向代理：加速网络，保护真实服务器
这个词相信搞网络的朋友都很熟悉的，但是具体是什么意思呢？说实话，复杂的我也不懂，就我个人理解而言，反向代理有很多用途，比如说保护真实服务器不被外界攻击，加速网络等等。今天我们要介绍的就是加速网络的一种。
```

