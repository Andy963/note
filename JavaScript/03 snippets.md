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