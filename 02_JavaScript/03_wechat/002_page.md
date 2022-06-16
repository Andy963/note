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