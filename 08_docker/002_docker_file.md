### docker file

1.编写docker file
```
FROM centos
VOLUME ["/dataVolContainer1","/dataVolContainer2"]
CMD echo "finished, ----success"
CMD /bin/bash
```
类似于：
`docker run -it  -v /host:/dataVolContainer1 -v /host:/dataVolContainer2'`

2.build
```
docker build -f /opt/dockerfile -t andy/centos
# "docker build" requires exactly 1 argument.
原因是-f后面不要跟完整的路径，应该把它放在后面，也可用相对路径
 ✘ ⚡ root@tx  /opt/docker_learn  docker build -f Dockerfile -t andy/centos /opt/docker_learn/
Sending build context to Docker daemon  2.048kB
Step 1/4 : FROM centos
latest: Pulling from library/centos
a1d0c7532777: Pull complete 
Digest: sha256:a27fd8080b517143cbbbab9dfb7c8571c40d67d534bbdee55bd6c473f432b177
Status: Downloaded newer image for centos:latest
 ---> 5d0da3dc9764
Step 2/4 : VOLUME ["/dataVolContainer1","/dataVolContainer2"]
 ---> Running in f80d51c6df0b
Removing intermediate container f80d51c6df0b
 ---> 913f1e428b1e
Step 3/4 : CMD echo "finished, ----success"
 ---> Running in 6a65c6e0340f
Removing intermediate container 6a65c6e0340f
 ---> 1d38e8b886e0
Step 4/4 : CMD /bin/bash
 ---> Running in 3db66975f444
Removing intermediate container 3db66975f444
 ---> db0c1d103d0d
Successfully built db0c1d103d0d
Successfully tagged andy/centos:latest

⚡ root@tx  /opt/docker_learn  docker images                                               
REPOSITORY            TAG       IMAGE ID       CREATED              SIZE
andy/centos           latest    db0c1d103d0d   About a minute ago   231MB
```

3.run
docker run --name myct 
容器间数据共享
```sh
docker run --name dc2 --volumes-from dc1
```
dc1 为模板，在dc1的卷中创建的文件，在创建dc2时也会创建，即使事后我们把dc1删除，dc2中也还是有，数据卷的生命周期一直持续到没有容器使用它为止。


### Dockerfile 基础知识
1.每条保留字指令必须为大写字母且后面要跟随至少一个参数
2.指令从上到下，顺序执行
3.#表示注释
4.每条指令都全创建一个新的镜像层，并对镜像进行提交


### 保留字
FROM  基础镜像
MAINTAINER 镜像维护者的姓名，邮箱
RUN 执行命令
EXPOSE 暴露出的端口
WORKDIR 工作的目录，终端默认登陆进来工作目录
ENV 在构建环境过程中设置环境变量
ADD 拷贝加解压
COPY 仅仅拷贝
VOLUME 容器数据卷，用于数据保存和持久化工作
CMD 指定容器启动时要运行的命令（dockerfile中可以有多条，但只有最后一个生效，CMD会被docker run 之后的参数替换）
ENTRYPOINT 指定容器启动时要运行的命令，和CMD一样，但ENTRYPOINT会在容器命令之后添加
ONBUILD 当构建一个被继承的dockerfile时运行命令，父镜像在被子继承后父镜像的Onbuild被触发


```shell
FROM centos
ENV mypath /tmp
WORKDIR $mypath
RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80
CMD /bin/bash
```

### ENV && ARG
env,arg都可以设置变量，在dockerfile中作为变量使用，避免硬编码，但两者作用范围不同，env定义的变量作用范围包括：构建+container, 即构建时可用，后面运行docker时仍然可用，但arg仅在构建时可用，到运行container时，arg定义的变量已经不存在。

arg在构建时甚至可以不修改dockerfile 而通过命令行`--build-args`来改变变量的值
假如我们的dockerfile中定义了VERSION=1,那么：
```sh
docker image build -f .\dockerfile -t ipinfo --build-arg VERSION=2.0
```
将修改version字段

### 容器启动命令
CMD可以用来设置容器启动时默认执行的命令
- 容器启动时默认执行的命令
- 如果docker container run 启动容器时指定了其它命令，则CMD命令会被忽略
- 如果定义了多个CMD,只有最后一个会被执行
如果dockerfile中指定了空命令，那么父级的cmd会被覆盖。
--rm 参数，当使用docker container run 命令时，指定了`--rm`，则当容器退出时，container会被自动删除

### Entrypoint && CMD
entrypoint无法被覆盖，一定会执行，但cmd可以被覆盖。通常两者结合一起用，通过命令行将cmd命令作为参数传给entrypoint.


### 分阶段编译

```docker
From gcc:9.4 AS builder
COPY hello.c /src/hello.c
WORKDIR /src
RUN gcc --static -o hello hello.c

FROM alphine:3.13.5
COPY --from=builder /src/hello /src/hello
ENTRYPOINT ["/src/hello"]
CMD []
```

这种技巧通常只对编译型语言有效，不过像python这种解释型语言也可以通过pyinstaller之类进行打包，前面编译出来的文件会复制到后面的镜像使用，这样体积就缩小了很多，同时构建时间也短了