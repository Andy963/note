
### filter and moment.js
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
```vue
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