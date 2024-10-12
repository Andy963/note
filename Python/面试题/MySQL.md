
### 列举常见的关系型数据库和非关系型都有那些？
```
关系型数据库(需要有表结构)
mysql、oracle、db2

非关系型数据库（是以key-value存储的，没有表结构）（NoSQL）
 MongoDB
MongoDB 是一个高性能，开源，无模式的文档型数据库，开发语言是C++。它在许多场景下可用于替代传统的关系型数据库或键/值存储方式。
 Redis
Redis 是一个开源的使用ANSI C语言编写、支持网络、可基于内存亦可持久化的日志型、Key-Value数据库，并提供多种语言的API。目前由VMware主持开发工作。
```

### MySQL 常见数据库引擎及区别
```
InnoDB 
支持事务
支持表锁、行锁（for update）
表锁：select * from tb for update
行锁：select id,name from tb where id=2 for update

myisam
查询速度快
全文索引
支持表锁
表锁：select * from tb for update

NDB
高可用、 高性能、高可扩展性的数据库集群系统

Memory 
默认使用的是哈希索引
```

### 简述事务及其特性？
```
事务用于将某些操作的多个SQL作为原子性操作，一旦有某一个出现错误，即可回滚到原来的状态，从而保证数据库数据完整性。

事务的特性：
原子性: 确保工作单元内的所有操作都成功完成，否则事务将被中止在故障点，和以前的操作将回滚到以前的状态。
一致性: 确保数据库正确地改变状态后，成功提交的事务。
隔离性: 使事务操作彼此独立的和透明的。
持久性: 确保提交的事务的结果或效果的系统出现故障的情况下仍然存在。

Mysql实现事务
InnoDB支持事务，MyISAM不支持
    # 启动事务：
        # start transaction；
        # update from account set money=money-100 where name='a';
        # update from account set money=money+100 where name='b';
        # commit；
        'start transaction 手动开启事务，commit 手动关闭事务'
```

### 简述触发器、函数、视图、存储过程？
```
触发器：
对数据库某张表的增加、删除，修改前后定义一些操作

函数：(触发函数是通过select)
聚合函数：max/sum/min/avg
时间格式化：date_format
字符串拼接：concat

存储过程：
将SQL语句保存到数据库中，并命名，以后在代码调用时，直接调用名称即可
参数类型：
　　in    只将参数传进去
　　out   只拿结果
　　inout 既可以传，可以取

函数与存储过程区别：
本质上没区别。只是函数有如：只能返回一个变量的限制。而存储过程可以返回多个。而函数是可以嵌入在sql中使用的,可以在select中调用，而存储过程不行。

视图：
视图是一个虚拟表，不是真实存在的
```

### MySQL 索引种类
```
单列
功能
   普通索引：加速查找
   唯一索引：加速查找 + 约束：不能重复（只能有一个空，不然就重复了）
   主键（primay key）：加速查找 + 约束：不能重复 +  不能为空
多列
　　联合索引（多个列创建索引）-----> 相当于单列的普通索引
　　联合唯一索引            -----> 相当于单列的唯一索引
　　ps：联合索引的特点：遵循最左前缀的规则
其他词语：
·· - 索引合并，利用多个单例索引查询；（例如在数据库查用户名和密码，分别给用户名和密码建立索引）
   - 覆盖索引，在索引表中就能将想要的数据查询到；
```

### 索引在什么情况下遵循最左前缀的规则？
```
联合索引
```

### MySQL 常见的函数？
```
聚合函数
max/sum/min/avg

时间格式化
date_format

字符串拼接
concat（当拼接了null，则返回null）

截取字符串
substring

返回字节个数
length
```

### 列举 创建索引但是无法命中索引的情况
```
1.- like '%xx'
    select * from tb1 where name like '%cn';
2.- 使用函数
    select * from tb1 where reverse(name) = 'wupeiqi';
3.- or
    select * from tb1 where nid = 1 or email = 'seven@live.com';
    特别的：当or条件中有未建立索引的列才失效，以下会走索引
            select * from tb1 where nid = 1 or name = 'seven';
            select * from tb1 where nid = 1 or email = 'seven@live.com' and name = 'alex'
4.- 类型不一致
    如果列是字符串类型，传入条件是必须用引号引起来，不然...
    select * from tb1 where name = 999;
5.- !=
    select * from tb1 where name != 'alex'
    特别的：如果是主键，则还是会走索引
        select * from tb1 where nid != 123
6.- >
    select * from tb1 where name > 'alex'
    特别的：如果是主键或索引是整数类型，则还是会走索引
        select * from tb1 where nid > 123
        select * from tb1 where num > 123
7.- order by
    select email from tb1 order by name desc;
    当根据索引排序时候，选择的映射如果不是索引，则不走索引
    特别的：如果对主键排序，则还是走索引：
        select * from tb1 order by nid desc;
 
8.- 组合索引最左前缀
    如果组合索引为：(name,email)
    name and email       -- 使用索引
    name                 -- 使用索引
    email                -- 不使用索引
```

### 数据库导入导出命令（结构+数据）
```
导出现有数据库数据：（当有提示出入密码。-p就不用加密码）
  mysqldump -u用户名 -p密码 数据库名称 >导出文件路径           # 结构+数据
  mysqldump -u用户名 -p密码 -d 数据库名称 >导出文件    路径       # 结构 

导入现有数据库数据：
    mysqldump -uroot -p密码  数据库名称 < 文件路径  
```

### 你了解那些数据库优化方案？
```
1、创建数据表时把固定长度的放在前面（）
2、将固定数据放入内存： 例如：choice字段 （django中有用到，数字1、2、3…… 对应相应内容）
3、char 和 varchar 的区别(char可变, varchar不可变 )
　　
4、联合索引遵循最左前缀(从最左侧开始检索)
5、避免使用 select * 
6、读写分离
　　　　- 实现：两台服务器同步数据
　　　　- 利用数据库的主从分离：主，用于删除、修改、更新；从，用于查；
读写分离:利用数据库的主从进行分离：主，用于删除、修改更新；从，用于查
7、分库
　　　　- 当数据库中的表太多，将某些表分到不同的数据库，例如：1W张表时
　　　　- 代价：连表查询
8、分表
　　　　- 水平分表：将某些列拆分到另外一张表，例如：博客+博客详情
　　　　- 垂直分表：讲些历史信息分到另外一张表中，例如：支付宝账单

9、加缓存
　　　　- 利用redis、memcache （常用数据放到缓存里，提高取数据速度）


如果只想获取一条数据
     - select * from tb where name=‘alex’ limit 1
```

### char 和varchar 的区别？
```
char 和 varchar 的区别(char可变, varchar不可变 )
```

### 简述MySQL 的执行计划的作用及使用方法？
```
查看有没有命中索引，让数据库帮看看运行速度快不快
explain select * from table;
```

### 1000w 条数据，使用limit offset 分页时，为什么越往后翻越慢？如何解决？
```
 答案一：
      先查主键，在分页。
      select * from tb where id in (
          select id from tb where limit 10 offset 30
      )
  答案二：
      按照也无需求是否可以设置只让用户看200页
  答案三：
      记录当前页  数据ID最大值和最小值
      在翻页时，根据条件先进行筛选；筛选完毕之后，再根据limit offset 查询。
      select * from (select * from tb where id > 22222222) as B limit 10 offset 0
      如果用户自己修改页码，也可能导致慢；此时对url种的页码进行加密（rest framework ）
```

### 什么是索引合并？
```
1、索引合并是把几个索引的范围扫描合并成一个索引。
2、索引合并的时候，会对索引进行并集，交集或者先交集再并集操作，以便合并成一个索引。
3、这些需要合并的索引只能是一个表的。不能对多表进行索引合并。

简单的说，索引合并，让一条sql可以使用多个索引。对这些索引取交集，并集，或者先取交集再取并集。
从而减少从数据表中取数据的次数，提高查询效率。
```

### 什么是覆盖索引
```
在索引表中就能将想要的数据查询到
```

### 简述数据库读写分离
```
- 实现：两台服务器同步数据
　　　　- 利用数据库的主从分离：主，用于删除、修改、更新；从，用于查；
```

### 简述数据库分库分表？（水平、垂直）
```
1、分库
    当数据库中的表太多，将某些表分到不同数据库，例如：1W张表时
    代价：连表查询跨数据库，代码变多
# 2、分表
    水平分表：将某些列拆分到另一张表，例如：博客+博客详情
    垂直分表：将某些历史信息，分到另外一张表中，例如：支付宝账单
```

### 数据库锁的作用？
```
根据不同的锁的作用域我们可以把数据库的锁分为三种，分别为：
行锁：对表中的某一行进行加锁。
页锁：对表中一组连续的行进行加锁。
表锁：对整张表进行加锁
不同的作用域对并发性能是有很大影响的，比如说如果数据库的插入都是使用表锁，那在大量用户对某张表进行插入读取操作的话，同时只能有一个用户可以访问该表，那并发量肯定就是惨不忍睹了。
```

### where 子句中有a,b,c 三个查询条件, 创建一个组合索引abc(a,b,c)，
以下哪种会命中索引
(a)
(b)
(c)
(a,b)
(b,c)
(a,c)
(a,b,c)

### mysql 下面那些查询不会使用索引,between, like "c%" , not in, not exists, !=, <, <=, =, >, >=,in
```

```

### mysql 中varchar 与char 的区别以及varchar(50)中的50 代表的含义
```
1)、varchar与char的区别char是一种固定长度的类型，varchar则是一种可变长度的类型 
尽可能的使用 varchar 代替 char ，因为首先变长字段存储空间小，可以节省存储空间，	
其次对于查询来说，在一个相对较小的字段内搜索效率显然要高些。

varchar(50)中50的涵义最多存放50个字符，varchar(50)和(200)存储hello所占空间一样，但后者在排序时会消耗更多内存，
因为order by col采用fixed_length计算col长度(memory引擎也一样)
```

### 请简述项目中优化sql 语句执行效率的方法
```
1)尽量选择较小的列
2)将where中用的比较频繁的字段建立索引
3)select子句中避免使用‘*’
4)避免在索引列上使用计算、not in 和<>等操作
5)当只需要一行数据的时候使用limit 1
6)保证单表数据不超过200W，适时分割表。
```

### 从delete 语句中省略where 子句, 将产生什么后果?
```
删除表中所有数据
```

### 叙述mysql 半同步复制原理
```

```

### mysql 中怎么创建索引？
```

```

### 请简述sql 注入的攻击原理及如何在代码层面防止sql 注入
```

```

### 使用Python 实现将数据库的student 表中取的数据写入db.txt？
```

```

### 简述left join 和right join 的区别？
```
left join(左联接) 返回包括左表中的所有记录和右表中联结字段相等的记录
right join(右联接) 返回包括右表中的所有记录和左表中联结字段相等的记录
inner join(等值连接) 只返回两个表中联结字段相等的行
```

### 索引有什么作用, 有那些分类, 有什么好处和坏处？
```
作用：加快查询，拖慢删除/添加的速度
分类：聚集索引：辅助索引
聚集索引：
- 每张表只能有一个聚集索引
- 叶子节点直接对应数据，所以找到索引就是找到数据
- 数据的存储物理地址是按照索引顺序来存的，所以按照聚集索引列排序非常快

辅助索引(非聚集索引)：
- 每张表可以有多个辅助索引，查询速度快，但占用更多磁盘空间，影响删除和添加的效率
- 叶子节点不直接存放数据，而是存放数据的地址，所以找到叶子节点后还需再做一次IO操作
- 数据的物理地址和索引顺序无关.

为了加快查询速度根据二分法速度快的原理，产生可平衡二叉树，但是b树高度高，查询次数多，就增加了分叉，形成了b-树：

b-树：会把数据行存储在中间节点中，所以导致节点中能存储的数据太少
b+树：中间节点不存放数据.innodb，myisam都是基于b+树创建索引
什么决定树的高度?数据的量和数据的长度。
什么是索引? 把数据的某个字段按照特殊的算法计算成一个树型结构，再根据树型结构提供的指针缩小范围，找到对应的磁盘块.通过这棵树，可以将我们每次的查询范围缩小1/3，加快了我们的查询速度，这棵树就是索引。
```

### 试列出至少三种目前流行的大型关系型数据库的名称
```
Oracle
SQL Server
MySQL
```

### 什么是MySQL 慢日志？
```
慢日志查询的主要功能就是，记录sql语句中超过设定的时间阈值的查询语句。例如，一条查询sql语句，我们设置的阈值为1s，当这条查询语句的执行时间超过了1s，则将被写入到慢查询配置的日志中.慢查询主要是为了我们做sql语句的优化功能.

配置项说明：
    登陆mysql服务：
    > show variables like '%query%';
    关注三个配置项即可。
  1.slow_query_log
  该配置项是决定是否开启慢日志查询功能，配置的值有ON或者OFF.
  2.slow_query_log_file
  该配置项是慢日志查询的记录文件,需要手动创建.
  3.long_query_time
  该配置项是设置慢日志查询的时间阈值，当超过这个阈值时，慢日志才会被记录.配置的值有0(任何的sql语句都记录下来)，或者>0(具体的阈值).该配置项是以秒为单位的，并且可以设置为小数.
  4.log-queries-not-using-indexes
  该配置项是为了记录未使用到索引的sql语句.
```

### redis 和memcached 的区别？
```
区别
1：redis不仅支持简单的key_value类型，还支持字典，字符串，列表，集合，有序集合类型
2：内存使用效率对比，使用简单的key-value存储的话，
   Memcached的内存利用率更高而如果Redis采用hash结构来做key-value存储，由于其组合式的压缩，其内存利用率会高于Memcached。
3.性能对比：由于Redis只使用单核，而Memcached可以使用多核，.
   所以平均每一个核上Redis在存储小数据时比Memcached性能更高。而在100k以上的数据中，Memcached性能要高Redis，
4.Redis虽然是基于内存的存储系统，但是它本身是支持内存数据的持久化的，而且提供两种主要的持久化策略：RDB快照和AOF日志。
   而memcached是不支持数据持久化操作的。
5.集群管理不同，Memcached本身并不支持分布式，因此只能在客户端通过像一致性哈希这样的分布式算法来实Memcached的分布式存储。
```

### 如何高效的找到redis 中所有以oldboy 开头的key？
```
# 语法：KEYS pattern
# 说明：返回与指定模式相匹配的所用的keys。
该命令所支持的匹配模式如下：
1、"?"：用于匹配单个字符。例如，h?llo可以匹配hello、hallo和hxllo等；
2、"*"：用于匹配零个或者多个字符。例如，h*llo可以匹配hllo和heeeello等；
2、"[]"：可以用来指定模式的选择区间。例如h[ae]llo可以匹配hello和hallo，但是不能匹配hillo。同时，可以使用“/”符号来转义特殊的字符
```

### 什么是一致性哈希？
```
一致性hash算法（DHT）可以通过减少影响范围的方式，解决增减服务器导致的数据散列问题，从而解决了分布式环境下负载均衡问题；
如果存在热点数据，可以通过增添节点的方式，对热点区间进行划分，将压力分配至其他服务器，重新达到负载均衡的状态。
```

### redis 是单进程单线程的吗？
```
单线程指的是网络请求模块使用了一个线程（所以不需考虑并发安全性），即一个线程处理所有网络请求，其他模块仍用了多个线程。
```
### redis 中数据库默认是多少个db 及作用？
```
Redis默认支持16个数据库，可以通过配置databases来修改这一数字。客户端与Redis建立连接后会自动选择0号数据库，不过可以随时使用SELECT命令更换数据库
  
Redis支持多个数据库，并且每个数据库的数据是隔离的不能共享，并且基于单机才有，如果是集群就没有数据库的概念
```

### 如果redis 中的某个列表中的数据量非常大，如果实现循环显示每一个值？
```
- 如果一个列表在redis中保存了10w个值，我需要将所有值全部循环并显示，请问如何实现？
       一个一个取值，列表没有iter方法，但能自定义
　　　　 def list_scan_iter(name,count=3):
            start = 0
            while True:
                result = conn.lrange(name, start, start+count-1)
                start += count
                if not result:
                    break
                for item in result:
                    yield item

        for val in list_scan_iter('num_list'):
            print(val)
　　场景：投票系统，script-redis
```

### redis 如何实现主从复制？以及数据同步机制？
```
优势：
    - 高可用
    - 分担主压力
注意： 
    - slave设置只读

从的配置文件添加以下记录，即可：
    slaveof 1.1.1.1 3306 
```

### redis 中的sentinel 的作用？
```

   帮助我们自动在主从之间进行切换
    检测主从中 主是否挂掉，且超过一半的sentinel检测到挂了之后才进行进行切换。
    如果主修复好了，再次启动时候，会变成从。

    启动主redis:
    redis-server /etc/redis-6379.conf  启动主redis
    redis-server /etc/redis-6380.conf  启动从redis
        
    在linux中：
        找到 /etc/redis-sentinel-8001.conf  配置文件，在内部：
            - 哨兵的端口 port = 8001
            - 主redis的IP，哨兵个数的一半/1
        
        找到 /etc/redis-sentinel-8002.conf  配置文件，在内部：
            - 哨兵的端口 port = 8002
            - 主redis的IP, 1 
    
        启动两个哨兵   
```

### 如何实现redis 集群？
```
redis集群、分片、分布式redis     
    redis-py-cluster
    集群方案：
        - redis cluster 官方提供的集群方案。
        - codis，豌豆荚技术团队。
        - tweproxy，Twiter技术团队。
    redis cluster的原理？
        - 基于分片来完成。
        - redis将所有能放置数据的地方创建了 16384 个哈希槽。
        - 如果设置集群的话，就可以为每个实例分配哈希槽：
            - 192.168.1.20【0-5000】
            - 192.168.1.21【5001-10000】
            - 192.168.1.22【10001-16384】
        - 以后想要在redis中写值时，
            set k1 123 
将k1通过crc16的算法，将k1转换成一个数字。然后再将该数字和16384求余，如果得到的余数 3000，那么就将该值写入到 192.168.1.20 实例中。
```

### redis 中默认有多少个哈希槽？
```
16384
```

### 简述redis 的有哪几种持久化策略及比较？
```
RDB：每隔一段时间对redis进行一次持久化。
      - 缺点：数据不完整
      - 优点：速度快
AOF：把所有命令保存起来，如果想到重新生成到redis，那么就要把命令重新执行一次。
      - 缺点：速度慢，文件比较大
      - 优点：数据完整
```

### 列举redis 支持的过期策略。
```
 voltile-lru：    从已设置过期时间的数据集（server.db[i].expires）中挑选最近频率最少数据淘汰
  volatile-ttl：   从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰
  volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰
  
  allkeys-lru：       从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰
  allkeys-random：    从数据集（server.db[i].dict）中任意选择数据淘汰
  no-enviction（驱逐）：禁止驱逐数据
```

### MySQL 里有 2000w 数据，redis 中只存 20w 的数据，如何保证 redis 中都是热点数据

```
相关知识：redis 内存数据集大小上升到一定大小的时候，就会施行数据淘汰策略（回收策略）。redis 提供 6种数据淘汰策略：

  volatile-lru：从已设置过期时间的数据集（server.db[i].expires）中挑选最近最少使用的数据淘汰
  volatile-ttl：从已设置过期时间的数据集（server.db[i].expires）中挑选将要过期的数据淘汰
  volatile-random：从已设置过期时间的数据集（server.db[i].expires）中任意选择数据淘汰
  allkeys-lru：从数据集（server.db[i].dict）中挑选最近最少使用的数据淘汰
  allkeys-random：从数据集（server.db[i].dict）中任意选择数据淘汰
  no-enviction（驱逐）：禁止驱逐数据

```

### 写代码，基于redis的列表实现 先进先出、后进先出队列、优先级队列
```
 参看script—redis源码
from scrapy.utils.reqser import request_to_dict, request_from_dict

  from . import picklecompat


  class Base(object):
      """Per-spider base queue class"""

      def __init__(self, server, spider, key, serializer=None):
          """Initialize per-spider redis queue.

          Parameters
          ----------
          server : StrictRedis
              Redis client instance.
          spider : Spider
              Scrapy spider instance.
          key: str
              Redis key where to put and get messages.
          serializer : object
              Serializer object with ``loads`` and ``dumps`` methods.

          """
          if serializer is None:
              # Backward compatibility.
              # TODO: deprecate pickle.
              serializer = picklecompat
          if not hasattr(serializer, 'loads'):
              raise TypeError("serializer does not implement 'loads' function: %r"
                              % serializer)
          if not hasattr(serializer, 'dumps'):
              raise TypeError("serializer '%s' does not implement 'dumps' function: %r"
                              % serializer)

          self.server = server
          self.spider = spider
          self.key = key % {'spider': spider.name}
          self.serializer = serializer

      def _encode_request(self, request):
          """Encode a request object"""
          obj = request_to_dict(request, self.spider)
          return self.serializer.dumps(obj)

      def _decode_request(self, encoded_request):
          """Decode an request previously encoded"""
          obj = self.serializer.loads(encoded_request)
          return request_from_dict(obj, self.spider)

      def __len__(self):
          """Return the length of the queue"""
          raise NotImplementedError

      def push(self, request):
          """Push a request"""
          raise NotImplementedError

      def pop(self, timeout=0):
          """Pop a request"""
          raise NotImplementedError

      def clear(self):
          """Clear queue/stack"""
          self.server.delete(self.key)


  class FifoQueue(Base):
      """Per-spider FIFO queue"""

      def __len__(self):
          """Return the length of the queue"""
          return self.server.llen(self.key)

      def push(self, request):
          """Push a request"""
          self.server.lpush(self.key, self._encode_request(request))

      def pop(self, timeout=0):
          """Pop a request"""
          if timeout > 0:
              data = self.server.brpop(self.key, timeout)
              if isinstance(data, tuple):
                  data = data[1]
          else:
              data = self.server.rpop(self.key)
          if data:
              return self._decode_request(data)


  class PriorityQueue(Base):
      """Per-spider priority queue abstraction using redis' sorted set"""

      def __len__(self):
          """Return the length of the queue"""
          return self.server.zcard(self.key)

      def push(self, request):
          """Push a request"""
          data = self._encode_request(request)
          score = -request.priority
          # We don't use zadd method as the order of arguments change depending on
          # whether the class is Redis or StrictRedis, and the option of using
          # kwargs only accepts strings, not bytes.
          self.server.execute_command('ZADD', self.key, score, data)

      def pop(self, timeout=0):
          """
          Pop a request
          timeout not support in this queue class
          """
          # use atomic range/remove using multi/exec
          pipe = self.server.pipeline()
          pipe.multi()
          pipe.zrange(self.key, 0, 0).zremrangebyrank(self.key, 0, 0)
          results, count = pipe.execute()
          if results:
              return self._decode_request(results[0])


  class LifoQueue(Base):
      """Per-spider LIFO queue."""

      def __len__(self):
          """Return the length of the stack"""
          return self.server.llen(self.key)

      def push(self, request):
          """Push a request"""
          self.server.lpush(self.key, self._encode_request(request))

      def pop(self, timeout=0):
          """Pop a request"""
          if timeout > 0:
              data = self.server.blpop(self.key, timeout)
              if isinstance(data, tuple):
                  data = data[1]
          else:
              data = self.server.lpop(self.key)

          if data:
              return self._decode_request(data)


  # TODO: Deprecate the use of these names.
  SpiderQueue = FifoQueue
  SpiderStack = LifoQueue
  SpiderPriorityQueue = PriorityQueue
```

### 如何基于redis 实现消息队列？
```
# 通过发布订阅模式的PUB、SUB实现消息队列
# 发布者发布消息到频道了，频道就是一个消息队列。
# 发布者：
import redis
conn = redis.Redis(host='127.0.0.1',port=6379)
conn.publish('104.9MH', "hahahahahaha")
# 订阅者：
import redis
conn = redis.Redis(host='127.0.0.1',port=6379)
pub = conn.pubsub()
pub.subscribe('104.9MH')
while True:
    msg= pub.parse_response()
    print(msg)
对了，redis 做消息队列不合适
业务上避免过度复用一个redis，用它做缓存、做计算，还做任务队列，压力太大，不好。
```

### 如何基于redis 实现发布和订阅？
```
   发布和订阅，只要有任务就给所有订阅者没人一份
  发布者：
      import redis

      conn = redis.Redis(host='127.0.0.1',port=6379)
      conn.publish('104.9MH', "hahaha")
  订阅者：
      import redis

      conn = redis.Redis(host='127.0.0.1',port=6379)
      pub = conn.pubsub()
      pub.subscribe('104.9MH')

      while True:
          msg= pub.parse_response()
          print(msg)
```

### 什么是codis？
```
Codis 是一个分布式 Redis 解决方案, 对于上层的应用来说, 连接到 Codis Proxy 和连接原生的 Redis Server 没有明显的区别 
(不支持的命令列表), 上层应用可以像使用单机的 Redis 一样使用, Codis 底层会处理请求的转发, 不停机的数据迁移等工作,所有后边的一切事情, 对于前面的客户端来说是透明的, 可以简单的认为后边连接的是一个内存无限大的 Redis 服务.
```

### 什么是twemproxy？
```
是Twitter 开源的一个 Redis 和 Memcache 代理服务器，主要用于管理 Redis 和 Memcached 集群，减少与Cache 服务器直接连接的数量。
```

### redis 如何实现事务。
```
 import redis

  pool = redis.ConnectionPool(host='10.211.55.4', port=6379)

  conn = redis.Redis(connection_pool=pool)

  # pipe = r.pipeline(transaction=False)
  pipe = conn.pipeline(transaction=True)
  # 开始事务
  pipe.multi()

  pipe.set('name', 'bendere')
  pipe.set('role', 'sb')

  # 提交
  pipe.execute()
  
  注意：咨询是否当前分布式redis是否支持事务
```

### redis 中的watch 的命令的作用？
```
  在Redis的事务中，WATCH命令可用于提供CAS(check-and-set)功能。
假设我们通过WATCH命令在事务执行之前监控了多个Keys，倘若在WATCH之后有任何Key的值发生了变化，
EXEC命令执行的事务都将被放弃，同时返回Null multi-bulk应答以通知调用者事务执行失败。
  
  面试题：你如何控制剩余的数量不会出问题？
      方式一：- 通过redis的watch实现
          import redis
          conn = redis.Redis(host='127.0.0.1',port=6379)

          # conn.set('count',1000)
          val = conn.get('count')
          print(val)

          with conn.pipeline(transaction=True) as pipe:

              # 先监视，自己的值没有被修改过
              conn.watch('count')

              # 事务开始
              pipe.multi()
              old_count = conn.get('count')
              count = int(old_count)
              print('现在剩余的商品有:%s',count)
              input("问媳妇让不让买？")
              pipe.set('count', count - 1)

              # 执行，把所有命令一次性推送过去
              pipe.execute()
     方式二 - 数据库的锁 
```

### 简述redis 分布式锁和redlock 的实现机制。
```
在不同进程需要互斥地访问共享资源时，分布式锁是一种非常有用的技术手段。 
有很多三方库和文章描述如何用Redis实现一个分布式锁管理器，但是这些库实现的方式差别很大
，而且很多简单的实现其实只需采用稍微增加一点复杂的设计就可以获得更好的可靠性。 
用Redis实现分布式锁管理器的算法，我们把这个算法称为RedLock。

实现
- 写值并设置超时时间
- 超过一半的redis实例设置成功，就表示加锁完成。
- 使用：安装redlock-py 
from redlock import Redlock

dlm = Redlock(
    [
        {"host": "localhost", "port": 6379, "db": 0},
        {"host": "localhost", "port": 6379, "db": 0},
        {"host": "localhost", "port": 6379, "db": 0},
    ]
)

# 加锁，acquire
my_lock = dlm.lock("my_resource_name",10000)
if  my_lock:
    # J进行操作
    # 解锁,release
    dlm.unlock(my_lock)
else:
    print('获取锁失败')

 redis分布式锁？
# 不是单机操作，又多了一/多台机器
# redis内部是单进程、单线程，是数据安全的(只有自己的线程在操作数据)
----------------------------------------------------------------
\A、B、C，三个实例(主)
1、来了一个'隔壁老王'要操作，且不想让别人操作，so，加锁；
    加锁：'隔壁老王'自己生成一个随机字符串，设置到A、B、C里(xxx=666)
2、来了一个'邻居老李'要操作A、B、C，一读发现里面有字符串，擦，被加锁了，不能操作了，等着吧~
3、'隔壁老王'解决完问题，不用锁了，把A、B、C里的key：'xxx'删掉；完成解锁
4、'邻居老李'现在可以访问，可以加锁了
# 问题：
1、如果'隔壁老王'加锁后突然挂了，就没人解锁，就死锁了，其他人干看着没法用咋办？
2、如果'隔壁老王'去给A、B、C加锁的过程中，刚加到Ａ，'邻居老李'就去操作C了，加锁成功or失败？
3、如果'隔壁老王'去给A、B、C加锁时，C突然挂了，这次加锁是成功还是失败？
4、如果'隔壁老王'去给A、B、C加锁时，超时时间为5秒，加一个锁耗时3秒，此次加锁能成功吗？
# 解决
1、安全起见，让'隔壁老王'加锁时设置超时时间，超时的话就会自动解锁(删除key：'xxx')
2、加锁程度达到（1/2）+1个就表示加锁成功，即使没有给全部实例加锁；
3、加锁程度达到（1/2）+1个就表示加锁成功，即使没有给全部实例加锁；
4、不能成功，锁还没加完就过期，没有意义了，应该合理设置过期时间
# 注意
    使用需要安装redlock-py
----------------------------------------------------------------
from redlock import Redlock
dlm = Redlock(
    [
        {"host": "localhost", "port": 6379, "db": 0},
        {"host": "localhost", "port": 6379, "db": 0},
        {"host": "localhost", "port": 6379, "db": 0},
    ]
)
# 加锁，acquire
my_lock = dlm.lock("my_resource_name",10000)
if  my_lock:
    # 进行操作
    # 解锁,release
    dlm.unlock(my_lock)
else:
    print('获取锁失败')
\通过sever.eval(self.unlock_script)执行一个lua脚本，用来删除加锁时的key
```

### 请设计一个商城商品计数器的实现方案？
```
import redis

conn = redis.Redis(host='192.168.1.41',port=6379)

conn.set('count',1000)

with conn.pipeline() as pipe:

    # 先监视，自己的值没有被修改过
    conn.watch('count')

    # 事务开始
    pipe.multi()
    old_count = conn.get('count')
    count = int(old_count)
    if count > 0:  # 有库存
        pipe.set('count', count - 1)

    # 执行，把所有命令一次性推送过去
    pipe.execute()
```

### 了解过 Hbase、DB2、SQLServer、Access 吗？
```

```