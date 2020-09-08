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