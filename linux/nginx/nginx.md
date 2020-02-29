# nginx


## 卸载

```shell
apt-get install nginx 

nginx is already the newest version.
0 upgraded, 0 newly installed, 0 to remove and 14 not upgraded.
```
应该是没卸载干净

```shell
find / -name nginx

rm -rf /etc/nginx
rm -rf /usr/sbin/nginx
rm /usr/share/man/man1/nginx.1.gz

apt-get remove nginx* (apt-get remove --purge nginx)
sudo apt-get remove nginx #Removes all but config files.
sudo apt-get purge nginx #Removes everything.
```
## 重装

```shell
apt-get purge nginx nginx-common nginx-full
apt-get install nginx
```


## 配置
```nginx

user root;
worker_processes 4;

#全局日志
error_log /usr/local/nginx/logs/error.log info;

#进程pid文件
pid /run/nginx.pid;

events {
    worker_connections 1024;
}

http {
include mime.types;
default_type application/octet-stream;
charset utf-8;

client_max_body_size 8m;
sendfile on;
keepalive_timeout 65;
gzip on;

# 日志格式
log_format access '$remote_addr - $remote_user [$time_local] "$request" '
'$status $body_bytes_sent "$http_referer" '
'"$http_user_agent" $http_x_forwarded_for';

upstream django {
server 127.0.0.1:8080;
}

server {
listen 443 ssl;
server_name www.jingang.ga;

ssl_certificate /root/.acme.sh/www.jingang.ga_ecc/www.jingang.ga.cer;
ssl_certificate_key /root/.acme.sh/www.jingang.ga_ecc/www.jingang.ga.key;

ssl_session_cache shared:SSL:1m;
ssl_session_timeout 5m;
ssl_ciphers HIGH:!aNULL:!MD5;
ssl_prefer_server_ciphers on;

location / {
uwsgi_pass django;
include uwsgi_params;
}

location  /static  {
alias   /root/sites/ownblog/collected_static;
} 

location  /media {
alias   /root/sites/ownblog/media;
} 

access_log  /usr/local/nginx/logs/jingang.access.log  access;
}

server {
listen       80;
server_name  www.jingang.ga;
rewrite ^(.*)$ https://$host$1 permanent;
}
}


```
