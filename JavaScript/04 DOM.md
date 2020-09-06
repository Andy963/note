## DOM
Document object model
HTML  Document Object Model（文档对象模型） 
HTML DOM 定义了访问和操作HTML文档的标准方法 
HTML DOM 把 HTML 文档呈现为带有元素、属性和文本的树结构（节点树) 

DOM 是这样规定的： 
> 整个文档是一个文档节点  
> 每个 HTML 标签是一个元素节点  
> 包含在 HTML 元素中的文本是文本节点  
> 每一个 HTML 属性是一个属性节点 

### relationship
节点树中的节点彼此拥有层级关系。 
父(parent),子(child)和同胞(sibling)等术语用于描述这些关系。父节点拥有子节点。同级的子节点被称为同胞（兄弟或姐妹）。 
```
在节点树中，顶端节点被称为根（root） 
每个节点都有父节点、除了根（它没有父节点） 
一个节点可拥有任意数量的子 
同胞是拥有相同父节点的节点 
```

### location
```js
document.getElementById(“idname”)  
document.getElementsByTagName(“tagname”) 
document.getElementsByName(“name”) 
document.getElementsByClassName(“name”) 
```
#### attr
这些是属性，通过点号调用
```
parentElement           // 父节点标签元素 
children                // 所有子标签，数组 
firstElementChild       // 第一个子标签元素 
lastElementChild        // 最后一个子标签元素 
nextElementtSibling     // 下一个兄弟标签元素 
previousElementSibling  // 上一个兄弟标签元素 
```
注意，js中没有办法找到所有的兄弟标签！ 一种方法是：先找到父节点，从父节点找它的子节点，然后去掉自己即可
### Node
#### create
```js
createElement(标签名) ：//创建一个指定名称的元素。 
var  tag=document.createElement(“input") 
tag.setAttribute('type','text'); 
```

#### insert/append
```js
//追加一个子节点（作为最后的子节点） 
somenode.appendChild(newnode) 
//把增加的节点放到某个节点的前边 
somenode.insertBefore(newnode,某个节点); 
```
#### delete
```js
removeChild()：//获得要删除的元素，通过父元素调用删除 
```
#### replace
```js
somenode.replaceChild(newnode, 某个节点); 
```
#### attr
##### innerText/innerHTML
获取文本节点的值：innerText    innerHTML 
取文本：ele.innerText 
赋值文本：ele.innerText="This is a text" 
innerHTML同样的道理 

##### attribute
elementNode.setAttribute(name,value),ele.id = "d2"; 
elementNode.getAttribute(属性名) <-------------->elementNode.属性名(DHTML) 
elementNode.removeAttribute(“属性名”); 
console.log(ele.getAttribute("id"); 
console.log(ele.id); 

##### value获
取当前选中的value值 
input    
select （selectedIndex） 
textarea   

##### class
elementNode.className 
elementNode.classList.add 
elementNode.classList.remove 
可以将一个写好的样式加到指定标签，实现动态效果 

##### css
```js
<p id="p2">Hello world!</p>
document.getElementById("p2").style.color="blue"; 
```

### event
onclick        当用户点击某个对象时调用的事件句柄。 
ondblclick     当用户双击某个对象时调用的事件句柄。 
onfocus        元素获得焦点。               练习：输入框 
onblur         元素失去焦点。               应用场景：用于表单验证,用户离开某个输入框时,代表已经输入完了,我们可以对它进行验证. 
onchange       域的内容被改变。             应用场景：通常用于表单元素,当元素内容被改变时触发.（三级联动） 
onkeydown      某个键盘按键被按下。          应用场景: 当用户在最后一个输入框按下回车按键时,表单提交. 
onkeypress     某个键盘按键被按下并松开。 
onkeyup        某个键盘按键被松开。 
onload         一张页面或一幅图像完成加载。 
onmousedown    鼠标按钮被按下。 
onmousemove    鼠标被移动。 
onmouseout     鼠标从某元素移开。 
onmouseover    鼠标移到某元素之上。 
onmouseleave   鼠标从元素离开 
onselect       文本被选中。 
onsubmit       确认按钮被点击。 

#### addListener
```js
//方式1:
<div id="div" onclick="foo(this)">点我呀</div>
<script>

function foo(self) { // 形参不能是this; 
    console.log("点你大爷!");
    console.log(self);
}
</script>

//方式2:
<p id="abc">试一试!</p>
<script>

var ele = document.getElementById("abc");
ele.onclick = function() {
    console.log("ok");
    console.log(this); // this直接用 
};
</script>
```
如果不能确定this指代什么，那么可以看看onclick动作前面的对象，在这里指代ele，也就是当前触发事件的对象。

#### onload
onload 属性开发中 只给 body元素加.这个属性的触发 标志着 页面内容被加载完成.应用场景: 当有些事情我们希望页面加载完立刻执行,那么可以使用该事件属性
```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script>
    window.onload = function() {
        var ele = document.getElementById("ppp");
        ele.onclick = function() {
            alert(123)
        };
    };


    function fun() {
        var ele = document.getElementById("ppp");
        ele.onclick = function() {
            alert(123)
        };
    }
    </script>
</head>

<body onload="fun()">
    <p id="ppp">hello p</p>
</body>

</html>
```

#### onsubmit 
当表单在提交时触发. 该属性也只能给form元素使用.应用场景: 在表单提交前验证用户输入是否正确.如果验证失败.在该方法中我们应该阻止表单的提交. 
```js
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script>
        window.onload=function(){ 
    //阻止表单提交方式1(). 
    //onsubmit 命名的事件函数,可以接受返回值. 其中返回false表示拦截表单提交.其他为放行. 

    var ele=document.getElementById("form"); 
    ele.onsubmit=function(event) { 
    //    alert("验证失败 表单不会提交!"); 
    //    return false; 

    // 阻止表单提交方式2 event.preventDefault(); ==>通知浏览器不要执行与事件关联的默认动作。 
     alert("验证失败 表单不会提交!"); 
     event.preventDefault(); 
    } 
}; 

</script>
</head>

<body>
    <form id="form">
        <input type="text" />
        <input type="submit" value="点我!" />
    </form>
</body>

</html>
```
#### onselect
```js
<input type="text">
<script>
var ele = document.getElementsByTagName("input")[0];

ele.onselect = function() {
    alert(123);
}
</script>
```

#### onchange
```js
<select name="" id=""> 
    <option value="">111</option> 
    <option value="">222</option> 
    <option value="">333</option> 
</select> 

<script> 
var ele=document.getElementsByTagName("select")[0]; 
ele.onchange=function(){ 
    alert(123); 
} 
</script> 
```
#### onkeydown: 
Event 对象：Event 对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。 
事件通常与函数结合使用，函数不会在事件发生前被执行！event对象在事件发生时系统已经创建好了,并且会在事件函数被调用时传给事件函数.我们获得仅仅需要接收一下即可.比如onkeydown,我们想知道哪个键被按下了，需要问下event对象的属性，这里就是KeyCode. 
```js
<input type="text" id="t1" />
<script type="text/javascript">
var ele = document.getElementById("t1");

ele.onkeydown = function(e) {

    e = e || window.event;

    var keynum = e.keyCode;
    var keychar = String.fromCharCode(keynum);

    alert(keynum + '----->' + keychar);

};
</script>
```

#### propagate
```
<div id="abc_1" style="border:1px solid red;width:300px;height:300px;"> 
        <div id="abc_2" style="border:1px solid red;width:200px;height:200px;"> 

</div> 
</div> 

<script type="text/javascript"> 
        document.getElementById("abc_1").onclick=function(){ 
            alert('111'); 
        }; 
        document.getElementById("abc_2").onclick=function(event){ 
            alert('222'); 
            event.stopPropagation(); //阻止事件向外层div传播. 
        } 
</script> 
```

#### diff between onmouseout and onmouseleave
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
    #container {
        width: 300px;
    }

    #title {
        cursor: pointer;
        background: #ccc;
    }

    #list {
        display: none;
        background: #fff;
    }

    #list div {
        line-height: 50px;
    }
    #list .item1 {
        background-color: green;
    }

    #list .item2 {
        background-color: rebeccapurple;
    }

    #list .item3 {
        background-color: lemonchiffon;
    }
    </style>
</head>

<body>
    <p>先看下使用mouseout的效果:</p>
    <div id="container">
        <div id="title">使用了mouseout事件↓</div>
        <div id="list">
            <div class="item1">第一行</div>
            <div class="item2">第二行</div>
            <div class="item3">第三行</div>
        </div>
    </div>
    <script>
    // 1.不论鼠标指针离开被选元素还是任何子元素，都会触发 mouseout 事件。 
    // 2.只有在鼠标指针离开被选元素时，才会触发 mouseleave 事件。 
    var container = document.getElementById("container");
    var title = document.getElementById("title");
    var list = document.getElementById("list");
    title.onmouseover = function() {
        list.style.display = "block";
    };
    container.onmouseleave = function() { // 改为mouseout试一下 
        list.style.display = "none";
    };
    /* 
     因为mouseout事件是会冒泡的，也就是onmouseout事件可能被同时绑定到了container的子元素title和list 
     上，所以鼠标移出每个子元素时也都会触发我们的list.style.display="none"; 
    /* 

     思考: 

     if: 
     list.onmouseout=function(){ 
     list.style.display="none"; 
     }; 
     为什么移出第一行时,整个list会被隐藏? 
     其实是同样的道理,onmouseout事件被同时绑定到list和它的三个子元素item上,所以离开任何一个 子元素同样会触发list.style.display="none"; 
     */
    </script>
</body>

</html>
```