## 数据库查询


### 关键字的执行优先级

* from 找到表:from
* where 拿着where指定的约束条件，去文件/表中取出一条条记录
* group by 将取出的一条条记录进行分组group by，如果没有group by，则整体作为一组
* having 将分组的结果进行having过滤
* select 执行select 
* distinct 去重,distinct必须写在所有查询字段的前面
* order by  结果按条件排序
* limit 限制结果的显示条数

### 内建函数

```sql
count
max
min
avg
sum

CONCAT() 函数用于连接字符串
SELECT CONCAT('姓名: ',name,'  年薪: ', salary*12)  AS Annual_salary

CONCAT_WS() 第一个参数为分隔符来进行字符串拼接
SELECT CONCAT_WS(':',name,salary*12)  AS Annual_salary  #通过冒号来将name和salary连接起来
   FROM employee;
group_concat()
```

### 单表查询
#### where 约束

> 比较运算符：> < >= <= <> !=
　between 80 and 100 值在80到100之间
　in(80,90,100)  值是80或90或100
　like 'egon%'
   pattern可以是%或_，%表示任意多字符, "_ _" 表示一个字符
　逻辑运算符：在多个条件直接可以使用逻辑运算符 and or not

#### GROUP BY
如果设置了only_full_group_by这个mode，那么我们在直接分组查询，就无法得到数据了，只能得到字段名。并且设置了sql_mode为only_full_group_by之后，select `*`，就不行了，会直接报错，只能select post ，post是你分组的那个字段。

注意：
如果我们用设置了unique约束的字段作为分组的依据，则每一条记录自成一组，这种分组没有意义。多条记录之间的某个字段值相同，该字段通常用来作为分组的依据

查看sql_mode信息
```sql
select @@global.sql_mode;
```

ONLY_FULL_GROUP_BY的语义就是确定select target list中的所有列的值都是明确语义，简单的说来，在ONLY_FULL_GROUP_BY模式下，target list中的值要么是来自于聚集函数的结果，要么是来自于group by list中的表达式的值。

#设置sql_mole如下操作(我们可以去掉ONLY_FULL_GROUP_BY模式)：
```sql
set global sql_mode= 'STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION';
```

我们按照post字段分组，那么select查询的字段只能是post，想要获取组内的其他相关信息，需要借助函数

GROUP BY关键字和GROUP_CONCAT()函数一起使用,比如说我想按部门分组，每个组有哪些员工，都显示出来:
```sql
SELECT post,GROUP_CONCAT(name) FROM employee GROUP BY post;#按照岗位分组，并查看组内所有成员名，通过逗号拼接在一起
    SELECT post,GROUP_CONCAT(name,':',salary) as emp_members FROM employee GROUP BY post;
```

GROUP BY一般都会与聚合函数一起使用，聚合是什么意思：聚合就是将分组的数据聚集到一起，合并起来搞事情，拿到一个最后的结果:
```sql
select post,count(id) as count from employee group by post;
#按照岗位分组，并查看每个组有多少人，每个人都有唯一的id号，我count是计算一下分组之后每组有多少的id记录，通过这个id记录我就知道每个组有多少人了
```

group by 如果不和聚合函数一起使用时，查询字段相同的为一组，但因为没有聚合函数，只会显示组中第一条数据，意义不大。所以通常会和聚合函数一起使用。
Group by field having exp
通常情况下，使用group by后无法显示分组里面有哪些元素，但我们可以通过group_concat达到这样的目的。
```sql
select sno,cno,group_concat(degree) from score group by sno having min(degree) > 80;
```
首先，它会根据sno分组，且将组内最低分数大于80的列出来，会列出sno,cno,但同时也会把组内所有的degree列出在一个字段中，可以通过 group_concat(degree) as all_degree 的方式对其进行重命名
#### 聚合函数

```sql
SELECT COUNT(*) FROM employee;  #count是统计个数用的
SELECT COUNT(*) FROM employee WHERE depart_id=1;  #后面跟where条件的意思是统计一下满足depart_id=1这个的所有记录的个数
SELECT MAX(salary) FROM employee;  #max（）统计分组后每组的最大值，这里没有写group by，那么就是统计整个表中所有记录中薪资最大的，薪资的值
SELECT MIN(salary) FROM employee;
SELECT AVG(salary) FROM employee;
SELECT SUM(salary) FROM employee;
```


#### HAVING过滤
讲having之前，我们补充一个点：之前我们写的查询语句是这样的：select id,name from employee;实际上我们在select每个字段的时候，省略了一个表名，有的人可能会这样写，select employee.id,employee.name from employee;你会发现查询出来的结果是一样的，但是如果你要将查询出来的结果表起一个新表名的话，带着表名这样写就错了:
```sql
select employee.id,employee.name from employee as tb1;#这样执行会下面的报错：
mysql> select employee.id,employee.name from employee as tb1;
ERROR 1054 (42S22): Unknown column 'employee.id' in 'field list'
```

因为这个语句先执行的是谁啊，是不是我们的from啊，那么后面的as也是比select要先执行的，所以你先将表employee起了个新名字叫做tb1，然后在tb1里面取查询数据，那么tb1里面找不到employee.id这个字段，就会报错，如果我们查询的时候不带表名，你as来起一个新的表名也是没问题的，简单提一下这个内容，知道就好了

HAVING与WHERE的区别？
having的语法格式和where是一模一样的，只不过having是在分组之后进行的进一步的过滤，where不能使用聚合函数，having是可以使用聚合函数的
#执行优先级从高到低：where > group by > having 
#1. Where 发生在分组group by之前，因而Where中可以有任意字段，但是绝对不能使用聚合函数。
#2. Having发生在分组group by之后，因而Having中可以使用分组的字段，无法直接取到其他字段,having是可以使用聚合函数

```sql
select post,avg(salary) as new_sa from employee where age>=30 group by post having avg(salary) > 10000;
#如果是where是不能用where avg(salary)>10000的。
```

#### DISTINCT
将查询的结果进行去重：select distinct post from employee; 注意distinct去重要写在查询字段的前面，不然会报错

有时需要查询出某个字段不重复的记录，这时可以使用mysql提供的distinct这个关键字来过滤重复的记录，但是实际中我们往往用distinct来返回不重复字段的条数（count(distinct id)）,其原因是distinct只能返回他的目标字段，而无法返回其他字段，distinct 想写在其他字段后面需要配合聚合函数来写

#### ORDER BY
默认是升序排列

```SQL
SELECT * FROM employee ORDER BY salary ASC; #升序
SELECT * FROM employee ORDER BY salary DESC; #降序
#  多条件
 SELECT * from employee
        ORDER BY age, #注意排序的条件用逗号分隔
        salary DESC;
```

#### LIMIT

```sql
ELECT * FROM employee ORDER BY salary DESC 
        LIMIT 3;                    #默认初始位置为0,从第一条开始顺序取出三条

SELECT * FROM employee ORDER BY salary DESC
        LIMIT 0,5; #从第0开始，即先查询出第一条，然后包含这一条在内往后查5条 

SELECT * FROM employee ORDER BY salary DESC
        LIMIT 5,5; #从第5开始，即先查询出第6条，然后包含这一条在内往后查5条
```

#### 使用正则表达式查询
之前我们用like做模糊匹配，只有%和_，局限性比较强，所以我们说一个正则，之前我们是不是学过正则匹配，你之前学的正则表达式都可以用，正则是通用的

```sql
SELECT * FROM employee WHERE name REGEXP '^ale';

SELECT * FROM employee WHERE name REGEXP 'on$';

SELECT * FROM employee WHERE name REGEXP 'm{2}';
```

### 多表查询

#### 交叉连接

不适用任何匹配条件，生成笛卡尔积
```sql
select * from department,employee; #表用逗号分隔
```
就是简单粗暴的将两个表的数据全部对应了一遍，用处就是什么呢，它肯定就能保证有一条是对应准的，你需要做的事情就是在笛卡儿积的基础上只过滤出我们需要的那些数据就行了，笛卡儿积不是咱们最终要得到的结果，只是给你提供了一个基础，它不管对应的对不对，全部给你对应一遍，然后你自己去筛选就可以了

#### 内连接

```sql
select employee.name from employee,department where employee.dep_id=department.id and department.name='技术';
```

左连接与右连接，先查的表为左表，后查的为右表，左连接以左表为准，即左表的记录都能显示，而右表中与左表不匹配的就显示为Null. 同样的道理，右连接以右表为准，右表的记录都能显示，但左表中与右表不匹配就显示Null

#### 外连接之左连接
优先显示左表全部记录
#以左表为准，即找出所有员工信息，当然包括没有部门的员工
#本质就是：在内连接的基础上增加左边有右边没有的结果 
```sql

#注意语法：
mysql> select employee.id,employee.name,department.name as depart_name from 
employee left join department on employee.dep_id=department.id;
```

#### 外连接之右连接
#以右表为准，即找出所有部门信息，包括没有员工的部门
#本质就是：在内连接的基础上增加右边有左边没有的结果
```sql
select employee.id,employee.name,department.name as depart_name from employee right join department on employee.dep_id=department.id;
```

#### 全外链接

在内连接的基础上增加左边有右边没有的和右边有左边没有的结果
#注意：mysql不支持全外连接 full JOIN
#强调：mysql可以使用此种方式间接实现全外连接

```sql
select * from employee left join department on employee.dep_id = department.id
union
select * from employee right join department on employee.dep_id = department.id;
```

#注意 union与union all的区别：union会去掉相同的纪录，因为union all是left join 和right join合并，所以有重复的记录，通过union就将重复的记录去重了.

#### 符合条件连接查询

以内连接的方式查询employee和department表，并且employee表中的age字段值必须大于25,即找出年龄大于25岁的员工以及员工所在的部门

```sql
select employee.name,department.name from employee inner join department
    on employee.dep_id = department.id
    where age > 25;
```

以内连接(隐式内连接)的方式查询employee和department表，并且以age字段的升序方式显示

```sql
select employee.id,employee.name,employee.age,department.name from employee,department
    where employee.dep_id = department.id
    and age > 25
    order by age asc;
```

### 子查询

子查询，把一个查询的结果（也是一张表）作为另一个查询的表来用。

获取技术部的员工姓名
我们已知的条件：技术部， 查询的结果： 姓名
涉及到两张表 部门表，员工表。 所以没法直接查，必须连表，所以我们必须找到技术部在员工表中对应的字段即dep_id
然后在员工一中过滤这个字段，获取姓名
```sql
select id from department where name='技术部';
select name from employee where dep_id = 'id';

select name from employee where dep_id = (select id from department where name='技术');
```

#1：子查询是将一个查询语句嵌套在另一个查询语句中。
#2：内层查询语句的查询结果，可以为外层查询语句提供查询条件。
#3：子查询中可以包含：IN、NOT IN、ANY、ALL、EXISTS 和 NOT EXISTS等关键字
#4：还可以包含比较运算符：= 、 !=、> 、<等

也就说两个表可以通过in, not in 连接比如：
```sql
select name from employee where dep_id in (select id from department where name = '技术');
```


#### 练习
通过连表的方式来查询每个部门最新入职的那位员工
```sql
company.employee
    员工id      id                  int             
    姓名        emp_name            varchar
    性别        gender                 enum
    年龄        age                 int
    入职日期     hire_date           date
    岗位        post                varchar
    职位描述     post_comment        varchar
    薪水        salary              double
    办公室       office              int
    部门编号     depart_id           int



#创建表，只需要创建这一张表
create table employee(
    id int not null unique auto_increment,
    name varchar(20) not null,
    gender enum('male','female') not null default 'male', #大部分是男的
    age int(3) unsigned not null default 28,
    hire_date date not null,
    post varchar(50),
    post_comment varchar(100),
    salary double(15,2),
    office int, #一个部门一个屋子
    depart_id int
);

#插入记录
#三个部门：教学，销售，运营
insert into employee(name,gender,age,hire_date,post,salary,office,depart_id) values
('egon','male',18,'20170301','老男孩驻沙河办事处外交大使',7300.33,401,1), #以下是教学部
('alex','male',78,'20150302','teacher',1000000.31,401,1),
('wupeiqi','male',81,'20130305','teacher',8300,401,1),
('yuanhao','male',73,'20140701','teacher',3500,401,1),
('liwenzhou','male',28,'20121101','teacher',2100,401,1),
('jingliyang','female',18,'20110211','teacher',9000,401,1),
('jinxin','male',18,'19000301','teacher',30000,401,1),
('成龙','male',48,'20101111','teacher',10000,401,1),

('歪歪','female',48,'20150311','sale',3000.13,402,2),#以下是销售部门
('丫丫','female',38,'20101101','sale',2000.35,402,2),
('丁丁','female',18,'20110312','sale',1000.37,402,2),
('星星','female',18,'20160513','sale',3000.29,402,2),
('格格','female',28,'20170127','sale',4000.33,402,2),

('张野','male',28,'20160311','operation',10000.13,403,3), #以下是运营部门
('程咬金','male',18,'19970312','operation',20000,403,3),
('程咬银','female',18,'20130311','operation',19000,403,3),
('程咬铜','male',18,'20150411','operation',18000,403,3),
('程咬铁','female',18,'20140512','operation',17000,403,3)
;

#ps：如果在windows系统中，插入中文字符，select的结果为空白，可以将所有字符编码统一设置成gbk
```
先按部门分组，查出入职日期最大的那个，通过部门表内连接，过滤条件是日期相同。

```sql
select * from employee as t1 inner join(
select post, max(hire_date) as max_date from employee group by post) as t2 
on t1.post=t2.post 
where t1.hire_date = t2.max_date;
```