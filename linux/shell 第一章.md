
shebang #!

命令通过分号或者换行符来分隔.

### echo  && printf
echo 用于终端打印
```sh
# -e 有转义时使用，echo默认会添加换行符，使用-n参数会不换行
 ~  echo -e "1\t2\t3"
1       2       3
```
printf 格式化打印，需要自己添加换行符
```sh
# 5表示字符宽度，不足用空格补全， -表示左对齐，.2f表示保留两位小数
 printf 　　"%-5s %-10s %-4.2f\n" 2 James 90.9989
　　2     James      91.00
```

### 变量
bash中每一个变量都是字符串
```sh
# pgrep zsh 返回zsh的进程id, cat /proc/pid/environ 得到进程的环境变量， tr命令将\0(null字符串) 换成\n
 cat /proc/$(pgrep zsh)/environ |tr '\0' '\n'
HOSTTYPE=x86_64
LANG=C.UTF-8
TERM=xterm-256color
WSLENV=
NAME=Andy963
HOME=/home/andy
USER=andy
LOGNAME=andy
SHELL=/usr/bin/zsh
WSL_DISTRO_NAME=Ubuntu-18.04
```
var = value, 如果value中没有任何空白字符，则不需要加引号
$var 获取 var变量的值 
length = ${#var} #获取变量字符串长度
```sh
 ~  v=vim
 ~  echo ${#v}
3
```

查看当前 shell
echo $SHELL
echo $0
```
 ~  echo $SHELL
/usr/bin/zsh
 ~  echo $0
-zsh
```
查看用户id， 超级管理员uid为0
```
 ~  echo $UID
1000
```
### export 
export 常用来设置环境变量
```sh
PATH=/home/usr/bin
export PATH
```

### let && []
```sh
n1=3
n2=4
let result = n1+n2
resutl = [n1+n2]

echo "scale=2;3/8" | bc
# scale设定小数位数为2，bc为计算工具
n=100
echo "obase=2;$n"|bc
```

### 文件
0 标准输入
1 标准输出
2 错误
```sh
> 写
>> 追加
```
tee命令 接收来自stdin的数据输出到标准输出，并可以保存到文件

exec创建文件描述符
exec 3 <input.txt 创建描述符3用于读取
exec 4 > output.txt 创建描述符4用于写入


### array
```sh
array=[0,1,2,3,5]
array[0]=0
array[1]=1
array[2]=2
array[3]=3
array[4]=4

 ~  echo ${array[*]}
[0,1,2,3,4]
 ~  echo ${array[@]}
[0,1,2,3,4]
#获取长度：
echo {#array[*]}
 ~  array=(0 1 2 3 4)
 ~  echo ${#array[*]}
5
```

### alias
别名
```sh
alias ll='ls -al'
```

echo 'alias cmd="command seq"' >> ~/.bashrc

### 将命令输出读入变量
```sh
cmd_output = $(ls |cat -n)
cmd_output = `ls |cat -n `

# ()可以定义子shell,如下，子进程的行为不会影响当前shell,所以最后打印出来的pwd相同
pwd;
(cd /bin; ls);
pwd;
```

### 文件测试表达式
常见
```
-f  file    文件存在且为普通文件 file
-d  file    文件存在且为目录 directory
-s  file    文件存在且大小不为0 size
-e  file    文件存在则为真，只要有文件就行 exists
-r  file    文件存在且可读 read
-w  file    文件存在且可写 write
-x  file    文件存在且可执行 execute
-L  file    文件存在且为链接 link
f1 -nt f2   f1比f2新  newer than
f1 -ot f2   f1比f2旧  older than
```
```sh
如果vimrc 文件存在则返回1否则返回0
[ -f /etc/vim/vimrc ]&& echo 1|| echo 0
```
