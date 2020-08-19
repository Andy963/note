
### 获取输入
```go
func main(){
	var a int // 声明变量
	fmt.Printf("请输入变量a:")
	// 会阻塞，等待用户输入
	fmt.Scanf("%d", &a) 
	// fmt.Scan(&a) 简写模式 
	fmt.Println("a= ",a)
}
```