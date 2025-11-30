### list database
```sql
\l
```

### choose your database
```sql
\c athena_visit
```
注意这里不要加;

### show tables
```sql
\dt
```

### show table structure
```sql 
\d table_name
test_zjg=# \d t
            数据表 "public.t"
+------+-----------------------+--------+
| 栏位 |         类型          | 修饰词 |
+------+-----------------------+--------+
| id   | integer               | 非空   |
| name | character varying(40) |        |
+------+-----------------------+--------+
索引：
    "t_pkey" PRIMARY KEY, btree (id)

```

上面的索引是t_pkey,可以通过`\d t_pkey` 查看索引信息
```sql
\d t_pkey
test_zjg=# \d t_pkey
  索引 "public.t_pkey"
+------+---------+------+
| 栏位 |  类型   | 定义 |
+------+---------+------+
| id   | integer | id   |
+------+---------+------+
主键(PK),btree, 给数据表 "public.t"
```

如果想看到外键关系，可以通过`\d+`
```sql
athena_visit=# \d+ hospital
                                                      数据表 "public.hospital"
+-------------------+--------------------------------+------------------------------------------------+----------+----------+------+
|       栏位        |              类型              |                     修饰词                     |   存储   | 统计目标 | 描述
+-------------------+--------------------------------+------------------------------------------------+----------+----------+------+
| id                | integer                        | 非空 默认 nextval('hospital_id_seq'::regclass) | plain    |          |      |
| hospital_name     | character varying(250)         | 非空                                           | extended |          |      |
| hospital_intro    | text                           | 非空                                           | extended |          |      |
| hospital_icon     | character varying(250)         |                                                | extended |          |      |
| hospital_level    | hospital_level                 |                                                | plain    |          |      |
| hospital_address  | character varying(250)         |                                                | extended |          |      |
| hospital_province | character varying(50)          |                                                | extended |          |      |
| hospital_city     | character varying(50)          |                                                | extended |          |      |
| contact_user      | character varying(50)          |                                                | extended |          |      |
| contact_phone     | character varying(50)          |                                                | extended |          |      |
| create_time       | timestamp(6) without time zone | 非空                                           | plain    |          |      |
索引：
    "hospital_pkey" PRIMARY KEY, btree (id)
由引用：
    TABLE "tbl_bot" CONSTRAINT "tbl_bot_hospital_id_fkey" FOREIGN KEY (hospital_id) REFERENCES hospital(id)
    TABLE "tbl_customer" CONSTRAINT "tbl_customer_hospital_id_fkey" FOREIGN KEY (hospital_id) REFERENCES hospital(id)
    TABLE "tbl_doctor" CONSTRAINT "tbl_doctor_hospital_id_fkey" FOREIGN KEY (hospital_id) REFERENCES hospital(id)
    TABLE "tbl_order" CONSTRAINT "tbl_order_hospital_id_fkey" FOREIGN KEY (hospital_id) REFERENCES hospital(id)
    TABLE "tbl_templates" CONSTRAINT "tbl_templates_hospital_id_fkey" FOREIGN KEY (hospital_id) REFERENCES hospital(id)
    TABLE "tbl_visit" CONSTRAINT "tbl_visit_hospital_id_fkey" FOREIGN KEY (hospital_id) REFERENCES hospital(id)
```

### postgresql set id start from 1 after delete data
```postgresql
# clear all data
TRUNCATE TABLE table_name CASCADE;

# start from 1
TRUNCATE TABLE table_name RESTART IDENTITY;

# start from 0
TRUNCATE TABLE table_name RESTART IDENTITY CASCADE;
```

### allow remote connect

```
# postgresql.conf中修改
listen_addresses = '*'

#pg_hba.conf 中
# TYPE  DATABASE  USER  CIDR-ADDRESS  METHOD
host  all  all 0.0.0.0/0 md5
```

### copy anoter table structure

```sql
create table student_bak (like student);
create table tbl_case_visit2 as (select * from tbl_case_visit limit 0)
-- postgresql 中后面必须使用括号括起来，在mysql中则不用
```

### 事务
在pg中任何语句默认是以隐式的事务执行的，但也可以显式的添加事务，可以通过：
BEGIN; COMMIT;
BEGIN WORK; COMMIT WOKR;
BEGIN TRANSCATION; COMMIT TRANSCATION; 

```sql
-- start a transaction
BEGIN;
-- insert a new row into the accounts table
INSERT INTO accounts(name,balance)VALUES('Alice',10000);
-- commit the change (or roll it back later)
COMMIT;

```

同样的，回滚可以是：
ROLLBACK;
ROLLBACK WORK;
ROLLBACK TRANSACTION;

ref: https://neon.tech/postgresql/postgresql-tutorial/postgresql-transaction

### 创建数据库表的三原则

在设计和创建数据库表时，需要遵循以下三大原则，以确保数据的完整性、性能和可维护性：

#### 1. **原子性原则（字段不可再分）**
- **含义**：
  - 每个字段的数据应该是不可再分的最小单位。
  - 一个字段只存储一个属性值，避免将多个值存储在同一个字段中。
- **目的**：
  - 保证数据的规范化，避免数据冗余。
  - 提高查询效率，便于数据的筛选和统计。
- **示例**：
  - 错误设计：
    ```sql
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        address VARCHAR(255) -- 地址字段包含省、市、区等信息
    );
    ```
  - 正确设计：
    ```sql
    CREATE TABLE users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        province VARCHAR(50),
        city VARCHAR(50),
        district VARCHAR(50) -- 将地址拆分为多个字段
    );
    ```

#### 2. **唯一性原则（主键唯一标识）**
- **含义**：
  - 每张表必须有一个主键，用于唯一标识每一行数据。
  - 主键可以是单个字段，也可以是多个字段的组合（复合主键）。
- **目的**：
  - 保证数据的唯一性，避免重复数据。
  - 提高数据查询的效率。
- **示例**：
  - 错误设计：
    ```sql
    CREATE TABLE orders (
        order_id INT,
        user_id INT,
        product_id INT -- 缺少主键
    );
    ```
  - 正确设计：
    ```sql
    CREATE TABLE orders (
        order_id SERIAL PRIMARY KEY, -- 添加主键
        user_id INT,
        product_id INT
    );
    ```

#### 3. **规范化原则（减少冗余，避免异常）**
- **含义**：
  - 遵循数据库的规范化设计（如第一范式、第二范式、第三范式）。
  - 将重复数据拆分到不同的表中，通过外键关联。
- **目的**：
  - 减少数据冗余，避免插入、更新、删除异常。
  - 提高数据的可维护性。
- **示例**：
  - 错误设计：
    ```sql
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        department_name VARCHAR(100) -- 部门名称重复存储
    );
    ```
  - 正确设计：
    ```sql
    CREATE TABLE employees (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        department_id INT -- 使用外键关联部门表
    );

    CREATE TABLE departments (
        id SERIAL PRIMARY KEY,
        department_name VARCHAR(100)
    );
    ```

#### 总结
- **原子性原则**：字段不可再分，保证数据的最小粒度。
- **唯一性原则**：主键唯一标识，避免重复数据。
- **规范化原则**：减少冗余，避免数据异常。

通过遵循以上三大原则，可以设计出高效、规范且易维护的数据库表结构。