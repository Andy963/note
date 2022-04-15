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
