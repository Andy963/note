### postgresql set id start from 1 after delete data
```postgresql
# clear all data
TRUNCATE TABLE table_name CASCADE;

# start from 1
TRUNCATE TABLE table_name RESTART IDENTITY;

# start from 0
TRUNCATE TABLE table_name RESTART IDENTITY CASCADE;
```