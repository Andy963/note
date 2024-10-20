


### 页面
```html
<form id='mmm'>
<input type="text" name='user' id='f1'/>
<input type="file" name='avatar' id='f2'/>
<input type="checkbox" />
</form>
```

### ajax
```javascript

var formData = new FormData();
formData.append('k1',$('#f1').val())
formData.append('k2',$('#f2')[0].files[0])

/*整个form作为表单append到FormData对象*/
// 注意 如果表单中有checkbox或者radio标签且未选中，则FormData不会构造到自己的数据中
var formData = new FormData($('#mmm')[0]);
$.ajax({
    url:'..',
    type:"post",
    data:formData,
    
    cache: false,
    contentType: false,
    processData: false,
    
    success:function(res){
        console.log(res)
    }
})
```

### 文件上传按钮美化，实时预览

#### css部分
```css
<style>
    .file-view {
        height: 80px;
        width: 80px;
        padding: 2px;
        border: 1px dotted #dddddd;
        position: relative;
    }

    .file-view .view-file {
        position: absolute;
        width: 100%;
        height: 100%;
        opacity: 0;
        z-index: 1001
    }
    .file-view .view-img {
        height: 100%;
        width: 100%;
        border: 0;
        overflow: hidden;
    }
</style>
```

#### Html部分

```html
<div class="file-view">
<input class="view-file" type="file" name="img">
<img class="view-img" src="{% static 'web/images/default-image.png'%}">
</div>
```

#### js部分
```javascript
$(function () {
    bindChangeImageFile();
});
function bindChangeImageFile() {
    $('#areaImage').on('change', '.view-file', function () {
        var fileObject = $(this)[0].files[0];
        var file_url = window.URL.createObjectURL(fileObject);
        $(this).next().attr('src', file_url);
        // 赋值完重新加载
        $(this).next().load(function () {
            window.URL.revokeObjectURL(file_url);
    })
})
```

### 头像实时预览
思路：文件选择框的change事件，获取到加载到内存中的文件对象，通过readAsDataURL方法读取内存中文件对象为Url,然后重新加载到文件显示位置
```js
#  文件change时将文件的url赋值过来
#   头像预览, 可能多次选择,要跟随选择发生变化,所以应该用change
$("#avatar_file").change(function(){
	var ele_file = $(this)[0].files[0];  # this.files
	var reader = new FileReader();  # 默认没有返回值,将值赋值给了self.result

	reader.readAsDataURL(ele_file); # 当前数据的url
reader.onload = function(){
	$("#preScan").attr("src", this.result);
}
})
```
