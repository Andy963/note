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

### vue 进入同一路由，页面不刷新
最近在写vue前端时，遇到一个问题，导航栏对应的路由是一样的，而且因为没有参数，即进入完全相同的路由，由于vue的机制，这种情况它是不会刷新页面的，而是重用了之前的页面，而我要达到的效果是再次点击时仍刷新，即向后端重新请求数据。
最后根据网上的方法，试了好几种，最后的解决办法是：
- 在请求是router.push()中添加了query:{time:time}这个time是动态获取的
- 在vue-view中添绑定了:key=key 这个key也是动态生成的
最后这样不管什么情况下点击导航都会重新请求数据，但也导致了问题，就是url中带着一个完全没用的参数time.

并且因为这个会导致另外一个问题： 为了达到在点击后仍能回到之前的页面，我在localStorage中存在了每次跳转时的路由，在创建页面时先去LocalSorage中获取保存的路由，如果存在就跳转到该页面，如果不存在则跳转到首页，因为上面的原因，导致这种情况失败。
最后的解决办法是：在保存时对路由做一定的处理，再往localStorage中存，具体的代码就不贴了，一是不记得，另外觉得这种方法只是临时办法，不优雅，如果有更好的办法后面再更新。

### vue 全局函数

```js
Vue.prototype.checkLogin = function () {
    let userId = localStorage.getItem('user_id')
    if (userId === '' || userId === null || userId === undefined) {
        return true
    } else {
        return false
    }
}

Vue.prototype.checkLogin = function () {
    let userId = localStorage.getItem('user_id')
    return userId === '' || userId === null || userId === undefined;
}

```

### vue 使用nginx二级路由
- 在项目要目录创建Vue.config.js

```js
module.exports = {
    publicPath: '/hlt'
}

const router = new VueRouter({
    # mode: 'history',
    routes: [
        {path: '/', component: Home},
    ],
    base: "/hlt"
});
```

### vue高亮 显示markdown
#### install 

```shell
npm install marked -S
npm install highlight.js --save
```

#### import
main.js
```js
import hljs from 'highlight.js'
import 'highlight.js/styles/monokai-sublime.css'
```
这里使用的sublime的高亮，也可以选择其它的，比如vs.css

marked 在需要使用的页面导入
```js
import marked from 'marked'
```

#### use
```js
#<div style="margin-top:30px;" v-highlight v-html="content">
this.content = marked(this.article.content)
```

### element ui table header height
when i am using element-ui table, I have tried many ways to changer the table header height, but all of it failed. the follow one is the success one
:cellStyle="CellStyle"
:header-cell-style="headerCellStyle"
```js 
CellStyle(){
    return {padding:'5px',height:'25px',textAlign:'center'}
}

headerCellStyle(){
    return {textAlign:'center',lineHeight:'30px',padding:'2px',height:'30px'}
}
```
ps: if the style name with a "-", you should change the name to camel case ,for ex: text-align ---> textAlign