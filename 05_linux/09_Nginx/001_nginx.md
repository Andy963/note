

- 高并发，高可用
- 热部署

配置语法：
- 配置文件由指令与指令块构成
- 每条指令以;分号结尾,指令与参数间以空格符号分隔
- 指令块以 {} 大括号将多条指令组织在一起
- include语句允许组合多个配置文件以提升可维护性
- 使用#符号添加注释,提高可读性
- 使用$符号使用变量
- 部分指令的参数支持正则表达式

http
upstream


### nginx signal

[nginx signal](https://github.com/Andy963/notePic/blob/57ccb7b79e957d498f8ce290b32fea82556d8bc9/0037_nginx%E8%BF%9B%E7%A8%8B%E7%9A%84%E4%BF%A1%E5%8F%B7.jpg)



```nginx

gzip on;
gzip_min_length 1;
gzip_comp_level 2;
gzip_types text/plain application/x-javascript image/jpeg image/gif image/png;

log_format main '$remote_addr - $remote_user [$time_local] "$request"'
'$status $body_bytes_sent "$http_referer"'
'$http_user_agent" "$http_x_forwarded_for"';

access_log logs/access.log main;


location / {
				proxy_set_header Host $host;
				proxy_set_header X-Real-IP $remote_addr;
				proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for ;
				
				#proxy_cache my_cache; # 共享内存
				#proxy_cache_key $host$uri$is_args$args;
				#proxy_cache_valid 200 304 302 1d;
				proxy_pass http://local;
			}
```
### 卸载

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
### 重装

```shell
apt-get purge nginx nginx-common nginx-full
apt-get install nginx
```


### 配置
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


### nginx sni 转发

```nginx
# 流量转发核心配置
stream {
    # 这里就是 SNI 识别，将域名映射成一个配置名
    map $ssl_preread_server_name $backend_name {
        domain.com web;
        domain.net web1;
        domain.cn web2;
    # 域名都不匹配情况下的默认值
        default web;
    }
 
    # web，配置转发详情
    upstream web {
        server 127.0.0.1:8080;
    }
 
    # web1，配置转发详情
    upstream web1 {
        server 127.0.0.1:8081;
    }
 
    # web2，配置转发详情
    upstream web2 {
        server 127.0.0.1:8082;
    }
 
    # 监听 443 并开启 ssl_preread
    server {
        listen 443 reuseport;
        listen [::]:443 reuseport;
        proxy_pass  $backend_name;
        ssl_preread on;
    }
}
```


### 502
这个当请求头过长时，nginx buffer过小会导致502且静态文件加载过慢
```nginx
proxy_buffer_size 64k
proxy_buffers 32 32k
proxy_busy_buffers_size 128k
```


### uwsgi

```uwsgi

[uwsgi]
# 自定义变量
projectname = ownblog
base = /var/www

# 启用主进程
master = true
#
socket = 127.0.0.1:8080
# 网络请求
#http = 127.0.0.1:8000

# 项目目录
chdir = %(base)/ownblog
# 环境目录
venv=/home/envs/ownblog-ccOfqkNN
# module wsgi文件
wsgi-file = %(base)/ownblog/ownblog/wsgi.py

# 进程数
processes = 2
# 启用线程,线程数量
enable-threads = true
threads = 4

# buffer size,default 4kb
buffer-size = 32768
# run background, loging to file
daemonize = /var/log/ownblog_uwsgi.log
pidfile = /var/run/ownblog.pid
# max size of log file
log-maxsize = 500000
# auto delete unix socket pid when exit server
vacuum = true
# max requests for every process
max-requests = 300
# after 60s request will timeout
harakiri = 60
```
