### csrf_token携带方式

```js
#方式一
$.ajaxSetup({
    data: {csrfmiddlewaretoken: '{{ csrf_token }}' },

});
# 上面的方式它的局限性在于必须放在html中,如果放在独立js文件中,客户端浏览器会请求js文件,此时csrf_taken没有渲染

# 方式二:
data:{
    "csrfmiddlewaretoken":$("[name='csrfmiddlewaretoken']").val(); 
}

#方式三:
<script src="{% static 'js/jquery.cookie.js' %}"></script> 
    $.ajax({
    headers:{"X-CSRFToken":$.cookie('csrftoken')},
    })
```
