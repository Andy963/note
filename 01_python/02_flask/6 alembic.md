## alembic笔记：

使用alembic的步骤：
1. 定义好自己的模型。
2. 使用alembic创建一个仓库：`alembic init [仓库的名字，推荐使用alembic]`。
3. 修改配置文件：
    * 在`alembic.ini`中，给`sqlalchemy.url`设置数据库的连接方式。这个连接方式跟sqlalchemy的方式一样的。
    * 在`alembic/env.py`中的`target_metadata`设置模型的`Base.metadata`。但是要导入`models`，需要将models所在的路径添加到这个文件中。示例代码如下：
        ```python
        import sys,os
        sys.path.append(os.path.dirname(os.path.dirname(__file__)))
        ```
4. 将ORM模型生成迁移脚本：`alembic revision --autogenerate -m 'message'`。
5. 将生成的脚本映射到数据库中：`alembic upgrade head`。
6. 以后如果修改了模型，重复4、5步骤。
7. 注意事项：在终端中，如果想要使用alembic，则需要首先进入到安装了alembic的虚拟环境中，不然就找不到这个命令。

### 常用命令：
1. init：创建一个alembic仓库。
2. revision：创建一个新的版本文件。
3. --autogenerate：自动将当前模型的修改，生成迁移脚本。
4. -m：本次迁移做了哪些修改，用户可以指定这个参数，方便回顾。
5. upgrade：将指定版本的迁移文件映射到数据库中，会执行版本文件中的upgrade函数。如果有多个迁移脚本没有被映射到数据库中，那么会执行多个迁移脚本。
6. [head]：代表最新的迁移脚本的版本号。
7. downgrade：会执行指定版本的迁移文件中的downgrade函数。
8. heads：展示head指向的脚本文件版本号。
9. history：列出所有的迁移版本及其信息。
10. current：展示当前数据库中的版本号。

### 经典错误：
1. FAILED: Target database is not up to date.
    * 原因：主要是heads和current不相同。current落后于heads的版本。
    * 解决办法：将current移动到head上。alembic upgrade head
2. FAILED: Can't locate revision identified by '77525ee61b5b'
    * 原因：数据库中存的版本号不在迁移脚本文件中
    * 解决办法：删除数据库的alembic_version表中的数据，重新执行alembic upgrade head
3. 执行`upgrade head`时报某个表已经存在的错误：
    * 原因：执行这个命令的时候，会执行所有的迁移脚本，因为数据库中已经存在了这个表。然后迁移脚本中又包含了创建表的代码。
    * 解决办法：（1）删除versions中所有的迁移文件。（2）修改迁移脚本中创建表的代码。

### memcache

安装
```shell
sudo apt install memcached
yum install memcached -y
```

启动
```shell
systemctl start memcached
cd /usr/bin
/usr/bin/memcached -d -u memcached -p 11211 -m 64 -l 0.0.0.0
# -d daemon
# -u user
# -p port (11211)
# -m memory (64M)
# -l ip list
```

连接
```shell
telnet ip port 
```
#### 常用命令
set 在memcached中添加一个key value 如果key已经存在过，那么就替换，否则就添加
```shell
set key 0[是否压缩] 60 过期时间 7[字符长度]
set name 0 60 4                                                                 
andy                                                                            STORED
```
get username[key] 从memcached中获取一个数据，根据key来获取
```shell
get name                                                                        
VALUE name 0 4                                                                  
andy                                                                            
END
```

add向memcached中添加数据，如果已经存在就添加失败，否则就添加
```shell
add name 0 60 4                                                                 
andy                                                                            STORED                                                                          
add name 0 60 4                                                                 
andy                                                                            NOT_STORED
```

delete key 删除数据
```shell
set name 0 60 4                                                                 
andy                                                                            STORED                                                                          delete name                                                                     DELETED                                                                         
get name                                                                        
END  
```

flush_all 删除memcached中所有的值

incr 相加,相加的必须都是数字类型，否则 无法相加，报错
```shell
set age 0 120 2                                                                 
12                                                                              STORED                                                                          
incr age 8                                                                      
20  
```
decr 相减
```shell
decr age 8                                                                      
12 
```

stats命令，查看状态
```shell
stats                                                                           
STAT pid 58180                                                                  
STAT uptime 1462                                                                
STAT time 1585363342                                                            
STAT version 1.4.15                                                             
STAT libevent 2.0.21-stable                                                     
STAT pointer_size 64                                                            
STAT rusage_user 0.010977                                                       
STAT rusage_system 0.098796                                                     
STAT curr_connections 5 # 当前有多少连接
STAT total_connections 6 # 总共多少连接
STAT connection_structures 6                                                    
STAT reserved_fds 20                                                            
STAT cmd_get 5 # 总共get多少次
STAT cmd_set 6 # 总共set多少次
STAT cmd_flush 0                                                                
STAT cmd_touch 0                                                                
STAT get_hits # 1 命中次数
STAT get_misses 4                                                               
STAT delete_misses 0                                                            
STAT delete_hits 1                                                              
STAT incr_misses 0                                                              
STAT incr_hits 1                                                                
STAT decr_misses 0                                                              
STAT decr_hits 1                                                                
STAT cas_misses 0                                                               
STAT cas_hits 0                                                                 
STAT cas_badval 0                                                               
STAT touch_hits 0                                                               
STAT touch_misses 0                                                             
STAT auth_cmds 0                                                                
STAT auth_errors 0                                                              
STAT bytes_read 312                                                             
STAT bytes_written 161                                                          
STAT limit_maxbytes 67108864                                                    
STAT accepting_conns 1                                                          
STAT listen_disabled_num 0                                                      
STAT threads 4                                                                  
STAT conn_yields 0                                                              
STAT hash_power_level 16                                                        
STAT hash_bytes 524288                                                          
STAT hash_is_expanding 0                                                        
STAT bytes 70                                                                   
STAT curr_items 1 # 当前有多少个元素
STAT total_items 7                                                              
STAT expired_unfetched 1                                                        
STAT evicted_unfetched 0                                                        
STAT evictions 0                                                                
STAT reclaimed 3                                                                
END
```
memcached默认最大连接1024

#### python 使用memcached
安装
```python
pip install python-memcached
```
连接
```py
import memcache
#如果要实现分布式在下面的列表中添加对应主机的ip:port
mc = memcache.Client(['192.168.16.8:11211'],debug=True)

mc.set('name', 'andy',120)
print(mc.get('name'))

mc.set_multi({'name':'jack','age':18,'telephone':110},time=120)
print(mc.get('age'))

mc.delete('telephone')
print(mc.get('telephone'))
mc.incr('age', 2)
print(mc.get('age'))

mc.decr('age', 3)
print(mc.get('age'))

andy
18
None
20
17
```
安全相关：
* 使用-l参数设置为只有本地可以连接，这种方式会导致别的机器不能访问，达到安全的目的
* 使用防火墙，关闭11211端口，外面 不能访问

```shell
ufw enable # 开启防火墙
ufw disable # 关闭防火墙
ufw deny port # 关闭某个指定端口
ufw allow port 开启某个端口
```


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