# mysql
 structured query language
 
## 数据库设计三范式
第一范式：
要有主键，并且每个字段原子性不可再分

第二范式：
要求所有非主键字段完全依赖主键，不能产生部分依赖
部分依赖指的能根据一个主键就确定一个数据，比如联合主键，那么就可能只是部分依赖。

第三范式：
所有非主键字段与主键字段之间不能产生传递依赖

[参考](https://www.jianshu.com/p/3e97c2a1687b)

## 设置

### 为root用户设置密码
在Linux 命令行，非mysql命令行中
```
mysqladmin -u root password'passwd'
mysqladmin -u -p'passwd' password 'passwd2' -S /data/3306/mysql.sock # 适合多实例

#修改密码
必须使用password函数，必须使用条件，必须
#方法一
mysqladmin -uroot -p'oldpassword' password 'newpassword'
mysqladmin -u root -p'passwd' password 'passwd2' -S /data/3306/mysql.sock # 适合多实例

# 方法二
# 在mysql中，下面这样设置的为明文密码，会导致无法登陆
# update msyql.user set password='passwd' where user='root' and host='localhost'
# 正确的应该使用password函数，然后刷新权限 priveleges;
# update msyql.user set password=password('passwd') where user='root' and host='localhost'
flush privileges;
当密码无法找回时，可以使用--skip-grant-talbes 然后通过上面的命令来修改密码

# 方法三
# 在mysql中
mysql> set password password('passwd'); # 不需要刷新权限 即可。
```
忘记密码
步骤：
* 停止mysql: /etc/init.d/mysql stop
* 忽略授权表登陆，修改密码，刷新权限表 --skip-grant-tables, flush privileges
* 停止mysql /etc/init.d/mysql stop
* 启动mysql
```
/etc/init.d/mysql stop
mysql_safe --skip-grant-tables --user=mysql
update mysql.user set password=password("admin123") where user="root" and host="localhost";
flush privileges;
quit;
mysqladmin -uroot -padmin123 shutdown
/etc/init.d/mysql start
```

优雅关闭mysql数据库的方法：
```
#方式一：
mysqladmin -uroot password shutdown 

#方式二：
/etc/init.d/mysql stop

#方式三：
systemctl stop mysql

kill -USR2 `cat path/pid'
```
### 存储引擎

常用的存储引擎为：MyISAM和InnoDB

查看命令
```sql
show engines；#查看MySQL所有的引擎，
show variables like "storage_engine%";查看当前正在使用的引擎
```
#### MyISAM引擎
1.不支持事务
            事务是指逻辑上的一组操作，组成这组操作的各个单元，要么全成功要么全失败。
2.表级锁定
            数据更新时锁定整个表：其锁定机制是表级锁定，也就是对表中的一个数据进行操作都会将这个表锁定，其他人不能操作这个表，这虽然可以让锁定的实现成本很小但是也同时大大降低了其并发性能。
3.读写互相阻塞
            不仅会在写入的时候阻塞读取，MyISAM还会再读取的时候阻塞写入，但读本身并不会阻塞另外的读。
4.只会缓存索引
            MyISAM可以通过key_buffer_size的值来提高缓存索引，以大大提高访问性能减少磁盘IO，但是这个缓存区只会缓存索引，而不会缓存数据。

5.读取速度较快
            占用资源相对较少
6.不支持外键约束，但支持全文索引

#### InnoDB引擎
支持事务，行级锁，支持外键

支持事务：支持4个事务隔离界别，支持多版本读。
行级锁定(更新时一般是锁定当前行)：通过索引实现，全表扫描仍然会是表锁，注意间隙锁的影响。
读写阻塞与事务隔离级别相关(有多个级别，这就不介绍啦~)。
具体非常高效的缓存特性：能缓存索引，也能缓存数据。
整个表和主键与Cluster方式存储，组成一颗平衡树。(了解)
所有SecondaryIndex都会保存主键信息。(了解)
支持分区，表空间，类似oracle数据库。
支持外键约束，不支持全文索引(5.5之前)，以后的都支持了。
和MyISAM引擎比较，InnoDB对硬件资源要求还是比较高的。

### 数据库表名大小写
```sql
show variables like '%lower_case_table_names%';
```
win一般默认值为1，表示是大小写不敏感，而linux环境的mysql是0

### 权限管理

#### 创建用户
```sql
create user 'andy'@'1.1.1.1' identified by 'password';
create user 'andy'@'1.1.1.%' identified by 'password';
create user 'andy'@'%' identified by 'password';
```
#### 授权：
对文件夹，对文件，对文件某一字段的权限。all可以代表除了grant之外的所有权限

```sql
#针对所有库的授权:*.*
grant select on *.* to 'andy'@'localhost' identified by 'password'; 

#针对某一数据库：db1.*
grant select on db1.* to 'andy'@'localhost' identified by 'password';

#针对某一个表：db1.t1
grant select on db1.t1 to 'andy'@'localhost' identified by 'password';

#删除权限
revoke select on db1.* from 'andy'@'%';  #  删除查的权限
```

## MySQL库和表的操作

### 库操作

#### 创建库

```sql
CREATE DATABASE 数据库名 charset utf8;
create database test charset utf8 collate utf8_general_cli;
  可以由字母、数字、下划线、＠、＃、＄

  区分大小写

  唯一性

  不能使用关键字如 create select

  不能单独使用数字

  最长128位
```
#### 其它

```sql
查看数据库

show databases;
show create database db1;
select database();

选择数据库
USE 数据库名

删除数据库
DROP DATABASE 数据库名;

修改数据库
alter database db1 charset utf8;
```

### 表操作

#### 创建表并指定引擎
```sql
create table t1(id int)engine=innodb; #指定innodb
create table t2(id int)engine=myisam; #指定myisam
```

```sql
create table 表名(
字段名1 类型[(宽度) 约束条件],
字段名2 类型[(宽度) 约束条件],
字段名3 类型[(宽度) 约束条件]
);

## 同一张表中，字段名不能相同，字段名和类型是必须指定的。

```

#### 查看表

```sql
show tables  #  查看当前库中所有表
describe tableName  # 查看指定的表， desc tableName
show create table tableName\G; #  \G指定查看详细信息

```

#### 修改表

```sql
#  重命名表名
alter table t1 rename t2;
#  添加字段
alter table t1 ADD filed_name int autoincrement;
#  可以指定添加到前面或者后面
ALTER TABLE t1 ADD field_name int autoincrement FIRST/AFTER; #  分别添加到第一个位置/最后位置。
#  删除字段
ALTER TABLE t1 DROP field_name;
# 修改字段
ALTER TABLE t1 MODIFY field_name int autocrement;
ALTER TABLE t1 CHANGE old_name new_name char(32);  #  如果后面的约束条件等没变，则只改了字段名
```

#### 删除表
```sql
DROP TABLE t1;

#  清空
DELETE FROM t1;  #  清空数据，但自增字段不会重新从1开始计数
TRUNCATE t1;  #  删除表，再新建表，自增字段重新开始计数
```

#### 复制表

```sql
CREATE TABLE new_t1 SELECT * FROM old_t1;  #  将旧表中的数据查询出来后交给新表

#  只复制表结构而不复制内容
CREATE TABLE new_t1 SELECT * FROM old_t1 where 1=2; #  因为条件永远不成立，所以查不到数据，只有表结构
```

####  外键关系
foreign key所在的表称为子表，与之关联的表可以称为父表

```sql
#  删除外键
ALTER TABLE t1 DROP foreign key foreign_key_name;

#  添加外键关系
ALTER TABLE t1 add foreign key(id) references t2(id);
#  创建表时添加外键关系
CREATE TABLE t1 (id int auto increatment constaraint fk_t1_publish foreign key(pid) references publish(id)
```

### 行操作
行操作主要就是我们通常说的增删改查


#### 增（插入）
```sql
INSERT INTO 表名(字段1,字段2,字段3…字段n) VALUES(值1,值2,值3…值n); #指定字段来插入数据，插入的值要和你前面的字段相匹配

INSERT INTO 表名 VALUES (值1,值2,值3…值n); #不指定字段的话，就按照默认的几个字段来插入数据

INSERT INTO 表名 VALUES
        (值1,值2,值3…值n),
        (值1,值2,值3…值n),
        (值1,值2,值3…值n);

INSERT INTO 表名(字段1,字段2,字段3…字段n) 
                    SELECT (字段1,字段2,字段3…字段n) FROM 表2
                    WHERE …;
```

#### 删

```sql
DELETE FROM 表名  WHERE CONITION; #删除符合条件的一些记录
```
#### 改（更新）

```sql
UPDATE 表名 SET 
        字段1=值1,  #注意语法，可以同时来修改多个值，用逗号分隔
        字段2=值2,
        WHERE CONDITION; #更改哪些数据，通过where条件来定位到符合条件的数据
```

