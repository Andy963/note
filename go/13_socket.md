## tcp

### server
```go
package main

import (
	"fmt"
	"net"
)

func main() {
	listener, err := net.Listen("tcp", "127.0.0.1:8000")
	if err != nil {
		fmt.Println("err= ", err)
		return
	}
	defer listener.Close()

	// block, to wait  for connect
	conn, err1 := listener.Accept()
	if err1 != nil {
		fmt.Println("err1= ", err1)
		return
	}

	// receive request
	buf := make([]byte, 1024)
	n, err2 := conn.Read(buf)
	if err2 != nil {
		fmt.Println("err2= ", err2)
		return
	}
	fmt.Println("buf= ", string(buf[:n]))

	defer conn.Close() // close connection
	fmt.Printf("")
}
```

### client
```go
package main

import (
	"fmt"
	"net"
)

func main() {
	conn, err := net.Dial("tcp", "127.0.0.1:8000")
	if err != nil {
		fmt.Println(err)
		return
	}
	defer conn.Close()

	// send msg
	conn.Write([]byte("Are u ok?"))
}
```