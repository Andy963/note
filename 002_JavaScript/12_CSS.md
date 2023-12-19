Css 的规则主要: 选择器 + 声明  两部分构成，前者表示是谁，后者表示要怎样。

css 有多种引入的方式：按优先级排序为：

- 行内式
- 嵌入式
- 链接式
- 导入式

行内式是通过在标签内通过`style`标签，嵌入式则在html的`head`标签内再嵌入`style`标签，链接式则是通过`link`标签的`href`属性指定文件路径。导入式则是在`style`标签中通过
`@import 'path/to/css'`的方式导入。导入式有一个缺点是它会先显示无样式的页面，再显示有样式的页面，因为它称装载网页，再加载样式。链接式虽然也是文件导入，但不存在这个问题。

### 选择器

#### 基本选择器：
看下面这张图：
![](https://raw.githubusercontent.com/Andy963/notePic/main/vnote/02_javascript/12_css.md/509531122239177.png =591x)


#### 组合选择器：
E,F 多元素选择器，同时匹配所有E,F元素，E,F之间用逗号分隔

E F后代元素选择器，匹配所有E元素后代F元素，E,F之间用空格

E>F 子元素选择器，匹配所有E元素的子元素F

E+F 毗邻元素选择器，匹配所有E元素之后的<u>**同级F元素**</u>

E ~ F 普通兄弟选择器

### 属性选择器

E[attr~=val] 匹配所有attr属性具有多个空格分隔的值，其中一个值等于“val"的E元素td[class~="name"]{color:red}
E[attr^=val] 匹配属性值以指定值开头的每个元素，div[class^="test"]{background:red}
E[attr$=val] 匹配属性值以指定结尾的每个元素,div[class$="test"]{color:blue}
E[attr*=val] 匹配属性值中包含指定值的每个元素,div[class="test"]{color:green}

### 伪类
*anchor* 伪类主要用来控制链接的显示样式

a:link（没有接触过的链接）,用于定义了链接的常规状态。
a:hover（鼠标放在链接上的状态）,用于产生视觉效果。   
a:visited（访问过的链接）,用于阅读文章，能清楚的判断已经访问过的链接。
a:active（在链接上按下鼠标时的状态）,用于表现鼠标按下时的链接状态。

*before* && *after* 在元素前后插入内容

```css
p:before{content:"hello";color:red;display: block;}
```

### 选择器的优先级
显式声明的规则都可以覆盖继承的样式。

- 内联的样式表权值最高  1000
- id属性个数            100
- class属性个数         10
- html标签个数          1

这些规则将数字逐位相加，得到最终权重，在比较取舍时按照从左到右的顺序逐位比较。但是10个class叠加并不能比id的权重高
但问题是：这些权重决定了显示吗？实际上最终显示的样式并不是按照它的属性个数来显示的？

文内的样式优先级为1000，即直接写在标签内的，始终高于外部定义的
!important声明高于一切，优先级为10000
如果优先权一样，则按照在源码中出现的顺序决定，后来者居上，覆盖前面的。
继承来的样式低于一切其它规则