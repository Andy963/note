
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