


### ruby安装
```sh
apt install ruby-full
```

### 基本数据类型：
数字：
文本：
范围:
符号:
布尔：

### 语句及其异常处理
ruby中gets直接获取从命令行传入的数据：
```ruby
input = gets.to_i
put input
```
chomp 去掉空格

case 语句
```ruby
case object
when condition
```

异常处理
```ruby
a = 100
while true
  b = gets.to_i
  begin
    puts a/b
  rescue Exception => e
    puts '不要输入0'
  end
end
```

类
类变量用双冒号来访问
```ruby
class Student

  def self.name # 类方法
  end
end
```
