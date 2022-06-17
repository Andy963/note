## 002_page

### wxss

新增了rpx尺寸单位
CSS中需要手动进行像素单位换算例如rem, WXSS在底层支持新的尺寸单位rpx,在不同大小的屏幕上小程序会自动进行换算

提供了全局的样式和局部样式
顶目根目录中的wxss会作用于所有小程序页面
局部页面的.wxss样式仅对当前页面生效

WXSS仅支持部分CSS选择器
.class和#id
element
并生華择器、后代选择器
::after和::before等伪类选择器

### js

app.js 整个小程序项目的入口文件，通过调用App()函数来启动整个小程序
页面.js  是页面入口文件，通过调用Page()函数来创建并运行页面
普通.js  普通的功能模块文件，用来封闭公共的函数或者属性


### flex 布局
list.wxml

```html
<!--pages/list/list.wxml-->
<text>pages/list/list.wxml</text>
<view class="container1">
  <view>A</view>
  <view>B</view>
  <view>C</view>
</view>
```

这里用到了nth-child选择器：用来选择父元素中的第n个子元素。

```js
/* pages/list/list.wxss */
.container1 view {
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100xp;
}

.container1 view:nth-child(1){
  background-color: #aff;
}
.container1 view:nth-child(2){
  background-color: #afa;
}
.container1 view:nth-child(3){ 
  background-color: #00f;
}
.container1{
  display: flex;
  justify-content: space-around;
}
```

### scroll-vew
实现上下滑动的效果：
将`view` 改为`scroll-view`
添加`scroll-y`属性,如果要横向滚动则要添加`scroll-x`
固定一个高度

list.wxml

```html
<!--pages/list/list.wxml-->
<text>pages/list/list.wxml</text>
<scroll-view class="container1" scroll-y>
  <view>A</view>
  <view>B</view>
  <view>C</view>
</scroll-view>
```

增加高度限制

```wxss
/* pages/list/list.wxss */
.container1 view {
  width: 100px;
  height: 100px;
  text-align: center;
  line-height: 100xp;
}

.container1 view:nth-child(1){
  background-color: #aff;
}
.container1 view:nth-child(2){
  background-color: #afa;
}
.container1 view:nth-child(3){ 
  background-color: #00f;
}
.container1{
  border:1px solid red;
  width:100px;
  height: 120px;
}
```

### swiper && swiper-item
用来实现轮播图效果

```html
<text>pages/list/list.wxml</text>
<swiper class="swiper-container1">
  <swiper-item>
    <view class="item">A</view>
  </swiper-item>
  <swiper-item>
    <view class="item">B</view>
  </swiper-item>
  <swiper-item>
    <view class="item">C</view>
  </swiper-item>
</swiper>
```

对应的wxss如下：

```css
.swiper-container1 {
  height: 150px;
}

.item {
  height: 100%;
  line-height: 150px;
  text-align: center;
}

swiper-item:nth-child(1) .item {
  background-color: lightblue;
}
swiper-item:nth-child(2) .item {
  background-color: lightgrey;
}
swiper-item:nth-child(3) .item {
  background-color: lightpink;
}
```

swiper 常用属性说明
```html
<swiper class="swiper-container1" indicator-dots indicator-color="white" indicator-active-color="grey" autoplay="true" interval="1000" circular="true">
```
indicator-dots是否有小圆点， indicator-color,indcator-active-color分别指示未激活，激活时的圆点的颜色， autoplay则指示是否自动播放， interval 自动切换的间隔。


### text
如果要文本可以选中，则需要给`text`标签加上selectable属性。
rich-text 可以将html渲染成对应的ui结构， 但需要通过nodes属性来实现：`<rich-text nodes="<h1 style='color:red;'>我是标题1</h1>"></rich-text>`


### button
可以通过设置`open-type`来调用不同微信的功能

```html
<button>普通按钮</button>
<button type="primary">主色调</button>
<button type="warn">警告</button>
<button size="mini">小按钮</button>
<button type="primary" size="mini">主色调小</button>
<button type="primary" size="mini" plain>镂空</button>
```

### image
image 可以通过mode属性来指定图片裁剪和缩放模式，常用的mode属性有：
scaleToFill 绽放模式，不保持纵横比，图片宽高完全拉伸至填满image元素
aspectFit 保持纵横缩放，保证长边完全显示，可以完整的将图片显示出来
aspectFill 缩放模式，保持纵横比缩放，只保证短边能能完全显示出来，可能导致长边的截取
widthFix 缩放模式，宽度不变，高度自动变化，保持原图宽高比不变
heightFix 缩放模式，高度不变，宽度自动变化，保持原图宽高比不变


### 事件绑定
常见事件有 tap,input, change 分别是手指触摸后离开，文本框输入，状态改变事件，绑定方式如：bindtap或者bind:tap. 事件触发时会传event对象，它包含一系列的属性。
type:事件类型
timestamp: 页面打开到触发事件所经历的毫秒数
target:触发事件的组件，源头
currentTarget:当前组件的一些属性值组合，当前事件的组件
detail:额外信息
touches:触摸事件，当前停留在屏幕中的触摸点信息的数组
changedTouches 触摸事件，当前变化的触摸点信息的数组


#### bindtap
传值操作
通过下面的按钮将上面的数字加一

```html
<button type="default">count:{{count}}</button>
<button type="primary" bindtap="plusOne">plus one</button>
```

在js中使用`this.setData`方法，里面是对象，`{key,value}`形式

```js
  plusOne(){
    this.setData({
      count:this.data.count +1
    })
  }
```

*注意* 在小程序中，`<button type="primary" bindtap='btnHandler(123)'>事件传参</button>`  这样小程序不会把123当成参数处理，而是整个当前一个名为：btnHandler(123)的事件来处理。

正确的传参方法为 `data-*` 如data-info, 而获取时通过 `event.target.dataset.info`即可获取，看下面示例：

通过data-变量名传入变量，如果直接使用data-c="2"，传入的是字符串，而非数字

```html
<span>count2:{{count2}}</span>
<button type="primary" bind:tap="plusTwo" data-c="{{2}}">plus two</button>
```

通过event.target.dataset.c 获取传入的参数值

```js
plusTwo(event){
 this.setData({
   count2:this.data.count2 + event.target.dataset.c
 })
},
```

#### bindinput
bindinput用法：`<input bindinput="inputHandler"><input>` 要拿到变化之后的值通过`e.detail.value`

绑定bindinput

```html
<input bindinput="inputHandler" placeholder="input value"></input>
```

通过e.detai.value获取到改变后的值：

```js
 /**
   * 输入
   * @param {*} options
   */
  inputHandler(e) {
    console.log(e.detail.value);
  },
```

### 条件渲染
可以通过`wx:if="{{condition}}"`来决定


```html
<view wx:if="{{type === 1}}">男</view>
<view wx:elif="{{ type=== 2}}">女</view>
<view wx:else>保密</view>
```

```js
data:{
    type:1
}
```

如果要一次性控制多个组件的展示与隐藏，可以使用一个`<block></block>`标签将多个组件包裹起来，并在block中使用wx:if控制，而block只是一个包裹性质的容器，不会在页面中做任何渲染

同样，hidden也可以达到类似目的 hidden="{{condition}}"

### wxss
rpx :微信小程序中定义的单位，r代表response ，将屏幕等分为750份。

@require

在根目录下建文件夹common/common.wxss

```css
.success{
  color:green;
}
```

在pages中的list.wxss导入：

```css
@import "/common/common.wxss";
```

这样在list.wxml中就可以直接使用了

```html
<view wx:if="{{type === 1}}" class="success">男</view>
```

### 全局配置
window 全局设置小程序窗口的外观
常用配置项：
app.json window对象中设置

```
// 导航栏相关
navigationBarTitleText  导航栏标题
navigationBarBackgroundColor 导航栏背景色，只支持十六进制
navigationBarTextStyle 导航栏标题文字颜色
//
backgroundColor 窗口背景色， 只支持十六进制
backgroundTextStyle 下拉时的三个小圆点样式，默认为light,
// 
enablePullDownRefresh 下拉刷新
onReachBottomDistance 上拉触底的距离，上拉到加载更多数据，默认为50px,设置时只需要写数字，不需要单位。通常不需要修改

```
tabBar 设置小程序底部的tabBar效果
