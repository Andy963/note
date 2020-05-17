
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

### tee 
tee 命令将标准输入发送到标准输出或者写入文件
```sh
 /mnt/d/code/vim_learn  tee tee_example.sh
teee command send stdin to stdout or save to fileteee command send stdin to stdout or save to file%                                                              /mnt/d/code/vim_learn  cat tee_example.sh
teee command send stdin to stdout or save to file%  
```
这里有个问题，像上面这样直接写内容的话在ctrl d 终止输入时会将内容重新输入一遍，但实际内容并没有写入这个文件，即只有前面一部分我输入的写入文件了，不知道这是不是和ctrl d 这个shell命令有关

在shell中管道符可以将前面命令的标准输出转为后面命令的输入，此时可以通过tee命令，同时将它保存到文件，又作为输出
```sh
 /mnt/d/code/vim_learn  ls |tee ls_tee.txt
total 0
drwxrwxrwx 1 andy andy 4096 May 17 17:32 .
drwxrwxrwx 1 andy andy 4096 May 12 22:21 ..
-rwxrwxrwx 1 andy andy    7 May 12 22:47 a.txt
-rwxrwxrwx 1 andy andy    0 May 12 22:21 b.txt
-rwxrwxrwx 1 andy andy  454 May 17 16:15 c1.sh
-rwxrwxrwx 1 andy andy  518 May 17 16:23 c2.sh
-rwxrwxrwx 1 andy andy   25 May 16 18:13 shell.sh
-rwxrwxrwx 1 andy andy  128 May 16 17:58 success_test.sh
-rwxrwxrwx 1 andy andy   49 May 17 18:58 tee_example.sh
drwxrwxrwx 1 andy andy 4096 May 16 08:23 temp
 /mnt/d/code/vim_learn  cat ls_tee.txt
total 0
drwxrwxrwx 1 andy andy 4096 May 17 17:32 .
drwxrwxrwx 1 andy andy 4096 May 12 22:21 ..
-rwxrwxrwx 1 andy andy    7 May 12 22:47 a.txt
-rwxrwxrwx 1 andy andy    0 May 12 22:21 b.txt
-rwxrwxrwx 1 andy andy  454 May 17 16:15 c1.sh
-rwxrwxrwx 1 andy andy  518 May 17 16:23 c2.sh
-rwxrwxrwx 1 andy andy   25 May 16 18:13 shell.sh
-rwxrwxrwx 1 andy andy  128 May 16 17:58 success_test.sh
-rwxrwxrwx 1 andy andy   49 May 17 18:58 tee_example.sh
drwxrwxrwx 1 andy andy 4096 May 16 08:23 temp
```
可以看到ls命令输出了，同时也定稿ls_tee.txt中了

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
test -f /etc/vim/vimrc &&echo 1 || echo 0
[ -f /etc/vim/vimrc ]&& echo 1|| echo 0
[[ -f /etc/vim/vimrc ]]&& echo 1|| echo 0
```

### 字符串操作符
特别注意：
> 表格中的字符串测试操作符号一定要用双引号“”括起来
> 比较符号两边有空格
```
-z "str"   若长度为0则为真 zero
-n "str"   若长度不为则为真  nonzero
"str1" = "str2" 若str1与str2相等则为真，可以用＝＝代替＝
"str1" != "str2" 若str1与str2不相等则为真 可用！==代替
```

```sh
 ~  [ "abc" = "1" ] &&echo 1||echo 0
0
 ~  [ "abc"="1" ] &&echo 1||echo 0  #等号两边没空格导致出错 
1
 ~  [ "abc" = 1 ] &&echo 1||echo 0
0
```

### 整数比较

```
[] test中使用      （（）） [[]]中使用       说明
-eq                == 或者=             equal
-ne                !=                   not equal
-gt                >                    greater than
-ge                >=                   greate equal
-lt                <                    less than
-le                <=                   less equal

```
"=" "!=" 在[]中不老板娘转义，而>,<在符号中需要转义，对数字不转义结果可能不会报错，但结果可能不对，同时也注意有无括号的区别
```sh
[ 2 > 1 ] && echo 1 || echo 0
[ 2 < 1 ] && echo 1 || echo 0
 ~  [ 2>1 ]&& echo 1||echo 0
0
 ~  [ 2<1 ]&& echo 1||echo 0
0
 ~  [ 2 < 1 ]&& echo 1||echo 0
1
 ~  [ 2 > 1 ]&& echo 1||echo 0
1
```

推荐[] -eq这种写法

### 逻辑连接符

```
[] test中使用    [[]]中使用      说明
-a               &&             and 两者都为真才为真
-o               ||             or 两者有一个为真即为真
！               ！             not 相反为真
```
如果使用[]但又想使用&&可以通过[] && [] 这种形式

#### 练习
```sh
#!/bin/bash

#判断参数个数
[ $# -ne 2 ] && {
    echo "USAGE: num1 num2"
    exit 1
}

#判断整数
[ "`echo "$1"|sed -r 's#[^0-9]##g'`" = "$1" ]||{
    echo "first arg must be int."
    exit 2
}
[ "`echo "$2"|sed -r 's#[^0-9]##g'`" = "$2" ]||{
    echo "seconde arg must be int."
    exit 2
}

#比较
[ $1 -lt $2 ]&& {
    echo "$1<$2"
    exit 0
}
[ $1 -eq $2 ]&& {
    echo "$1=$2"
    exit 0
}
[ $1 -gt $2 ]&& {
    echo "$1>$2"
    exit 0
}
```

read 方式
```sh
#!/bin/bash

read -p "pls input 2 num:" num1 num2
a=$num1
b=$num2

#判断参数个数
[ -z "$a" -o -z "$b" ] && {
    echo "USAGE: num1 num2"
    exit 1
}

#判断整数
[ "`echo "$a"|sed -r 's#[^0-9]##g'`" = "$a" ]||{
    echo "first arg must be int."
    exit 2
}
[ "`echo "$b"|sed -r 's#[^0-9]##g'`" = "$b" ]||{
    echo "seconde arg must be int."
    exit 2
}

#比较
[ $a -lt $b ]&& {
    echo "$a<$b"
    exit 0
}
[ $a -eq $b ]&& {
    echo "$a=$b"
    exit 0
}
[ $a -gt $b ]&& {
    echo "$a>$b"
    exit 0
}
```