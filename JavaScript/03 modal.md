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
    $("#input_id").val("传过来的值");
}
```