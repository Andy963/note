## BOM
Browser object model

### window对象 
所有浏览器都支持 window 对象。 
- 概念上讲.一个html文档对应一个window对象. 
- 功能上讲: 控制浏览器窗口的. 
- 使用上讲: window对象不需要创建对象,直接使用即可. 

#### method
alert()            显示带有一段消息和一个确认按钮的警告框。 
confirm()          显示带有一段消息以及确认按钮和取消按钮的对话框。 
prompt()           显示可提示用户输入的对话框。 
open()             打开一个新的浏览器窗口或查找一个已命名的窗口。 
close()            关闭浏览器窗口。 
setInterval()      按照指定的周期（以毫秒计）来调用函数或计算表达式。 
clearInterval()    取消由 setInterval() 设置的 timeout。 
setTimeout()       在指定的毫秒数后调用函数或计算表达式。 
clearTimeout()     取消由 setTimeout() 方法设置的 timeout。 
scrollTo()         把内容滚动到指定的坐标。 

alert confirm prompt以及open函数 
```
var result = confirm("您确定要删除吗?");
alert(result); 

//prompt 参数1 : 提示信息. 参数2:输入框的默认值. 返回值是用户输入的内容.
// var result = prompt("请输入一个数字!","haha");
// alert(result);

open方法 打开和一个新的窗口 并 进入指定网址.参数1 : 网址.
//调用方式1
//open("http://www.baidu.com");
参数1 什么都不填 就是打开一个新窗口. 参数2.填入新窗口的名字(一般可以不填). 参数3: 新打开窗口的参数.
open('','','width=200,resizable=no,height=100'); // 新打开一个宽为200 高为100的窗口
//close方法 将当前文档窗口关闭.
//close();
```

#### settimeOut
```html
<!DOCTYPE html>
<html lang='en'>

<head>
    <meta charset="UTF-8">
    <title>js_timeout</title>
    <script language="javascript" type="text/javascript"></script>
</head>

<body>
    <script>
    function foo() {
        alert(123)
    }
    var timer = setTimeout(foo, 1000);
    //    clearTimeout(timer)
    </script>
</body>

</html>
```
这里页面打开后并不会立即弹出123的框框，而是经过一秒后。 最后的clearTimeout(timer)会将timer这个清除，它与setInterval的不同在,于它不需要事件触发

#### setInterval
```html
<!DOCTYPE html>
<html lang='en'>

<head>
    <meta charset="UTF-8">
    <title>Js_setInterval</title>
    <link rel="stylesheet" type="text/css" href="" />
    <script language="javascript" type="text/javascript"></script>
</head>

<body>
    <input type="text" id="clock" size="35" />
    <button name="start" onclick="set()">Run</button>
    <button name="stop" onclick="stop()">stop</button>
    <script>
    // 得到输入框元素 
    ele = document.getElementById("clock");
    // 得到当前时间，并格式化成本地时间格式 
    // 将当前时间赋值给输入框 
    function start() {
        var now_t = new Date().toLocaleString();
        ele.value = now_t;
    }
    // 清除定时器 
    function stop() {
        clearInterval(counter);
    }
    // 当再次运行时只需要再次建立这个定时器即可 
    function set() {
        counter = setInterval(start, 1000);
    }
    // 当加载完网页时应该已经存在的定时器 
    counter = setInterval(start, 10000);
    </script>
</body>

</html>
```

#### get all brother
```html
<!DOCTYPE html>
<html lang='en'>

<head>
    <meta charset="UTF-8">
    <title>js找到所有兄弟标签</title>
    <!--<link rel="stylesheet" type="text/css" href="*.css"/>-->
    <script language="javascript" type="text/javascript"></script>
</head>

<body>
    <div class="c2">
        <div class="c3">
            <p class="p1">P1</p>
        </div>
        <p class="p2">P2</p>
        <p class="p2">P2</p>
        <p class="p2">P2</p>
        <p class="p2">P2</p>
        <p class="p2">P2</p>
    </div>
</body>
<script>
var brothers = []; //定义兄弟节点数组 
function get_brothers(self) {
    parents = self[0].parentElement; //由c3得到低级节点 
    all_children = parents.children; // 由低级节点得到所有后代节点 
    for (var i = 0; i < all_children.length; i++) {
        if (all_children[i] != ele[0]) {
            brothers.push(all_children[i]); // 将后代节点与c3比较，兄弟节点加入数组 
        }
    }
    return brothers; // 返回包含兄弟节点的数组 
}

var ele = document.getElementsByClassName("c3"); //得到c3数组 
result = get_brothers(ele);
console.log(result);
</script>

</html>
```

#### add new content to table
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>添加删除表格</title>
    <link rel="stylesheet" type="text/css" href="" />
    <script language="javascript" type="text/javascript"></script>
    <link rel="stylesheet" href="bootstrap-3.3.7/css/bootstrap.min.css" type="text/css">
    <style>
        .shade { 
            width: 100%; 
            height: 1600px; 
            border: solid 1px red; 
            background-color: darkgray; 
            position: fixed; 
            opacity: 0.5; 
        } 
        .hide { 
            display: none; 
        } 
        .dialog { 
            position: fixed; 
            background: white; 
            margin-left: 40%; 
            top: 150px; 
            width: 250px; 
            height: 220px; 
        } 
        form { 
            margin-top: 20px; 
            margin-left: 20px; 
        } 
        td button { 
            background-color: red; 
        } 
        #send { 
            margin-left: 70px; 
        } 

        .btn_add { 
            margin-top:50px; 
            margin-right:20px; 
        } 

    </style>
</head>

<body>
    <div class="shade hide"></div>
    <div class="dialog hide">
        <form action="" id="e_form">
            <p>name<input type="text" name='user' id="name" placeholder="name"></p>
            <p>age&nbsp;&nbsp;&nbsp;<input name='age' id="age" type="text" placeholder="age"></p>
            <p><input type="submit" value="添加" id="send"></p>
        </form>
    </div>
    <div class="container">
        <div class="btn_add ">
            <button class="btn">Add</button>
        </div>
        <table class="table table-striped table-bordered text-center table-hover">
            <thead>
            </thead>
            <tbody>
                <tr>
                    <td>name</td>
                    <td>age</td>
                    <td>
                        operation
                    </td>
                </tr>
                <tr>
                    <td>a</td>
                    <td>18</td>
                    <td>
                        <button class="btn del btn-font-color" type="submit">
                            <span class="glyphicon glyphicon-remove" aria-hidden="true">删除</span>
                        </button>
                    </td>
                </tr>
                <tr>
                    <td>b</td>
                    <td>18</td>
                    <td>
                        <button class="btn del btn-font-color" type="submit">
                            <span class="glyphicon glyphicon-remove" aria-hidden="true">删除</span>
                        </button>
                    </td>
                </tr>
                <tr>
                    <td>c</td>
                    <td>18</td>
                    <td>
                        <button class="btn del btn-font-color" type="submit">
                            <span class="glyphicon glyphicon-remove" aria-hidden="true">删除</span>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</body>
<script>
var btn_add = document.getElementsByClassName('btn_add')[0];
var shade = document.getElementsByClassName('shade')[0];
var dialog = document.getElementsByClassName('dialog')[0];
var tbody = document.getElementsByTagName('tbody')[0];
btn_add.onclick = function() {
    shade.classList.remove('hide');
    dialog.classList.remove('hide');

};

var e_form = document.getElementById('e_form');
e_form.onsubmit = function(event) {
    var t = document.createElement('tr');
    var user_name = document.getElementById('name');
    var user_age = document.getElementById('age');
    name = user_name.value;
    age = user_age.value;
    t.innerHTML = '<td>' + name + '</td><td>' + age + '</td><td><button class="btn del btn-font-color" type="submit"><span class="glyphicon glyphicon-remove" aria-hidden="true">删除</span></button></td>';
    tbody.appendChild(t);

    ele_dels = document.getElementsByClassName('btn');
    for (var i = 0; i < ele_dels.length; i++) {
        ele_dels[i].onclick = function() {
            var btn_pp = this.parentElement.parentElement;
            tbody.removeChild(btn_pp);
        };
    }

    event.preventDefault();
    dialog.classList.add('hide');
    shade.classList.add('hide');

};

// 代码重复，实现重新加载删除操作 
ele_dels = document.getElementsByClassName('btn');
for (var i = 0; i < ele_dels.length; i++) {
    ele_dels[i].onclick = function() {
        var btn_pp = this.parentElement.parentElement;
        tbody.removeChild(btn_pp);
    };
}
</script>

</html>
```
#### scroll
最直接的方式 
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>js之滚动到顶部</title>
    <link rel="stylesheet" type="text/css" href="" />
    <script language="javascript" type="text/javascript"></script>
    <style>
        body{ 
            height: 1200px; 
        } 

        .btn{ 
            margin-top:1100px; 
            margin-left:95%; 
            background-color: red; 
        } 

        h1{ 
            text-align: right; 
        } 
    </style>
</head>

<body>
    <h1>This is top</h1>
    <button class="btn" type="submit" name="top">GO</button>
    <h1>This is bottom</h1>
</body>
<script>
btn_go = document.getElementsByName("top")[0];
btn_go.onclick = function() {
    window.scrollTo(0, 0);
}
</script>
</html>
```

#### scroll to top with diy speed
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>js之滚动到顶部</title>
    <link rel="stylesheet" type="text/css" href="" />
    <script language="javascript" type="text/javascript"></script>
    <style>
        body { 
            height: 1200px; 
        } 

        .btn { 
            margin-top: 1100px; 
            margin-left: 95%; 
            background-color: red; 
        } 

        h1 { 
            text-align: right; 
        } 

    </style>
</head>

<body>
    <h1>This is top</h1>
    <button class="btn" type="submit" name="top">GO</button>
    <h1>This is bottom</h1>
</body>
<script>
btn_go = document.getElementsByName("top")[0];

function go() { // 向上滑动的函数 
    y_index = window.pageYOffset;
    x_index = window.pageXOffset;
    console.log(x_index, y_index);
    if (y_index > 0) {
        window.scrollTo(x_index, y_index - 100);

    } else {
        window.clearInterval(counter); // 如果已经顶部了记得清除定时器 
    }
}
btn_go.onclick = function() {
    counter = setInterval(go, 500);
}
</script>

</html>
```

#### scroll to top with jquery
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>滚动到顶部</title>
    <link rel="stylesheet" type="text/css" href="bootstrap-3.3.7/css/bootstrap.min.css" />
    <script type="text/javascript" src="jquery-3.2.1.min.js"></script>
    <script language="javascript" type="text/javascript" src="bootstrap-3.3.7/css/bootstrap.min.css"></script>
    <style>
    .c1 {
        height: 500px;
    }

    #b1 {
        button: 30px; // 此处必须要设置 
        right: 20px position: fixed;
    }
    </style>
</head>

<body>
    <div class="c1">1</div>
    <div class="c1">2</div>
    <div class="c1">3</div>
    <div class="c1">4</div>
    <div class="c1">5</div>
    <div class="c1">6</div>
    <div class="c1">7</div>
    <div class="c1">8</div>
    <div class="c1">9</div>
    <div class="c1">10</div>
    <button id="b1" class="hidden">回到顶部</button>
</body>
<script>
// $(window).scroll(function){} 与下面的效果相同 

$(window).on("scroll", function() {
    if ($(window).scrollTop() > 100) {
        $("#b1").removeClass("hidden"); //当超出当前窗口时显示出来,最开始时是隐藏的 
    } else {
        $("#b1").addClass("hidden"); //否则隐藏起来 
    }
});

$("#b1").on("click", function() {
    $(window).scrollTop(0); //当scrollTop有参数时是设置值，没参数则取值 
})
</script>

</html>
```