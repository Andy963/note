## routine
### goroutine
```go
package main

import (
	"fmt"
	"time"
)

func Task() {
	for {
		fmt.Println("this is new task")
		time.Sleep(time.Second)
	}
}
func main() {

	go Task() // 新建一个协程
	for {
		fmt.Println("this is main task")
		time.Sleep(time.Second)
	}
}
```