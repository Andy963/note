### 97 结识global 命令
：global命令允许在某个指定模式的所有匹配行上运行Ex命令
：[range]global[!]/{pattern}/[cmd]
默认情况下global的作用域是整个文件

### 98 删除所有包含模式的文本行
：g/re/d   # re表示正则表达式， d则是删除
结果就是删除所有匹配的行
vg 表示 revert global 结果是删除所有不匹配的行，保留匹配的行。

### 99 将TODO项收集到寄存器
当文件中有多个todo时，若我们需要将todo收集起来，可以通过下面的命令将它们收到到寄存器a中
`:g/TODO/yank A`

### 100 将css文件中所有规则的属性按照字母排序
pass