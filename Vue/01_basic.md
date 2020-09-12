## basic
### template
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <!-- template language -->
    <p>{{ msg }}</p>
    <p>
        {{ 'string will not change'}}
    </p>
    <!--    2-->
    <p>{{ 1+1 }}</p>
    <!--    name:andy-->
    <p>{{ {'name':'andy'} }}</p>
    <!--    andy-->
    <p> {{ person.name }}</p>
</div>

</body>
<!--import-->
<script src="../Vue.js"></script>
<script>
    // init a object
    new Vue({
        el: '#app',
        // bind data
        data: {
            msg: 'cucumber',
            person: {
                name: 'andy',
                age: 29
            }
        }
    })
</script>
</html>
```

### command
#### v-text && v-html
v-text ==> innerText
v-html ==> innerHtml

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <p>{{ msg }}</p>
    <div v-text="msg"></div>
    <div v-html="msg"></div>
    <div>{{ add(2,3) }}</div>
</div>

</body>
<script src="../Vue.js"></script>
<script>
    // init a object
    new Vue({
        el: '#app',
        // bind data
        // single model
        data() {
            let msg = '<p>cucumber</p>'
            // data is a function, and must return and object
            return {'msg': msg}
        },
        methods: {
            add(x, y) {
                return x + y
            }
        }
    })
</script>
</html>
```
you can use methods to define a function like add.

#### v-show v-if
v-show ==> display
v-show="isShow" the value must be a string
v-on:click ==> onclick
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .box {
            width: 200px;
            height: 100px;
            background-color: red;
        }
    </style>
</head>
<body>
<div id="app">
    <!--    the value of v-show must be a string-->
    <button v-on:click="handleClick">隐藏</button>
    <div class="box" v-show="isShow"></div>
    <div v-if="isShow">你看到我了吗</div>
    <div v-if="Math.random()>0.5">
        有了
    </div>
    <div v-else>没了</div>
</div>

</body>
<script src="../Vue.js"></script>
<script>
    // init a object
    new Vue({
        el: '#app',
        // bind data
        // single model
        data() {
            return {isShow: true}
        },
        methods: {
            handleClick() {
                this.isShow = !this.isShow
            }
        }
    })
</script>
</html>
```

#### v-bind v-on
v-bind can be simplify to : bind any attr
v-on can be simplify to @  listen any event
class should be : v-bind:class="{active:isActive}"

```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .box {
            background-color: green;
            width: 200px;
            height: 100px;
        }

        .active {
            background-color: red;
        }
    </style>
</head>
<body>
<div id="app">
    <div>
        <img src="./1.jpg" alt="静态图片">
        <img v-bind:src="imgSrc" v-bind:alt="alt">
        <div class="box" v-bind:class="{active:isActive}"></div>
        <button v-on:click="changeColor">change</button>
        <!--        v-bind can be simplifed to :-->
        <!--        v-on can simplify to @-->
        <div class="box" :class="{active:isActive}"></div>
        <button @click="changeColor">change</button>
    </div>
</div>

</body>
<script src="../Vue.js"></script>
<script>
    new Vue({
        el: '#app',
        data() {
            return {
                imgSrc: './1.jpg',
                alt: "动态图片",
                isActive: true
            }

        },
        methods: {
            changeColor() {
                this.isActive = !this.isActive
            }
        }
    })
</script>
</html>
```
#### v-for
when you use for, it's better bo bind the id to li by using: :key="item.id"
if you loop a object, it return (value, key)
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <ul v-if="data.status==='ok'">
        <!--        use :key to bind the id to the li-->
        <li v-for="(item,index) in data.users" :key="item.id">
            {{ index}}. {{ item.id }} -- {{ item.name }} -- {{ item.age }}
        </li>
    </ul>
    <ul>
        <!--        the first is value,second is key-->
        <li v-for="(value,key) in data.person">{{ key }} --> {{ value }}</li>
    </ul>
</div>

</body>
<script src="../Vue.js"></script>
<script>
    new Vue({
        el: '#app',
        data() {
            return {
                data: {
                    status: 'ok',
                    users: [
                        {id: 1, name: "andy", age: 29},
                        {id: 2, name: "jack", age: 19},
                        {id: 3, name: "mary", age: 19},
                    ],
                    person: {
                        name: "andy"
                    }
                }
            }

        },
        methods: {}
    })
</script>
</html>
```
#### v-model
v-model只能用于 input, textarea, select等。
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <input type="text" v-model="msg">
    <p>{{ msg }}</p>
</div>
</body>
<script src="../Vue.js"></script>
<script>
    new Vue({
        el: "#app",
        data() {
            return {
                msg: ""
            }
        }
    })
</script>
</html>
```
#### carousel
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <img :src="images[curIndex].imgSrc" alt="">
    <br>
    <button @click="prev">上一张</button>
    <button @click="next">下一张</button>
</div>

</body>
<script src="../Vue.js"></script>
<script>
    let vm = new Vue({
        el: "#app",
        data() {
            return {
                images: [
                    {id: 1, imgSrc: '../images/1.jpg'},
                    {id: 2, imgSrc: '../images/2.jpg'},
                    {id: 3, imgSrc: '../images/3.jpg'},
                ],
                curIndex: 0
            }
        },
        methods: {
            prev() {
                if (this.curIndex === 0) {
                    this.curIndex = 2;
                } else {
                    this.curIndex--;
                }
            }
            ,
            next() {
                if (this.curIndex === 2) {
                    this.curIndex = 0;
                } else {
                    this.curIndex++;
                }
            }
        },
        // 钩子函数
        // 定时更换图片
        created() {
            setInterval(() => {
                // 箭头函数会改变this，指代vue对象
                if (this.curIndex === 2) {
                    this.curIndex = 0
                } else {
                    this.curIndex++
                }
            }, 1000)
            // 将外部的this保存起来，外部this为vue对象
            // let _this = this;
            // setInterval( function () {
            //     console.log(_this);
            // })
        }
    })
</script>
</html>
```
### method
#### ajax for data
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <span v-for="(category,index) in categoryList" :key="category.id">
        {{ category.name }}
    </span>
</div>

</body>
<script src="../Vue.js"></script>
<script src="../jquery.min.js"></script>
<script>
    let vm = new Vue({
        el: "#app",
        data() {
            return {}
        },
        // 钩子函数
        created() {
            $.ajax({
                url: "/categoryList/",
                type: "get",
                success: (data) => {
                    if (data.error_no === 0) {
                        let data = data.data;
                        let obj = {
                            id: 0,
                            name: "全部",
                            category: 0
                        }
                        this.categoryList = data;
                        this.categoryList.unshift(obj);
                    }
                },
                error: function (error) {
                    console.log(error);
                }
            })
        }
    })
</script>
</html>
```

#### watch
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <p>{{ msg }}</p>
    <button @click="change"> change</button>
</div>
</body>
<script src="../Vue.js"></script>
<script>
    new Vue({
        el: "#app",
        data() {
            return {
                msg: "andy"
            }
        },
        methods: {
            change() {
                this.msg = 'mike';
            }
        },
        watch: {
            'msg': function (val) {
                console.log(val);
                if (val === "mike") {
                    // 如果属性修改会触发此片
                    alert("修改");
                    this.msg = 'change mike';
                }
            }
        }
    })
</script>
</html>
```
#### computed
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <p>{{ msg }}</p>
    <!--    use the computed method name-->
    <p>{{ upperName }}</p>
</div>
</body>
<script src="../Vue.js"></script>
<script>
    new Vue({
        el: "#app",
        data() {
            return {
                msg: "andy"
            }
        },
        methods: {
            change() {
                this.msg = 'mike';
            }
        },
        computed: {
            upperName() {
                return this.msg.toUpperCase()
            }
        }
    })
</script>
</html>
```

### component

#### components
组件模板中必须有个父标签，将所有标签包裹
注意App 组件的写法，与Vue对象是不同的
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
    // 组件的变量名，首字母要大写，data必须为函数，有返回值
    // 声明一个组件
    let App = {
        data() {
            return {
                text: "App中的text"
            }
        },
        template: `
        <div>
            <p>{{ text }}</p>
        </div>
        `
    };

    new Vue({
        el: "#app",
        data() {
            return {
                msg: "组件"
            }
        },
        //使用组件
        template: `
            <div class="app">
<!--             <p> {{ msg }}</p>-->
             <App/>
            </div>
        `,
        components: {
            // 如果key,value一样，可以 只写一个
            // 注册组件
            App
        }
    })
</script>
</html>
```
#### slot
slot为vue提供的内容分发组件。
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <p>{{msg}}</p>
</div>
</body>
<script src="../Vue.js"></script>
<script>
    // 组件的变量名，首字母要大写，data必须为函数，有返回值
    // 对应组件的内容将会替换 slot标签。slot为 vue内置组件
    Vue.component("Btn", {
        data() {
            return {}
        },
        template: `
       <button><slot></slot></button>
        `
    })
    // 声明一个组件
    let App = {
        data() {
            return {
                text: "App中的text"
            }
        },
        template: `
        <div>
            <p>{{ text }}</p>
            <btn>子btn</btn>
        </div>
        `
    };

    new Vue({
        el: "#app",
        data() {
            return {
                msg: "组件"
            }
        },
        //使用组件
        template: `
            <div class="app">
             <p> {{ msg }}</p>
             <btn>主btn</btn>
             <App/>
            </div>
        `,
        components: {
            // 如果key,value一样，可以 只写一个
            // 注册组件
            App
        }
    })
</script>
</html>
```

### transfer data

#### parent2child
在子组件中定义props,它的值可以是一个列表，其中为变量名。然后就可以使用了。
在父组件中，需要通过 v-bind:props_name=props_name 将值传递给子组件
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
    let Vheader = {
        data() {
            return {}
        },
        // 挂载父组件的属性
        props: ['msg', 'post'],
        template: `
            <div>
            <h2>日天</h2>
            <h2>{{ msg }}</h2>
            <h2> {{ post.id }}</h2>
            <h2> {{ post.name }}</h2>
            </div>
        `
    }

    new Vue({
        el: "#app",
        data() {
            return {
                text: "App中的text",
                post: {
                    id: 1,
                    name: "andy"
                }
            }
        },
        //使用组件
        template: `
            <Vheader :msg="text" v-bind:post="post"></Vheader>
        `,
        components: {
            // 如果key,value一样，可以 只写一个
            // 注册组件
            Vheader
        }
    })
</script>
</html>
```
#### child2parent
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
    Vue.component("Btn", {
        data() {
            return {}
        },
        template: `
       <button @click="clickBtn">{{ id }}</button>
        `,
        props: ['id'],
        methods: {
            clickBtn() {
                this.id++
                this.$emit('VheaderAddNum', this.id) // this.id作为参数传给 Vheader,add
            }
        }
    })
    let Vheader = {
        data() {
            return {}
        },
        // 挂载父组件的属性
        props: ['msg', 'post'],
        template: `
            <div>
            <h2>日天</h2>
            <h2>{{ msg }}</h2>
            <h2>post id :{{ post.id }}</h2>
            <h2>post name : {{ post.name }}</h2>
            <Btn v-bind:id = "post.id" @VheaderAddNum="clickAddNum"></Btn>
            </div>
        `,
        methods: {
            clickAddNum(val_from_Btn) {
                this.$emit('appClick', val_from_Btn);
            }
        }
    }

    new Vue({
        el: "#app",
        data() {
            return {
                text: "App中的text",
                post: {
                    id: 1,
                    name: "andy"
                }
            }
        },
        //使用组件
        template: `
            <div class="a">
                我是父组件的post id:{{post.id}}
            <Vheader :msg="text" v-bind:post="post" @appClick="rootClick"></Vheader>
            </div>
        `,
        methods: {
            rootClick(val_from_vheader) {
                this.post.id = val_from_vheader;
            }
        },
        components: {
            // 如果key,value一样，可以 只写一个
            // 注册组件
            Vheader
        }
    })
</script>
</html>
```
#### sibling2sibling
```vue
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<div id="app">
    <App/>
</div>
</body>
<script src="../Vue.js"></script>
<script>
    let bus = new Vue();
    <!--    A向B传值，B要声明事件，$on("事件名",function(val){}), A触发事件， $emit('A组件中声明的事件名',function(){})-->
    Vue.component("Dest", {
        data() {
            return {
                text: ''
            }
        },
        template: `
        <div>
        <h2>我是Dest</h2>
        <h2>{{ text }}</h2>
        </div>
        `,
        methods: {},
        created() {
            bus.$on('destData', (val) => {
                console.log(val);
                this.text = val;
            })
        }
    })
    Vue.component("Source", {
        data() {
            return {
                msg: "我是子组件source的msg"
            }
        },
        template: `<div>
        <h2>我是Source的btn</h2>
        <button @click="sourceHandler">传递</button>
        </div>
        `,
        methods: {
            sourceHandler() {
                bus.$emit('destData', this.msg)
            }
        }
    })
    let VHeader = {
        data() {
            return {}
        },
        template: `
       <div class="header">
        <Dest></Dest>
        <br>
        <Source></Source>
    </div>
       `
    }
    let App = {
        data() {
            return {}
        },
        template: `
       <div class="app">
       <VHeader></VHeader>
</div>
       `,
        components: {
            VHeader
        }
    }
    new Vue({
        el: "#app",
        data() {
            return {
                text: "App中的text",
                post: {
                    id: 1,
                    name: "andy"
                }
            }
        },
        components: {
            // 如果key,value一样，可以 只写一个
            // 注册组件
            App
        }
    })
</script>
</html>
```