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