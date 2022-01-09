### MySQL

#### SQL语言介绍及分类
SQL结构化查询语言包括6部分：
DQL:data query language 数据查询语言
DMQ:data manipulation language 数据操作语言
TPL:  事务处理语言
DCL: data control language 数据控制语言：
DDL: data definition language 数据定义语言
CCL: cursor control language 指针控制语言

它们主要的动词如下：
DQL:
```
select, where, order by, group by, having
```
DMQ:
```
#操作表中数据
Update, insert, delete
```
TPL:
```
BEGIN,TRANSATION, COMMIT, ROLLBACK
```
DCL:
```
GRANT,REVOKE
```
DDL:
```
create, drop
```
CCL:
```
declare,cursor, fetch, into, update, where,current
```
总结：
DDL 数据定义语言（CREATE,ALTER,DROP)
DML 数据操作语言（SELECT,INSERT,DELETE,UPDATE)
DCL 数据控制语言 （GRANT,REVOKE,COMMIT, ROLLBACK)
查询是最常用的，分为单表查询，多表查询。


### 数据库常见管理应用

#### 创建数据库
命令：create database 数据库名   库名不能以数字开头

创建不同字符集格式的数据库命令：
charset == character set
```sql
create databse db1; 默认数据库配置， 相当于拉丁字符集数据库
create database db2 default charset gbk collate gbk_chinese_ci; 创建gbk字符庥数据库
create database db3 default charset utf8 collate utf8_general_ci; 创建gbk字符庥数据库
```

企业如何创建数据库：
```
#根据开发程序确定字符集（建议utf8)
#编译时指定字符集：
-DDEFAULT_CHARSET=utf8 \
-DDEFAULT_COLLATION=utf8_general_ci \
#这样创建库时使用默认即可
```

#### 显示数据库
```sql
show databases;
show databases lik '%flask%';

#当前数据库
select databse(); # 数据库
select user(); # 用户
select version(); #版本
select now(); #时间
```

#### 删除数据库
```
drop database test_db;
```

删除多余用户
```sql
drop user "username"@"host" # 注意要有引号，没有的部分用两个单引号代替即可
#如果drop删除不了，用下面的
delete from mysql.user where user='username' and host ='localhost';
flush privileges;
```

#### 创建用户并授权
```
CREATE USER 'ANDY'@'localhost' IDENTIFIED BY 'password';
GRANT ALL ON db1.* TO 'andy'@localhost';
GRANT SELECT ON db2.article TO 'andy'@'localhost';
GRANT USAGE ON *.* TO 'andy' WITH MAX_QUERIES_PER_HOUR 90;

#Grant命令相当于create, grant
Create User 'andy'@'localhost' Identified By 'password';
Grant All On db1.* To 'andy'@'localhost';
```
#### 查看权限 
```
Show Grants for 'andy'@'localhost';
#不进入mysql查看权限 的方法
mysql -uroot -ppassword -e"show grants for andy@localhost;"grep -i grant
```
#### 收回权限 
```
Revoke Insert On db.* From 'andy'@'localhost';
```

### 表

#### 查看有哪些表
```sql
show tables;
show tables like 'user';
show tables in db1;
```
#### 查看表结构
```sql
desc student;
show columns from student;
MariaDB [oldboy]> show columns from student;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| id    | int(4)      | NO   |     | NULL    |       |
| name  | char(20)    | NO   |     | NULL    |       |
| age   | tinyint(3)  | NO   |     | 0       |       |
| dept  | varchar(16) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
4 rows in set (0.00 sec)
```

#### 创建表
```mysql
MariaDB [oldboy]> 
create table student(
    -> id int(4) not null,
    -> name char(20) not null,
    -> age tinyint(3) not null default '0',
    -> dept varchar(16) default NULL);
Query OK, 0 rows affected (0.02 sec)
```
系统生成的语句
```sql
*************************** 1. row ***************************
       Table: student
Create Table: CREATE TABLE `student` (
  `id` int(4) NOT NULL,
  `name` char(20) NOT NULL,
  `age` tinyint(3) NOT NULL DEFAULT 0,
  `dept` varchar(16) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
1 row in set (0.00 sec)
```
##### 为表创建索引
```sql
create table student(
id int(4) not NULL AUTO_INCREMENT,
name char(20) not NULL,
age tinyint(3) not NULL default '0',
dept varchar(16) default NULL,
primary key(id),
Index index_name(name)
);
#PRI为主键索引，MUL为普通索引
MariaDB [oldboy]> desc student;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(4)   | NO   | PRI | NULL    | auto_increment |
| name  | char(20) | NO   | MUL | NULL    |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.00 sec)
```
###### 主键索引

添加主键索引
```sql
alter table student change id id int primary key auto_increment;
```

###### 普通索引
分为普通索引和唯一索引
```sql
create table student(
id int(4) not NULL AUTO_INCREMENT,
name char(20) not NULL,
age tinyint(3) not NULL default '0',
dept varchar(16) default NULL,
primary key(id),
Index index_name(name)
);
普通索引可以用Index,也可以用KEY来定义
```
添加普通索引：
```sql
alter table student add index index_name(name);
#create添加索引
create index index_name on student(name(8)); # 8指定对该字段前8个字符创建索引
```

查看索引的详细信息
```sql
MariaDB [oldboy]> show index from student \G;
*************************** 1. row ***************************
        Table: student
   Non_unique: 0
     Key_name: id
 Seq_in_index: 1
  Column_name: id
    Collation: A
  Cardinality: 0
     Sub_part: NULL
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
*************************** 2. row ***************************
        Table: student
   Non_unique: 1
     Key_name: index_name
 Seq_in_index: 1
  Column_name: name
    Collation: A
  Cardinality: 0
     Sub_part: 8
       Packed: NULL
         Null:
   Index_type: BTREE
      Comment:
Index_comment:
2 rows in set (0.01 sec)
```

###### 联合索引
创建联合索引时也可以指定每个字段的前多少个字符如：name(8),dept(5)
```sql
create index name_dept on student(name, dept);
```
联合索引存在最左前缀特性：
index(a,b,c) 仅a,ab,abc三个查询条件列可以走索引，b,bc,c不能命中索引

###### 唯一索引
```sql
create unique index uin_name on student(name);
MariaDB [oldboy]> create unique index uni_name on student(name);
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [oldboy]> desc student;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(4)   | NO   | PRI | NULL    | auto_increment |
| name  | char(20) | NO   | UNI | NULL    |                |
| dept  | char(20) | YES  |     | NULL    |                |
| t     | char(20) | NO   |     | NULL    |                |
+-------+----------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```
###### 添加索引总结

```sql
#w创建时添加索引
create table student(
id int(4) not NULL AUTO_INCREMENT,
name char(20) not NULL,
age tinyint(3) not NULL default '0',
dept varchar(16) default NULL,
primary key(id),
Index index_name(name)
);

#alter创建索引
alter table student add index index_name(name);

#create添加索引
create index index_name on student(name(8)); # 8指定对该字段前8个字符创建索引
```

##### 删除索引

删除主键索引
```sql
MariaDB [oldboy]> alter table student drop primary key;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0
#此时primary key已经删除了，但desc仍能看到PRI
MariaDB [oldboy]> desc student;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(4)   | NO   | PRI | NULL    | auto_increment |
| name  | char(20) | NO   | MUL | NULL    |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.00 sec)
```

删除普通索引
```sql
注意索引的名字是index_name,而不是写索引的字段name
alter table student drop index name;
MariaDB [oldboy]> alter table student drop index index_name;
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [oldboy]> desc student;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(4)   | NO   | PRI | NULL    | auto_increment |
| name  | char(20) | NO   |     | NULL    |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.00 sec)

#drop删除
drop index index_name on student;
```

删除唯一索引
```sql
MariaDB [oldboy]> drop index uni_name on student;
Query OK, 0 rows affected (0.00 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [oldboy]> desc student;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(4)   | NO   | PRI | NULL    | auto_increment |
| name  | char(20) | NO   | MUL | NULL    |                |
| dept  | char(20) | YES  |     | NULL    |                |
| t     | char(20) | NO   |     | NULL    |                |
+-------+----------+------+-----+---------+----------------+
4 rows in set (0.00 sec)
```

###### 删除索引总结
```sql
#alter删除索引
alter table student drop index name;

#drop删除索引
drop index uni_name on student;
```
问题:
需要在哪些列上创建索引？
select user,host from msyql.user where host=... 索引要创建在where 后的条件列上，而不是select后的选择数据列，尽量选择唯一值多的大表创建索引。

#### 修改表

rename修改表名
```sql
MariaDB [oldboy]> alter table test rename test1;
Query OK, 0 rows affected (0.00 sec)

MariaDB [oldboy]> show tables;
+------------------+
| Tables_in_oldboy |
+------------------+
| student          |
| t1               |
| test1            |
+------------------+
3 rows in set (0.00 sec)
```

向指定位置添加字段 after,first. after指定某列之后，first插入到最前面
```sql
MariaDB [oldboy]> alter table test add age int(4) after id;
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [oldboy]> desc test;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| age   | int(4)   | YES  |     | NULL    |                |
| name  | char(32) | NO   | MUL | NULL    |                |
+-------+----------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```
改变字段 
```sql
alter table test change age ages int(4) comment '年龄';
MariaDB [oldboy]> desc test;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| ages  | int(4)   | YES  |     | NULL    |                |
| name  | char(32) | NO   | MUL | NULL    |                |
+-------+----------+------+-----+---------+----------------+
3 rows in set (0.00 sec)

```

修改字段类型
```sql
alter table test modify column ages int(3) ;
MariaDB [oldboy]> alter table test modify column ages int(3) ;
Query OK, 0 rows affected (0.01 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [oldboy]> desc test;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| ages  | int(3)   | YES  |     | NULL    |                |
| name  | char(32) | NO   | MUL | NULL    |                |
+-------+----------+------+-----+---------+----------------+
3 rows in set (0.00 sec)
```


#### 查询数据

尽量不要使用*
```
MariaDB [oldboy]> select id,name from test;
+----+-------+
| id | name  |
+----+-------+
|  1 | jack  |
|  3 | mary  |
|  4 | david |
|  5 | lili  |
+----+-------+
4 rows in set (0.00 sec)
# 查询两条记录
MariaDB [oldboy]> select id,name from test limit 2;
+----+------+
| id | name |
+----+------+
|  1 | jack |
|  3 | mary |
+----+------+
2 rows in set (0.00 sec)

MariaDB [oldboy]> select id,name from test limit 0,2;
+----+------+
| id | name |
+----+------+
|  1 | jack |
|  3 | mary |
+----+------+
2 rows in set (0.00 sec)
```

条件查询,字符型的查询条件要带引号
```sql
select id,name from test where id =4;
MariaDB [oldboy]> select id,name from test where id =4;
+----+-------+
| id | name  |
+----+-------+
|  4 | david |
+----+-------+
1 row in set (0.00 sec)

select id,name from test where id>2 and id<5;
MariaDB [oldboy]> select id,name from test where id>2 and id<5;
+----+-------+
| id | name  |
+----+-------+
|  3 | mary  |
|  4 | david |
+----+-------+
2 rows in set (0.00 sec)
```

排序
```sql
select id,name from test order by name desc;
MariaDB [oldboy]> select id,name from test order by name desc;
+----+-------+
| id | name  |
+----+-------+
|  3 | mary  |
|  5 | lili  |
|  1 | jack  |
|  4 | david |
+----+-------+
```

##### 是否命中索引
通过explain查看查询的过程是否使用索引
```sql
#未添加索引查询
MariaDB [oldboy]> explain select id,name from test where name = 'andy'\G;
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: test
         type: ALL
possible_keys: NULL
          key: NULL
      key_len: NULL
          ref: NULL
         rows: 4
        Extra: Using where
1 row in set (0.00 sec)
#添加索引后
MariaDB [oldboy]> create index index_name on test(name);
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB [oldboy]> desc test;
+-------+----------+------+-----+---------+----------------+
| Field | Type     | Null | Key | Default | Extra          |
+-------+----------+------+-----+---------+----------------+
| id    | int(11)  | NO   | PRI | NULL    | auto_increment |
| name  | char(32) | NO   | MUL | NULL    |                |
+-------+----------+------+-----+---------+----------------+
2 rows in set (0.01 sec)
#再次查询 
explain select id,name from test where name = 'andy' \G;
MariaDB [oldboy]> explain select id,name from test where name = 'andy' \G;
*************************** 1. row ***************************
           id: 1
  select_type: SIMPLE
        table: test
         type: ref
possible_keys: index_name
          key: index_name
      key_len: 32
          ref: const
         rows: 1
        Extra: Using where; Using index
1 row in set (0.00 sec)
```
#### 插入数据

```sql
create table test(id int primary key auto_increment, name char(32) not NULL);

insert into test(id,name) values(1,'andy');
insert into test(name) values('jack'); #id 自增
insert into test values(3, 'mary'); # 省略字段名，必须按列的顺序插入
insert into test values(4,'david'),(5,'lili'); # 批量插入提高效率
#备份数据，mysqldump以sql语句的形式导出，称为逻辑备份
mysqldump -uroot -p -B oldboy > /opt/oldboy_bak.sql
```
#### 修改数据

```sql
MariaDB [oldboy]> select * from test;
+----+-------+
| id | name  |
+----+-------+
|  4 | david |
|  1 | jack  |
|  5 | lili  |
|  3 | mary  |
+----+-------+
4 rows in set (0.00 sec)

MariaDB [oldboy]> update test set name ='Amy' where id =5;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [oldboy]> select id,name from test;
+----+-------+
| id | name  |
+----+-------+
|  5 | Amy   |
|  4 | david |
|  1 | jack  |
|  3 | mary  |
+----+-------+
4 rows in set (0.00 sec)
```


#### 删除数据

```sql
delete from test where id=3;
#清空表
truncate tablename

truncate table test和delete from test区别：
truncate table test 更快，清空物理文件
delete from test 逻辑清除，按行删除
```


#### 数据备份与恢复
#如果没有指定修改的数据会将整个表都修改，
```sql
#恢复备份
mysql -uroot -p oldboy </opt/oldboy_bak.sql 
#也可以用source恢复

#增量备份binlog
在my.cnf中打开bin log记录
mysqlbinlog /opt/mysqlbin_oldboy.00001 # 查看binlog
msyqladmin -uroot -p flush-log # 切割日志
mysqlbinlog mysqlbin_oldboy.00001 > bin.sql
mysql -uroot -p oldboy <bin.sql
```
#### 防止误操作的技巧
```sql
#在mysql命令加上选项-U后，当发出没有WHERE或LIMIT关键字的UPDATE或DELETE时，mysql程序就会拒绝执行

alias mysql="mysql -U"

MariaDB [oldboy]> update test set name ='andy';
ERROR 1175 (HY000): You are using safe update mode and you tried to update a table without a WHERE that uses a KEY column
```

#### 视图

```
MariaDB [oldboy]> select id,name from test;
+----+--------------+
| id | name         |
+----+--------------+
|  5 | Amy          |
|  6 | dad          |
|  4 | david        |
|  1 | jack         |
|  2 | å‘¨â€        |
+----+--------------+
5 rows in set (0.01 sec)
```

##### 创建视图
```mysql
create view test_view as select id,age,name from test;
select * from test_view;
MariaDB [oldboy]> select * from test_view;
+----+------+--------------+
| id | age  | name         |
+----+------+--------------+
|  1 | NULL | jack         |
|  2 |   18 | å‘¨â€        |
|  4 | NULL | david        |
|  5 | NULL | Amy          |
|  6 |   18 | dad          |
+----+------+--------------+
5 rows in set (0.00 sec)

#指定视图的字段名
create view test2_view(id,ag,na) as select id, age, name from test;
MariaDB [oldboy]> select * from test2_view;
+----+------+--------------+
| id | ag   | na           |
+----+------+--------------+
|  1 | NULL | jack         |
|  2 |   18 | å‘¨â€        |
|  4 | NULL | david        |
|  5 | NULL | Amy          |
|  6 |   18 | dad          |
+----+------+--------------+
5 rows in set (0.00 sec)
```
视图只是查询语句，当数据库数据改变时，视图查询出来的数据也会跟着改变
下面将test表中id=2的的乱码数据更改，可以看到更改数据后，视图查出来的数据也改变了
```mysql
MariaDB [oldboy]> update test set name = 'mary' where id=2;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [oldboy]> select id,name from test where id=2;
+----+------+
| id | name |
+----+------+
|  2 | mary |
+----+------+
1 row in set (0.00 sec)

MariaDB [oldboy]> select * from test_view;
+----+------+-------+
| id | age  | name  |
+----+------+-------+
|  1 | NULL | jack  |
|  2 |   18 | mary  |
|  4 | NULL | david |
|  5 | NULL | Amy   |
|  6 |   18 | dad   |
+----+------+-------+
5 rows in set (0.00 sec)
```
总结： 创建视图主要通过： create view 视图名 As 查询语句来实现
##### 查看视图
```mysql
desc test_view;
MariaDB [oldboy]> desc test_view;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| id    | int(11)  | NO   |     | 0       |       |
| age   | int(4)   | YES  |     | NULL    |       |
| name  | char(32) | NO   |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
3 rows in set (0.00 sec)

#show table status like "test_view" \G;
MariaDB [oldboy]> show table status like "test_view" \G;
*************************** 1. row ***************************
           Name: test_view
         Engine: NULL
        Version: NULL
     Row_format: NULL
           Rows: NULL
 Avg_row_length: NULL
    Data_length: NULL
Max_data_length: NULL
   Index_length: NULL
      Data_free: NULL
 Auto_increment: NULL
    Create_time: NULL
    Update_time: NULL
     Check_time: NULL
      Collation: NULL
       Checksum: NULL
 Create_options: NULL
        Comment: VIEW
1 row in set (0.00 sec)
#可以看到上面的Comment值为View，说明它是一个视图，而其它信息为NULL,说明它是一个虚表，下面看看test表，比较下不同
MariaDB [oldboy]> show table status like 'test' \G;
*************************** 1. row ***************************
           Name: test
         Engine: InnoDB
        Version: 10
     Row_format: Dynamic
           Rows: 3
 Avg_row_length: 5461
    Data_length: 16384
Max_data_length: 0
   Index_length: 16384
      Data_free: 0
 Auto_increment: 7
    Create_time: 2020-03-26 11:19:40
    Update_time: 2020-03-26 17:22:16
     Check_time: NULL
      Collation: latin1_swedish_ci
       Checksum: NULL
 Create_options:
        Comment:
1 row in set (0.00 sec)

# show create view test_view \G;
MariaDB [oldboy]> show create view test_view \G;
*************************** 1. row ***************************
                View: test_view
         Create View: CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`%` SQL SECURITY DEFINER VIEW `test_view` AS select `test`.`id` AS `id`,`test`.`age` AS `age`,`test`.`name` AS `name` from `test`
character_set_client: utf8
collation_connection: utf8_general_ci
1 row in set (0.00 sec)

#查看所有的视图的信息
MariaDB [oldboy]> select * from information_schema.views \G
*************************** 1. row ***************************
       TABLE_CATALOG: def
        TABLE_SCHEMA: oldboy
          TABLE_NAME: test2_view
     VIEW_DEFINITION: select `oldboy`.`test`.`id` AS `id`,`oldboy`.`test`.`age` AS `ag`,`oldboy`.`test`.`name` AS `na` from `oldboy`.`test`
        CHECK_OPTION: NONE
        IS_UPDATABLE: YES
             DEFINER: root@%
       SECURITY_TYPE: DEFINER
CHARACTER_SET_CLIENT: utf8
COLLATION_CONNECTION: utf8_general_ci
           ALGORITHM: UNDEFINED
*************************** 2. row ***************************
       TABLE_CATALOG: def
        TABLE_SCHEMA: oldboy
          TABLE_NAME: test_view
     VIEW_DEFINITION: select `oldboy`.`test`.`id` AS `id`,`oldboy`.`test`.`age` AS `age`,`oldboy`.`test`.`name` AS `name` from `oldboy`.`test`
        CHECK_OPTION: NONE
        IS_UPDATABLE: YES
             DEFINER: root@%
       SECURITY_TYPE: DEFINER
CHARACTER_SET_CLIENT: utf8
COLLATION_CONNECTION: utf8_general_ci
           ALGORITHM: UNDEFINED
2 rows in set (0.02 sec)
```
总结 ：
查看视图有三种方式：
* desc 视图名;
* show table status like "视图名";
* show create view 视图名;

##### 修改视图
```mysql
alter view test_view as select id, name from test;
MariaDB [oldboy]> alter view test_view as select id, name from test;
Query OK, 0 rows affected (0.01 sec)

MariaDB [oldboy]> select * from test_view;
+----+-------+
| id | name  |
+----+-------+
|  5 | Amy   |
|  6 | dad   |
|  4 | david |
|  1 | jack  |
|  2 | mary  |
+----+-------+
5 rows in set (0.00 sec)

# create or replace 
create or replace view test_view as select id, age, name from test;
MariaDB [oldboy]> create or replace view test_view as select id, age, name from test;
Query OK, 0 rows affected (0.00 sec)

MariaDB [oldboy]> select * from test_view;
+----+------+-------+
| id | age  | name  |
+----+------+-------+
|  1 | NULL | jack  |
|  2 |   18 | mary  |
|  4 | NULL | david |
|  5 | NULL | Amy   |
|  6 |   18 | dad   |
+----+------+-------+
5 rows in set (0.00 sec)
```
##### 更新视图
更新视图是指通过视图来插入（Insert）、更新（Update）和删除（Delete）表中的数据。因为视图是一个虚拟表，其中没有数据。通过视图更新时，都是转换到基本表来更新
```mysql
# 先查看视图信息
MariaDB [oldboy]> select * from test_view;
+----+------+-------+
| id | age  | name  |
+----+------+-------+
|  1 | NULL | jack  |
|  2 |   18 | mary  |
|  4 | NULL | david |
|  5 | NULL | Amy   |
|  6 |   18 | dad   |
+----+------+-------+
5 rows in set (0.01 sec)
#更新
update test_view set age =20 where id=1;
MariaDB [oldboy]> update test_view set age =20 where id=1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

MariaDB [oldboy]> select * from test_view;
+----+------+-------+
| id | age  | name  |
+----+------+-------+
|  1 |   20 | jack  |
|  2 |   18 | mary  |
|  4 | NULL | david |
|  5 | NULL | Amy   |
|  6 |   18 | dad   |
+----+------+-------+
5 rows in set (0.00 sec)

#此时查看原表，可以看到原表数据也更改了，当视图中包含多张表时这非常危险
MariaDB [oldboy]> select * from test;
+----+------+-------+
| id | age  | name  |
+----+------+-------+
|  1 |   20 | jack  |
|  2 |   18 | mary  |
|  4 | NULL | david |
|  5 | NULL | Amy   |
|  6 |   18 | dad   |
+----+------+-------+
5 rows in set (0.00 sec)

#insert 
insert into test_view values(3,21,'Amyli');
MariaDB [oldboy]> insert into test_view values(3,21,'Amyli');
Query OK, 1 row affected (0.01 sec)

MariaDB [oldboy]> select * from test_view;
+----+------+-------+
| id | age  | name  |
+----+------+-------+
|  1 |   20 | jack  |
|  2 |   18 | mary  |
|  3 |   21 | Amyli |
|  4 | NULL | david |
|  5 | NULL | Amy   |
|  6 |   18 | dad   |
+----+------+-------+
6 rows in set (0.00 sec)

#delete
delete from test_view where id=4;
MariaDB [oldboy]> delete from test_view where id=4;
Query OK, 1 row affected (0.01 sec)

MariaDB [oldboy]> select * from test_view;
+----+------+-------+
| id | age  | name  |
+----+------+-------+
|  1 |   20 | jack  |
|  2 |   18 | mary  |
|  3 |   21 | Amyli |
|  5 | NULL | Amy   |
|  6 |   18 | dad   |
+----+------+-------+
5 rows in set (0.00 sec)
```
注意：下面这些情况下视图是不可更新的
 聚合函数；
 DISTINCT 关键字；
 GROUP BY 子句；
 ORDER BY 子句；
 HAVING 子句；
 UNION 运算符；
 位于选择列表中的子查询；
 FROM 子句中包含多个表；
 SELECT 语句中引用了不可更新视图；
 WHERE 子句中的子查询，引用FROM 子句中的表；

总结 ：
视图更新主要有：删除时有from关键字
* update test_view set age =20 where id=1;
* insert into test_view values(3,21,'Amyli');
* delete from test_view where id=4;

##### 删除视图
```mysql
drop view test_view2;
MariaDB [oldboy]> drop view test2_view;
Query OK, 0 rows affected (0.00 sec)
drop view if exist test_view; # 如果存在的话删除
MariaDB [oldboy]> drop view if exists test2_view;
Query OK, 0 rows affected, 1 warning (0.00 sec)
```

#### 存储过程

##### 创建存储过程
每个参数有三部分组成：输入输出类型，参数名称，参数类型
```mysql
create procedure procedure_name;
in 输入参数
out 输出参数
inout 输入/输出
DECLARE 过程体中声明变量，只能在begin,end之间声明，且在开始就声明，即声明再使用
set 赋值 也可以用select into,select name into name from test where id =2; name 需要先定义

delimeter 设置结束符，默认为;
delimiter ##
CREATE PROCEDURE del_pro(IN t_id INT)
BEGIN
    DELETE FROM test WHERE id = t_id;
END ##
delimiter ;

delimiter ##
create procedure age_from_test(in name char(4),out ages int)
begin
  select age into ages
  from test
  where name = name;
end ##
delimiter ;
```
查看：
```mysql
MariaDB [oldboy]> show procedure status \G
*************************** 1. row ***************************
                  Db: mysql
                Name: AddGeometryColumn
                Type: PROCEDURE
             Definer: root@localhost
            Modified: 2019-12-19 11:20:15
             Created: 2019-12-19 11:20:15
       Security_type: INVOKER
             Comment:
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
*************************** 2. row ***************************
                  Db: mysql
                Name: DropGeometryColumn
                Type: PROCEDURE
             Definer: root@localhost
            Modified: 2019-12-19 11:20:15
             Created: 2019-12-19 11:20:15
       Security_type: INVOKER
             Comment:
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
*************************** 3. row ***************************
                  Db: oldboy
                Name: del_pro
                Type: PROCEDURE
             Definer: root@%
            Modified: 2020-03-26 21:10:45
             Created: 2020-03-26 21:10:45
       Security_type: DEFINER
             Comment:
character_set_client: utf8mb4
collation_connection: utf8mb4_general_ci
  Database Collation: latin1_swedish_ci
3 rows in set (0.00 sec)
```

带参数存储过程
```mysql
delimiter //
create procedure get_count(out ct int)
begin
 select count(1) into ct from test;
end //
delimiter ;

MariaDB [oldboy]> delimiter ;
MariaDB [oldboy]> call get_count(@ct);
Query OK, 1 row affected (0.00 sec)

MariaDB [oldboy]> select @ct;
+------+
| @ct  |
+------+
|    5 |
+------+
1 row in set (0.00 sec)

delimiter //
create procedure get_age(in id int, out _age int)
begin
  select age into _age
  from test
  where id = id;
end //
delimiter ;

delimiter //
create procedure get_age(in _id int, out _age int)
begin
  select age into _age
  from test
  where id = _id;
end //
delimiter ;

@ 注意参数名不能与列名相同，否则查不到数据
MariaDB [oldboy]> delimiter ;
MariaDB [oldboy]> call get_age(6,@_age);
Query OK, 1 row affected (0.00 sec)

MariaDB [oldboy]> select @_age;
+-------+
| @_age |
+-------+
|    18 |
+-------+
1 row in set (0.00 sec)
```

在执行上面的存储过程中出现 两个错误：
```
MariaDB [oldboy]> call get_age(1,_age);
ERROR 1414 (42000): OUT or INOUT argument 2 for routine oldboy.get_age is not a variable or NEW pseudo-variable in BEFORE trigger
#错误原因是调用的参数_age 前面没有加@
```

```
MariaDB [oldboy]> call get_age(1,@_age);
ERROR 1172 (42000): Result consisted of more than one row
错误原因，存储过程中的where id = id; 参数名与列名相同 修改为where id = _id正常
```

###### 流程控制 if

```mysql
delimiter //
create procedure check_age(in _id int, out is_adult int)
begin
  declare _age int;
  select age into _age
  from test
  where id = _id;
  if _age >18 then
    set is_adult=1;
  elseif _age < 18 then
    set is_adult =0;
   else
     set is_adult =1;
   end if;
end //
delimiter ;

MariaDB [oldboy]> delimiter ;
MariaDB [oldboy]> call check_age(1,@is_adult);
Query OK, 1 row affected (0.00 sec)

MariaDB [oldboy]> select @is_adult;
+-----------+
| @is_adult |
+-----------+
|         1 |
+-----------+
1 row in set (0.00 sec)
#这里is_adult=1表示是成年，但上面的存储过程有个bug, else中的 is_adult=1,导致除了小于18的都返回1，另外declare 语句要在begin,end之间，且要加上分号（；）否则会报语法错误
```

###### 流程控制 case
```mysql
delimiter //
create procedure get_gender_count(in _gender char(6), out gender_count int)
begin
  case _gender
    when 'male' then select count(name) into gender_count 
      from test where gender='male';
    when 'female' then select count(name) into gender_count 
      from test where gender='female';
    else select count(1) into gender_count from test;
  end case;
end //
delimiter ;

MariaDB [oldboy]> call get_gender_count('female',@gender_count);
Query OK, 1 row affected (0.00 sec)

MariaDB [oldboy]> select @gender_count;
+---------------+
| @gender_count |
+---------------+
|             3 |
+---------------+
1 row in set (0.00 sec)

MariaDB [oldboy]> call get_gender_count('male',@gender_count);
Query OK, 1 row affected (0.00 sec)

MariaDB [oldboy]> select @gender_count;
+---------------+
| @gender_count |
+---------------+
|             2 |
+---------------+
1 row in set (0.00 sec)

MariaDB [oldboy]> call get_gender_count('fm',@gender_count);
Query OK, 1 row affected (0.00 sec)

MariaDB [oldboy]> select @gender_count;
+---------------+
| @gender_count |
+---------------+
|             5 |
+---------------+
1 row in set (0.00 sec)
```
###### 循环语句 while
```mysql
delimiter //
create procedure dowhile(inout v int)
begin
  while @v >0 do
      set @v = @v-1;
  end while;
end //
delimiter ;
```
这里有个问题，这种情况怎么传参数进去呢?call dowhile(4)语法报错，而且不知道怎么获取存储过程的值，此坑待填。

###### 循环语句loop
label是标志，可以省略不写
leave 跳出循环
```mysql
delimiter //
create procedure doloop()
begin
    set @a =10
    lable:loop
    set @a = @-1;
    if @a<0 then
    leave label;
    end if;
    end loop label;
end //
delimiter ;
```
###### 循环语句 while
```mysql
delimiter //
create procedure dorepeat()
begin
  repeat
  v = v-1
  until v <1
  end repeat;
end //
delimiter ;
```
###### 再次循环iterate
```mysql
delimiter //
create procedure doiterate()
begin
    declare p int default 0;
    my_loop: Loop
        set p = p +1;
        if p<10 then iterate my_loop;
        elseif p >20 then leave my_loop;
        end if;
        select 'p is between 10 and 20';
    end loop my_loop;
end//
delimiter ;

#执行后会多次打印下面的内容
MariaDB [oldboy]> call doiterate();
+------------------------+
| p is between 10 and 20 |
+------------------------+
| p is between 10 and 20 |
+------------------------+
1 row in set (0.00 sec)
```

##### 修改存储过程
```mysql
delimite //
CREATE PROCEDURE num_from_student(IN _birth DATE,OUT count_num INT)
READS SQL DATA
BEGIN
    SELECT COUNT(*) INTO count_num
    FROM student
    WHERE sbirthday=_birth;
END//
delimiter ;

alter procedure dowhnum_from_studentile
modifiles sql data  # 将读写权限修改为modifiels sql data, 并指名调用者可以执行
sql security inviker;
```

##### 删除存储过程
```mysql
drop procedure if exists age_from_test;
MariaDB [oldboy]> drop procedure if exists age_from_test;
Query OK, 0 rows affected (0.00 sec)
```

在说到存储函数前， 查看存储过程或者存储函数都可以通过show procedure  status like 'get_name' ;

#### 存储函数
存储过程中的语句在存储函数中都可以用，但不能指定in,out,inout,且必须有返回return,当return语句中包含select时，返回结果只能有一行

##### 创建存储函数
```mysql
delimiter //
create function get_name(_id int)
returns char(6)
begin
    return (select name from test where id=_id);
end//
delimiter ;

# 当添加in,out 等关键字时会报错，但mysql5.7从入门到精通书里竟然可以加，我实践后报错，然后help create function udf 提示的也没有这个参数。
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'in _id int)
```

##### 调用存储函数
```mysql
select get_name(1);

MariaDB [oldboy]> select get_name(1);
+-------------+
| get_name(1) |
+-------------+
| jack        |
+-------------+
1 row in set (0.00 sec)
```

##### 查看存储函数
```mysql
MariaDB [oldboy]> show function status like 'get_name' \G
*************************** 1. row ***************************
                  Db: oldboy
                Name: get_name
                Type: FUNCTION
             Definer: root@%
            Modified: 2020-03-27 17:40:12
             Created: 2020-03-27 17:40:12
       Security_type: DEFINER
             Comment:
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
1 row in set (0.00 sec)
```

##### 修改存储函数
```mysql
alter function get_name from oldboy
reads sql data
comment  'get name';
```

##### 删除存储函数
```mysql
drop function function_name;
```

#### 触发器
触发器可以理解为一种回调。主要关键词有insert, update,delete，before, after等

##### 创建触发器
```mysql
create trigger aft_insert_data after insert
   on test for each row set @msg='insert one row data';
```
执行过程
```mysql
MariaDB [oldboy]> create trigger aft_insert_data after insert
    ->    on test for each row set @msg='insert one row data';
Query OK, 0 rows affected (0.01 sec)

MariaDB [oldboy]> select @msg;
+------+
| @msg |
+------+
| NULL |
+------+
1 row in set (0.00 sec)
# 插入数据
MariaDB [oldboy]> insert into test values(7,30,'saul', 'male');
Query OK, 1 row affected (0.01 sec)

MariaDB [oldboy]> select @msg;
+---------------------+
| @msg                |
+---------------------+
| insert one row data |
+---------------------+
1 row in set (0.00 sec)
```

##### 查看触发器
```mysql
MariaDB [oldboy]> show triggers \G
*************************** 1. row ***************************
             Trigger: aft_insert_data
               Event: INSERT
               Table: test
           Statement: set @msg='insert one row data'
              Timing: AFTER
             Created: 2020-03-27 17:50:50.86
            sql_mode: STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
             Definer: root@%
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
1 row in set (0.00 sec)

#第二种方式
MariaDB [oldboy]> select * from information_schema.triggers where trigger_name='aft_insert_data' \G
*************************** 1. row ***************************
           TRIGGER_CATALOG: def
            TRIGGER_SCHEMA: oldboy
              TRIGGER_NAME: aft_insert_data
        EVENT_MANIPULATION: INSERT
      EVENT_OBJECT_CATALOG: def
       EVENT_OBJECT_SCHEMA: oldboy
        EVENT_OBJECT_TABLE: test
              ACTION_ORDER: 1
          ACTION_CONDITION: NULL
          ACTION_STATEMENT: set @msg='insert one row data'
        ACTION_ORIENTATION: ROW
             ACTION_TIMING: AFTER
ACTION_REFERENCE_OLD_TABLE: NULL
ACTION_REFERENCE_NEW_TABLE: NULL
  ACTION_REFERENCE_OLD_ROW: OLD
  ACTION_REFERENCE_NEW_ROW: NEW
                   CREATED: 2020-03-27 17:50:50.86
                  SQL_MODE: STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
                   DEFINER: root@%
      CHARACTER_SET_CLIENT: utf8
      COLLATION_CONNECTION: utf8_general_ci
        DATABASE_COLLATION: latin1_swedish_ci
1 row in set (0.01 sec)
```

##### 删除触发器
database_name.trigger_name
```mysql
drop trigger oldboy.aft_insert_data;
```

#### 防止乱码

思想：linux, client, server database, table 字符集一致
```sql
MariaDB [oldboy]> show create table test \G;
*************************** 1. row ***************************
       Table: test
Create Table: CREATE TABLE `test` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `age` int(4) DEFAULT NULL,
  `name` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `index_name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1
1 row in set (0.00 sec)
```
字符 集为latin1

方法一：
```mysql
msyql>set names latin1;
```

方法二：
```mysql
vim test.sql
set names latin1;
Insert into test values(1,18,'andy');
mysql> source test.sql
```
方法三：
在sql文件中指定set names latin1;然后通过mysql 命令导入数据
```mysql
mysql> mysql -uroot -p oldboy < test.sql;
```

方法四：
```mysql
mysql> mysql -uroot -p --default-character-set=latin1 oldboy<test.sql;
```

方法五：
```mysql
[client]
default-charcter-set-latin1
# 无需重启服务，退出重新登陆就生效，相当于set names latin1;

或者修改my.cnf
[mysqld]
default-character-set=latin1 # 5.1以前版本
character-set-server=latin1 #5.5
```

创建表时指定：

```mysql
# show charset;  # 查看
create database oldboy default charset utf8 collate utf8_general_ci;

MariaDB [oldboy]> show variables like "character_set%";
+--------------------------+----------------------------+
| Variable_name            | Value                      |
+--------------------------+----------------------------+
| character_set_client     | latin1                     |
| character_set_connection | latin1                     |
| character_set_database   | latin1                     |
| character_set_filesystem | binary                     |
| character_set_results    | latin1                     |
| character_set_server     | latin1                     |
| character_set_system     | utf8                       |
| character_sets_dir       | /usr/share/mysql/charsets/ |
+--------------------------+----------------------------+
8 rows in set (0.00 sec)

```

##### ubuntu maridb 设置utf8

```mysql
# 编辑/etc/my.cnf
vim /etc/my.cnf
# 如果里面没有内容查看 includedir

#server
# 在[mysqld]标签下添加下面内容
default-storage-engine = innodb
innodb_file_per_table
max_connections = 4096
collation-server = utf8_general_ci
character-set-server = utf8

# 编辑/etc/my.cnf.d/client.cnf
vim /etc/my.cnf.d/client.cnf
# 在[client]标签下添加下面内容
default-character-set=utf8

# 编辑/etc/my.cnf.d/mysql-clients.cnf
vim /etc/my.cnf.d/mysql-clients.cnf
# 在[mysql]标签下添加下面内容
default-character-set=utf8
# 重启mysql
#查看修改是否生效
SHOW VARIABLES LIKE 'character%
```