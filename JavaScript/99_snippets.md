### left Menu
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    * {
        margin: 0;
        padding: 0;
    }

    .left {
        width: 20%;
        height: 500px;
        float: left;
        background-color: wheat;
    }

    .right {
        float: left;
        width: 80%;
        height: 500px;
        background-color: lightgray;

    }

    .title {
        text-align: center;
        line-height: 40px;
        background-color: #0e90d2;
        color: white;
    }

    .item {
        padding: 10px;
    }

    .hide {
        display: none;
    }
    </style>
</head>

<body>
    <div class="outer">
        <div class="left">
            <div class="item">
                <div class="title">菜单一</div>
                <ul class="con">
                    <li>111</li>
                    <li>111</li>
                    <li>111</li>
                </ul>
            </div>
            <div class="item">
                <div class="title">菜单二</div>
                <ul class="con hide">
                    <li>222</li>
                    <li>222</li>
                    <li>222</li>
                </ul>
            </div>
            <div class="item">
                <div class="title">菜单三</div>
                <ul class="con hide">
                    <li>333</li>
                    <li>333</li>
                    <li>333</li>
                </ul>
            </div>
        </div>
        <div class="right"></div>
    </div>
    <script>
    var eles_title = document.getElementsByClassName("title");

    for (var i = 0; i < eles_title.length; i++) {
        eles_title[i].onclick = function() {
            // 当前菜单隐藏或者展示
            this.nextElementSibling.classList.contains("hide") ? this.nextElementSibling.classList.remove("hide") : this.nextElementSibling.classList.add("hide");

            for (var j = 0; j < eles_title.length; j++) {
                // 其它（非当前点击的菜单）都加隐藏
                if (eles_title[j] != this) {
                    eles_title[j].nextElementSibling.classList.add("hide")
                }

            }

        }

    }
    </script>
</body>

</html>
```
### input with tips
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script>
    function Focus(){ 

    var input=document.getElementById("ID1"); 
    if (input.value=="请输入用户名"){ 
        input.value=""; 
    } 
} 

    function Blurs(){ 
    var ele=document.getElementById("ID1"); 
        var val=ele.value; 
        if(!val.trim()){ 
            ele.value="请输入用户名"; 
        } 
    } 

</script>
</head>

<body>
    <input id="ID1" type="text" value="请输入用户名" onblur="Blurs()" onfocus="Focus()">
</body>

</html>


```
### diy modal
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .back{ 
            background-color: white; 
            height: 2000px; 
        } 

    .shade{ 
            position: fixed; 
            top: 0; 
            bottom: 0; 
            left:0; 
            right: 0; 
            background-color: grey; 
            opacity: 0.4; 
        } 

    .hide{ 
            display: none; 
        } 

    .models{ 
            position: fixed; 
            top: 50%; 
            left: 50%; 
            margin-left: -100px; 
            margin-top: -100px; 
            height: 200px; 
            width: 200px; 
            background-color: wheat; 

        } 
    </style>
</head>

<body>
    <div class="back">
        <input class="c" type="button" value="click">
    </div>
    <div class="shade hide handles"></div>
    <div class="models hide handles">
        <input class="c" type="button" value="cancel">
    </div>
    <script>
    var eles = document.getElementsByClassName("c");
    var handles = document.getElementsByClassName("handles");
    for (var i = 0; i < eles.length; i++) {
        eles[i].onclick = function() {
            if (this.value == "click") {
                for (var j = 0; j < handles.length; j++) {
                    handles[j].classList.remove("hide");
                }
            } else {
                for (var j = 0; j < handles.length; j++) {
                    handles[j].classList.add("hide");
                }
            }
        }
    }
    </script>
</body>

</html>
```
### table
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>

<body>
    <button class="select_all">全选</button>
    <button class="select_reverse">反选</button>
    <button class="cancel">取消</button>
    <hr>
    <table class="server_table" border="2px" cellspacing="2px">
        <tr>
            <td><input type="checkbox" class="item"></td>
            <td>111</td>
            <td>111</td>
            <td>111</td>
        </tr>
        <tr>
            <td><input type="checkbox" class="item"></td>
            <td>222</td>
            <td>222</td>
            <td>222</td>
        </tr>
        <tr>
            <td><input type="checkbox" class="item"></td>
            <td>333</td>
            <td>333</td>
            <td>333</td>
        </tr>
        <tr>
            <td><input type="checkbox" class="item"></td>
            <td>444</td>
            <td>444</td>
            <td>444</td>
        </tr>
    </table>
    <script>
    var input_arr = document.getElementsByClassName("item");
    var button_arr = document.getElementsByTagName("button");

    for (var i = 0; i < button_arr.length; i++) {
        button_arr[i].onclick = function() {
            for (var j = 0; j < input_arr.length; j++) {
                var inp = input_arr[j]
                if (this.innerText == "全选") {
                    console.log("ok");
                    inp.checked = true;
                } else if (this.innerText == "取消") {
                    inp.checked = false;
                } else {
                    if (inp.checked) {
                        inp.checked = false;
                    } else {
                        inp.checked = true;
                    }
                }
            }
        }
    }
    </script>
</body>

</html>
```

### select option move to right
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    .outer {
        margin: 0 auto;
        background-color: darkgray;
        width: 80%;
        height: 600px;
        margin-top: 30px;
        word-spacing: -5px;

    }

    #left {
        display: inline-block;
        width: 100px;
        height: 140px;
        background-color: wheat;
        text-align: center;

    }

    #choice {
        display: inline-block;
        height: 140px;
        background-color: darkolivegreen;

        vertical-align: top;
        padding: 0 5px;

    }

    #choice button {
        margin-top: 20px;
    }

    #right {
        display: inline-block;
        width: 100px;
        height: 140px;
        background-color: wheat;
        text-align: center;
        line-height: 140px;

    }
    </style>
</head>

<body>
    <div class="outer">
        <select multiple="multiple" size="5" id="left">
            <option>红楼梦</option>
            <option>西游记</option>
            <option>水浒传</option>
            <option>JinPingMei</option>
            <option>三国演义</option>
        </select>
        <span id="choice">
            <button id="choose_move"> > </button><br>
            <button id="all_move"> >> </button>
        </span>
        <select multiple="multiple" size="10" id="right">
            <option>放风筝的人</option>
        </select>
    </div>
    <script>
    var choose_move = document.getElementById("choose_move");
    var all_move = document.getElementById("all_move");
    var right = document.getElementById("right");
    var left = document.getElementById("left");
    var options = left.options;

    choose_move.onclick = function() {
        for (var i = 0; i < options.length; i++) {
            var option = options[i];
            if (option.selected == true) {
                // var news=option.cloneNode(true); 
                // console.log(news); 
                right.appendChild(option);
                i--;
            }
        }
    };

    all_move.onclick = function() {

        for (var i = 0; i < options.length; i++) {
            var option = options[i];
            right.appendChild(option);
            i--;
        };
    };
    </script>
</body>

</html>
```


### mall with tab
```
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>tab</title>
    <style>
    * {
        margin: 0;
        padding: 0;
        list-style: none;
    }

    body {
        font-family: "Helvetica Neue", "Hiragino Sans GB", "Microsoft YaHei", "\9ED1\4F53", Arial, sans-serif;
    }

    h3 {
        text-align: center;
        color: darkcyan;
        margin-top: 30px;
        letter-spacing: 5px;
    }

    .box {
        width: 1000px;
        margin: 50px auto 0px;
    }

    #title {
        line-height: 40px;
        background-color: rgb(247, 247, 247);
        font-size: 16px;
        font-weight: bold;
        color: rgb(102, 102, 102);
    }

    #title span {
        float: left;
        width: 166px;
        text-align: center;
    }

    #title span:hover {
        /*color: black;*/
        cursor: pointer;
    }

    #content {
        margin-top: 20px;
    }

    #content li {
        width: 1050px;
        display: none;
        background-color: rgb(247, 247, 247);
    }

    #content li div {
        width: 156px;
        margin-right: 14px;
        float: left;
        text-align: center;
    }

    #content li div a {
        font-size: 14px;
        color: black;
        line-height: 14px;
        /*  float: left;*/
        display: inline-block;
        margin-top: 10px;
    }

    #content li a:hover {
        color: #B70606;
    }

    #content li div span {
        font-size: 16px;
        line-height: 16px;
        /*float: left;*/
        display: block;
        color: rgb(102, 102, 102);
        margin-top: 10px;
    }

    #content img {
        float: left;
        width: 155px;
        height: 250px;
    }

    #title .select {
        background-color: #2459a2;
        color: white;
        border-radius: 10%;
    }

    #content .show {
        display: block;
    }

    .show span {
        color: red !important;
        font-size: 30px;
    }
    </style>
</head>

<body>
    <h3 id="wel">京东商城欢迎您</h3>
    <!--  direction="right up down left" -->
    <!--  behavior：滚动方式(包括3个值：scroll、slide、alternate) -->
    <!--  说明：scroll：循环滚动，默认效果；slide：只滚动一次就停止；alternate：来回交替进行滚动。 -->
    <!--  scrollamount="5" 滚动速度 -->
    <marquee behavior="scroll" direction="right">欢迎您</marquee>
    <script>
    function test() {

        var mywel = document.getElementById("wel");
        var content = mywel.innerText;

        var f_content = content.charAt(0);
        var l_content = content.substring(1, content.length);

        var new_content = l_content + f_content;
        mywel.innerText = new_content;

    }

    // setInterval("test();", 500);
    </script>
    <div class="box">
        <p id="title">
            <span class="select">家用电器</span>
            <span>家具</span>
            <span>汽车</span>
            <span>食品</span>
            <span>女鞋</span>
            <span>医疗保健</span>
        </p>
        <ul id="content">
            <li class="show">
                <div><img src="https://img10.360buyimg.com/n1/s450x450_jfs/t4786/325/2470647304/119102/9e1a4ed5/59005841Nd786a8df.jpg" alt="冰箱"><a href="#">容声(Ronshen)冰箱</a><span>价格:5600</span></div>
                <div><img src="https://img12.360buyimg.com/n1/s450x450_jfs/t3037/347/1290968859/201366/7c1028a0/57c00194N9d0a54c6.jpg" alt="洗衣机"><a href="#">海尔洗衣机</a><span>价格:5400</span></div>
                <div><img src="https://img11.360buyimg.com/n1/jfs/t3289/128/2393835119/236360/af1d283b/57e0f300N53dde603.jpg" alt="电饭煲"><a href="#">福库(CUCKOO)电饭煲</a><span>价格:3999</span></div>
                <div><img src="https://img13.360buyimg.com/n1/jfs/t3235/137/2361713777/152258/a6908440/57e098c2N44a90a5d.jpg" alt="智能电视"><a href="#">三星智能电视</a><span>价格:8999</span></div>
                <div><img src="https://img10.360buyimg.com/n1/jfs/t2053/101/1391591157/215066/572e131b/5696ee9bN2376492d.jpg" alt="净水器"><a href="#">净水器</a><span>价格:1300</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t3175/78/2357430273/262835/9a8e7f65/57e0a3e9Nbda39dd2.jpg" alt="空气净化器"><a href="#">空气净化器</a><span>价格:5300</span></div>
            </li>
            <li>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t1948/172/2877517581/556924/682eb107/56f63dc8Naddf77e5.jpg" alt="沙发"><a href="#">沙发</a><span>价格:2900</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t1948/172/2877517581/556924/682eb107/56f63dc8Naddf77e5.jpg" alt="沙发"><a href="#">沙发</a><span>价格:2900</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t1948/172/2877517581/556924/682eb107/56f63dc8Naddf77e5.jpg" alt="沙发"><a href="#">沙发</a><span>价格:2900</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t1948/172/2877517581/556924/682eb107/56f63dc8Naddf77e5.jpg" alt="沙发"><a href="#">沙发</a><span>价格:2900</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t1948/172/2877517581/556924/682eb107/56f63dc8Naddf77e5.jpg" alt="沙发"><a href="#">沙发</a><span>价格:2900</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t1948/172/2877517581/556924/682eb107/56f63dc8Naddf77e5.jpg" alt="沙发"><a href="#">沙发</a><span>价格:2900</span></div>
            </li>
            <li>
                <div><img src="http://img11.360buyimg.com/n1/jfs/t4969/76/45396935/144539/347153d4/58d9cff4N36872ad6.jpg" alt="长安汽车"><a href="#">长安汽车</a><span>价格:12900</span></div>
                <div><img src="http://img11.360buyimg.com/n1/jfs/t4969/76/45396935/144539/347153d4/58d9cff4N36872ad6.jpg" alt="长安汽车"><a href="#">长安汽车</a><span>价格:12900</span></div>
                <div><img src="http://img11.360buyimg.com/n1/jfs/t4969/76/45396935/144539/347153d4/58d9cff4N36872ad6.jpg" alt="长安汽车"><a href="#">长安汽车</a><span>价格:12900</span></div>
                <div><img src="http://img11.360buyimg.com/n1/jfs/t4969/76/45396935/144539/347153d4/58d9cff4N36872ad6.jpg" alt="长安汽车"><a href="#">长安汽车</a><span>价格:12900</span></div>
                <div><img src="http://img11.360buyimg.com/n1/jfs/t4969/76/45396935/144539/347153d4/58d9cff4N36872ad6.jpg" alt="长安汽车"><a href="#">长安汽车</a><span>价格:12900</span></div>
                <div><img src="http://img11.360buyimg.com/n1/jfs/t4969/76/45396935/144539/347153d4/58d9cff4N36872ad6.jpg" alt="长安汽车"><a href="#">长安汽车</a><span>价格:12900</span></div>
            </li>
            <li>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t4414/110/2582917360/207971/b7e129ad/58f0ee1fN94425de1.jpg" alt="嘉兴粽子"><a href="#">嘉兴粽子</a><span>价格:1</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t4414/110/2582917360/207971/b7e129ad/58f0ee1fN94425de1.jpg" alt="嘉兴粽子"><a href="#">嘉兴粽子</a><span>价格:1</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t4414/110/2582917360/207971/b7e129ad/58f0ee1fN94425de1.jpg" alt="嘉兴粽子"><a href="#">嘉兴粽子</a><span>价格:1</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t4414/110/2582917360/207971/b7e129ad/58f0ee1fN94425de1.jpg" alt="嘉兴粽子"><a href="#">嘉兴粽子</a><span>价格:1</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t4414/110/2582917360/207971/b7e129ad/58f0ee1fN94425de1.jpg" alt="嘉兴粽子"><a href="#">嘉兴粽子</a><span>价格:1</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t4414/110/2582917360/207971/b7e129ad/58f0ee1fN94425de1.jpg" alt="嘉兴粽子"><a href="#">嘉兴粽子</a><span>价格:1</span></div>
            </li>
            <li>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t3079/298/5759209435/92674/14818594/587f1c33N53e5d2a9.jpg" alt="星期六"><a href="#">星期六</a><span>价格:439</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t3079/298/5759209435/92674/14818594/587f1c33N53e5d2a9.jpg" alt="星期六"><a href="#">星期六</a><span>价格:439</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t3079/298/5759209435/92674/14818594/587f1c33N53e5d2a9.jpg" alt="星期六"><a href="#">星期六</a><span>价格:439</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t3079/298/5759209435/92674/14818594/587f1c33N53e5d2a9.jpg" alt="星期六"><a href="#">星期六</a><span>价格:439</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t3079/298/5759209435/92674/14818594/587f1c33N53e5d2a9.jpg" alt="星期六"><a href="#">星期六</a><span>价格:439</span></div>
                <div><img src="https://img14.360buyimg.com/n1/jfs/t3079/298/5759209435/92674/14818594/587f1c33N53e5d2a9.jpg" alt="星期六"><a href="#">星期六</a><span>价格:439</span></div>
            </li>
            <li>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t5755/127/1139389729/356866/99d4e869/5923e410Nb2983f70.jpg" alt="汇仁 肾宝片"><a href="#">汇仁 肾宝片</a><span>价格:322</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t5755/127/1139389729/356866/99d4e869/5923e410Nb2983f70.jpg" alt="汇仁 肾宝片"><a href="#">汇仁 肾宝片</a><span>价格:322</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t5755/127/1139389729/356866/99d4e869/5923e410Nb2983f70.jpg" alt="汇仁 肾宝片"><a href="#">汇仁 肾宝片</a><span>价格:322</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t5755/127/1139389729/356866/99d4e869/5923e410Nb2983f70.jpg" alt="汇仁 肾宝片"><a href="#">汇仁 肾宝片</a><span>价格:322</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t5755/127/1139389729/356866/99d4e869/5923e410Nb2983f70.jpg" alt="汇仁 肾宝片"><a href="#">汇仁 肾宝片</a><span>价格:322</span></div>
                <div><img src="https://img12.360buyimg.com/n1/jfs/t5755/127/1139389729/356866/99d4e869/5923e410Nb2983f70.jpg" alt="汇仁 肾宝片"><a href="#">汇仁 肾宝片</a><span>价格:322</span></div>
            </li>
        </ul>
    </div>
    <script>
    var title = document.getElementById('title');
    var content = document.getElementById('content');
    var category = title.getElementsByTagName('span');
    var item = content.getElementsByTagName('li');

    for (var i = 0; i < category.length; i++) {
        category[i].index = i;
        category[i].onclick = function() {
            for (var j = 0; j < category.length; j++) {
                category[j].className = '';
                item[j].className = '';
            }
            this.className = 'select';
            item[this.index].className = 'show';
        }
    }
    </script>
</body>

</html>
```
### 二级联动
```html
<select id="province">
    <option>请选择省:</option>
</select>
<select id="city">
    <option>请选择市:</option>
</select>
<script>
data = { "河北省": ["廊坊", "邯郸"], "北京": ["朝阳区", "海淀区"] };
var p = document.getElementById("province");
var c = document.getElementById("city");

for (var i in data) {
    var option_pro = document.createElement("option");
    option_pro.innerHTML = i;
    p.appendChild(option_pro);
}

p.onchange = function() {
    pro = (this.options[this.selectedIndex]).innerHTML;
    citys = data[pro];
    c.options.length = 0;
    for (var i in citys) {
        var option_city = document.createElement("option");
        option_city.innerHTML = citys[i];
        c.appendChild(option_city);
    }
}
</script>
```

### 向模态框传入值

data-target 指定的是目标，即将数据传输给谁
- 绑定modal对象
```html
<td><input type="button" data-toggle="modal" data-target="#modal_id" onclick="send_val();"/></td>
```
这里的模态框的id与上面的按钮的data-target中绑定的id保持一致
- modal 对象
```html
<div class="modal fade" id="modal_id" tabindex="-1" role="dialog" aria-labelledby="myModalLabel" aria-hidden="true"> ....
<input type="hidden" id="input_id" name="input_id" value="">
</div>
```

- 通过按钮绑定的事件传值
```js
function send_val(){
    $("#modal_id").modal("show");
    $("#input_id").val("传过来的值");
}
```

### 模态框背景黑掉的bug
最近在做一个弹出对话框的评论，在用户添加评论后，点击确认，为了让用户看到刚刚添加的评论，会重新获取所有评论，再弹出对话框(想到这里可以用js动态向后追加评论，不知道 是否可行)。在上面的情况下，会出现一个问题，就是第二次弹出时，会导致背景黑掉，经研究是因为第一次的模态框还没有关掉的原因，解决办法是在第一次的基础上添加一点时间等待。目前我测试的时间是400毫秒，再短就可能出现无法弹出的情况
```js
<div class="modal-backdrop fade in></div>
//面的div每弹出一次对话框产生一个。其作用是，在弹出对话框的时候，页面暂时变半透明灰色，点击确定或取消关闭对话框后，这个随之消失,如果时间太短，它还没消失。就会出现上面的bug
$("#modalId").modal("hide") // 第一个关闭
setTimeout(function){
    $.ajax(
    success:function(data){
        $("$modalId").modal("show");
    },400)
}
```

### time format
```js
Date.prototype.format = function(fmt) { 
     var o = { 
        "M+" : this.getMonth()+1,                 //月份 
        "d+" : this.getDate(),                    //日 
        "h+" : this.getHours(),                   //小时 
        "m+" : this.getMinutes(),                 //分 
        "s+" : this.getSeconds(),                 //秒 
        "q+" : Math.floor((this.getMonth()+3)/3), //季度 
        "S"  : this.getMilliseconds()             //毫秒 
    }; 
    if(/(y+)/.test(fmt)) {
            fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length)); 
    }
     for(var k in o) {
        if(new RegExp("("+ k +")").test(fmt)){
             fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
         }
     }
    return fmt; 
} 

// 调用
var time1 = new Date().format("yyyy-MM-dd hh:mm:ss");
console.log(time1);
```

### randInt
```js
function randInt(min,max){
    return Math.floor(Math.random()* (max-min) + min)
}
```

### getCurrentDomain, Url, relativeUlr
```js
//domain
var domain = document.domain;
var domain = window.location.host;

//url
var url = window.location.href;
var url = self.location.href;
var url = document.URL;
var url = document.location;

//relative url
window.location.pathname
function GetUrlRelativePath(){
    var url = document.location.toString();
    var arrUrl = url.split("//");

    var start = arrUrl[1].indexOf("/");
    var relUrl = arrUrl[1].substring(start);//stop省略，截取从start开始到结尾的所有字符

  if(relUrl.indexOf("?") != -1){
      relUrl = relUrl.split("?")[0];// 取参数之前的部分
    }
    return relUrl;
  }
```

### jq get selected option
```js
let select_item = $("select_id option:selected");
let select_val = select_item.val();
# input value can be like this
$("input[name='name']").val();
```

### stop propagation
```js
$("#id").on("click","tr td",function(){
	if(e.target.tagName === "TD"){
		console.log("do outside operation");
	}else if(e.target.tagName === 'INPUT'){
		console.log("do inner operation");
	}
})
```

### axios interceptor
```js
const instance = axios.create({
	baseUrl:'http://127.0.0.1:8000',
	timeout: 2000,
	headers:{
		"content-Type":"application/json",
		"Authorization":"Bearer " + get_local_token("access_token")
	}
})

function refresh_token(){
	return instance.get('http://127.0.0.1:8000/refresh_token/',{
		headers:{
			"content-Type":"application/json",
			"Authorization":"Bearer " + get_local_token("refresh_token")
		}
	})
	.then(res=>{
		return res.data;
	})
}

instance.interceptors.response.user(response =>{
	const code = response.data.code;
	if(code === 600){
		return refresh_token().then(res=>{
			// 刷新token,并更新到storage和header中
			let new_access_token = res.data['access_token'];
			instance.set_token("access_token",new_access_token);
			const config = response.config;
			config.headers['Authorization'] = "Bearer " + new_access_token;
			config.baseUrl = "http://127.0.0.1:8000/refresh_token/index";
			return instance(config);
		}).catch(err=>{
			// 刷新失败了，跳转到首页重新登陆
			window.location.href = '/';
			console.log(err);
		})
	}
	return response
}
.error =>{
	// 请求失败，状态码为400之类
	return Promise.reject(error);
})

function get_local_token(name) {
	return localStorage.getItem(name);
}

instance.set_token:(name,token)=>{
	instance.defaults.headers['Authorization'] = "Bearer " + token;
	localStorage.setItem(name,token);
}

export instance;
```

### vue elementUi table calculate rowspan
```js
function calcSpan(data, field) {
    // data 为已经处理好的数据，不存在嵌套格式
    // field 为对应字段，即需要合并的列对应的字段
    // 返回结果为数组：[4,0.0.0]
    let rowCols = [];
    for (let i = 0; i < data.length; i++) {
        if (i === 0) {
            rowCols.push(1);
            this.index = 0;
        } else {
            if (data[i][field] === data[i - 1][field]) {
                rowCols[this.index] += 1;
                rowCols.push(0);
            } else {
                rowCols.push(1);
                this.index = i;
            }
        }
    }
    return rowCols;
}


function SpanHandler({rowIndex, colIndex}) {
    // 根据需要合并的列计算，合并数组对应的合并数（rowspan)
    if (colIndex === 0) {
        const row = this.calcSpan(this.data, 'type')[rowIndex];
        const col = row > 0 ? 1 : 0;
        return {
            rowspan: row,
            colspan: col
        }
    } else if (colIndex === 1) {
        const row = this.calcSpan(this.data, 'ip')[rowIndex];
        const col = row > 0 ? 1 : 0;
        return {
            rowspan: row,
            colspan: col
        }
    }
}
```

### Vue axios bind baseURL
```js
import axios from 'axios
axios.defaults.baseURL = "http://127.0.0.1:8000"
```

### rbSweetalert
```js
/**
 * Created by Administrator on 2016/12/14.
 */

var rbalert = {
    /*
        功能：提示错误
        参数：
            - msg：提示的内容（可选）
    */
    'alertError': function (msg) {
        swal('提示',msg,'error');
    },
    /*
        功能：信息提示
        参数：
            - msg：提示的内容（可选）
    */
    'alertInfo':function (msg) {
        swal('提示',msg,'warning');
    },
    /*
        功能：可以自定义标题的信息提示
        参数：
            - msg：提示的内容（可选）
    */
    'alertInfoWithTitle': function (title,msg) {
        swal(title,msg);
    },
    /*
        功能：成功的提示
        参数：
            - msg：提示的内容（必须）
            - confirmCallback：确认按钮的执行事件（可选）
    */
    'alertSuccess':function (msg,confirmCallback) {
        args = {
            'title': '提示',
            'text': msg,
            'type': 'success',
        }
        swal(args,confirmCallback);
    }, 
    /*
        功能：带有标题的成功提示
        参数：
            - title：提示框的标题（必须）
            - msg：提示的内容（必须）
    */
    'alertSuccessWithTitle':function (title,msg) {
        swal(title,msg,'success');
    },
    /*
        功能：确认提示
        参数：字典的形式
            - title：提示框标题（可选）
            - type：提示框的类型（可选）
            - confirmText：确认按钮文本（可选）
            - cancelText：取消按钮文本（可选）
            - msg：提示框内容（必须）
            - confirmCallback：确认按钮点击回调（可选）
            - cancelCallback：取消按钮点击回调（可选）
    */
    'alertConfirm':function (params) {
        swal({
            'title': params['title'] ? params['title'] : '提示',
            'showCancelButton': true,
            'showConfirmButton': true,
            'type': params['type'] ? params['type'] : '',
            'confirmButtonText': params['confirmText'] ? params['confirmText'] : '确定',
            'cancelButtonText': params['cancelText'] ? params['cancelText'] : '取消',
            'text': params['msg'] ? params['msg'] : ''
        },function (isConfirm) {
            if(isConfirm){
                if(params['confirmCallback']){
                    params['confirmCallback']();
                }
            }else{
                if(params['cancelCallback']){
                    params['cancelCallback']();
                }
            }
        });
    },
    /*
        功能：带有一个输入框的提示
        参数：字典的形式
            - title：提示框的标题（可选）
            - text：提示框的内容（可选）
            - placeholder：输入框的占位文字（可选）
            - confirmText：确认按钮文字（可选）
            - cancelText：取消按钮文字（可选）
            - confirmCallback：确认后的执行事件
    */
    'alertOneInput': function (params) {
        swal({
            'title': params['title'] ? params['title'] : '请输入',
            'text': params['text'] ? params['text'] : '',
            'type':'input',
            'showCancelButton': true,
            'animation': 'slide-from-top',
            'closeOnConfirm': false,
            'showLoaderOnConfirm': true,
            'inputPlaceholder': params['placeholder'] ? params['placeholder'] : '',
            'confirmButtonText': params['confirmText'] ? params['confirmText'] : '确定',
            'cancelButtonText': params['cancelText'] ? params['cancelText'] : '取消',
        },function (inputValue) {
            if(inputValue === false) return false;
            if(inputValue === ''){
                swal.showInputError('输入框不能为空！');
                return false;
            }
            if(params['confirmCallback']){
                params['confirmCallback'](inputValue);
            }
        });
    },
    /*
        功能：网络错误提示
        参数：无
    */
    'alertNetworkError':function () {
        this.alertErrorToast('网络错误');
    },
    /*
        功能：信息toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertInfoToast':function (msg) {
        this.alertToast(msg,'info');
    },
    /*
        功能：错误toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertErrorToast':function (msg) {
        this.alertToast(msg,'error');
    },
    /*
        功能：成功toast提示（1s后消失）
        参数：
            - msg：提示消息
    */
    'alertSuccessToast':function (msg) {
        if(!msg){msg = '成功！';}
        this.alertToast(msg,'success');
    },
    /*
        功能：弹出toast（1s后消失）
        参数：
            - msg：提示消息
            - type：toast的类型
    */
    'alertToast':function (msg,type) {
        swal({
            'title': msg,
            'text': '',
            'type': type,
            'showCancelButton': false,
            'showConfirmButton': false,
            'timer': 1000,
        });
    },
    // 关闭当前对话框
    'close': function () {
        swal.close();
    }
};
```

### rbAjax
```js
'use strict';
var rbajax = {
    'get':function(args) {
        args['method'] = 'get';
        this.ajax(args);
    },
    'post':function(args) {
        args['method'] = 'post';
        this.ajax(args);
    },
    'ajax':function(args) {
        // 设置csrftoken
        this._ajaxSetup();
        $.ajax(args);
    },
    '_ajaxSetup': function() {
        $.ajaxSetup({
            'beforeSend':function(xhr,settings) {
                if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type) && !this.crossDomain) {
                    var csrftoken = $('meta[name=csrf-token]').attr('content');
                    xhr.setRequestHeader("X-CSRFToken", csrftoken)
                }
            }
        });
    }
};
```

### checkIsActive
```js
// 检测用户活跃情况
function isActive() {
    var arr = ['index', 'login']
    var result = arr.some(function(item) {
        return window.location.href.indexOf(item) > 0
    })
    // result 表示当前页面可能是index或者注册页面 
    // 不是index页面 ，不是注册页面才会去检测用户的活跃状态（鼠标移动状态）
    if (!result) {
        var lastTime = new Date().getTime();
        var currentTime = new Date().getTime();
        //设置超时时间： 10分
        var timeOut = 10 * 60 * 1000; 

        window.onload = function() {
            /* 检测鼠标移动事件 */
            document.addEventListener('mousemove', function() {
                // 更新最后的操作时间
                console.log('鼠标移动了')
                lastTime = new Date().getTime();
            })
        }

        /* 定时器  间隔1分钟，检测是否长时间未操作页面  */
        var quitTime = window.setInterval(testTime, 60000);

        // 超时函数
        function testTime() {
            //更新当前时间
            currentTime = new Date().getTime();
            console.log('currentTime', currentTime)
            //判断是否超时
            if (currentTime - lastTime > timeOut) {
                // console.log('超时拉')
                // 超时操作
                axios.post(logoutUrl,params)
                .then(function (res) {
                  // 写超时执行的代码,例如退出登录什么的
                })
                .catch(function (error) {
                  console.log(error);
                });
                // 清除掉定时器
                window.clearInterval(quitTime)
            }
        }
    }
}

isActive()
```
ref: https://blog.csdn.net/cofecode/article/details/82429016

### decode jwt
use js to parse jwt token
```js
function parseJwt (token) {
    var base64Url = token.split('.')[1];
    var base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
    var jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
        return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
    }).join(''));

    return JSON.parse(jsonPayload);
};
```