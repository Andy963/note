## 安装mysql

### ubuntu 安装mysql
```bash
sudo apt-get install mysql-server 
sudo apt install mysql-client 
sudo apt install libmysqlclient-dev
```


#### 查看是否安装成功:
```bash
sudo netstat -tap | grep mysql
```
### ubuntu设置密码

### 查看默认密码
```bash
sudo cat /etc/mysql/debian.cnf
```
#### 用默认密码登陆
```bash
mysql -u debian-sys-maint -p
```
#### 设置密码
```bash

use mysql;
// 下面这句命令有点长，请注意。
update mysql.user set authentication_string=password('root') where user='root' and Host ='localhost';
update user set plugin="mysql_native_password";
flush privileges;
```

### 忘记密码

#### 跳过验证
```bash
sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

#  添加内容 skip-external-locking,在下面添加一行:
skip-grant-tables
```

#### 重启mysql
```bash
systemctl restart msyql
```

#### 重新设置密码
```bash
mysql #  此时不需要密码验证
user msyql;
```
修改用户 密码
```sql
UPDATE mysql.user SET authentication_string=password('你想设置的密码') WHERE User='root' AND Host ='localhost';
UPDATE user SET plugin="mysql_native_password";
flush privileges; #  刷新权限
quit;
```
最后注释掉(/etc/mysql/mysql.conf.d/mysqld.cnf)添加的命令


### 创建数据库:
```sql
CREATE DATABASE mysite_db DEFAULT CHARSET=UTF8 DEFAULT COLLATE utf8_unicode_ci;
```

### 创建用户:
```sql
CREATE USER 'zjg'@'localhost' IDENTIFIED BY 'Zjgisadmin';
```

### 分配权限:
```sql
GRANT ALL PRIVILEGES ON mysite_db.* TO 'zjg'@'localhost';
```

### 刷新权限:
```sql
FLUSH PRIVILEGES;
```

### 将mysql数据导出:
```sql
mysqldump -u zjg -p --databases mysite_db > /home/mysite_db.sql;
```

### 允许从任意ip远程连接:
```sql
mysql> GRANT ALL PRIVILEGES ON *.* TO 'zjg'@'%' IDENTIFIED BY 'Zjgisadmin' WITH GRANT OPTION;
```

### 从指定ip连接:
允许用户jack从任意ip以密码654321登陆
```sql
GRANT ALL PRIVILEGES ON *.* TO 'jack'@’10.10.50.127’ IDENTIFIED BY '654321' WITH GRANT OPTION;
```
### 修改绑定:
```sql
/etc/mysql/mysql.conf.d/mysqld.cnf
将bind_ipaddress 127.0.0.1 注释掉
```
### 重启
```bash
service mysql restar
```

