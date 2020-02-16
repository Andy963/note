
## if判断语句
```html
  <view>
    <button wx:if="{{item.status_code}}" size="mini" bindtap="receive_coupon" data-coupon_id="{{item.id}}">{{item.status}}</button>
    <button wx:else="{{item.status_code}}" size="mini" bindtap="receive_coupon" data-coupon_id="{{item.id}}">{{item.status}} </button>
  </view>
```



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

## 页面中去掉share

> 去掉   onShareAppMessage: function() 
> 在页面的onload函数中使用 wx.hideShareMenu({})


## 闭包的使用

自执行函数

```javascript
#先写两个人括号， 第一个括号中function的参数arg即 后面括号中的taget

（function(arg)）（target）
    (function(idx) {
            cos.postObject({
              Bucket: 'auction-1255763912',
              Region: 'ap-beijing',
              Key: fileName,
              FilePath: imageFilePath,
              onProgress: (info) => {
              }
            }, (err, data) => {
              // 上传成功或失败

              ths.setData({
                ["onlineImageList[" + idx + "]"]: data.Location
              });
              // 判断是否上传完成，没完成不能发布
              if (ths.data.imageList.length == ths.data.onlineImageList.length) {
                ths.setData({
                  disabled: false
                })
              }
            });
          })(targetIndex)
```


## 支付功能的设计

* 付款时可以选择使用优惠券
    * 使用优惠券，扣款时判断优惠券是否可用，扣对应的金额，更改优惠券状态为已已使用
    * 不使用