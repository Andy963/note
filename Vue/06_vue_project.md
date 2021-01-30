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
