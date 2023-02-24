### 创建 mysql 

初始root密码可以考虑一次性密码，或者创建后立马修改
```
docker run --name mysql -e  MYSQL_ROOT_PASSWORD pwd -p 3306:3306 -d mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci

docker exec -it mysql bash
#apt-get install vim
```

### 用户，权限
```mysql

#创建数据库
CREATE Database Better  DEFAULT CHARSET=UTF8 DEFAULT COLLATE utf8_unicode_ci;

#创建用户/修改用户密码
CREATE USER 'better'@'%' IDENTIFIED BY 'pwd';
ALTER USER 'better'@'%' IDENTIFIED BY 'pwd';

#给予远程访问权限权限
GRANT ALL PRIVILEGES ON *.*  TO 'better'@'%' IDENTIFIED BY 'pwd' WITH GRANT OPTION;
UPDATE user SET host = '%' WHERE user = 'better';

#刷新权限
FLUSH PRIVILEGES

#查看权限
select host,user,authentication_string from user;
```




