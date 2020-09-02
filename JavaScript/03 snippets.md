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