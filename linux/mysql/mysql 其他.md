## 视图

视图是一个虚拟表（非真实存在），是存在于内存中的表。可以通过django中的视图来帮助理解，它是查询出来 的一个结果，并非真实存在于数据库中。

视图有什么优缺点？为什么用视图
>视图可以把查询过程中的临时表保存下来，这样以后再想操作该临时表的数据时就无需重写复杂的sql了，直接去视图中查找即可。
但视图有明显地效率问题，并且视图是存放在数据库中的，如果我们程序中使用的sql过分依赖数据库中的视图，即强耦合，那就意味着扩展sql极为不便，因此并不推荐使用


### 创建视图

```sql
create view emp_view as select name from employee;

# 查看视图；
MariaDB [learn]> show tables;
+-----------------+
| Tables_in_learn |
+-----------------+
| emp_view        |
| employee        |
+-----------------+
2 rows in set (0.00 sec)
MariaDB [learn]> desc emp_view;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| name  | varchar(20) | NO   |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
```
#注意：
>开发方便，但效率低下
>使用不便，保存在数据库中，如果sql中修改了关于视图的部分，慢则需要修改数据库中的视图
>如果修改了视图，导致其它相关的表都被修改。

### 使用视图

```sql
select * from course_view;
update course_view set cname='xxx'; #更新视图中的数据
insert into course_view values(5,'yyy',2); #往视图中插入数据
```

### 修改视图
语法：ALTER VIEW 视图名称 AS SQL语句（类似于先删除，再创建）
```sql
alter view teacher_view as select * from course where cid>3;
```

### 删除视图
```sql
drop view emp_view;
```

## 触发器
触发器类似于python中的回调函数

### 创建触发器
```sql
CREATE TRIGGER tri_before_insert_tb1 BEFORE INSERT ON tb1 FOR EACH ROW;
#begin和end里面写触发器要做的sql事情，注意里面的代码缩进，并且给触发器起名字的时候，名字的格式最好这样写，有表示意义，一看名字就知道要做什么，是给哪个表设置的触发器
BEGIN 
    ...
END

# 插入后
CREATE TRIGGER tri_after_insert_tb1 AFTER INSERT ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除前
CREATE TRIGGER tri_before_delete_tb1 BEFORE DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 删除后
CREATE TRIGGER tri_after_delete_tb1 AFTER DELETE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新前
CREATE TRIGGER tri_before_update_tb1 BEFORE UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END

# 更新后
CREATE TRIGGER tri_after_update_tb1 AFTER UPDATE ON tb1 FOR EACH ROW
BEGIN
    ...
END
```
### 实例
```sql
CREATE TABLE cmd (  #这是一张指令信息表，你在系统里面执行的任何的系统命令都在表里面写一条记录
    id INT PRIMARY KEY auto_increment,  #id
    USER CHAR (32),  #用户
    priv CHAR (10),  #权限          
    cmd CHAR (64),   #指令
    sub_time datetime, #提交时间  
    success enum ('yes', 'no') #是否执行成功，0代表执行失败
);

CREATE TABLE errlog ( #指令执行错误的信息统计表，专门提取上面cmd表的错误记录
    id INT PRIMARY KEY auto_increment, #id
    err_cmd CHAR (64),  #错误指令
    err_time datetime   #错误命令的提交时间
);
#现在的需求是：不管正确或者错误的cmd，都需要往cmd表里面插入，然后，如果是错误的记录，还需要往errlog表里面插入一条记录
#若果没有触发器，我们会怎么实现，我们可以通过咱们的应用程序来做，根据cmd表里面的success这个字段是哪个值（yes成功，no表示失败），在给cmd插入记录的时候，判断一下这个值是yes或者no，来判断一下成功或者失败，如果失败了，直接给errlog来插入一条记录
#但是mysql说，你的应用程序可以省事儿了，你只需要往cmd表里面插入数据就行了，没必要你自己来判断了，可以使用触发器来实现，可以判断你插入的这条记录的success这个字段对应的值，然后自动来触发触发器，进行errlog表的数据插入

#创建触发器
delimiter //      （或者写$$，其他符号也行，但是不要写mysql不能认识的，知道一下就行了），delimiter 是告诉mysql，遇到这句话的时候，就将sql语句的结束符分号改成delimiter后面的//
CREATE TRIGGER tri_after_insert_cmd AFTER INSERT ON cmd FOR EACH ROW #在你cmd表插入一条记录之后触发的。
BEGIN   #每次给cmd插入一条记录的时候，都会被mysql封装成一个对象，叫做NEW，里面的字段都是这个NEW的属性
    IF NEW.success = 'no' THEN           #mysql里面是可以写这种判断的，等值判断只有一个等号，然后写then
            INSERT INTO errlog(err_cmd, err_time) VALUES(NEW.cmd, NEW.sub_time) ;     #必须加分号，并且注意，我们必须用delimiter来包裹，不然，mysql一看到分号，就认为你的sql结束了，所以会报错
      END IF ;       #然后写end if，必须加分号
END//      #只有遇到//这个完成的sql才算结束
delimiter ; 
```

### 使用触发器
触发器无法由用户直接调用，而由对表的【增/删/改】操作被动引发的。

### 删除触发器
```sql
drop trigger tri_after_insert_cmd;
```

## 事务
什么哪事务？
就是原子性操作，要么全部成功，要么全部失败。

```sql
#原子操作
start transaction;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='chao'; #中介拿走10元
update user set balance=1090 where name='ysb'; #卖家拿到90元
commit;  #只要不进行commit操作，就没有保存下来，没有刷到硬盘上

#出现异常，回滚到初始状态
start transaction;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='chao'; #中介拿走10元
uppdate user set balance=1090 where name='ysb'; #卖家拿到90元,出现异常没有拿到
rollback;  #如果上面三个sql语句出现了异常，就直接rollback，数据就直接回到原来的状态了。但是执行了commit之后，rollback这个操作就没法回滚了
#我们要做的是检测这几个sql语句是否异常，没有异常直接commit，有异常就rollback，但是现在单纯的只是开启了事务，但是还没有说如何检测异常，我们先来一个存储过程来捕获异常，等我们学了存储过程，再细说存储过程。
commit;
```

#通过存储过程来捕获异常：(写存储过程的是，注意每一行都不要缩进！！！！)
```sql
delimiter //
create PROCEDURE p5()
BEGIN
DECLARE exit handler for sqlexception
BEGIN
rollback;
END;

START TRANSACTION;
update user set balance=900 where name='wsb'; #买支付100元
update user set balance=1010 where name='chao'; #中介拿走10元
#update user2 set balance=1090 where name='ysb'; #卖家拿到90元
update user set balance=1090 where name='ysb'; #卖家拿到90元
COMMIT;

END //
delimiter ;
```


## 存储过程

存储过程包含了一系列可执行的sql语句，存储过程存放于MySQL中，通过调用它的名字可以执行其内部的一堆sql。

存储过程有哪些优点？缺点
>用于替代程序写的SQL语句，实现程序与sql解耦
>基于网络传输，传别名的数据量小，而直接传sql数据量大
>缺点是程序员扩展功能不方便

程序与数据库结合的使得方式：
> #方式一：
>MySQL：存储过程
    程序：调用存储过程

> 方式二：
    MySQL：
    程序：纯SQL语句

> 方式三：
    MySQL:
 >   程序：类和对象，即ORM（本质还是纯SQL语句）

### 创建存储过程

```sql
delimiter //
create procedure p1()
BEGIN
    select * from blog;
    INSERT into blog(name,sub_time) values("xxx",now());
END //
delimiter ;

#在mysql中调用
call p1(); #类似于MySQL的函数，但不是函数昂，别搞混了，MySQL的函数(count()\max()\min()等等)都是放在sql语句里面用的，不能单独的使用，存储过程是可以直接调用的  call 名字+括号;
#MySQL的视图啊触发器啊if判断啊等等都能在存储过程里面写，这是一大堆的sql的集合体，都可以综合到这里面
#在python中基于pymysql调用
cursor.callproc('p1') 
print(cursor.fetchall())
```


### 执行存储过程
```sql
-- 无参数
call proc_name()

-- 有参数，全in
call proc_name(1,2)

-- 有参数，有in，out，inout
set @t1=0;
set @t2=3;
call proc_name(1,2,@t1,@t2)
```

### 删除存储过程
```sql
drop procedure proc_name;
```

## 什么是索引
存储引擎用于快速找到记录的一种数据结构。

索引的本质是：通过不断地缩小想要获取数据的范围来筛选出最终想要的结果，同时把随机的事件变成顺序的事件，也就是说，有了这种索引机制，我们可以总是用同一种查找方式来锁定数据。

### 聚集索引

聚集索引是什么呢，其实就是我们说的那个主键。
优点：
> 它对主键的排序查找和范围查找速度非常快，叶子节点的数据就是用户所要查询的数据。
> 范围查询（range query），即如果要查找主键某一范围内的数据，通过叶子节点的上层中间节点就可以得到页的范围，之后直接读取数据页即可

### 辅助索引
除了聚集索引外其他索引都是辅助索引

### MySQL索引管理
索引的功能就是加速查找

### MySQL常用的索引
普通索引INDEX：加速查找

唯一索引：
    -主键索引PRIMARY KEY：加速查找+约束（不为空、不能重复）
    -唯一索引UNIQUE:加速查找+约束（不能重复）

联合索引：
    -PRIMARY KEY(id,name):联合主键索引
    -UNIQUE(id,name):联合唯一索引
    -INDEX(id,name):联合普通索引

## 锁
锁分为
> 表级锁，(MyISAM，MEMORY，CSV)
> 行级锁，(Innodb)
> 页级锁,  (BerkeleyDB)

### 乐观锁和悲观锁
