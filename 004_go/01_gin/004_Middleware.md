### middleware

Next
在我们定义的众多中间件,会形成一条中间件链,而通过 Next 函数来对后面的中间件进行执行
特点:
	1.当遇到c.Next()函数时 它取出所有的没被执行过的注册的函数都执行一遍,然后再回到本函数中,有点类似递归函数
	 2.Next 函数是在请求前执行,而 Next 函数后是在请求后执行。
	 3.可以用在token校验,把用户id存起来共给功能性函数使用

Abort
	1. ctx.Abort()方法的作用 终止调用整个链条
	2. 比如:token认证没有通过,不能直接使用return返回,而是使用Abort来终止

示例：

定义：chapter5/middleware.go

```go
package chapter5  
  
import (  
    "fmt"  
    "github.com/gin-gonic/gin")  

// 方式一
func Middle1(c *gin.Context) {  
    fmt.Println("Middle1 start")  
    c.Next()
    fmt.Println("Middle1 end")  
  
}  
// 方式二返回一个函数
func Middle2() gin.HandlerFunc {  
    return func(c *gin.Context) {  
       fmt.Println("Middle2 start")  
		c.Next()
       fmt.Println("Middle2 end")  
    }  
}
```

main.go
使用时，两种方式不同，返回函数要加括号调用

```go
router.Use(chapter5.Middle1)  
router.Use(chapter5.Middle2())

//如果只想在某个路由组上使用则从路由组使用即可
chapter2.User(middle1)
//局部使用，只针对 某一路由
func Router(rg *gin.RouterGroup) {  
    rg.GET("/bind_form", middle1, BindForm)  
    rg.POST("/post/bind_form", PostBindForm)
}
```

执行顺序：

```
middle1 start
middle2 start
middle2 end
middle1 end
```

注意理解："它取出所有的没被执行过的注册的函数都执行一遍,然后再回到本函数中" 中的本函数。

