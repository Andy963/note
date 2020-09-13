## pymysql模块

### 安装
```bash
pip3 install pymysq
```

### 连接
```python
import pymysql
#指定库名，还要指定字符集。不然会出现乱码
conn=pymysql.connect(host='localhost',port=3306,user='root',password='123',database='student',charset='utf8')
```

### 使用

```sql
#游标
cursor=conn.cursor() #这就想当于mysql自带的那个客户端的游标mysql> 在这后面输入指令，回车执行
cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) #获取字典数据类型表示的结果，默认返回的是元组

sql='select * from userinfo where name="%s" and password="%s"' %(user,pwd) #注意%s需要加引号，执行这句sql的前提是要有个userinfo表，里面有name和password两个字段，还有一些数据，

res=cursor.execute(sql) #返回sql查询成功的记录数目，是个数字，是受sql语句影响到的记录行数，同时数据也返回给了游标

all_data=cursor.fetchall()  #获取返回的所有数据，注意凡是取数据，取过的数据就没有了，结果都是元祖格式的
many_data=cursor.fetchmany(3) #一下取出3条数据，
one_data=cursor.fetchone()  #按照数据的顺序，一次只拿一个数据，下次再去就从第二个取了，因为第一个被取出去了，取一次就没有了，结果也都是元祖格式的

conn.commit() #必须执行conn.commit,注意是conn，不是cursor,执行后数据才写入到文件中

cursor.close()  # 关闭游标
conn.close()  # 关闭连接
```

上面的使用方式存在mysql注入的问题
解决办法：
```sql
改写为（execute帮我们做字符串拼接，我们无需且一定不能再为%s加引号了）
sql="select * from userinfo where name=%s and password=%s" #！！！注意%s需要去掉引号，因为pymysql会自动为我们加上
res=cursor.execute(sql,[user,pwd]) #pymysql模块自动帮我们解决sql注入的问题，只要我们按照pymysql的规矩来。
```

## DBUtils 模块


### 基于函数的数据库连接池

```py
import pymysql
from DBUtils.PooledDB import PooledDB

POOL = PooledDB(
    creator=pymysql,  # 使用链接数据库的模块
    maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
    mincached=2,  # 初始化时，链接池中至少创建的链接，0表示不创建
    blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
    ping=0,  # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always

    host='127.0.0.1',
    port=3306,
    user='root',
    password='222',
    database='cmdb',
    charset='utf8'
)


def fetchall(sql, *args):
    """ 获取所有数据 """
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()

    return result


def fetchone(sql, *args):
    """ 获取单挑数据 """
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    return result 
```

### 基于类的数据库连接池
```py
import pymysql
from DBUtils.PooledDB import PooledDB

class SqlHelper(object):
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=6,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的链接，0表示不创建
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host='127.0.0.1',
            port=3306,
            user='root',
            password='222',
            database='cmdb',
            charset='utf8'
        )

    def open(self):
        conn = self.pool.connection()
        cursor = conn.cursor()
        return conn,cursor

    def close(self,cursor,conn):
        cursor.close()
        conn.close()

    def fetchall(self,sql, *args):
        """ 获取所有数据 """
        conn,cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        self.close(conn,cursor)
        return result

    def fetchone(self,sql, *args):
        """ 获取所有数据 """
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        self.close(conn, cursor)
        return result

db = SqlHelper() 

```

## mysql注入
对于sql语句，不要自己拼接。
mysql connector使用%s作为占位符，而pymysql使用？作为占位符，所以两种都可以。
```python
args = (id, name)
sql = "select id, name from test where id=%s and name=%s"
cursor.execute(sql, args)
```

