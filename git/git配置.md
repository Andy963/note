## git配置

### 编码
```shell
 git config --global core.quotepath false # 显示 status 编码
 git config --global gui.encoding utf-8 # 图形界面编码
 git config --global i18n.commit.encoding utf-8 # 提交信息编码
 git config --global i18n.logoutputencoding utf-8 # 输出 log 编码
 export LESSCHARSET=utf-8 # 最后一条命令是因为 git log 默认使用 less 分页，所以需要 bash 对 less 命令进行 utf-8 编码
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