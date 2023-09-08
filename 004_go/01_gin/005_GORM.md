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
迁移schema  

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

那么根据蛇形为列名 [[005_GORM#^3cbbb6]]  生成的表名应该是author_name, author_email, up_voates,实际情况是：

![表情况](https://github.com/Andy963/note/blob/dev/004_go/99_statics/blog.jpg?raw=true)

将 embeddedPrefix去掉后的结果是：

![无embedding](https://github.com/Andy963/note/blob/dev/004_go/99_statics/no_embedding.jpg?raw=true)

从上面两种情况看，嵌套后只有指定了prefix才会加被嵌套结构体前缀，否则是没有的，像upvotes这种单词也不会拆分成蛇形。

#### 字段标签 
TODO

### 关联关系
TODO

### CRUD

#### Create

```go
user := User{Name: "Jinzhu", Age: 18, Birthday: time.Now()}  
  
result := db.Create(&user) // 通过数据的指针来创建  
  
user.ID             // 返回插入数据的主键  
result.Error        // 返回 error  
result.RowsAffected // 返回插入记录的条数

users := []*User{
		&User{Name: "zhou", Age: 18, Addr: "beijing"},
		&User{Name: "gao", Age: 18, Addr: "beijing"},
	}
db.Create(users)
```

复用已经存在的字段

```go
user := User{Name: "zhou", Age: 18, Addr: "beijing"}  
// db.Create(&user)
db.Select("Name", "Age", "Addr").Create(&user)
```

这两种情况下可以对同一组值添加多次

#### Retrieve

```go
rs := db.First(&user)   // 按主键排序
fmt.Println(rs.Error, rs.RowsAffected, user)
// <nil> 1 {3 zhou 18 }

rs := db.Take(&user)   // take不指定排序 
fmt.Println(rs.Error, rs.RowsAffected, user)
//<nil> 1 {3 zhou 18 }

rs := db.Last(&user)  
fmt.Println(rs.Error, rs.RowsAffected, user)
// <nil> 1 {8 zhou 22 beijing}
```

##### primary key

```go
rs := db.First(&user, 3)  
// rs := db.First(&user, "3") works well  
fmt.Println(rs.Error, rs.RowsAffected, user)


var users []User
rs := db.Find(&users, []int{5, 4, 3})  
fmt.Println(rs.Error, rs.RowsAffected, users)
// <nil> 3 [{3 zhou 18 } {4 zhou 19 beijing} {5 zhou 20 beijing}]
// 如果指定id 1,2,3,但只查到了id为3的，则只返回3的，not raise error
```

if primary key is a string:

```go
rs := db.Find(&users, "name = ?", "zhou")
rs := db.Find(&users, "id= ?", "1")
```

and this will get all the objects, like .all() in django

```go
rs := db.Find(&users)
```

#### conditions

##### String condition

```go
// get the first one who's age > 18
rs := db.Where("age > ?", 18).First(&users)
// get all the people age older than 18
rs := db.Where("age > ?", 18).Find(&users)  

// get name in zhou, gao
rs := db.Where("name IN ?", []string{"zhou", "gao"}).Find(&users)
// Like
rs := db.Where("name LIKE ?", "%z%").Find(&users)

// AND    use "19" will have same effect
rs := db.Where("name LIKE ? AND age > ?", "%z%", 19).Find(&users)

// Time
today := time.Now().Format("2006-01-02")  
rs := db.Where("updated_at < ?", today).Find(&users)

// between
rs := db.Where("age BETWEEN ? AND ?", 18, 20).Find(&users)
```

##### struct, map condition 

```go
// struct
rs := db.Where(&User{Name: "zhou", Age: 19}).Find(&users)

// map, same effect with above
rs := db.Where(map[string]interface{}{"name": "zhou", "age": 19}).Find(&users)

// slice of primary keys, this means get the id is 3, 4 user
rs := db.Where([]int64{3, 4}).Find(&users)
```

if a field is 0, false, '', it will be ignored.

```go
rs := db.Where(&User{Name: "zhou", Age: 0}).Find(&users)
// <nil> 4 [{4 zhou 19 beijing} {5 zhou 20 beijing} {7 zhou 21 beijing} {8 zhou 22 beijing}]

rs := db.Where(map[string]interface{}{"Name": "zhou", "Age": 0}).Find(&users)
// <nil> 0 []

```

you can see the first query, the Age 0, not work at all.

##### inline condition

conditions can be inlined into methods like First, Find

```go
//rs := db.First(&users, "id = ?", "string_primary_key")   // this get nothing
rs := db.Find(&users, "name = ?", "gao")
```

 didn't see any difference between this from the query above

```go
rs := db.Find(&users, "name <> ? AND age > ?", "gao", 20)
// <nil> 2 [{7 zhou 21 beijing} {8 zhou 22 beijing}]
rs := db.Find(&users, User{Age: 20})
// <nil> 1 [{5 zhou 20 beijing}]
rs := db.Find(&users, map[string]interface{}{"age": 20})
// <nil> 1 [{5 zhou 20 beijing}]
```

##### Not condition

```go
rs := db.Not("name = ?", "zhou").Find(&users)

rs := db.Not(map[string]interface{}{"name": []string{"zhou", "gao"}}).Find(&users)

rs := db.Not(User{Name: "zhou", Age: 19}).First(&users)

rs := db.Not([]int64{1, 2, 5}).Find(&users)
```

##### or condition 

```go
rs := db.Where("age = ?", "18").Or("age = ?", 19).Find(&users)
// <nil> 2 [{3 gao 18 } {4 zhou 19 beijing}]
rs := db.Where("name = 'gao'").Or(map[string]interface{}{"name": "zhou", "age": 19}).Find(&users)

```

##### specified field

```go
rs := db.Select("name", "age").Find(&users)
// <nil> 5 [{0 gao 18 } {0 zhou 19 } {0 zhou 20 } {0 zhou 21 } {0 zhou 22 }]
rs := db.Select([]string{"name", "age"}).Find(&users)
// <nil> 5 [{0 gao 18 } {0 zhou 19 } {0 zhou 20 } {0 zhou 21 } {0 zhou 22 }]

the above condition not specified id field, so it's 0 in the result
rs, r := db.Table("users").Select("COALESCE(age,?)", 4).Rows()
```

##### order

```go
rs := db.Order("age desc, name").Find(&users)
// <nil> [{8 zhou 22 beijing} {7 zhou 21 beijing} {5 zhou 20 beijing} {4 zhou 19 beijing} {3 gao 18 }]

// the first order has a higher priority
db.Order("age desc").Order("name").Find(&users)
```

##### Limit & Offset 

```go
rs := db.Limit(3).Find(&users)

rs := db.Limit(2).Find(&users).Limit(-1).Find(&users2)

// SELECT * FROM users LIMIT 2; (users1)  
// SELECT * FROM users; (users2)

// this will not work in mysql/maridb
db.Offset(3).Find(&users)

rs := db.Limit(10).Offset(1).Find(&users)
rs := db.Offset(2).Find(&users).Offset(-1).Find(&users)
```

##### Group & Having 



##### Distinct

##### Join

##### Scan 