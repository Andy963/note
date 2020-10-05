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
## channel
### use
```go
package main

import (
    "fmt"
    "time"
)

func main(){
    ch := make(chan  string)
    defer fmt.Println("主协程结束")

    go func(){
        defer fmt.Println("子协程调用完毕")

        for i :=0; i<2;i++{
            fmt.Println("子协程i=",i)
            time.Sleep(time.Second)
        }
        ch <- "I am sub routine.I have job to do "
    }()
    // <-ch  means get mes from channel. <-ch "hello"  add msg to channel.
    str := <-ch // if ch is empty, it will blocked
    fmt.Println("str = ", str)
}
```
### no cache channel
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	ch := make(chan int, 0) // set capacity to 0  means no cache

	fmt.Printf("len(ch)= %d, cap(ch) =%d\n", len(ch), cap(ch))

	go func() {
		for i := 0; i < 3; i++ {
			ch <- i
			fmt.Printf("sub routine: i=%d\n", i)
		}
	}()

	time.Sleep(2 * time.Second)
	for i := 0; i < 3; i++ {
		num := <-ch
		fmt.Println("num = ", num)
	}
	fmt.Printf("")
}
```

### cached goroutine
```go
package main

import (
    "fmt"
    "time"
)

func main(){

    ch := make(chan int, 3) // set capacity to 0  means no cache

    fmt.Printf("len(ch)= %d, cap(ch) =%d\n", len(ch), cap(ch))

    go func() {
        for i := 0; i < 3; i++ {
            ch <- i
            fmt.Printf("sub go routine. index[%d], len(ch)= %d, cap(ch) =%d\n",i, len(ch), cap(ch))
        }
    }()

    time.Sleep(2 * time.Second)
    for i := 0; i < 3; i++ {
        num := <-ch
        fmt.Println("num = ", num)
    }
}
//len(ch)= 0, cap(ch) =3
//sub go routine. index[0], len(ch)= 1, cap(ch) =3
//sub go routine. index[1], len(ch)= 2, cap(ch) =3
//sub go routine. index[2], len(ch)= 3, cap(ch) =3
//num =  0
//num =  1
//num =  2
// if you send 10 item to channel, it will block, bc it's full.
```

### close channel
```go
package main

import "fmt"

func main() {
	ch := make(chan int)

	go func() {
		for i := 0; i < 5; i++ {
			ch <- i
		}
		close(ch)
	}()

	for {
		if num, ok := <-ch; ok == true {
			fmt.Println("num =", num)
		} else {
			break
		}
	}
}

//if no data to send. you can close channel, otherwise no need.
// after close, you can not send data to channel
// but you can receive data after close if it have
// if nil channel no matter send or receive will blocked.
```

### range 
```go
package main

import "fmt"

func main() {
	ch := make(chan int)
	go func() {
		for i := 0; i < 5; i++ {
			ch <- i
		}
		close(ch)
	}()
	for num := range ch {
		fmt.Println("num=", num)
	}
}
```

### single direction channel
```go
package main

func main() {
	ch := make(chan int)
	// double direction channel can transfer to single direction channel implicitly
	var writeCh chan<- int = ch // only write, no read
	var readCh <-chan int = ch  // only read, no write

	writeCh <- 666
	<-readCh
}
```
or in, out
```go
package main

import "fmt"

func producer(out chan<- int) {
	for i := 0; i < 10; i++ {
		out <- i * i
	}
	close(out)
}
func consumer(in <-chan int) {
	for num := range in {
		fmt.Println("num = ", num)
	}
}
func main() {

	ch := make(chan int)
	go producer(ch)

	consumer(ch)
}

```

## timer && ticker
### timer
```go
package main

import (
    "fmt"
    "time"
)

func main2()  {
   <-time.After(2*time.Second)
   fmt.Println("on time.")
}

func main1()  {
    time.Sleep(2*time.Second)
    fmt.Println("on time.")
}
func main(){
    timer := time.NewTimer(2*time.Second)
    <- timer.C
    fmt.Println("on time.")
}
```

### stop and reset timer
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	timer := time.NewTimer(3 * time.Second)

	go func() {
		<-timer.C
		fmt.Println("go routine can print.")
	}()
	timer.Stop() // stop timer
	timer.Reset(time.Second) // reset to 1 sec.
}

```

### ticker
```go
package main

import (
	"fmt"
	"time"
)

func main() {

	ticker := time.NewTicker(time.Second)
	i := 0
	for {
		<-ticker.C
		i++
		fmt.Println("i= ", i)
		if i == 5 {
			ticker.Stop()
			break
		}
	}
}
```