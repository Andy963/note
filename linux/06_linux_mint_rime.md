### install 
```
apt install ibus-rime
apt install librime-data-wubi
```

### add rime
```
进入设置->区域和语言
点输入源下边那个+号
你会发现现在已经多了一个汉语(Rime)，把它添加进来
这时你按win+space就可以把输入法切换到rime了，但是还是无法输入五笔，还需要设置一下.
```

### add wubi
```
编辑这个文件：~/.config/ibus/rime/build/default.yaml
这个文件也有可能是~/.config/ibus/rime/default.yaml，也就是少了一层build目录.
在schema_list下边添加一行内容:- schema: wubi86，然后把其他的方案都删除掉.（其他方案就是下图方框中的内容）
schema_list:
  - schema: wubi86
  - schema: luna_pinyin
  - schema: luna_pinyin_simp
  - schema: luna_pinyin_fluency
  - schema: bopomofo
  - schema: bopomofo_tw
  - schema: cangjie5
  - schema: stroke
  - schema: terra_pinyin

```

### 部署
```
按win+space把输入法切换到rime
然后点开右上角输入法的下拉菜单，点击部署
```

ref: https://blog.csdn.net/Sacredness/article/details/92195032