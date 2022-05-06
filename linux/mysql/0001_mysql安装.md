## 安装mysql

### ubuntu 安装mysql
```bash
sudo apt-get install mysql-server 
sudo apt install mysql-client 
sudo apt install libmysqlclient-dev

#docker 
docker pull mysql:5.7
docker run -p 3306:3306 --privileged=true -v /opt/mysql/conf:/etc/mysql/conf.d -v /opt/mysql/logs:/logs -v /opt/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=yourpassword -d mysql:5.7
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
可以由数字，字母，下划线，@，$, #组成 且<strong>区分大小写</strong>,不能使用关键字，不能纯数字，唯一性，最长128位。
```sql
CREATE DATABASE mysite_db DEFAULT CHARSET=UTF8 DEFAULT COLLATE utf8_unicode_ci;
show databases; 查看所有数据库
select database();
```


### 创建用户:
```sql
CREATE USER 'zjg'@'localhost' IDENTIFIED BY 'Zjgisadmin';
```

```sql
#创建用户
create user 'andy'@'192.168.1.1' identified by 'password'; 
create user 'andy'@'%' identified by 'password'; 
#删除用户
drop user 'andy'@'ip_address'; 
#修改用户： 
rename user 'andy'@'ip_address' to 'jack'@'ip_address'; 
#修改密码
set password for 'andy'@'ip_address' = paswword('new_password'); 
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

