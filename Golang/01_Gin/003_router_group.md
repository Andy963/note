### router

main.go

```go
// router参数是gin自带的gin.Default()
MyRouter.Router(router)  
  
router.LoadHTMLGlob("templates/**/*")  
router.Static("/static", "static")
```

router/router.go

```go
package MyRouter  
  
import (  
    "gin_project/controller/chapter1"  
    "gin_project/controller/chapter2"   
     "gin_project/controller/chapter3"    
     "gin_project/controller/chapter4"   
      "github.com/gin-gonic/gin"
      )  
  
func Router(router *gin.Engine) {  
    c1 := router.Group("/chapter1")  
    c2 := router.Group("/chapter2")  
    c3 := router.Group("/chapter3")  
    c4 := router.Group("/chapter4")  
    chapter1.Router(c1)  
    chapter2.Router(c2)  
    chapter3.Router(c3)  
    chapter4.Router(c4)  
}
```

chapter/chapter1/router.go

```go
package chapter1  
  
import "github.com/gin-gonic/gin"  
  
func Router(rg *gin.RouterGroup) {  
    rg.GET("/", GetView)  
    rg.GET("/index", IndexView)  
}
```