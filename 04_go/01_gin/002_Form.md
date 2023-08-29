### Must Bind / Should Bind

区别是如果是MustBind，发生错误时会终止程序。

#### Form

view

```go
func BindForm(c *gin.Context) {  
    c.HTML(http.StatusOK, "chapter4/bind_form.html", nil)  
  
}  
  
type User struct {  
    Name    string `form:"name"`  
    Age     int    `form:"age"`  
    Address string `form:"address"`  
}  
  
func PostBindForm(c *gin.Context) {  
    var user User  
    err := c.ShouldBind(&user)  
    if err != nil {  
       c.HTML(http.StatusOK, "chapter4/bind_form.html", nil)  
    }  
    c.HTML(http.StatusOK, "chapter4/bind_form.html", nil)  
}
```
因为gin要访问自定义的结构体User中的字段，所以必须将这些字段首字母大写。

html

```html
{{ define "chapter4/bind_form.html"}}  
    <!DOCTYPE html>  
    <html lang="en">  
    <head>        <meta charset="UTF-8">  
        <title>Bind Form</title>  
    </head>    <body>    <form action="/post/bind_form" method="post">  
        name:<input type="text" name="name"> <br>  
        age :<input type="text" name="age"> <br>  
        address:<input type="text" name="address"><br>  
        <input type="button" value="提交">  
    </form>  
    </body>    
    </html>{{end}}
```

route

```go
router.GET("/bind_form", chapter4.BindForm)  
router.GET("/post/bind_form", chapter4.PostBindForm)
```

#### Query string

view

```go
package chapter4  
  
import (  
    "fmt"  
    "github.com/gin-gonic/gin")  
  
func BindQueryString(c *gin.Context) {  
    var user User  
    err := c.ShouldBindQuery(&user)  
    if err != nil {  
       c.String(200, err.Error())  
    }  
    fmt.Println(user)  
    c.String(200, c.Request.URL.Query().Get("name"))  
}
```

router

```go
router.GET("/bind_query", chapter4.BindQueryString)
```

#### JSON

view

```go
package chapter4  
  
import (  
    "fmt"  
    "github.com/gin-gonic/gin"    "net/http")  
  
func BindForm(c *gin.Context) {  
    c.HTML(http.StatusOK, "chapter4/bind_form.html", nil)  
  
}  

type User struct {  
    Name    string `form:"name" json:"name"`  
    Age     int    `form:"age" json:"age"`  
    Address string `form:"address" json:"address"`  
}  
  
func BindJson(c *gin.Context) {  
    c.HTML(http.StatusOK, "chapter4/bind_json.html", nil)  
}  

func PostBindJson(c *gin.Context) {  
    var user User  
    err := c.ShouldBindJSON(&user)  
    if err != nil {  
       fmt.Println(err)  
       c.JSON(http.StatusNotFound, gin.H{  
          "code": 404,  
          "data": "",  
       })  
    }  
    fmt.Println(user)  
    c.JSON(http.StatusOK, gin.H{  
       "code": 200,  
       "data": user,  
    })  
}
```

router

```go
router.GET("/bind_json", chapter4.BindJson)  
router.POST("/post/bind_json", chapter4.PostBindJson)
```

html

```html
{{ define "chapter4/bind_json.html"}}  
    <!DOCTYPE html>  
    <html lang="en">  
    <head>        <meta charset="UTF-8">  
        <title>Bind Json</title>  
        <script src="/static/js/jquery.js"></script>  
    </head>    <body>    <form>        <input type="text" id="name" name="name"><br>  
        <input type="text" id="age" name="age"><br>  
        <input type="text" id="address" name="address"><br>  
        <input type="button" value="提交" id="btn">  
    </form>  
    </body>    <script>        var btn = document.getElementById('btn');  
        btn.onclick = function (e) {  
            let name = document.getElementById("name").value;  
            let age = document.getElementById("age").value;  
            let address = document.getElementById("address").value;  
            $.ajax({  
                url: "/post/bind_json",  
                type: "POST",  
                contentType: "application/json",  
                dataType: "json",  
                data: JSON.stringify({  
                        "name": name,  
                        "age": Number(age),  
                        "address": address  
                    }  
                ),  
                success: function (data) {  
                    alert(data["code"]);  
                },  
                fail: function (data) {  
                    alert("server error");  
                },  
  
  
            })  
        }  
    </script>  
    </html>{{end}}
```

#### uri 
与前面的类似，它是在url中使用： /:name/:age/:address
对就的struct中也是添加对应的字段

```go
type User struct {  
    Name    string `form:"name" json:"name" uri:"name"`  
    Age     int    `form:"age" json:"age" uri:"age"`  
    Address string `form:"address" json:"address" uri:"address"`  
}  
  
```

### validate field

```
-  忽略字段 
required  必填
min,max 最小/大长度
|  或 binding "rgb|gba" 枚举
omitempty, 如果字段为空，就不展示在结果中

```

#### structonly, dive

```go
type Address struct {
	Street string
	City   string
}

type User struct {
	Name    string
	Address Address `binding:"required,structonly"`
}
// 上面的不会验证到Street, City
// 下面则会递归到内部结构体Address中的Street, City
type Address struct {
	Street string
	City   string
}

type User struct {
	Name    string
	Address Address `binding:"required,dive"`
}

```

eqfield
nefield
alpha
alphanumber
email
contains
excludes

### 自定义验证器

#### 安装validator

```go
go get github.com/go-playground/validator/v10
```

#### 定义验证器

```go
var LenValidator validator.Func = func(fl validator.FieldLevel) bool {  
    // 通过fl.Field() 获取到字段  
    return len(fl.Field().String()) >= 5  
}
```

#### 注册验证器

注意要在router之前注册

```go
v, ok := binding.Validator.Engine().(*validator.Validate)  
if ok {  
    err := v.RegisterValidation("lenValidate", chapter4.LenValidator)  
    if err != nil {  
       fmt.Println(err)  
    }  
}
```

#### 使用验证器

```go
type Article struct {  
    Id      int    `form:"-"` // - 表示不校验  
    Title   string `form:"title" binding:"required,lenValidate"`  
    Content string `form:"content" binding:"min=5"`  
}
// Key: 'Article.Title' Error:Field validation for 'Title' failed on the 'lenValidate' tag
```


### beego

安装

```go
go get github.com/astaxie/beego/validation
```

#### 定义

```go
func Validate4Beego(c *gin.Context) {  
    var art Artic  
    _ := c.ShouldBind(&art)  
  
    //初始化validator  
    valid := validation.Validation{}  
    isValid, err := valid.Valid(&art)  
    fmt.Println(err)  
    if !isValid {  
       for _, e := range valid.Errors {  
          fmt.Println(e.Key, e.Message)  
       }  
       return  
    }  
}
```

#### 使用

```go
type Artic struct {  
    Id      int    `form:"-"`  
    Title   string `form:"title" valid:"Required"`  
    Content string `form:"content" valid:"Min(5)"`  
}
```

#### 重写错误信息

```go
var MsgTpl = map[string]string{  
    "Required": "不能为空",  
}  
validation.SetDefaultMessage(MsgTpl)  
  
//初始化validator  
valid := validation.Validation{}
```