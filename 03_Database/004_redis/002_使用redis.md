## redis

redis使用场景

* 登陆会话存储，存储在redis中与memcached相比，数据不会丢失
* 排行榜/计数器：比如一些秀场项目，经常会有一引起前多少名主播排名，一些文章阅读量的，微博点赞数
* 作为消息队列，celery使用redis作为中间人
* 当前在线人数，经常在变
* 一些常用数据缓存：比如论坛bbs，板块不会经常变化，但每次都要从mysql获取，可以在redis中缓存起来，不用每次请求数据库
* 把前200篇文章缓存或者评论缓存，一般用户浏览网站，只会浏览前面一部分文章或者评论，那么可以把前面200篇文章对应评论缓存起来，用户访问超时时就访问数据库，并且以后文章超过200篇，就把之前的文章删除掉
* 好友关系，微博
* 发布和订阅功能，用心用来做聊天软件

### redis 编译安装
连接redis
```shell
redis-cli -h -p
```
设置日志级别
```redis
127.0.0.1:6379> config set loglevel warning
OK
127.0.0.1:6379> config get loglevel
1) "loglevel"
2) "warning"
```
选择数据库
redis默认有16个数据库从0开始，默认连接后自动选择0号数据库，用select命令更换数据库.事实上这个序号只相当于命名空间的作用，无法自定义名字，无法做到真正隔离，也无法为不同库设置不同密码，flush_all会清空所有库的内容。
```redis
127.0.0.1:6379> select 0
OK
127.0.0.1:6379> select 1
OK
127.0.0.1:6379[1]>
```

#### 一些通用命令
```redis
#当前redis中所有的key:
keys *
#删除
del key
#incr 增加 无法指定增加多少，当键不存在时默认0，第一次incr返回1
127.0.0.1:6379> set age 18
OK
# incrby命令指定增加多少
127.0.0.1:6379> incr andy
(integer) 1
127.0.0.1:6379> incrby andy 10
(integer) 11
#incrbyfloat增加浮点数
127.0.0.1:6379> incrbyfloat andy 1.12
"12.12"

127.0.0.1:6379> incr age
(integer) 19
127.0.0.1:6379> decr age
(integer) 18
#判断是否存在
127.0.0.1:6379> exists person
(integer) 1
#不存在的返回值
127.0.0.1:6379> get noexists
(nil)
#查看数据类型
127.0.0.1:6379> type school
list
```
SORT #命令可以对列表类型、集合类型和有序集合类型键进行排序

#### 过期
expire key timeout # 单位为秒， 为已经添加到redis中的数据设置超时时间.也可以在添加数据时设置超时时间
```redis
EXPIRE key seconds # 设置多少秒后过期
TTL # 查看还有多少秒
PERSIST key #设置为不过期
EXPIREAT # 使用Unix时间作为过期时间
PEXPIREAT # 与Expireat的区别是单位是毫秒

```


### 字符串

#### set
```redis
#set key value EX timeout
127.0.0.1:6379> set name andy ex 10
OK
127.0.0.1:6379> ttl name

#setex key time value
127.0.0.1:6379> setex name 10 andy
OK
127.0.0.1:6379> ttl name
(integer) 7
127.0.0.1:6379> ttl name  # ttl查看过期时间还剩下多少
(integer) 6
```

#### append 
append向尾部追加值 
```redis
127.0.0.1:6379> set welcome hello
OK
127.0.0.1:6379> append welcome ' world'
(integer) 11
127.0.0.1:6379> get welcome
"hello world"
```
#### strlen
strlen获取字符串长度
```redis
127.0.0.1:6379> strlen welcome
(integer) 10
```
#### mget/mset
mget,mset 获取 设置多个值
```redis
127.0.0.1:6379> mset name andy age 20
OK
127.0.0.1:6379> mget name age
1) "andy"
2) "20"
```
#### setbit/getbit
setbit getbi位操作
```redis
127.0.0.1:6379> set foo bar
OK
127.0.0.1:6379> getbit foo 0
(integer) 0
127.0.0.1:6379> setbit foo 7 1
(integer) 0
127.0.0.1:6379> get foo
"car"
```
#### bitop
bitop 位运算
```redis
127.0.0.1:6379> set foo1 bar
OK
127.0.0.1:6379> set foo2 aar
OK
127.0.0.1:6379> bitop or res foo1 foo2
(integer) 3
127.0.0.1:6379> get res
"car"
```
#### bitpos
bitpos 获取 某个位的位置
```redis
127.0.0.1:6379> bitpos foo 1
(integer) 1
```

### 列表

#### lpush
在列表左边添加元素
lpush key value 将值插入到key的表头，如果key不存在，一个空列表会被创建，并执行lpush,如果key存在但不是列表类型时会报错. 同理有rpush key value
```redis
127.0.0.1:6379> lpush search google
(integer) 1
```
#### lrange
查看列表中的元素.lrange key start stop  返回指定区间内的元素
```redis
127.0.0.1:6379> lrange search 0 -1
1) "google"
127.0.0.1:6379> lpush search baidu
(integer) 2
127.0.0.1:6379> lrange search 0 -1
1) "baidu"
2) "google"
```
#### lpop
移除并返回列表中元素
```redis
127.0.0.1:6379> lpop search
"baidu"
```
#### lindex
通过索引获取 值
```redis
127.0.0.1:6379> lindex search 0
"baidu"
127.0.0.1:6379> lindex search 1
"google"
```
#### llen
获取 列表中元素个数
```redis
127.0.0.1:6379> llen search
(integer) 2
```
#### lrem
删除指定元素,lrem key count value. 根据参数count的值 移除列表中与参数value相等的元素，count有三种情况
count > 0: 从表头开始向表尾搜索，移除value相等的元素，个数为count
count < 0: 从表尾开始向表头
count = 0: 移除所有value
```redis
127.0.0.1:6379> lrange search 0 -1
1) "baidu"
2) "google"
3) "baidu"
127.0.0.1:6379> lrem search 2 baidu
(integer) 2
127.0.0.1:6379> lrange search 0 -1
1) "google"
```
#### linsert
向指定位置插入元素, before,after指定某个元素的前后
```redis
127.0.0.1:6379> lrange school 0 -1
1) "peking"
2) "yangtze"
3) "yangtze"
127.0.0.1:6379> linsert school before yangtze wuhan
(integer) 4
127.0.0.1:6379> lrange school 0 -1
1) "peking"
2) "wuhan"
3) "yangtze"
4) "yangtze"
127.0.0.1:6379> lrange search 0 -1
1) "baidu"
2) "google"
127.0.0.1:6379> linsert search after baidu sogou
(integer) 3
127.0.0.1:6379> lrange search 0 -1
1) "baidu"
2) "sogou"
3) "google"
```
#### rpoplpush
从一个列表转到另一个列表 rpoplpush = rpop lpush source destination
```redis
127.0.0.1:6379> lpush name1 jack
(integer) 1
127.0.0.1:6379> lpush name1 amy
(integer) 2
127.0.0.1:6379> lpush name2 lili
(integer) 1
127.0.0.1:6379> rpoplpush name1 name2
"jack"
127.0.0.1:6379> lrange name1 0 -1
1) "amy"
127.0.0.1:6379> lrange name2 0 -1
1) "jack"
2) "lili"
```

### 集合
#### sadd
添加元素 `sadd set value1 value2`
```redis
localhost:6379> sadd school1 peking tsing
(integer) 2
```
#### smembers
查看元素 `smembers set`
```redis
localhost:6379> smembers school1
1) "tsing"
2) "peking"
```
#### srem
移除元素 `srem set memeber`
```redis
localhost:6379> srem school1 tsing
(integer) 1
localhost:6379> smembers school1
1) "peking"
```
#### scard
查看集合中元素个数 scard
```redis
localhost:6379> scard school1
(integer) 1
```
#### sinter/sdiff/sunion
```redis
localhost:6379> smembers school1
1) "yangtze"
2) "tsing"
3) "peking"
localhost:6379> smembers school2
1) "yangtze"
2) "wuhan"
3) "huake"
```

获取交集`sinter set1 set2`
```redis
localhost:6379> sinter school1 school2
1) "yangtze"
```
获取并集 `sunion set1 set2`
```redis
localhost:6379> sunion school1 school2
1) "yangtze"
2) "wuhan"
3) "tsing"
4) "peking"
5) "huake"
```
获取差集`sdiff set1 set2`
注意前后顺序不同，结果可能不同

```redis
localhost:6379> sdiff school1 school2
1) "tsing"
2) "peking"

localhost:6379> sdiff school2 school1
1) "wuhan"
2) "huake"
```

#### sdiffstore/ sunionstore/ sinterstore
获取交并存储运算结果
```redis
127.0.0.1:6379> sadd s1 a b c
(integer) 3
127.0.0.1:6379> sadd s2 b c d
(integer) 3
127.0.0.1:6379> sdiffstore s_diff s1 s2
(integer) 1
127.0.0.1:6379> smembers s_diff
1) "a"
```
#### srandmember key
随机获取一个值 
```redis
127.0.0.1:6379> smembers s_diff
1) "a"
127.0.0.1:6379> srandmember s1
"a"
127.0.0.1:6379> srandmember s1
"b"
#指定获取个数
127.0.0.1:6379> srandmember s1 2
1) "a"
2) "c"
127.0.0.1:6379> srandmember s1 2
1) "b"
2) "c"
```

### 有序集合

#### zadd
添加元素 注意值在键的前面
```redis
127.0.0.1:6379> zadd score 89 tom 67 peter
(integer) 2
```
#### zscore
获取元素的传下
```redis
127.0.0.1:6379> zscore score tom
"89"
```
#### zrange
获取排名范围内的元素 ,注意是排名
```redis
127.0.0.1:6379> zrange score 1 3
1) "jack"
2) "tom"
#倒序
127.0.0.1:6379> zrevrange score 1 3
1) "jack"
2) "peter"
#同时返回分数
127.0.0.1:6379> zrange score 1 3 withscores
1) "jack"
2) "76"
3) "tom"
4) "89"
```

#### zcard
获取元素个数
```redis
127.0.0.1:6379> zcard score
(integer) 3

#### zcount
#指定范围 ZCOUNT key min max
127.0.0.1:6379> zcount score 60 80
(integer) 2
```

#### ZRANGEBYSCORE
分数的范围 #ZRANGEBYSCORE key min max [WITHSCORES] [LIMIT offset count]
```redis
127.0.0.1:6379> zrangebyscore score 70 90 withscores
1) "jack"
2) "76"
3) "tom"
4) "89"
```
#### zrem
删除元素
```redis
127.0.0.1:6379> zrem score jack
(integer) 1
#ZREMRANGEBYRANK key start stop 按排名删除
#ZREMRANGEBYSCORE key min max 按分数范围删除
```

#### zrank
获取元素排名
```redis
#ZRANK key member 从0开始
127.0.0.1:6379> zrank score tom
(integer) 1
#ZREVRANK key member
127.0.0.1:6379> zrevrank score tom
(integer) 0
```

#### ZINTERSTORE
计算有序集合的交集,#ZINTERSTORE destination numkeys key SUM|MIN|MAX] 默认为sum
```redis
127.0.0.1:6379> zrange score 0 -1 withscores
1) "peter"
2) "67"
3) "Amy"
4) "88"
5) "tom"
6) "94"
127.0.0.1:6379> zrange score2 0 -1 withscores
1) "Amy"
2) "88"
3) "jack"
4) "99"
127.0.0.1:6379> zrange inter_score 0 -1 withscores
1) "Amy"
2) "176" # sum
```

#### zincrby
增加某个元素的分数,当分数为负数时表示 减
```redis
#ZINCRBY key increment member
127.0.0.1:6379> zincrby score 5 tom
"94"
```
### 哈希 Hash

#### hset
添加`hset key field value`
```redis
localhost:6379> hset person name 'andy' age 28
(integer) 2
```
#### hget/hmget/hgetall
获取`hget key field`, 获取所有field value`hgetall key field`
```redis
localhost:6379> hget person name
"andy"

127.0.0.1:6379> hmget person name age
1) "Andy"
2) "20"

127.0.0.1:6379> hset  person name andy
(integer) 0
127.0.0.1:6379> hset person name Andy
(integer) 0
127.0.0.1:6379> hset person age 20
(integer) 0
127.0.0.1:6379> hgetall person
1) "name"
2) "Andy"
3) "age"
4) "20"
```
#### hexists
判断 是否存在
```redis
127.0.0.1:6379> hexists person age
(integer) 1
```
#### hsetnx
不存在时赋值hset not exitst, #它与hset的不同在于如果字段已经存在，则不执行
```redis
127.0.0.1:6379> hsetnx person gender male
(integer) 1
```

#### hincrby
增加值 hash类型没有hincr命令
```redis
127.0.0.1:6379> hincrby person age 2
(integer) 22
```
#### hkeys
获取某个hash中所有的field `hkeys key`
```redis
localhost:6379> hkeys person
1) "name"
2) "age"
```
#### hvals
获取某个hash中所有的value`hvals key`
```redis
localhost:6379> hvals person
1) "andy"
2) "28"
```
#### hdel
删除`hdel key field`
```redis
localhost:6379> hset person school yangtze
(integer) 1
localhost:6379> hgetall person
1) "name"
2) "andy"
3) "age"
4) "28"
5) "school"
6) "yangtze"
localhost:6379> hdel person school
(integer) 1
localhost:6379> hgetall person
1) "name"
2) "andy"
3) "age"
4) "28"
```
#### hlen
获取hash中总共键值对`hlen field`
```redis
localhost:6379> hlen person
(integer) 2
```

### 事务
事务操作：redis 事务可以一次执行多个命令，事务具有以下特征：
* 隔离操作：事务中的所有命令都会序列化，按照顺序插，不会被其它命令打扰
* 原子操作：事务中的命令要么全部执行成功，要么都不执行

开启一个事务：`multi`后面执行的命令都在这个事务中执行
执行事务`exec` 将multi 与exec之间的所有命令执行
取消事务`discard`将multi后的所有命令取消
监视一个或者多个key`watch key` 监视一个或多个key,如果在事务执行之前这个key被其它命令所改动，那么事务被打断，不会执行

取消所有key的监视`unwatch`
```redis
localhost:6379> hgetall person
1) "name"
2) "andy"
3) "age"
4) "28"
5) "salary"
6) "10000"
localhost:6379> multi
OK
localhost:6379> hdel person salary
QUEUED
localhost:6379> exec
1) (integer) 1
localhost:6379> hgetall person
1) "name"
2) "andy"
3) "age"
4) "28"

localhost:6379> multi
OK
localhost:6379> hset person age 29
QUEUED
localhost:6379> discard
OK
localhost:6379> exec
(error) ERR EXEC without MULTI
```

### 排序
```redis
127.0.0.1:6379> LPUSH mylist 4 2 6 1 3 7
(integer) 6
127.0.0.1:6379> SORT mylist
1) "1"
2) "2"
3) "3"
4) "4"
5) "6"
6) "7"
```
#by
```redis
127.0.0.1:6379> LPUSH sortbylist 2 1 3
(integer) 3
127.0.0.1:6379> SET itemscore:1 50
OK
127.0.0.1:6379> SET itemscore:2 100
OK
127.0.0.1:6379> SET itemscore:3 -10
OK
127.0.0.1:6379> SORT sortbylist BY itemscore:* DESC
1) "2"
2) "1"
3) "3"
# store  将结果存入某个变量中
127.0.0.1:6379> SORT sortbylist BY itemscore:* DESC store desc_list
127.0.0.1:6379> lrange desc_list 0 -1
1) "2"
2) "1"
3) "3"
```
### 消息通知
BRPOP命令和RPOP命令相似，唯一的区别是当列表中没有元素时BRPOP命令会一直阻塞住连接，直到有新元素加入
除了 BRPOP命令外，Redis 还提供了 BLPOP，和 BRPOP的区别在与从队列取元素时BLPOP会从队列左边取

BRpop命令有两个参数：第一个是键名，第二个是超时时间，单位是秒。当超过了此时间仍然没有获得新元素的话就会返回 nil。上例中超时时间为"0"，表示不限制等待的时间，即如果没有新元素加入列表就会永远阻塞下去。当获得一个元素后 BRPOP 命令返回两个值，分别是键名和元素值

### 发布  订阅
发布/订阅
```redis
publish channel message
subscribe channel

127.0.0.1:6379> publish ccav this is ccav
(error) ERR wrong number of arguments for 'publish' command
127.0.0.1:6379> publish ccav "this is ccav"
(integer) 0
127.0.0.1:6379> publish ccav 'this ccav'
(integer) 1
127.0.0.1:6379> subscribe ccav
Reading messages... (press Ctrl-C to quit)
1) "subscribe"
2) "ccav"
3) (integer) 1
1) "message"
2) "ccav"
3) "this ccav"
```

另外还有Psubscribe/punsubscribe命令支持通配符:PSUBSCRIBE channel.?* 可以订阅：channel.1,channel.10 但无法订阅channel.


### 管道
redis 的底层通信协议对管道（pipelining）提供了支持。通过管道可以一次性发送多条命令并在执行完后一次性将结果返回，当一组命令中每条命令都不依赖于之前命令的执行结果时就可以将这组命令一起通过管道发出

### 持久化
#### RDB同步机制：
1. 开启和关闭：默认情况下是开启了。如果想关闭，那么注释掉`redis.conf`文件中的所有`save`选项就可以了。
2. 同步机制：
    * save 900 1：如果在900s以内发生了1次数据更新操作，那么就会做一次同步操作。
    * save 300 10：如果在300s以内发生了10数据更新操作，那么就会做一次同步操作。
    * save 60 10000：如果在60s以内发生了10000数据更新操作，那么就会做一次同步操作。
3. 存储内容：具体的值，而是命令。并且是经过压缩后存储进去的。
4. 存储路径：根据`redis.conf`下的`dir`以及`rdbfilename`来指定的。默认是`/var/lib/redis/dump.rdb`。
5. 优点：
    * 存储数据到文件中会进行压缩，文件体积比aof小。
    * 因为存储的是redis具体的值，并且会经过压缩，因此在恢复的时候速度比AOF快。
    * 非常适用于备份。
6. 缺点：
    * RDB在多少时间内发生了多少写操作的时候就会出发同步机制，因为采用压缩机制，RDB在同步的时候都重新保存整个Redis中的数据，因此你一般会设置在最少5分钟才保存一次数据。在这种情况下，一旦服务器故障，会造成5分钟的数据丢失。
    * 在数据保存进RDB的时候，Redis会fork出一个子进程用来同步，在数据量比较大的时候，可能会非常耗时。

#### AOF同步机制：
1. 开启和关闭：默认是关闭的。如果想要开启，那么修改redis.conf中的`appendonly yes`就可以了
2. 同步机制：
    * appendfsync always：每次有数据更新操作，都会同步到文件中。
    * appendfsync everysec：每秒进行一次更新。
    * appendfsync no：使用操作系统的方式进行更新。普遍是30s更新一次。
3. 存储内容：存储的是具体的命令。不会进行压缩。
4. 存储路径：根据`redis.conf`下的`dir`以及`appendfilename`来指定的。默认是`/var/lib/redis/appendonly.aof`。
5. 优点：
    * AOF的策略是每秒钟或者每次发生写操作的时候都会同步，因此即使服务器故障，最多只会丢失1秒的数据。 
    * AOF存储的是Redis命令，并且是直接追加到aof文件后面，因此每次备份的时候只要添加新的数据进去就可以了。
    * 如果AOF文件比较大了，那么Redis会进行重写，只保留最小的命令集合。
6. 缺点：
    * AOF文件因为没有压缩，因此体积比RDB大。 
    * AOF是在每秒或者每次写操作都进行备份，因此如果并发量比较大，效率可能有点慢。
    * AOF文件因为存储的是命令，因此在灾难恢复的时候Redis会重新运行AOF中的命令，速度不及RDB。

### 给redis指定密码：
1. 设置密码：在`redis.conf`配置文件中，将`requirepass pasword`取消注释，并且指定你想设置的密码。
2. 使用密码连接redis：
    * 先登录上去，然后再使用`auth password`命令进行授权。
    * 在连接的时候，通过`-a`参数指定密码进行连接。

### 其他机器连接redis：
如果想要让其他机器连接本机的redis服务器，那么应该在`redis.conf`配置文件中，指定`bind 本机的ip地址`。这样别的机器就能连接成功。不像是网上说的，要指定对方的ip地址

### python操作redis
安装`pip install redis`
```python
from redis import Redis

cache = Redis(host='192.168.16.8',port=6379,password='zjgisadmin')


cache.set('username','andy')
username = cache.get('username')
print(username)


cache.lpush('school', 'yangtze')
lmembers = cache.lrange('school', 0,-1)
print(lmembers)

cache.sadd('language', 'python')
language = cache.smembers('language')
print(language)

cache.hset('search', 'baidu','www.baidu.com')
search = cache.hget('search','baidu')
print(search)

"""
(flask_env)  ✘  /mnt/d/code/flask_alembic_demo  python py_redis.py
b'andy'
[b'yangtze', b'yangtze', b'yangtze', b'yangtze']
{b'python'}
b'www.baidu.com'
"""
```