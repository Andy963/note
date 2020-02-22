
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

## wechat绑定数据的获取

input框：bindinput: `e.detail.value`
radio: radioChange: `e.detail.value`
data-id: 传参数: `e.currentTarget.dataset.id`


## get_queryset与filterbackends
通常情况下如果在serializer中需要过滤，有两种做法：重写get_queryset方法，或者写filterbackends

这里的主要目的是过滤当前用户：

### filterbackends的方式：
```python
class OrderFilterBackends(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return models.Order.objects.filter(user=request.user)


class Order(ListAPIView):
    authentication_classes = [UserAuthentication, ]
    serializer_class = ser_order.OrderModelSerializer
    queryset = models.Order.objects.all().order_by('-id')
    filter_backends = [ser_order.OrderFilterBackends, ]

    def list(self, *args, **kwargs):
        response = super(Order, self).list(*args, **kwargs)
        if response.status_code != status.HTTP_200_OK:
            return response

        order_dict = OrderedDict()

        # 将订单的状态码，状态描述文字组成字典
        for item in models.Order.status_choices:
            order_dict[item[0]] = {'text': item[1], 'child': []}

        # 将每个状态对应的订单信息放到child列表中，即根据状态码进行了分类
        for row in response.data:
            order_dict[row['status']]['child'].append(row)

        response.data = order_dict
        return response
```

### 重写get_queryset的方式
```python
def get_queryset(self):
    return models.Order.objects.filter(user=self.request.user).order_by('id')
```


## 自定义ModelForm的钩子上传文件

```python
class AuctionItemEditModelForm(BootStrapModelForm):
    exclude_bootstrap_class = ['cover']

    class Meta:
        model = models.AuctionItem
        exclude = ['auction', 'uid', 'deal_price', 'video', 'bid_count', 'look_count']

    def clean(self):
        cleaned_data = self.cleaned_data
        # 上传文件
        cover_file_object = cleaned_data.get('cover')
        if not cover_file_object or isinstance(cover_file_object, FieldFile):
            return cleaned_data
        ext = cover_file_object.name.rsplit('.', maxsplit=1)[-1]
        file_name = "{0}.{1}".format(str(uuid.uuid4()), ext)
        cleaned_data['cover'] = upload_file(cover_file_object, file_name)
        return cleaned_data
```
