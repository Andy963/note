### DBconnector
Before version 2.0 the module should be import by: `from DBUtils.PooledDB import PooledDB`. In version 2: ` from dbutils.pooled_db import PooledDB`

```python
# ！/usr/bin/env python
# encoding:utf-8
# Created by Andy at 2021/4/4

import pymysql
from dbutils.pooled_db import PooledDB


class DBConnector:
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,  # the module to connect db
            maxconnections=6,  # max connections, if set to 0,none will not restrict connections
            mincached=3,  # create 3 connections when initialize
            blocking=True,  # if no free connections then will wait
            ping=0,  # check mysql service 0 means never, 1 means whenever requested,2 means when created cursor
            host='127.0.0.1',
            port=3306,
            user='root',
            password='zjgisadmin',
            database='itcase',
            charset='utf8'
        )
        self.conn = None
        self.cursor = None

    def open(self):
        self.conn = self.pool.connection()
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()

    # def __enter__(self):
    #     self.open()
    #     return self.cursor
    # 
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     self.close()

    def fetchall(self, sql, *args):
        self.open()
        self.cursor.execute(sql, *args)
        result = self.cursor.fetchall()
        self.close()
        return result

    def fetchone(self, sql, args):
        self.open()
        self.cursor.execute(sql, args)
        result = self.cursor.fetchone()
        self.close()
        return result


sql = "select * from it_user_info where ui_user_id in %s"
with DBConnector() as cursor:
    cursor.execute(sql, ([1, 2],))
    print(cursor.fetchall())
```