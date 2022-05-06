# pip源

## 创建文件目录
linu在用户home目录下，win下为：C:\Users\Andy Andy即我的用户名

```shell
mkdir .pip
cd .pip
vim pip.conf
```

## 添加源
```python
[global]
index-url = http://mirrors.aliyun.com/pypi/simple/
extra-index-url=
        https://pypi.org/simple

[install]
trusted-host=
        mirrors.aliyun.com
        pypi.org

```

##  更多源的配置
```python
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
extra-index-url=
        http://mirrors.aliyun.com/pypi/simple/
        http://pypi.douban.com/simple/
        https://pypi.org/simple

[install]
trusted-host=
        pypi.tuna.tsinghua.edu.cn
        mirrors.aliyun.com
        pypi.douban.com 
        pypi.org
```
