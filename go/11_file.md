## file

### read && write
```go
package main

import (
	"fmt"
	"io"
	"os"
)

func WriteFile(path string) {
	// open
	f, err := os.Create(path)
	if err != nil {
		fmt.Println("err=", err)
		return
	}
	// close
	defer f.Close()

	var buf string
	for i := 0; i < 10; i++ {
		buf = fmt.Sprintf("i=%d\n", i)
		_, err := f.WriteString(buf)
		if err != nil {
			fmt.Println("err=", err)
		}
	}
}

func ReadFile(path string) {
	// open
	f, err := os.Open(path)
	if err != nil {
		fmt.Println("err=", err)
		return
	}
	//close
	defer f.Close()

	buf := make([]byte, 1024*2)
	readLength, err1 := f.Read(buf)
	if err1 != nil && err1 != io.EOF {
		fmt.Println("err1=", err1)
		return
	}
	fmt.Println("buf=", buf[:readLength])
}
func main() {
	path := "./demo.txt"
	//WriteFile(path)
	ReadFile(path)
}
```