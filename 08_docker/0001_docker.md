### docker search
```
-s star

```
### docker ps 
```
a -all查看所有容器
q --quit 只显示容器编号
```

### docker attach
```
用来连接一个正在运行中的容器

```

### docker exec
```
#直接在容器内执行命令
docker exec -it mymongo:mongo
```

### docker rm
it's better to use docker container rm. so it's clear to know it's container or image.
```
#删除容器
docker rm ubuntu
-f force
-l link 删除链接，但保留容器
-v volumns=false 容器挂载的数据卷
```
### docker commit
```
-a  author
-m message
-p pause 提交时停止窗口运行
```
### docker load
```
#load的gz包会被自动解压
docker load < /opt/centos.tar.gz
docker load --input /opt/centos.tar.gz
```

### docker save
```
docker save -o ubuntu_14.04.tar ubuntu:14.04
```

### docker push
```
docker tag test:latest user/test:latest
```

### docker inspect 
```
sudo docker inspect -f
-f参数指数需要哪些内容
sudo docker inspect -f {{".Architecture"}} 550 # 只要Architecture
```

### docker create
```
#创建一个容器
docker create -it ubuntu:latest
docker start ubuntu # 再启动
docker stop ubuntu # 停止
```

### docker run
对于基于镜像的docker run 相当于 docker create, docker start
```
docker run ubuntu  /bin/echo 'Hello world'
-t  terminal
-i interface
-d daemon

docker run -d -p 9000:9000 --name v2ray --restart=always -v /etc/v2ray:/etc/v2ray teddysun/v2ray

-d daemon 后台运行
-p 指定端口映射 P 随机端口
--name 为容器自定义命名
-v volumn /etc/v2ray:/etc/v2ray将主机的v2ray文件挂载到容器中使用，这里用来存放config
删除数据卷不会删除它挂载的容器，
```
#### v
```
 docker run -it -v /dbdata --name dbdata ubuntu
 sudo docker run -it --volumes-from dbdata --name db1 ubuntu
 sudo docker run -it --volumes-from dbdata --name db2 ubuntu
 --volumes-from来挂载dbdata容器中的数据卷，例如创建db1和db2两个容器，并从dbdata容器挂载数据卷
```

### docker image
docker image is read only file, it contains file system,source code, lib file,dependency tools etc. you can treat it as a template. docker image contains layer.

### docker containers
a container is a running images. it copy a image and add read-write layer(container layer) upon it. one images can create many containers, and that's why you can't delete the image when there is some container is running.

### 构建镜像实例
```docker
# This my first django Dockerfile
# Version 1.0
# Base images 基础镜像
FROM centos:centos7.5.1804
#MAINTAINER 维护者信息
LABEL maintainer="inspur_lyx@hotmail.com"
#ENV 设置环境变量
ENV VERSION v1.0
#RUN 执行以下命令
RUN yum install -y wget
RUN wget -P /etc/yum.repos.d/
http://mirrors.aliyun.com/repo/Centos-7.repo
RUN yum install -y python36 python3-devel gcc
#工作目录
WORKDIR /opt
#拷贝文件至工作目录
COPY . /opt
RUN pip3 install -i
http://mirrors.aliyun.com/pypi/simple/ --trusted-host
mirrors.aliyun.com Django==2.1.8
RUN rm -rf ~/.cache/pip
#EXPOSE 映射端口
EXPOSE 8000
#容器启动时执行命令
CMD ["python3", "manage.py", "runserver",
"0.0.0.0:8000"]
```

### docker限制日志大小
如果没有创建文件： `sudo vim /etc/docker/daemon.json`

```json
{
  "log-driver":"json-file",
  "log-opts": {"max-size":"50m", "max-file":"3"}
}
```

```sh
# 重启docker守护进程
sudo systemctl daemon-reload
# 重启docker
sudo systemctl restart docker
```