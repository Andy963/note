### 包导入
```
import "包的路径"
GOPATH/src/a/b/ 下定义一个包 c。在包 c 的源码中只需声明为package c，而不是声明为package a/b/c，但是在导入 c 包时，需要带上路径，例如import "a/b/c"。
```
import 导入语句通常放在源码文件开头包声明语句的下面；
导入的包名需要使用双引号包裹起来；
包名是从GOPATH/src/ 后开始计算的，使用/ 进行路径分隔。

导入路径分为全路径导入和相对路径导入，相对路径只能导入GOPATH下的包，标准包的导入只能使用全路径导入。

### 包引用格式

1.标准引用：

```go
package main
import "fmt"
func main() {
    fmt.Println("C语言中文网")
}

```
此时`fmt.`作为前缀来使用fmt包中的方法

2.自定义别名引用:

```go
package main

import F "fmt"
func main() {
    F.Println("C语言中文网")
}
```
这里引入的别名就是F，类似于python 中的as 

3.省略引用格式:

```go
package main

import . "fmt"
func main() {
    //不需要加前缀 fmt.
    Println("hello world")
}
```

这种格式相当于把fmt包直接合并到当前程序中，在使用fmt包的方法是可以不用加前缀fmt.

4.匿名引用格式

```go
package main

import (
    _ "database/sql"
    "fmt"
)

func main() {
    fmt.Println("hello")
}
```

引用某个包时，如果只是希望执行包初始化的init函数，而不使用包内部的数据时，可以匿名引用

> 使用标准格式引用包，但是代码中却没有使用包，编译器会报错。如果包中有 init 初始化函数，则通过import _ "包的路径" 这种方式引用包，仅执行包的初始化函数，即使包没有 init 初始化函数，也不会引发编译器报错

一个包可以有多个 init 函数，包加载时会执行全部的 init 函数，但并不能保证执行顺序，所以不建议在一个包中放入多个 init 函数，将需要初始化的逻辑放到一个 init 函数里面。
包不能出现环形引用的情况，比如包 a 引用了包 b，包 b 引用了包 c，如果包 c 又引用了包 a，则编译不能通过。
包的重复引用是允许的，比如包 a 引用了包 b 和包 c，包 b 和包 c 都引用了包 d。这种场景相当于重复引用了 d，这种情况是允许的，并且 Go 编译器保证包 d 的 init 函数只会执行一次。