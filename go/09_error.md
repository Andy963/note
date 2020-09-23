
## error
### error interface
```go
package main

import "fmt"

func main(){
    var err1  error = fmt.Errorf("%s","this is an error.")
    fmt.Println("err1",err1)
    err2 := fmt.Errorf("%s","this is a normal err2")
    fmt.Println("err2",err2)
}
// or use built in error interface
package main

import (
	"errors"
	"fmt"
)

func main() {
	error1 := errors.New("this is normal error.")
	fmt.Println("error1", error1)
}
```

### use errors module
```go
package main

import (
	"errors"
	"fmt"
)

func myDiv(a, b int) (result int, err error) {
	err = nil
	if b == 0 {
		err = errors.New("b can not be zero")
	} else {
		result = a / b
	}
	return
}

func main() {
	result, err := myDiv(10, 0)
	if err != nil {
		fmt.Println("err=", err)
	} else {
		fmt.Println("result=", result)
	}
}
```
## panic
### panic
```go
package main

import "fmt"

func test1() {
	fmt.Println("test1")
}
func test2() {
	panic("panic test, program will stop here.")
	fmt.Println("test2")
}
func test3() {
	fmt.Println("test3")
}

func main() {
	test1()
	test2()
	test3()
}
test1
panic: panic test, program will stop here.

goroutine 1 [running]:
main.test2(...)
        /home/andy/GoProjects/learn/09_error/03_panic.go:9
main.main()
        /home/andy/GoProjects/learn/09_error/03_panic.go:18 +0x96
exit status 2
```