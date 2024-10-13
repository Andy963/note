

## regexp
go regexp is similar to python.
### regexp.MustCompile
```go
package main

import (
	"fmt"
	"regexp"
)

func main() {
	buf := "abc azc a7c aaa acc tac"
	pattern := regexp.MustCompile(`a.c`)
	if pattern == nil {
		fmt.Println("pattern err")
		return
	}

	result := pattern.FindAllStringSubmatch(buf, -1)
	fmt.Println("result= ", result)
	// result=  [[abc] [azc] [a7c] [acc]] 返回的是二维数组
}
```

## json

### struct2Json marshal marshalIndent
```go
package main

import (
	"encoding/json"
	"fmt"
)

// 成员变量名首字母必须大写,小写字母开头的将会被忽略
type info struct {
	Company string
	Subject []string
	Status  bool
	Price   float64
}

func main() {
	s := info{"gian", []string{"python", "go", "js"}, true, 666}
	//j_s, err := json.Marshal(s)
	j_s, err := json.MarshalIndent(s, "", " ")
	if err != nil {
		fmt.Println("err=", err)
		return
	}

	fmt.Println("j_s=", string(j_s))
}
```
### struct2json format
```go
package main

import (
    "encoding/json"
    "fmt"
)

// 成员变量名首字母必须大写,小写字母开头的将会被忽略
// 如果要输出时的字段是小写，则 `json: "new name"`
type info struct {
    Company string `json:"company"`
    Subject []string `json:"-"` // 此字段不会输出
    Status  bool `json:",string"` // 此字段不会显示true,而是字符串"true"
    Price   float64 `json:",string"`
}

func main() {
    s := info{"gian", []string{"python", "go", "js"}, true, 666}
    //j_s, err := json.Marshal(s)
    j_s, err := json.MarshalIndent(s, "", " ")
    if err != nil {
        fmt.Println("err=", err)
        return
    }

    fmt.Println("j_s=", string(j_s))
}
```
### map2json
```go
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	m := make(map[string]interface{}, 4)
	m["company"] = "giant"
	m["subjects"] = []string{"python", "go", "js"}
	m["status"] = true
	m["price"] = 666.6
	result, err := json.MarshalIndent(m, "", " ")
	if err != nil {
		fmt.Println("err:", err)
		return
	}
	fmt.Println("result = ",string(result))
}
```
### json2struct 
```go
package main

import (
	"encoding/json"
	"fmt"
)

type info struct {
	Company string
	Subject []string
	Status  bool
	Price   float64
}

func main() {
	j_s := `
 {
 "Company": "gian",
 "Subject": [
  "python",
  "go",
  "js"
 ],
 "Status": true,
 "Price": 666
}

`
	var tmp info
	err := json.Unmarshal([]byte(j_s), &tmp)
	if err != nil {
		fmt.Println("err=", err)
		return
	}
	fmt.Printf("tmp= %+v\n", tmp)

	// if you only need some filed of it.
	type info2 struct {
		Company string `json:"company"`
	}
	var tmp2 info2
	err = json.Unmarshal([]byte(j_s), &tmp2)
	if err != nil {
		fmt.Println("err = ", err)
		return
	}
	fmt.Printf("tmp2 = %+v\n", tmp2)
}
```
### json2map
json to map can only use type assert
```go
package main

import (
	"encoding/json"
	"fmt"
)

func main() {
	j_s := `
 {
 "Company": "gian",
 "Subject": [
  "python",
  "go",
  "js"
 ],
 "Status": true,
 "Price": 666
}
`
	m := make(map[string]interface{}, 4)
	err := json.Unmarshal([]byte(j_s), &m)
	if err != nil {
		fmt.Println("err=", err)
		return
	}
	fmt.Printf("m = %+v\n", m)
	// var str string
	// str = string(m["company"]) 无法强制转换
	for key, value := range m {
		switch data := value.(type) {
		case string:
			fmt.Printf("map[%s]=%s\n", key, data)
		case bool:
			fmt.Printf("map[%s]=%v\n", key, data)
		case []interface{}:
			fmt.Printf("map[%s]=%v\n", key, data)
		}
	}
	fmt.Printf("")
}
m = map[Company:gian Price:666 Status:true Subject:[python go js]]
map[Subject]=[python go js]
map[Status]=true
map[Company]=gian
```