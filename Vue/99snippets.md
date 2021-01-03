### show html but not source code
```js
   show_html(str) {
                return marked(str
                    .replace(str ? /&(?!#?\w+;)/g : /&/g, '&amp;')
                    .replace(/&lt;/g, "<")
                    .replace(/&gt;/g, ">")
                    .replace(/&quot;/g, "\"")
                    .replace(/&#39;/g, "\\'"))
            },
```

### elementUi navMenu line height
```vue
::v-deep .el-menu li {
  height: 35px;
  line-height: 35px;
}
// or like this
::v-deep .el-menu-item {
	height: 45px;
	line-height: 45px;
}
::v-deep .el-submenu__title{
	height: 45px;
	line-height: 45px;
}
```