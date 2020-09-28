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
### main and sub
if main routine exit, the sub routine exit too.
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	go func() {
		i := 0
		for {
			i++
			fmt.Println("sub i=", i)
			time.Sleep(time.Second)
		}
	}()
	i := 0
	for {
		i++
		fmt.Println("main i=", i)
		time.Sleep(time.Second)
		if i == 3 {
			break
		}
	}
	fmt.Printf("")
}
```
### go exit
if Goexit, then routine finish, "routine finish" will never print
```go
package main

import (
	"fmt"
	"runtime"
)

func test() {
	defer fmt.Println("defer")
	runtime.Goexit()
	fmt.Println("test finish")
}

func main() {
	go func() {
		fmt.Println("start")

		test()
		fmt.Println("routine finish.")
	}()
	// forever loop, prevent main exit.
	for {

	}
}
```
### goMaxProcs
GOMAXPROCS set how many core to run this program.
```go
package main

import (
    "fmt"
    "runtime"
)

func main(){
    n := runtime.GOMAXPROCS(4)
    fmt.Println("n =",n)
    for {
        go fmt.Print(1)

        fmt.Print(0)
    }
}
```