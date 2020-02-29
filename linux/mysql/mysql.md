# mysql

## 设置

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


## MySQL库和表的操作

### 库操作

#### 创建库

```sql
CREATE DATABASE 数据库名 charset utf8;

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

