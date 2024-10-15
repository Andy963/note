## git

### git 常见命令
```git
init add commit branch checkout pull push clone rebase merge
```
### 简述以下git 中stash 命令作用以及相关其他命令
```
作用：保存当前暂存区，工作区的进度
git stash list 显示保存进度的列表
git stash pop 恢复最新进度到工作区（恢复后会删除当前进度
git stash apply 恢复最新的进度到工作区，但不会删除当前进度
git stash drop 删除一个进度
git stash clear 删除所有保存的进度
```

### git 中 merge 和 rebase 命令 的区别
```
rebase是找共同的祖先，会并了之前的提交历史，去掉了merge commit ,得到的是简洁的提交历史 
merge记录了真实的提交历史，包括分支的，会产生一个merge commit
```

### git 如何实现v1.0 、v2.0 等版本的管理？
```
git tag
```

### 什么是gitlab？
```
gitlab 是一个基于git实现的在线代码仓库软件，提供web可视化管理界面，通常用于企业团队内部协作开发
```

### github 和gitlab 的区别？
```
GitLab是可以部署到自己的服务器上,适合团队内部协作开发，数据都可以自己控制
github则主要是开源代码分享，但也可以建私有仓库，但数据库自己不能控制
```

