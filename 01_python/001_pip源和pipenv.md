
## 源

### 创建文件目录
linu在用户home目录下，win下为：C:\Users\Andy Andy即我的用户名

```shell
mkdir .pip
cd .pip
vim pip.conf
```

### 添加源
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

###  更多源的配置
添加多个源有个问题是每次都会把所有的源都会遍历一次，最后才做选择，这样有个问题是如果访问其实一个源有问题时导致不断在尝试，从而浪费很多时间。

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


使用了一段时间的pipenv后，感觉这玩意问题真多，还是回到virtualenv + virtualenvwrapper的老路上来，连尝试poetry的兴趣都没有了，配置virtualenv+virtualenvwrapper原来有记录，现在就懒得记了，直接贴个链接吧：
<a href="https://segmentfault.com/a/1190000014935970" target="_blank">virtualenv+virutalenvwrapper</a>
## Pipenv
pipenv是Python官方推荐的包管理工具.
它能够自动为项目创建和管理虚拟环境，从Pipfile文件添加或删除安装的包，同时生成Pipfile.lock来锁定安装包的版本和依赖信息，避免构建错误。

pipenv主要解决了如下问题:

不用再单独使用pip和virtualenv, 现在它们合并在一起了
不用再维护requirements.txt, 使用Pipfile和Pipfile.lock来代替
可以使用多个python版本(python2和python3)
在安装了pyenv的条件下，可以自动安装需要的Python版本
### 全局安装
```
pip3 install pipenv
```

虚拟环境如果不存在的话，会自动创建
当install命令没有传递参数指定安装包时，所有[packages]里指定的包都会被安装
pipenv --three可以初始化一个python3版本的虚拟环境
pipenv --two可以初始化一个python2版本的虚拟环境

### 指定镜像源：
`pipenv install --pypi-mirror` 或者设置环境变量`PIPENV_PYPI_MIRROR`
但是有个坑就是即使你设置了，在它生成的Pipefile,Pipefile.lock中仍然显示的官方的pypi,可能这是最后的backend吧，下面是我的验证过程：
```sh
value=============>https://pypi.tuna.tsinghua.edu.cn/simple
value=============>https://pypi.tuna.tsinghua.edu.cn/simple
Creating a virtualenv for this project...
Pipfile: /home/andy/PycharmProjects/env_test/Pipfile
Using /usr/bin/python (3.8.10) to create virtualenv...
⠴ Creating virtual environment...created virtual environment CPython3.8.10.final.0-64 in 315ms
  creator CPython3Posix(dest=/opt/envs/env_test-SMK1PzgL, clear=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/andy/.local/share/virtualenv)
    added seed packages: pip==21.0.1, setuptools==60.9.3, wheel==0.37.1
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment! 
Virtualenv location: /opt/envs/env_test-SMK1PzgL
Creating a Pipfile for this project...
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Updated Pipfile.lock (db4242)!
Installing dependencies from Pipfile.lock (db4242)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/0 — 00:00:00
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
 andy@Andy  ~/PycharmProjects/env_test  echo $PIPENV_PYPI_MIRROR
https://pypi.tuna.tsinghua.edu.cn/simple
 andy@Andy  ~/PycharmProjects/env_test  vim Pipfile.lock
 andy@Andy  ~/PycharmProjects/env_test  cat Pipfile
[[source]]
url = "https://pypi.org/simple"
verify_ssl = true
name = "pypi"

[packages]

[dev-packages]

[requires]
python_version = "3.8"
```
最上面的两行打印，是我修改了pipenv的源码，最后面是Pipfile中的内容，可以看到安装时使用的是我指定的mirror,但Pipefile仍然是官方源，我在这里卡了半天，一直在找为什么没生效。

说句题外话，大家通常的做法是直接修改pipefile,pipefile.lock, 但是，事实上每次这么修改是很low的做法

### 指定虚拟环境目录
 设置`WORKON_HOME`变量为目标目录文件路径

#ref: [pypi-mirror](https://pipenv.pypa.io/en/latest/changelog/#id1)
### 常用命令
```python
# 安装包
pipenv install
pipenv install requests==2.13.0

# 激活当前项目的虚拟环境
pipenv shell

# 安装开发依赖包
pipenv install pytest --dev

# 图形显示包依赖关系
pipenv graph

# 生成lockfile
pipenv lock

# 删除所有的安装包
pipenv uninstall --all
```

### 导入requirements.txt
当在执行pipenv install命令的时候，如果有一个requirements.txt文件，那么会自动从requirements.txt文件导入安装包信息并创建一个Pipfile文件。

同样可以使用`pipenv install -r path/to/requirements.txt`来导入requirements.txt文件

### 指定Python的版本信息
在创建虚拟环境的时候，我们可以指定使用的python版本信息，类似pyenv

```python
 pipenv --python 3
 pipenv --python 3.6
 pipenv --python 2.7.14
```
pipenv会自动扫描系统寻找合适的版本信息，如果找不到的话，同时又安装了pyenv, 它会自动调用pyenv下载对应的版本的python

### 指定安装包的源
如果我们需要在安装包时，从一个源下载一个安装包，然后从另一个源下载另一个安装包，我们可以通过下面的方式配置

```
[[source]]
url = "https://pypi.python.org/simple"
verify_ssl = true
name = "pypi"

[[source]]
url = "http://pypi.home.kennethreitz.org/simple"
verify_ssl = false
name = "home"

[dev-packages]

[packages]
requests = {version="*", index="home"}
maya = {version="*", index="pypi"}
records = "*"
```
设置了两个源，同时指定requests包从home源下载，maya包从pypi源下载

### 生成requirements.txt文件
我们也可以从Pipfile和Pipfile.lock文件来生成requirements.txt

生成requirements.txt文件
` pipenv lock -r`

生成dev-packages的requirements.txt文件
`pipenv lock -r -d`

### 自定义虚拟环境的路径
默认情况下,pipenv使用pew来管理虚拟环境的路径，我们可以自定义WORKON_HOME环境变量来设置虚拟环境的路径。比如:
`export WORKON_HOME=~/.venvs`
我们也可以通过设置环境变量PIPENV_VENV_IN_PROJECT使虚拟环境在每个项目的根目录下project/.venv

### 自动激活虚拟环境
配合virtualenv-autodetect和设置PIPENV_VENV_IN_PROJECT环境变量可以自动激活虚拟环境。

在.bashrc或.bash_profile中配置如下
```
export PIPENV_VENV_IN_PROJECT=1
source /path/to/virtualenv-autodetect.sh
```
如果使用了oh-my-zsh, 可以直接使用它的插件形式


### courtesy notice
> pipenv detects itself running in a virtual env even though there isn't on

: installed pipenv via pip but not pip3
```shell
pip3 uninstall pipenv
pip3 install pipenv
```
ref: [courtesy notice](https://github.com/pypa/pipenv/issues/4327)


#### 安装插件
$ git@github.com:RobertDeRose/virtualenv-autodetect.git ~/.oh-my-zsh/custom/plugins
再修改.zshrc文件启动插件

#### 找到启动plugins的行添加启用插件
plugins=(... virtualenv-autodetect)
