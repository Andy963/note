# GoJs

GoJs是一个js库，实现动态绘图的神器。功能实在是太过强大，这里只记录一点基本用法。为达到基本功能，我们需要用到四部分组件：TextBlock，Shape，Node，Link。 下面就按这个顺序来做一些记录。

使用的基本步骤为： 
* 引入js
* 添加容器
* 创建一个目标gojs对象
* 向容器中添加元素

需要说明的是$只是为了简单，方便，也可以用其它字符串，比如$$，因为我们一般习惯用$来表示 jQuery.

```js
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script src="go-debug.js"></script>
</head>
<body>
<div id="myDiagramDiv" style="width:500px; height:350px; background-color: #DAE4E4;"></div>

<script>
    var $ = go.GraphObject.make;
    // 第一步：创建图表
    var myDiagram = $(go.Diagram, "myDiagramDiv"); // 创建图表，用于在页面上画图

    // 第二步：创建一个节点，内容为andy
    var node = $(go.Node, $(go.TextBlock, {text: "andy"}));

    // 第三步：将节点添加到图表中
    myDiagram.add(node)
</script>
</body>
</html>
```

## TextBlock
文字信息

### Font and colors
字体与颜色：

```js
#  字体
$(go.TextBlock, { text: "a Text Block", font: "bold 14pt serif" })
#  颜色这里叫stroke
$(go.TextBlock, { text: "a Text Block", stroke: "red" }),
#  背景色
$(go.TextBlock, { text: "a Text Block", background: "lightblue" }),
```
考虑到不同浏览器对文本的渲染不一样，所以最好不要用没有指定大小的TextBlock来限制/规定其它对象的大小。

### Sizing and Clipping

大小与裁剪,当我们的外框比文本内容还要小时，就会导致文字被裁剪，只能看到一部分文字
```js
$(go.TextBlock, { text: "a Text Block", background: "lightgreen", margin: 2, width: 40, height: 9 })
```

## Shape
图形

```js
var node1 = $(go.Node,
        $(go.Shape, {figure: "Ellipse", width: 40, height: 40})
);
//  fill 指定填充
 var node2 = $(go.Node,
        $(go.Shape, {figure: "RoundedRectangle", width: 40, height: 40, fill: 'green',stroke:'red'})
    );

// 对于非内置的图形，需要引入Figures.js
    var node5 = $(go.Node,
        $(go.Shape, {figure: "Club", width: 40, height: 40, fill: 'red'})
    );
```
## Node
节点

```js
 var node1 = $(go.Node,
        "Vertical",  //指定排列的纵横，"Horizontal", 水平
        {
            background: 'yellow',
            padding: 8
        },
        $(go.Shape, {figure: "Ellipse", width: 40, height: 40}),
        $(go.TextBlock, {text: "andy"})
    );
```
## Link
连接线

```js
<script>
    var $ = go.GraphObject.make;
    // 第一步：创建图表
    var myDiagram = $(go.Diagram, "myDiagramDiv"); // 创建图表，用于在页面上画图
    
    //创建第一个节点
    var startNode = $(go.Node, "Auto",
        $(go.Shape, {figure: "Ellipse", width: 40, height: 40, fill: '#79C900', stroke: '#79C900'}),
        $(go.TextBlock, {text: '开始', stroke: 'white'})
    );
    
    //创建第二个节点
    var endNode = $(go.Node, "Auto",
        $(go.Shape, {figure: "RoundedRectangle", height: 40, fill: '#79C900', stroke: '#79C900'}),
        $(go.TextBlock, {text: '继续', stroke: 'white'})
    );
    // 第三步：将节点添加到图表中
    myDiagram.add(startNode);
    myDiagram.add(endNode);

    // 将上面两个节点连接起来
    var start2end = $(go.Link,
        {fromNode: startNode, toNode: endNode},
        $(go.Shape, {strokeWidth: 1}),
        $(go.Shape, {toArrow: "OpenTriangle", fill: null, strokeWidth: 1})
    );
    myDiagram.add(start2end);
</script>
```

但如果这样一个个添加实在太费劲了，有没有更好的方式呢？

## 数据绑定

```js
<script>
    var $ = go.GraphObject.make;
    // 第一步：创建图表
    var myDiagram = $(go.Diagram, "myDiagramDiv"); // 创建图表，用于在页面上画图
    // 指定连接的模板
    myDiagram.linkTemplate =
        $(go.Link,
            $(go.Shape, {isPanelMain: true, stroke: "transparent", strokeWidth: 8}),  // thick undrawn path
            $(go.Shape, {isPanelMain: true}),  // default stroke === "black", strokeWidth === 1
            $(go.Shape, {toArrow: "Standard"})
        );
    //创建Model
    var myModel = $(go.Model);
    // 绑定model中的对象
    myModel.nodeDataArray = [
        {key: 'a'},
        {key: 'b'},
        {key: 'c'},
    ];
    // 绑定link的属性
    var linkDataArray = [
        { from: "a", to: "b" },
        { from: "a", to: "c" }
    ];
    // 将model对象与link绑定到一起
    myDiagram.model = myModel;
    myDiagram.model = new go.GraphLinksModel(myModel.nodeDataArray, linkDataArray);
</script>
```

ref: https://gojs.net/latest/intro/textBlocks.html
ref: https://www.cnblogs.com/wupeiqi/articles/11978547.html