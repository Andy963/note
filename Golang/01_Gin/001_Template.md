
### static, template

```go
router.LoadHTMLGlob("templates/**/*")  
router.Static("/static", "static")
```

当template目录下分了子文件夹时，则上面路由要添加一层 `**`  
对应的html文件中要添加define:

```go
{{ define "index.html" }}  
	<!DOCTYPE html>  
	<html lang="en">  
	<head>  
	    <meta charset="UTF-8">  
	    <title>Hello</title>  
	</head>  
	<body>  
	<h3> hello gin</h3>  
	</body>  
	</html>  
  
{{ end }}
```

#TODO /static 只代表路由

### render 

```go
func User(c *gin.Context) {  
    name := "andy"  
    c.HTML(http.StatusOK, "user/user.html", name)  
  
}  
  
type UserInfo struct {  
    Id   int  
    Name string  
    Age  int  
}

func UserInfoStruct(c *gin.Context) {  
    userInfo := UserInfo{  
       Id:   1,  
       Name: "andy",  
       Age:  18,  
    }  
    c.HTML(http.StatusOK, "chapter2/user_info.html", userInfo)  
}  
  
func ArrayView(c *gin.Context) {  
    arr := []int{1, 2, 3, 4, 5}  
    c.HTML(http.StatusOK, "chapter2/arr.html", arr)  
}  
  
func ArrayStructView(c *gin.Context) {  
    arrayStruct := [3]UserInfo{  
       {  
          Id:   1,  
          Name: "andy",  
          Age:  18,  
       },  
       {  
          Id:   2,  
          Name: "andy2",  
          Age:  19,  
       },  
       {  
          Id:   3,  
          Name: "andy3",  
          Age:  20,  
       },  
    }  
    c.HTML(http.StatusOK, "chapter2/array_struct.html", arrayStruct)  
  
}  
  
func MapView(c *gin.Context) {  
    m := map[string]string{  
       "name": "andy",  
       "age":  "18",  
    }  
    m2 := map[string]string{  
       "gender": "male",  
       "height": "180",  
    }  
    obj := map[string]interface{}{"m": m, "m2": m2}  
    c.HTML(http.StatusOK, "chapter2/map.html", obj)  
}  
  
func MapStructView(c *gin.Context) {  
    mapStruct := map[string]UserInfo{"user1": {1, "andy", 18}, "user2": {2, "andy2", 19}}  
  
    c.HTML(http.StatusOK, "chapter2/map_struct.html", mapStruct)  
}

func SliceView(c *gin.Context) {  
    s := []int{1, 2, 3, 4, 5}  
  
    c.HTML(http.StatusOK, "chapter2/slice.html", s)  
}
```

对应html:

```html
{{ define "chapter2/user_info.html" }}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>UserInfo</title>  
</head>  
<body>  
This is user info page.  
<br>  
User name: {{.Name}} <br>  
User Id : {{.Id}} <br>  
User Age: {{.Age}} <br>  
</body>  
</html>  
{{end}}
```

#### Array

```html
{{ define "chapter2/arr.html" }}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Array</title>  
</head>  
<body>  
<!--第一种显示方式-->  
{{range .}}  
{{.}}<br>  
{{end}}  
  
<!--第二种显示方式-->  
{{range $i, $v := .}}  
{{$i}}:{{$v}}<br>  
{{end}}  
</body>  
</html>  
  
{{end}}
```

#### Array struct

```html
{{ define "chapter2/array_struct.html" }}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Array struct</title>  
</head>  
<body>  
{{range .}}  
{{.Id}}  
{{.Name}}  
{{.Age}}  
<br>  
{{end}}  
  
<br>  
<!--第二种显示方式-->  
<!--可以不写$i,对应的是里面的值，不会附带下标-->  
{{ range $i, $v := . }}  
{{$i}}:{{$v.Id}}:{{$v.Name}}:{{$v.Age}}<br>  
{{ end }}  
</body>  
</html>  
  
{{end}}
```

#### Map

```html
{{ define "chapter2/map.html" }}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Map</title>  
</head>  
<body>  
This is map page  
<br>  
{{.m.name}}  
<br>  
{{.m2.gender}}  
  
</body>  
</html>  
  
{{end }}
```

#### Map Struct

```html
{{ define "chapter2/map_struct.html" }}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Map struct</title>  
</head>  
<body>  
this is map struct page  
<br>  
{{.user1.Name}}  
{{.user1.Age}}  
</body>  
</html>  
  
{{ end}}
```

#### Slice 

```html
{{ define "chapter2/slice.html" }}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Slice</title>  
</head>  
<body>  
This is slice page  
<br>  
{{ range . }}  
{{.}}  
{{ end}}  
  
<br>  
second way to show  
  
{{ range $v := . }}  
{{$v}}<br>  
{{ end }}  
</body>  
</html>  
  
{{ end }}
```

### get param from url

#### method 1 get by ":"
route

```go
router.GET("/param/:id", chapter2.ParamView)
```

view

```go
func ParamView(c *gin.Context) {  
    id := c.Param("id")  
    c.String(http.StatusOK, "id:%s", id)  
}
```

#### method 2 get by "*"

route

```go
router.GET("/param/*id", chapter2.ParamView)
```

view

```go
func ParamView(c *gin.Context) {  
    id := c.Param("id")  
    c.String(http.StatusOK, "id:%s", id)  
}

// result  /123 带 /
```

method 3 get by query

route
```go
router.GET("/query", chapter2.GetQueryDataView)
```

view

```go
func GetQueryDataView(c *gin.Context) {  
    id := c.Query("id")  
    c.String(http.StatusOK, "id:%s", id)  
}
```

DefaultDquery 比Query多个参数，如果没获取到则使用默认值

### query array

route

```go
router.GET("/queryArray", chapter2.GetQueryArrayDataView)
```

view

```go
func GetQueryArrayDataView(c *gin.Context) {  
    ids := c.QueryArray("ids")  
    c.String(http.StatusOK, "id:%s", ids)  
}
```

result:

```html
http://localhost:8080/queryArray?ids=23,34,56

ids: [23,34,56]
```

### query map

route

```go
router.GET("/queryMap", chapter2.GetQueryMapDataView)
```

view

```go
func GetQueryMapDataView(c *gin.Context) {  
    m := c.QueryMap("user")  
    c.String(http.StatusOK, "id:%s", m)  
}
```

result

```
http://localhost:8080/queryMap?user[name]=andy&user[age]=18

id:map[age:18 name:andy]
```

### post Form

route

```go
router.GET("/postUser", chapter2.PostUserData)  
router.POST("/afterpostUser", chapter2.AfterPostUserData)
```

view

```go
func PostUserData(c *gin.Context) {  
    c.HTML(http.StatusOK, "chapter2/addUser.html", nil)  
}  
  
func AfterPostUserData(c *gin.Context) {  
    name := c.PostForm("name")  
    age := c.PostForm("age")  
    c.String(http.StatusOK, "name:%s,age:%s", name, age)  
}

// 设置默认值使用 c.DefaultPostForm
```

如果是Ajax请求，后端 返回时使用 `c.JSON()`

array, map 对应的使用 `c.PostFormArray, c.PostFormMap`
html

```html
{{ define "chapter2/addUser.html" }}  
<!DOCTYPE html>  
<html lang="en">  
<head>  
    <meta charset="UTF-8">  
    <title>Add User</title>  
</head>  
<body>  
添加用户  
<form action="/afterpostUser" method="POST">  
    <label for="name">Name</label>  
    <input name="name" type="text" id="name">  
    <br>    <label for="age">Age</label>  
    <input name="age" type="text" id="age">  
    <br>    <input type="submit" value="提交">  
</form>  
</body>  
</html>  
{{ end }}
```

list

```html
<form action="/hello add" method="post">
<input type="text"name="username"><br>
<input type="text"name="age"><br>
ck1:<input type="checkbox" name="ck" value="1">
ck2:<input type="checkbox" name="ck" value="2">
ck3:<input type="checkbox" name="ck" value="3">
<input type="submit" value="提交"></form>
```

map

```html
<form action="/hello_add" method="post">
<input type="text" name="username[1]"><br>
<input type="text" name="username[2]"><br>
<input type="submit” value="提交">
</form>
```

### bindForm

view
```go
type UserInfo struct {  
    Id   int    `form:"id" json:"id"`  
    Name string `form:"name" json:"name"`  
    Age  int    `form:"age" json:"age"`  
}

func bindForm(c *gin.Context) {  
    var user UserInfo  
    if err := c.ShouldBind(&user); err != nil {  
       c.String(http.StatusBadRequest, "请求参数错误：%s", err.Error())  
       return  
    }  
    c.String(http.StatusOK, "name:%s,age:%d", user.Name, user.Age)  
}
```

### upload file

view

```go
	router.GET("/getupload", chapter2.GetUploadView)
	router.POST("/postupload", chapter2.PostUploadView)

func GetUploadView(c *gin.Context) {
	c.HTML(200, "chapter2/upload.html", gin.H{
		"title": "upload",
	})
}

func PostUploadView(c *gin.Context) {
	file, _ := c.FormFile("file")
	dst := "upload/" + file.Filename
	c.SaveUploadedFile(file, dst)
	c.String(200, "%s uploaded!", file.Filename)
}

// multifile
func PostMultiFileView(c *gin.Context) {
	form, _ := c.MultipartForm()
	files := form.File["file"]
	for file := range files {
		dst := "upload/" + files[file].Filename
		c.SaveUploadedFile(files[file], dst)
	}
}

```

### upload via ajax

如果使用ajax 要注意：
processData:false 默认为true,当设置为true的时候,jquery ajax 提交的时候不会序列化 data,而是直接使用data
contentType: false ，不使用默认的application/x-www-form-urlencoded这种contentType
● 分界符:目的是防止上传文件中出现分界符导致服务器无法正确识别文件起始位置
● ajax 中 contentType 设置为 false 是为了避免 JQuery 对其操作,从而失去分界符

### redirect

view

```go
func RedirectView(c *gin.Context){

    // http.StatusFounc 302
    // http.StatusMovedPermanently 301
    c.Redirect(http.StatusMovedPermanently, "http://www.baidu.com")
}
```


### http config

```go
	router.Run()
	// http.ListenAndServe(":8080", router)
	// s := &http.Server{
	// 	Addr:    ":8080",
	// 	Handler: router,
	// 	ReadTimeout: 10 * time.Second,
	// 	WriteTimeout: 10 * time.Second,}
	// 	s.ListenAndServe()
```


### context

```html

. 访问当前位置的上下文
$ 引用当前模板根级的上下文
$. 引用模板中的根级上下文

{{define "chapter3/test.html"}}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>模板语法</title>
</head>
<body>
    这是模板语法页面
{{.name}}
{{range .arr}}
{{.}}
/*  此时如果要用name 则应该使用$.{name} */
{{$.name}}
{{end}}
</body>
</html>

{{end}}

{{ "andy"}} 字符串
{{'a'}}  显示字母的ascii码对应的数字
{{`a`}}  显示字母a,不会转义

{{print "andy"}}

```

#### 定义变量

```html
定义变量
{{$name := "andy"}}
使用：
{{$name}}
```

### pipeline

```html
{{.name}} 是上下文的变量输出 
{{“hallen"|len}} 函数通过管理传递返回值，是pipeline
```

#### if

if 可以进行嵌套

```
{{ if .name}}
   欢迎 {{.name}}
{{else}}
	欢迎 游客
{{end}}
```

#### range

```
第一种
{{range $v := .arr_struct }}
	{{$v.name}}
	 {{$v.age}}
{{end}}

{{ range $v  := .arr}}
	{{ /*{{$v}}*/}}
	 {{.}}
{{end}}

第二种
{{ range .arr_struct }}
	{{ .name }}
	 {{ .age}}
  {{ $.total}}  // 使用"$." 引用模板中的根级上下文
{{end}}
```

range 中也可以像if一样写else

#### with

```
{{with .user}}  // 本来是.article.user,通过with可以不用每次都输入article 
		{{.id}} // 如果没有.user 可以通过else殒，让它显示别的
	{{.name}} 
{{end}}
```


#### template

引入另一个网页，类似django中的 include

```
{{ template "chapter/base.html"}}
// 如果base 页面想共享扩展它的页面的上下文，则在后面加上点
{{ template "chapter/base.html" . }}
```

#### 注释

```
{{ /* 这是注释*/}}
```

### 模板函数

print  对应fmt.Sprint  不会打印，但可以格式化返回结果
printf 对应fmt.Sprintf
println 对应fmt.Sprintln

#### 括号

{{ printf "nums is %s %d " (prinf "%d %d" 1 2) 3 }}

#### and
作用： 只要有一个为空，则整体为空，如果都不为空，则返回最后一个

#### or 
只要有一个为空，就返回第一个不为空的，否则返回空


#### index

```go
package chapter3

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

func TplFunc(c *gin.Context) {

	slice_data := []string{"张三", "李四", "王五"}
	data := map[string]interface{}{
		"Name": "张三",
		"Age":  18,
	}
	map_data := map[string]interface{}{
		"Name":       "张三",
		"Age":        18,
		"slice_data": slice_data,
		"map_":       data,
	}

	c.HTML(http.StatusOK, "chapter3/func.html", map_data)

}


{{ define "chapter3/func.html"}}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>模板函数</title>
</head>
<body>
{{/* 后端传的变量为slice_data,
slice_data := []string{"张三", "李四", "王五"}
index 变量名 索引 */}}

{{/* 对于map index 后面可以使用map 的key进行索引  */}}
slice for map : {{index .map_ "Name"}}<br>
</body>
</html>


{{ end }}
```

#### len 

```go
{{ "andy" | len}}

{{ len "andy"}}
```

#### not
not 取反

#### urlquery

有些符号在url中是不能直接传递的，如果要传递这些包含特殊字符的url,就要使用urlquery

```go
{{ urlquery "http://www.baidu.com"}}
结果： http%3A%2F%2Fwww.baidu.com
```

#### js

对js字符串进行编码

```go
{{js "<script> alert(1) </script"}}
```
### 自定义template func

定义函数

```go
//1 定义函数  
func Add(a, b int) int {  
    return a + b  
}
```

注册函数

```go
router := gin.Default()  
// 注册要在router.LoadHTMLGlob之前  
router.SetFuncMap(template.FuncMap{  
    "add": chapter3.Add,  
})
```

使用

```html
<br>  
{{   len "andy" }}  
<br>  
{{ add 1 0}}
```