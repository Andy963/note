## wechat 自定义tabbar

### 创建目录component
创建页面时是选择component而非pages

### 全局app.json中配置
```json
// 指定tabBar为custom
 "tabBar": {
    "custom": true,
    }
```

### article.json中配置
```json
//  指定要使用的组件
{
  "usingComponents": {
  
    "tb":"/component/tabbars/tabbar"
  },
  "enablePullDownRefresh":true
}
```

### article.wxml中添加 
```html
// 名字与上面json中保持一致
<tb></tb>
```

### 其它页面使用
#### 页面中嵌入
首页中引用tab使用的`<tb selected="{{0}}"></tb>`, 后面的页面可以依次是：`<tb selected="{{0}}"></tb>`

#### 在tabbar的js中
```javascript
  properties: {
    selected: {
      type: Number,
      value: 0
    }
  },

```
#### tabbar中定义switch tab 方法,要跳转的路径从页面中传过来

```javascript
methods: {
    switchTab(e) {
      const data = e.currentTarget.dataset
      const url = data.path
      wx.switchTab({url})
      this.setData({
        selected: data.index
      })
    }
  }
```

### 页面中去掉share

> 去掉   onShareAppMessage: function() 
> 在页面的onload函数中使用 wx.hideShareMenu({})