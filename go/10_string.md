## string
### method
```go
package main

import (
	"fmt"
	"strings"
)

func main() {

	//Contains
	fmt.Println(strings.Contains("hellogo", "hello"))
	fmt.Println(strings.Contains("hellogo", "abc"))
	//Join
	s := []string{"hello", "andy", "go"}
	result := strings.Join(s, "--")
	fmt.Println("result=", result)
	//Index
	fmt.Println(strings.Index("hello andy","andy"))
	fmt.Println(strings.Index("hello andy","jack")) // -1
	//Repeat
	rp := strings.Repeat("go",5)
	fmt.Println("rp=",rp)
	//Split
	sp := "hello world hello andy"
	fmt.Println(strings.Split(sp," "))
	//Trim
	tr :="  Are you ok, Andy "
	fmt.Println("tr=",strings.Trim(tr," ")) // remove space on the start and end
	//Fields
	fi :="  Are you ok, Andy"
	fmt.Println("fi=",strings.Fields(fi)) // trim space, split with space
}
```