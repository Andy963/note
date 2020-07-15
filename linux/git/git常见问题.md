
### git status乱码
现象
status查看有改动但未提交的文件时总只显示数字串，显示不出中文文件名，非常不方便。如下图：
```shell
 ~/Documents/vnote   dev ●  git status                                     
On branch dev
Your branch is up to date with 'origin/dev'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   python/_vnote.json
	modified:   python/flask/_vnote.json
	modified:   python/flask/view.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
	python/flask/flask_mail.md
	"python/\350\260\203\347\224\250\345\207\275\346\225\260\344\270\200\346\240\267\350\260\203\347\224\250\347\261\273\345\257\271\350\261\241.md"

```
原因
在默认设置下，中文文件名在工作区状态输出，中文名不能正确显示，而是显示为八进制的字符编码。

解决办法
将git 配置文件 core.quotepath项设置为false。quotepath表示引用路径，加上--global表示全局配置
```shell
git config --global core.quotepath false
```