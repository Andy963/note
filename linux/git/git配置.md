# GIT


## git配置

使用配置项的顺序：本地配置--全局配置--系统配置
> 仓库级的配置文件：在仓库的 .git/.gitconfig，该配置文件只对所在的仓库有效。
> 全局配置文件：Mac 系统在 ~/.gitconfig，Windows 系统在 C:\Users\<用户名>\.gitconfig。
> 系统级的配置文件：在 Git 的安装目录下（Mac 系统下安装目录在 /usr/local/git）的 etc 文件夹中的 gitconfig。

### 编码
```shell
 git config --global core.quotepath false # 显示 status 编码
 git config --global gui.encoding utf-8 # 图形界面编码
 git config --global i18n.commit.encoding utf-8 # 提交信息编码
 git config --global i18n.logoutputencoding utf-8 # 输出 log 编码
 export LESSCHARSET=utf-8 # 最后一条命令是因为 git log 默认使用 less 分页，所以需要 bash 对 less 命令进行 utf-8 编码
```
### 配置beyond compare工具
```shell
git config --local merge.tool bc3
git config --local mergetool.path '/usr/local/bin/bcomp' #工具路径
git config --local mergetool.keepBackup false
```

### 配置实例
通过git config --global --list查看
```shell
user.name=Andy963
user.email=zjgxs518@126.com
core.autocrlf=false
core.quotepath=false
color.ui=true
http.proxy=socks5://127.0.0.1:10808
https.proxy=socks5://127.0.0.1:10808
```

### 中文显示

#### 中文文件名乱码
```shell
#git log内容已可正常使用、显示中文，但git status和push、pull时，中文文件名仍然乱码
#不对0x80以上的字符进行quote，解决git status/commit时中文文件名乱码
git config --global core.quotepath false
```

#### ls显示中文文件名
```shell
alias ls='ls --show-control-chars --color=auto'
```
ref: http://xstarcd.github.io/wiki/shell/git_chinese.html

## git 三大区

工作区,暂存区（stage或者叫index)，本地仓库
![](vimages/20200218220607879_11472.png =547x)




## 回滚操作git reset

 获取版本号
`git log`

执行回滚
`git reset --hard 版本号`

如果从v3版本回滚到v2版本，但你又想回滚到v3版本，此时不能用上面的命令，因为你看不到v3的版本信息
此时需要使用`git reflog`命令查看日志，这个日志包含回滚操作记录

然后执行`git rest --hard`

将文件从已修改的工作区回滚到未修改的状态
`git checkout -- filename`

将已经添加到暂存区的文件回滚到修改状态
`git reset HEAD fielname`
它有三个参数：
#--soft # 还原 HEAD
#--mixed # 还原 HEAD、Index # 默认参数
#--hard # 还原 HEAD、Index、Working Directory
![](vimages/20200218223248870_444.png =550x)


## git branch
```shell
git branch #查看当前分支
git branch dev #创建一个名为dev的分支
git checkout dev #将工作切换到dev分支上
git checkout -b dev #创建并切换到dev分支上，和上面两个指令的效果一样

git branch master
git merge bug #分支合并---首先切换到master分支，然后在master分支上执行merge指令来合并bug分支的代码
git branch -d bug 删除bug分支
```

## git rebase

当前有v1,v2,v3,v4,共4次提交记录，其中v2,v3,v4版本改变很小，当前处于v4版本。现在想将这三次提交记录合并成一次提交记录。

方式一：
```shell
git rebase -i v2版本号
```
表示将v2版本一直到目前最新版本(v4)全部合并到一起

方式二：
```shell
git rebase -i HEAD~3
```
3表示合并3个版本，而HEAD~3表示从当前最新的版本开始，合并最近的三个版本，即v2,v3,v4合并到一起。
在弹出的编辑框分别是三个pick 版本号， pick表示使用commit,这里需要将后面两个pick更改为squash(压缩）接着是更改commit 信息。

尽量合并(squash)自己本地版本,再push到远程，否则容易出现混乱。



git log --graph #图形化界面显示所有的提交记录
git log --graph --pretty=format:'%h %s' #让图形化界面显示记录的时候更清晰一些：%h是显
示版本号，%s是显示版本描述。

