
### filter and moment.js
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">

</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script src="../moment.js"></script>
<script>
    // 全局过滤器
    Vue.filter('myTimeFilter', function (val, formatStr) {
        return moment(val).format(formatStr);
    })

    // init a object
    let App = {
        data() {
            return {
                msg: 'hello world',
                now: new Date()
            }
        },
        template: `
        <div>我是app,反转后的hello world ==> {{ msg | reverseWorld }}
        <h2>{{ now | formatTime('YYYY-MM-DD') }}</h2>
        </div>
        `,
        filters: {
            reverseWorld: function (val) {
                console.log(val);
                return val.split('').reverse().join('');
            },
            formatTime: function (val, formatStr) {
                return moment(val).format(formatStr);
            }
        }
    }
    new Vue({
        el: '#app',
        // bind data
        data: {},
        template: `
        <div>
        <App></App>
        </div>
        `,
        components: {
            App
        }
    })
</script>
</html>
```

### life cycle
keep-alive 是Vue 提供的内置组件，主要作用让组件产生缓存
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <App></App>
</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script src="../moment.js"></script>
<script>
    let Life = {
        data() {
            return {
                msg: "andy is here.",
                timer:'',
                count:0
            }
        },
        template:
            `
        <div>
        I'm life component。<br> {{ msg }}<br>
         {{ count }}
        <button @click="change">修改</button>
</div>
        `,
        methods: {
            change() {
                this.msg = 'want to change?'
            }
        },
        beforeCreate() {
            console.log('not created yet.')
        },
        created() {
            console.log('already created.')
            // you can send ajax request to get data, and influence the view of html
            this.timer = setInterval(()=>{
                this.count ++;
            },1000);
        },
        beforeMount() {
            // 装载数据到dom之前调用
        },
        mounted() {
            // 装载数据到DOM之后会调用，可以获取到真实存在的DOM元素，vue操作以后的DOM
        },
        beforeUpdate() {
            // 更新之前调用此钩子，获取原始DOM
            console.log(document.getElementById('app').innerHTML);
            // <div><div>I'm life component。<br> andy is here.<br> <button>修改</button></div></div>
        },
        updated() {
            // 更新之后获取此钩子，获取最新的DOM
            console.log(document.getElementById('app').innerHTML);
            // <div><div>I'm life component。<br> want to change?<br> <button>修改</button></div></div>
        },
        beforeDestroy(){
            console.log('I will let Life disappear');
        },
        destroyed(){
            // 定时器的销毁要在此处理
            console.log('Disappear.');
            clearInterval(this.timer);
        }
    }
    let App = {
        data() {
            return {
                isShow:true
            }
        },
        template: `
        <div>
            <Life v-if="isShow"></Life>
            <button @click="isShow=!isShow">改变Life</button>
        </div>
        `,
        components: {
            Life: Life
        }
    }
    new Vue({
        el: '#app',
        // bind data
        data: {},
        // template: `
        // <div>
        // <App></App>
        // </div>
        // `,
        components: {
            App
        }
    })
</script>
</html>
```
### router 
$.route 路由信息对象
$.router 路由对象（VueReouter)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">

</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script src="../Vue-router.js"></script>
<script>
    // 如果以后模块化编程，Vue.Prototype.$VueRouter = VueRouter 将VueRouter挂载到Vue原型上
    // Vue.use(VueRouter);
    // 1. 定义 (路由) 组件。
    // 可以从其他文件 import 进来
    const Home = {
        data() {
            return{}
        },
        template: '<div>Home page </div>'
    };

    const Course = {
        data() {
            return {}
        },
        template: '<div>Course</div>'
    };

    // 2. 定义路由
    // 每个路由应该映射一个组件。 其中"component" 可以是
    // 通过 Vue.extend() 创建的组件构造器，
    // 或者，只是一个组件配置对象。
    // 我们晚点再讨论嵌套路由。
    // const routes = [
    //     {path: '/', component: Home},
    //     {path: '/course', component: Course}
    // ]

    // 3. 创建 router 实例，然后传 `routes` 配置
    // 你还可以传别的配置参数, 不过先这么简单着吧。
    const router = new VueRouter({
        //routes // (缩写) 相当于 routes: routes
        mode: 'history',// 默认为hash模式，路由看起来很乱，历史模式就会很清晰
        routes: [
            // 重定向
            // {
            //     path: '/',
            //     redirect:'/home'
            // }
            {
                path: '/',
                component: Home
            },
            {
                path: '/course',
                component: Course
            }
        ],
    })

    let App = {
        data() {
            return {}
        },
        template:
            `<div>
               <div class="header">
               <router-link to="/">首页</router-link>
               <router-link to="/course">课程</router-link>
                </div>

                <router-view></router-view>
            </div>
            `,
    };

    new Vue({
        el: '#app',
        // 挂载路由
        router: router,
        data() {
            return {}
        },
        template:
            `
                <App></App>
            `,
        components: {
            App
        }
    })
</script>

</html>
```
### named router
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">

</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script src="../Vue-router.js"></script>
<script>
    const Home = {
        data() {
            return {}
        },
        template: '<div>Home page </div>'
    };

    const Course = {
        data() {
            return {}
        },
        template: '<div>Course</div>'
    };

    const router = new VueRouter({
        mode: 'history',// 默认为hash模式，路由看起来很乱，历史模式就会很清晰
        routes: [
            {
                path: '/',
                name: "Home", // 给路由取个名，类似django中的路由后面的name
                component: Home
            },
            {
                path: '/course',
                name: "Course",
                component: Course
            }
        ],
    })

    let App = {
        data() {
            return {}
        },
        <!-- 使用命名的路由 用name 指定，并绑定to-->
        template:
            `<div>
               <div class="header">

               <router-link :to="{name:'Home'}">首页</router-link>
               <router-link :to="{name: 'Course'}">课程</router-link>
                </div>

                <router-view></router-view>
            </div>
            `,
    };

    new Vue({
        el: '#app',
        // 挂载路由
        router: router,
        data() {
            return {}
        },
        template:
            `
                <App></App>
            `,
        components: {
            App
        }
    })
</script>

</html>
```
### dynamic router
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">

</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script src="../Vue-router.js"></script>
<script>
    const User = {
        data() {
            return {
                user_id: null
            }
        },
        template: '<div>我是用户(id={{ user_id }} )</div>',
        // 这里用create会出现第二次请求的id不会变化的情况，因为vue 组件复用
        // created() {
        //     console.log(this.$route.params.id);
        // },
        watch: {
            '$route'(to, from) {
                console.log(to);
                this.user_id = to.params.id
                console.log(from);
            }
        }
    };

    const Course = {
        data() {
            return {}
        },
        template: '<div>Course</div>'
    };

    const router = new VueRouter({
        // mode: 'history',// 默认为hash模式，路由看起来很乱，历史模式就会很清晰
        routes: [
            {
                path: '/user/:id',
                name: "User", // 给路由取个名，类似django中的路由后面的name
                component: User
            },
            {
                path: '/course',
                name: "Course",
                component: Course
            }
        ],
    })

    let App = {
        data() {
            return {}
        },
        <!-- 使用命名的路由 用name 指定，并绑定to-->
        template:
            `<div>
               <div class="header">

               <router-link :to="{name:'User',params:{id:1}}">用户1</router-link>
               <router-link :to="{name:'User',params:{id:2}}">用户2</router-link>
               <router-link :to="{name: 'Course'}">课程</router-link>
                </div>

                <router-view></router-view>
            </div>
            `,
    };

    new Vue({
        el: '#app',
        // 挂载路由
        router: router,
        data() {
            return {}
        },
        template:
            `
                <App></App>
            `,
        components: {
            App
        }
    })
</script>

</html>
```

### program router
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">

</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script src="../Vue-router.js"></script>
<script>
    const Home = {
        data() {
            return {}
        },
        template: '<div>Home page </div>'
    };

    const User = {
        data() {
            return {
                user_id: null
            }
        },
        template:
            `
         <div>
         <p>我是user: {{ user_id }}</p>
                <button @click="jump">跳转首页</button>
                </div>
        `
        ,
        methods: {
            // 编程式导航，点击按钮跳转，而不是通过router-link跳转
            jump() {
                this.$router.push({
                    name: "Home",
                })
            }
        },
        watch: {
            '$route'(to, from) {
                console.log(to);
                this.user_id = to.params.id
                console.log(from);
            }
        }
    };

    const router = new VueRouter({
        // mode: 'history',// 默认为hash模式，路由看起来很乱，历史模式就会很清晰
        routes: [
            {
                path: '/user/:id',
                name: "User", // 给路由取个名，类似django中的路由后面的name
                component: User
            },
            {
                path: '/home',
                name: "Home",
                component: Home
            }
        ],
    })

    let App = {
        data() {
            return {}
        },
        <!-- 使用命名的路由 用name 指定，并绑定to-->
        template:
            `<div>
               <div class="header">

               <router-link :to="{name:'User',params:{id:1}}">用户1</router-link>
               <router-link :to="{name:'User',params:{id:2}}">用户2</router-link>
<!--               <router-link :to="{name: 'Course'}">课程</router-link>-->
                </div>

                <router-view></router-view>
            </div>
            `,
    };

    new Vue({
        el: '#app',
        // 挂载路由
        router: router,
        data() {
            return {}
        },
        template:
            `
                <App></App>
            `,
        components: {
            App
        }
    })
</script>

</html>
```

### 相同路由不重新请求的解决办法：
```js
<script>
export default {

  created() {
    // 当路由参数变化时，/user/1切换到/user/2原来的组件实例会被利用
    // 因为两个路由渲染了同一个组件，
    console.log(this.$route.params.id)
  },
  // 解决方法一
  // watch:{
  //   $route:(to,from)=>{
  //     console.log(to.params.id)
  //     // 发起ajax请示后端接口数据
  //   }
  // }
  // 解决方法二
  beforeRouteUpdate(to, from, next) {
    console.log(to.params.id)
    // 一定要调用next,不然会阻塞整个路由
    next();
  }
}
</script>
```

### 404路由
基于优先级的考虑，这条必须放在最后面，即当其它所有路由都无法匹配到时，匹配这条
```js
{
  path: '*',
  component:()=>import('@/views/404')
}
```

### alias 别名, redirect重定向
```js
{
 path:'/home',
 name:'home',
 component:Home,
 alias: '/aaa'
 redirect:'/index'
}
```
### 路由组件传值
组件a中
```js
{
  path:'/user/:id',
  name:'user',
  component:User,
  props:true // 这里设置为true,就可以将上面的id传给对应的user组件中
}

// 或者为一个函数
{
  path:'/user/:id',
  name:'user',
  component:User,
  props:(route)=>（{
   id:route.params.id,
   title:route.query.title
}

）
}
```
在user组件中接收：
```js
export default{
    // 在这里接收，然后可以直接使用id
    props:['id'],
}
```

### 编程式导航
通过方法来跳转
```js
goRoute(){
    this.$router.push('/')
    this.$router.push('name')
    this.$router.push({
     path:'/'
     })
    this.$router.push({
    name:'user',
    params:{id:2}
     })
    this.$router.push({
    name:'user',
    query:{id:2}
     })

}

goBack(){
    this.$router.goback(-1) // 负值为后退，正值为前进
}
```


### get dom ref
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">

</div>

</body>
<script src="../Vue.js"></script>
<script>
    Vue.component('Test', {
        data() {
            return {}
        },
        template: `<p>我是输入框</p>`
    })
    let App = {
        data() {
            return {}
        },
        template: `
        <div>
        <input type="text" ref="input1">
        <Test ref="test" />
        </div>`,
        mounted() {
            this.$refs.input1.focus(); // 获取原生的DOM
            // this.$refs.test 获取到的是组件Test实例对象
            // this.$refs.test.$parent 获取父组件
            // this.$refs.test.$root 获取根组件即Vue对象
            // this.$children 获取子组件
            for (let key in this.$refs) {
                this.$refs[key];
            }
        }

    }
    new Vue({
        el: "#app",
        data() {
            return {}
        },
        template: `
            <App></App>
        `,
        components: {
            App
        }
    })
</script>
</html>
```

### css scoped
```vue

<style scoped>
这样定义的style只对当前组件有效
</style>
```

### $ref
```html
<div ref='div'>
<input ref='input'>
</div>
<Home ref='home'></Home>

let inputDom = this.$refs.input
inputDom.focus() // 获取焦点
//如果给组件绑定ref，则this.$refs获取到的是组件实例化对象
.$parent获取父组件
.$root获取要组件，vue
.$children
```

### 自定义指令
自定义指定大致步骤：
- 安装 vuex
- 创建vuex文件夹，和对应的文件
- 在main中引入 vuex,并注入
- 在vuex中声明变量，此时可以在任意地方访问
- getters, mutation/commit ,actions/dispatch

#TODO 些处待补充实例

### vue指定中的el parentNode 为Null
最近 有写一个vue的权限管理，因为考虑到要精确到按钮级别，在元素渲染时会验证是否有权限，如果没有权限会通过该元素的父级换到该元素，所以用到了`el.parentNode.removeChild(el)`, 但总是遇到el 为null的情况，经搜索发现是钩子函数没用对的问题：
```js
if (el.parentNode && !Vue.prototype.$_has(binding.value)) {
            el.parentNode.removeChild(el);
        }
```
钩子函数：
```
bind：只调用一次，指令第一次绑定到元素时调用。在这里可以进行一次性的初始化设置。
inserted：被绑定元素插入父节点时调用 (仅保证父节点存在，但不一定已被插入文档中)。
update：所在组件的 VNode 更新时调用，但是可能发生在其子 VNode 更新之前。指令的值可能发生了改变，也可能没有。但是你可以通过比较更新前后的值来忽略不必要的模板更新 (详细的钩子函数参数见下)。
componentUpdated：指令所在组件的 VNode 及其子 VNode 全部更新后调用。
unbind：只调用一次，指令与元素解绑时调用。
```
通过官方的这个文档，可以理解的，之前出错是使用的bind钩子，而使用bind在第一次绑定到元素时，父节点可能还没绑定，或者是第二次调用时。（具体的得深入原理）
ref:https://www.cnblogs.com/chenmz1995/p/11453228.html

#### 自定义指令
项目中使用到自定义指令，比较复杂，这里用官方的一个小例子来作一下记录，大致的使用
#### 局部自定义指令
```js
directives: {
  focus: {
    // 指令的定义
    inserted: function (el) {
      el.focus()
    }
  }
}
/**
inserted 为钩子函数，即什么时候绑定
focus为指令名称，在vue中使用时为v-facus
fuction部分为具体的操作
*/

```

#### 全局指令
```js
Vue.directive('focus', {
  // 当被绑定的元素插入到 DOM 中时……
  inserted: function (el) {
    // 聚焦元素
    el.focus()
  }
})
```