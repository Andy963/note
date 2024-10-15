MQ全称为Message Queue 消息队列（MQ）是一种应用程序对应用程序的通信方法。MQ是消费-生产者模型的一个典型的代表，一端往消息队列中不断写入消息，而另一端则可以读取队列中的消息。这样发布者和使用者都不用知道对方的存在

消息队列可以简单理解为：把要传输的数据放在队列中

应用赏景：生产者，消费者模型

![订单系统](https://raw.githubusercontent.com/Andy963/notePic/main/vnote/python/01_rabbitmq/01_mq.md/574915013615188.png =692x)

ref: [引用博客](https://www.cnblogs.com/pyedu/p/11866829.html)

安装：
```sh
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```
pika模块安装：
```py
python -m pip install pika --upgrade
```
### 简单模式
1.连接rabbitmq
2.创建队列
3.向队列插入消息

 producer
```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2


import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建队列
channel.queue_declare(queue='hello')

# 添加数据
channel.basic_publish(exchange='',  # 简单模式，非交换机，所以置空
                      routing_key='hello',  # 队列名
                      body='Hello World!')  # 插入的数据
print(" [x] Sent 'Hello World!'")

connection.close()
```

consumer
```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2

import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建队列
# 为什么创建？ 如果消费者先启动，则消费者创建，那么生产者就不会创建
channel.queue_declare(queue='hello')


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


# 确定监听队列参数
channel.basic_consume(queue='hello', on_message_callback=callback,
                      auto_ack=True  # 默认应答
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始消费，此时才真正去队列拿数据
channel.start_consuming()
```

#### 应答参数
当自动应答时，只要队列里面有数据就会被消费者拿走，此时如果消费者在处理过程中出错，而数据又已经被拿走，当我们处理完消费者的bug后重启消费者，此时队列中已经没有数据了，要怎么防止这种情况发生呢？
> 将自动应答模式改为False,即手动应答

```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2

import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建队列
# 为什么创建？ 如果消费者先启动，则消费者创建，那么生产者就不会创建
channel.queue_declare(queue='hello')


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    # 给队列信号，我已经处理完了，你可以删除信息了 
    ch.basic_ack(delivery_tag=method.delivery_tag)


# 确定监听队列参数
channel.basic_consume(queue='hello', on_message_callback=callback,
                      auto_ack=False  # 非自动应答，即只有给队列发送一个信号后，才会将消息从队列删除
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始消费，此时才真正去队列拿数据
channel.start_consuming()
```

#### 持久化
如果rabbitMQ服务器在运行过程中崩溃了，当我们再次启动服务器时，所有的message都没有了，那要怎么办呢？
> 持久化数据

1.声明队列为持久化队列（持久化是在创建时决定的，无法更改）

```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2


import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建队列，hello1已经声明过了，无法修改其属性，所以这里换了名字
# durable=True,此时队列具有可持久化的能力，但并没有对消息持久化处理，需要显式处理
channel.queue_declare(queue='hello2'，durable=True)

# 添加数据
channel.basic_publish(exchange='',  # 简单模式，非交换机，所以置空
                      routing_key='hello2',  # 队列名
                      body='Hello World!'，
                       properties=pika.BasicProperties(
                          delivery_mode=2,  # make message persistent
                          )
                      )  # 插入的数据
print(" [x] Sent 'Hello World!'")

connection.close()
```

注意，当消费者连接时，也应指定队列是可持久化的`durable=True`


### 交换机模式

交换机模式：
    发布订阅
    关键字模式
    模糊匹配模式
    

生产者：
    连接rabbitMQ
    创建交换机
    插入数据
    
```py
import pika

# 连接rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

# 声明一个名为Logs 发布订阅模式的交换机,
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout' # 发布订阅模式
                         )

# 向交换机中插入数据
message = "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='', # 交换机模式，没有队列，routing_key置空
                      body=message)
print(" [x] Sent %r" % message)
connection.close()
```

消费者：

```py
import pika

# 连接rabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

#声明交换机，与简单模式一样，如果消费者先启动，则交换机由消费者创建，如果交换机已经由生产者创建，则什么也不做
channel.exchange_declare(exchange='logs',
                         exchange_type='fanout')

# 创建队列
result = channel.queue_declare("",exclusive=True) # 随机名字，避免自己取名重复情况的发生
queue_name = result.method.queue # 获取队列名字

# 绑定到交换机
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)


channel.basic_consume(queue=queue_name,
                      auto_ack=True,
                      on_message_callback=callback)

channel.start_consuming()
```

#### 分发参数

默认为轮询分发： 一人一个，即使有空闲的消费者，也不会分发给他，而是等到当前这个消费完，然后交给他。
producer
```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2


import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建队列
channel.queue_declare(queue='hello4')

# 添加数据
channel.basic_publish(exchange='',  # 简单模式，非交换机，所以置空
                      routing_key='hello4',  # 队列名
                      body='Hello World!')  # 插入的数据
print(" [x] Sent 'Hello World!'")

connection.close()
```

consumer
```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2

import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建队列
# 为什么创建？ 如果消费者先启动，则消费者创建，那么生产者就不会创建
channel.queue_declare(queue='hello4')


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 确定监听队列参数
channel.basic_consume(queue='hello4', on_message_callback=callback,
                      auto_ack=False  # 默认应答
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始消费，此时才真正去队列拿数据
channel.start_consuming()

```

公平分发，谁有空，就给谁

在*消费者*中进行设定：`channel.basic_qos(prefetch_count=1)` 限制每次只发送不超过1条消息到同一个消费者，消费者必须手动反馈告知队列，才会发送下一个


#### 关键字模式

consumer
```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2

import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明交换机
channel.exchange_declare(exchange='log', exchange_type='direct')
# 创建队列
channel.queue_declare("", exclusive =True)


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_bind(
    exchange='log',
    queue=queue_name,
    routing_key='error' # 关键字，一次只能绑定一个，如果有多个需要声明多次，或者用循环
)

# 确定监听队列参数
channel.basic_consume(queue='hello4', on_message_callback=callback,
                      auto_ack=False  # 默认应答
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始消费，此时才真正去队列拿数据
channel.start_consuming()

```

producer
```py
import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 创建队列
channel.exchange_declare(exchange='log', exchange_type='direct')

# 添加数据
channel.basic_publish(exchange='log',  # 简单模式，非交换机，所以置空
                      routing_key='error',  # 队列名
                      body='Hello World!,error')  # 插入的数据
print(" [x] Sent 'Hello World!'")

connection.close()
```

#### 通配符模式
“通配符交换机”（Topic Exchange）将路由键和某模式进行匹配。此时队列需要绑定在一个模式上。符号“#”匹配一个或多个词，符号“*”仅匹配一个词。因此“audit.#”能够匹配到“audit.irs.corporate”，但是“audit.*”只会匹配到“audit.irs”。（这里与我们一般的正则表达式的“*”和“#”刚好相反，这里我们需要注意一下。）

![Topic Exchange](https://raw.githubusercontent.com/Andy963/notePic/main/vnote/python/01_rabbitmq/01_mq.md/284442222268574.png)

consumer
```py
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2022/3/2

import pika

# 连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 声明交换机
channel.exchange_declare(exchange='log3', exchange_type='topic') # 指定类型为topic
# 创建队列
result = channel.queue_declare("", exclusive =True)
queue_name = result.method.queue


# 确定回调函数
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.queue_bind(
    exchange='log3',
    queue=queue_name,
    routing_key='error.#' # #匹配多个字符，
)

# 确定监听队列参数
channel.basic_consume(queue=queue_name, on_message_callback=callback,
                      auto_ack=False  # 自动应答
                      )

print(' [*] Waiting for messages. To exit press CTRL+C')
# 开始消费，此时才真正去队列拿数据
channel.start_consuming()
```