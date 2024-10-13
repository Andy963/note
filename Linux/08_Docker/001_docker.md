### docker search
```
-s star

```
### docker ps 
```sh
a -all查看所有容器
q --quiet 只显示容器编号
- l 显示最近创建的容器
- n 显示最近创建的n个容器

# 因为ps -aq 能显示出所有的container id ,那么可以据此实现批量删除
docker container stop $(docker container ps -aq)
docker container stop $(docker ps -aq) # 这个container 可以省略

```
-- no-trunc 不截断输出，显示详细信息

### docker create
```sh
#创建一个容器
docker create -it ubuntu:latest
docker start ubuntu # 再启动
docker stop ubuntu # 停止
```

### docker run
对于基于镜像的docker run 相当于 docker create, docker start
```sh
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
### docker volumes
```sh
# 指定卷
 docker run -it -v /dbdata --name dbdata ubuntu
 sudo docker run -it --volumes-from dbdata --name db1 ubuntu
 sudo docker run -it --volumes-from dbdata --name db2 ubuntu
 --volumes-from来挂载dbdata容器中的数据卷，例如创建db1和db2两个容器，并从dbdata容器挂载数据卷
docker run -d -v /host/path:/container/path:ro container_name;  # ro read only

# 创建卷
docker volume create [卷名]

# 列出卷
docker volume ls

# 检查卷的详细信息
docker volume inspect

# 删除卷
docker volume rm 卷名
# 删除所有未使用的卷
docker volume prune

```

### docker attach
```sh
# 用来连接一个正在运行中的容器
docker attach docker_id
cd /root
ls -l
```

attach 为前端执行模式，detach则在后台运行。如果使用attach模式，通过ctrl +c 终止时，窗口也会终止
### docker exec
```sh
#直接在容器内执行命令
docker exec -it mymongo:mongo

docker exec -it docker_id ls -l /root  # 直接获取到结果
docker exec -it docker_id /bin/bash 
ls -l /root

docker exec -it ubuntu sh # 进入ubuntu这个容器的shell模式

```

### docker cp
```sh
# 从docker 拷贝到 宿主机中，docker_id与/path/file_name之间不应该有空格
docker cp docker_id:/path/file_name /root/
# 从宿主机拷贝到容器中
docker cp /root/file_name docker_id:/path/

```


### docker rm
it's better to use docker container rm. so it's clear to know it's container or image.
```sh
#删除容器
docker rm ubuntu
-f force
-l link 删除链接，但保留容器
-v volumns=false 容器挂载的数据卷

#一次删除多个容器
docker rm -f $(docker ps -a -q)
docker ps -a -q | xargs docker rm

# dangling=true means images has no tag or repository
# q means to show the numeric id if use docker rmi
# but docker images -f -q means quiet
docker rmi $(docker images -f "dangling=true" -q)
```
### docker commit
```sh
-a  author
-m message
-p pause 提交时停止窗口运行

docker commit -m='author info' -a='author' docker_id container_name:tag_name
```
### docker load
```sh
#load的gz包会被自动解压
docker load < /opt/centos.tar.gz
docker load --input /opt/centos.tar.gz
```

### docker save
```sh
# 将 Docker 镜像 ubuntu:14.04 保存为一个 tar 归档文件，文件名为 ubuntu_14.04.tar。
docker save -o ubuntu_14.04.tar ubuntu:14.04
```

### docker push
```shell

docker tag test:latest user/test:latest
docker push user/test:latest
```

### docker inspect 

```sh
sudo docker inspect -f
-f参数指数需要哪些内容
sudo docker inspect -f {{".Architecture"}} 550 # 只要Architecture
```



### docker top
```sh
docker top docker_id
```


### docker stop & kill 
docker stop 是温柔停止
docker kill 是强制停止

强制删除
```sh
docker container rm docker_id -f
```
### docker logs
logs查看容器的日志，默认只查看当前最新的，并非实时更新的，要实时更新则使用`-f`参数，这与上面的attach模式下的日志一样
```sh
docker logs -t -f --tail docker_id
docker container logs v2
docker container logs -f v2
```

### exit：
exit 停止退出
ctrl + p +q 不停止退出
### docker image
docker image is read only file, it contains file system,source code, lib file,dependency tools etc. you can treat it as a template. docker image contains layer.

### docker containers
a container is a running images. it copy a image and add read-write layer(container layer) upon it. one images can create many containers, and that's why you can't delete the image when there is some container is running.

1. Image是Container的基础：Container是从Image创建的运行实例。

2. Image是静态的，Container是动态的：Image是只读的模板，而Container是可读写的运行环境。

3. 一个Image可以创建多个Container：同一个Image可以用来启动多个相同配置的Container。

4. Container可以创建新的Image：通过对Container的修改,可以创建新的Image。

### 构建镜像实例
```docker
# This my first django Dockerfile
# Version 1.0
# Base images 基础镜像
FROM centos:centos7.5.1804
#MAINTAINER 维护者信息
LABEL maintainer="abc@gmail.com"
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