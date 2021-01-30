### mvvm
mvvm结构图解

![](vimages/2479014148401.png =1000x)


### 事件修饰符
事件修饰符有：self,prevent,stop,once等
self:只能阻止自己的事件冒泡
prevent：阻止元素默认事件
stop:阻止事件继续传递
once:只触发一次

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="../Vue.js"></script>
</head>
<body>
<div id="app">
    <div class="inner" @click="divHandler">
        <input type="button" value="戳他" @click="btnHandler">
    </div>
    <div>
        <a href="http://www.google.com" @click.prevent="linkClick">百度一下</a>
    </div>
</div>
<script>
    /*
    默认情况下，点击内部的按钮，会向外面传播，即先btn,后div
    当我在btn上使用stop修饰符 @click.stop，那么事件就不会向外传播，而只在btn上触发

    <a href="http://www.google.com" @click.prevent="linkClick">百度一下</a>
    prevent阻止默认事件,点击链接后不会跳转

    <div class="inner" @click.capture="divHandler">
        <input type="button" value="戳他" @click="btnHandler">
    </div>
    capture 在外层的div,即点击btn时会选被外层div捕获，触发顺序也是div, btn


    <div class="inner" @click.self="divHandler">
        <input type="button" value="戳他" @click="btnHandler">
    </div>
    .self  在外层div,@click.self.只有点击当前元素才会触发事件

    <div class="inner" @click="divHandler">
        <input type="button" value="戳他" @click.once="btnHandler">
    </div>
    .once 只会触发一次，可以和其它修饰符一起用 如@click.prevent.once

    stop 与self的区别
    self只能阻止自己的事件冒泡，但不能阻止别的事件的冒泡
     */
    var vm = new Vue({
        el: '#app',
        data: {},
        methods: {
            divHandler() {
                console.log('div点击事件')
            },
            btnHandler() {
                console.log('btn点击事件')
            },
            linkClick() {
                console.log('触发a点击事件')
            }
        },
    })
</script>
</body>
</html>
```

### v-bind:value && v-model
v-bind:value单向绑定，v-model则是双向绑定
```js
 <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="../Vue.js"></script>
</head>
<body>
<div id="app">
    <input type="text" style="width:100%;" :value="msg">
    <input type="text" style="width:100%;" v-model="msg">

</div>
<script>
    /*
    v-bind:value 只能单向绑定，从model(data)到v（html),无法双向
    v-model 可以实现表单元素和model中数据的双向绑定
    表单元素包括：input(radio,text,address,email),select, checkbox, textarea等
     */
    var vm = new Vue({
        el: "#app",
        data: {
            msg: '好好学习，天天向上'
        },
        methods: {}
    })
</script>
</body>
</html>
```
### watch
对于复杂数据结构如对象，数组需要使用深度监视才能监测到变化 

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="../Vue.js"></script>
</head>
<body>
<div id="app">
    <input type="text" v-model="msg">
    <h3>{{msg}}</h3>
    <h3>{{students[0].name}}</h3>
    <button @click="students[0].name='jack'">change</button>
</div>
<script>
    var vm = new Vue({
        el: "#app",
        data: {
            msg: '',
            students: [{'name': 'andy'}]
        }
        ,
        watch: {
            // 对于基本的字符串，数字等可以直接使用watch,而复杂数据结构如对象，数组等需要使用深度监视才行
            'msg': function (newVal, oldVal) {
                console.log(newVal, oldVal)
            },
            // 当监测的对象为一个对象时 这种情况下，是监测不到变化的
            // 'students': function (newVal, oldVal) {
            //     console.log(newVal, oldVal)
            // },
            // 深度监视,因为监视的是对象的内存地址，而这个地址不会变化 ，所以也就监测不到
            students: {
                deep: 'true',
                handler: function (newVal, oldVal) {
                    console.log(newVal[0].name)
                }
            }
        }
    })
</script>
</body>
</html>
```

### compute setter
通常情况下getter就够了，setter较少用

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>compute setter</title>
    <script src="../Vue.js"></script>
</head>
<body>
<div id="app">
    <input type="text" v-model="content" @input="handleInput">
    {{content}}
</div>
<script>
    var vm = new Vue({
        el: "#app",
        data: {
            msg: '',
        },
        methods: {
            handleInput: function (event) {
                // console.log(event.target.value) 获取target的值
                const {value} = event.target
                this.content = value
            }
        },
        computed: {
            // 当要使用set时，content应该是一个对象，而非函数
            // content: function () {
            //     return this.msg
            // }
            content: {
                set: function (newVal) {
                    console.log(newVal)
                    this.msg = newVal
                },
                get: function () {
                    return this.msg
                }
            }
        }
    })
</script>
</body>
</html>
```

### filter
filter 与django filter 类似，通过 “|”来处理

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>filter</title>
    <script src="../Vue.js"></script>
</head>
<body>
<div id="app">
    <h3>{{price | filterPrice('$')}}</h3>
</div>
<script>
    // 创建全局过滤器
    Vue.filter('filterReverse', (val) => {
        return val.split('').reverse().join('')
    })
    var vm = new Vue({
        el: "#app",
        data: {
            price: 10,
        },
        // 局部过滤器
        filters: {
            filterPrice: function (price, flag) {
                return flag + price
            }
        }
    })
</script>

</body>
</html>
```