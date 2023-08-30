
#### 安装

```go
go get github.com/gin-contrib/sessions

```

main.go

```go

store := cookie.NewStore()

router.Use(session.Sessions("ginSession", store))
```

view:

```go
package chapter5  
  
import (  
    "github.com/gin-contrib/sessions"  
    "github.com/gin-gonic/gin")  
  
func SessionView(c *gin.Context) {  
    session := sessions.Default(c)  
    session.Set("name", "zhangsan")  
  
    // 获取session  
    session.Get("name")  
    // 删除session  
    session.Delete("name")  
    // 删除所有session  
    session.Clear()  
  
    // 保存session  
    session.Save()  
  
    c.HTML(200, "session.html", nil)  
}
```