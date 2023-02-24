## datetimepicker使用


### 引入css,js
```css
<link rel="stylesheet" href="{% static 'plugin/datetimepicker/bootstrapdatetimepicker.min.css' %}">
```

```javascript
<script src="{% static 'plugin/datetimepicker/bootstrapdatetimepicker.min.js' %}"></script>
<script src="{% static 'plugin/datetimepicker/bootstrapdatetimepicker.zh-CN.js' %}"></script>
```

### html
```html
<input id='start_time' />
```

### 应用到标签
```javascript
$('#start_time,#end_time').datetimepicker({
    language: "zh-CN",
    minView: "hour",
    sideBySide: true,
    format: 'yyyy-mm-dd hh:ii',
    bootcssVer: 3,
    startDate: new Date(),
    autoclose: true
})
```

### 对时间格式化

```javascript
Date.prototype.Format = function (fmt) { //author: meizz
var o = {
        "M+": this.getMonth() + 1, //月
        "d+": this.getDate(), //日
        "h+": this.getHours(), //小时
        "m+": this.getMinutes(), //分
        "s+": this.getSeconds(), //秒
        "q+": Math.floor((this.getMonth() + 3) / 3), //季度
        "S": this.getMilliseconds() //毫秒
    };
    if (/(y+)/.test(fmt)) fmt = fmt.replace(RegExp.$1,
    (this.getFullYear() + "").substr(4 - RegExp.$1.length));
        for (var k in o)
        if (new RegExp("(" + k + ")").test(fmt)) fmt =
        fmt.replace(RegExp.$1, (RegExp.$1.length == 1) ? (o[k]) : (("00" +
        o[k]).substr(("" + o[k]).length)));
    return fmt;
    };
Date.prototype.format = function (fmt){
    return 123
}

var ctime = new Date()
// ctime -> Tue Feb 11 2020 09:50:27 GMT+0800 (中国标准时间)
var result = ctime.format('yyyy-MM-dd')
console.log(result);
```

## 传参数

### html中：
```html
</view>
  <view><button size="mini" bindtap="receive_coupon" data-auction_id="{{item.id}}">领取</button>
</view>
```

### js中获取 ：
```javascript
receive_coupon: function(options) {
    var auction_id = options.currentTarget.dataset.auction_id;
}
```

## 图片叠加

### html
图片在底层，文字浮在图片上面
```html
<view wx:for="{{coupon_list}}" wx:key="{{index}}" class="main">
  <view class="back-ground">
    <image src="{{item.cover}}"></image>
  </view>
  <view class="info">
    <view>
      <text>{{item.title}}</text>
    </view>
    <view>
      <text>{{item.start_time}}</text>
    </view>
    <text>¥{{item.money}}</text>
    <text>剩余{{item.left_count}}张</text>
    <text>{{item.status}}</text>
  </view>
  <view><button size="mini" bindtap="receive_coupon" data-auction_id="{{item.id}}">领取</button></view>
</view>
```

### css部分
z-index小的在里面，需要设置为position:absolute, 而z-index大的在外面，设置position:relative
```stylesheet
.back-ground{
  z-index: 0;
  position:absolute;
}

.back-ground image{
  width:740rpx;
  height:350rpx;
}

.info{
  z-index:1;
  position: relative;
  color:red;
}
```