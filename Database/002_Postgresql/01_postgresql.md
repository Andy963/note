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
