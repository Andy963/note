
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