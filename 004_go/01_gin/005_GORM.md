### 连接数据库

#### connect

```go
package main  
  
import (  
    "gorm.io/driver/mysql"  
    "gorm.io/gorm")  
  
func main() {  
    dsn := "root:root@tcp(192.168.208.1:3306)/gorm_project?charset=utf8&parseTime=True&loc=Local"  
    db, err := gorm.Open(mysql.Open(dsn), &gorm.Config{})  
    if err != nil {  
       panic(err)  
    }  
    // Get the underlying *sql.DB connection and close it  
    sqlDB, err := db.DB()  
    if err != nil {  
       panic(err)  
    }  
    sqlDB.Close()  
}
```

#### CreateTable 

```go
db.AutoMigrate(&User{})
```

#### started

```go
// 迁移schema  
db.AutoMigrate(&User{})  
//Create  
db.Create(&User{Name: "zhou", Age: 20, Addr: "WuHan", Pic: "http://www.zhougao.win"})  
// Read
var user User  
rs := db.First(&user, 1)  // 获取到的结果已经存在user中了
fmt.Println(user)   // {1 zhou 20 WuHan http://www.zhougao.win}, 也可以通过user.Name
// 下面这些没什么作用
if rs.Error != nil {  
    panic(rs.Error)  
} else {  
    fmt.Println(rs.RowsAffected, rs)  
}
// 通过条件过滤
db.First(&user, "name = ?", "zhou")


// update  
db.Model(&user).Update("age", 18)  
db.First(&user, "name = ?", "zhou")  
fmt.Println(user)  
// 更新多个字段  
db.Model(&user).Updates(User{Age: 18, Name: "zhou gao"})  
db.First(&user, "age = ?", 18)  
fmt.Println(user)  
db.Model(&user).Updates(map[string]interface{}{"age": 20, "name": "zhou"})  
db.First(&user, "age = ?", 20)  
fmt.Println(user)

// delete
db.delete(&user, 1)
```

### 字段

*约定*
GORM 倾向于约定优于配置 默认情况下，GORM 使用 `ID` 作为主键，使用结构体名的 `蛇形复数` 作为表名，字段名的 `蛇形` 作为列名，并使用 `CreatedAt`、`UpdatedAt` 字段追踪创建、更新时间 ^3cbbb6

一个model 在gorm中是一个结构体：

```go
type Model struct {  
  ID        uint           `gorm:"primaryKey"`  
  CreatedAt time.Time  
  UpdatedAt time.Time  
  DeletedAt gorm.DeletedAt `gorm:"index"`  
}
```

通过约定，可以少写一些字段,其中 `gorm.Model` 将 `ID, CreatedAt, UpdatedAt, DeleteAt` 默认加入表中 ^296606

```go
type User struct {
  gorm.Model
  Name string
}
// 等效于
type User struct {
  ID        uint           `gorm:"primaryKey"`
  CreatedAt time.Time
  UpdatedAt time.Time
  DeletedAt gorm.DeletedAt `gorm:"index"`
  Name string
}
```

显式嵌入另一个结构体：

```go
type Author struct {
    Name  string
    Email string
}

type Blog struct {
  ID      int
  Author  Author `gorm:"embedded"`
  Upvotes int32
}
// 等效于
type Blog struct {
  ID    int64
  Name  string
  Email string
  Upvotes  int32
}
```

为嵌入的结构体添加前缀

```go
type Blog struct {
  ID      int
  Author  Author `gorm:"embedded;embeddedPrefix:author_"`
  Upvotes int32
}
// 等效于
type Blog struct {
  ID          int64
  AuthorName string
  AuthorEmail string
  Upvotes     int32
}
```

那么根据蛇形为列名 [[005_GORM#^3cbbb6]]  生成的表名应该是author_name, author_email, up_voates, 