# mysql


### 数据库表名大小写
```sql
show variables like '%lower_case_table_names%';
```
win一般默认值为1，表示是大小写不敏感，而linux环境的mysql是0