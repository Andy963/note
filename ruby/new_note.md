


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

### 类
```ruby
class Person
  def self.say_hello
    puts 'hello world'
  end
end

#p = Person.new
#p.say_hello
Person.say_hello  类方法
```

**扩充一个类的功能**
将类重新写一次，添加新的功能
```ruby
class Person
  def self.say_hello
    puts 'hello world'
  end
end

class Person
  def walk
    puts 'I can walk'
  end
end

p = Person.new
p.walk
```
#### 模块
module是不能被实例化的，所以下面定义的sqrt方法无法调用，只能添加self
```ruby
module MyMath
  PI = 3.1415

  def sqrt(num)
    Math.sqrt(num)
  end
end

# module 是不能被实例化的

puts MyMath::PI
p MyMath::sqrt(2)  # 报错
```
而要使用module中的实例方法，则可以通过将module**混入类中（mixin）**实现
```ruby
module Skill
  def talk
    p "I can talk"
  end
end

class Student
  include Skill

  def walk
    p "i can walk"
  end
end

s = Student.new
s.talk
s.walk

```

### 自定义符号
**定义函数名为+
```ruby
class Vector
  attr_reader :x, :y

  def initialize(x, y)
    @x = x
    @y = y
  end

  def +(the_vector)
    Vector.new(@x + the_vector.x, @y + the_vector.y)
  end
end

a = Vector.new(1,2)
b = Vector.new(2,3)
p a +b
```