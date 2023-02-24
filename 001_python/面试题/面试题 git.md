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

### 公司如何基于git 做的协同开发？
```
1.创建一个git裸服务器 （git init --bare）
2.从裸服务器将版本库克隆至本地（git clone ）
3.本地常规操作
4.推送版本至服务器 （git remote +  git push origin master）
5.从远程服务器拉取版本（git pull）
```

### 如何基于git 实现代码review？


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

### 如何为github 上牛逼的开源项目贡献代码？
```
1、fork需要协作项目
2、克隆/关联fork的项目到本地
3、新建分支（branch）并检出（checkout）新分支
4、在新分支上完成代码开发
5、开发完成后将你的代码合并到master分支
6、添加原作者的仓库地址作为一个新的仓库地址
7、合并原作者的master分支到你自己的master分支,用于和作者仓库代码同步
8、push你的本地仓库到GitHub
9、在Github上提交 pull requests
10、等待管理员（你需要贡献的开源项目管理员）处理
```

### git 中 .gitignore 文件的作用?
```
告诉git哪些文件不需要进行版本控制
```