


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


### 字符串
**定义字符串**
```ruby
单引号 a ='a'
双引号 b ="a的值是#{a}"
%q()  %q(不会转义）
%Q()  %Q(双引号会自动转义）
#多行：
<<-text
this is mutil line text
text
```
**方法**
```ruby
reverse
include？
index
sub(source,to) # 替换
size
to_sym
```
### 符号

### 数组
```ruby
a=[]
b=Array.new
irb(main):001:0> c =Array.new(3)
=> [nil, nil, nil]
irb(main):002:0> c =Array.new(3,2)
=> [2, 2, 2]

#方法一
#注意，这里每个元素都只是引用而已，是同一份，如果要创建不同的，用下面的第二种方法
irb(main):005:0> d = Array.new(3,'abc')
=> ["abc", "abc", "abc"]
irb(main):006:0> d[0][0]='d'
=> "d"
irb(main):007:0> d
=> ["dbc", "dbc", "dbc"]
# 方法二
irb(main):008:0> e = Array.new(3){'abc'}
=> ["abc", "abc", "abc"]
irb(main):009:0> e[0][0]='e'
=> "e"
irb(main):010:0> e
=> ["ebc", "abc", "abc"]
# 定义字符串Array
%w
irb(main):015:0> arr=%w(a b c) # 注意不要加逗号，否则会只有一个元素
=> ["a", "b", "c"]
```
**方法**
```ruby
irb(main):012:0> arr=%w(a,b,c)
=> ["a,b,c"]
irb(main):013:0> arr[0]
=> "a,b,c"
irb(main):014:0> arr.fetch(0)
=> "a,b,c"
irb(main):015:0> arr=%w(a b c)
=> ["a", "b", "c"]
irb(main):016:0> arr[0]
=> "a"
irb(main):017:0> arr.fetch(0)
=> "a"
irb(main):018:0> arr.fetch(5,'default') # 获取get
=> "default"
irb(main):019:0> arr.include?('c') # 是否包含
=> true
irb(main):020:0> arr.empty? # 是否为空
=> false
irb(main):021:0> arr.push('end') # 追加
=> ["a", "b", "c", "end"]
irb(main):022:0> arr[8]='eight'
=> "eight"
irb(main):023:0> arr
=> ["a", "b", "c", "end", nil, nil, nil, nil, "eight"]
irb(main):024:0> arr.delete_at(5) # 按索引位置删除
=> nil
irb(main):025:0> arr
=> ["a", "b", "c", "end", nil, nil, nil, "eight"]
irb(main):026:0> arr.delete(nil) # 删除某个值，有多个会删除多个
=> nil
irb(main):027:0> arr
=> ["a", "b", "c", "end", "eight"]
irb(main):028:0> arr.push('eight') # 追加
=> ["a", "b", "c", "end", "eight", "eight"]
irb(main):029:0> arr.uniq # 去重
=> ["a", "b", "c", "end", "eight"]
irb(main):030:0> arr.shuffle # 随机
=> ["a", "eight", "end", "b", "c", "eight"]
irb(main):031:0> arr=['a',[1,2],[3,4]]
=> ["a", [1, 2], [3, 4]]
irb(main):032:0> arr.flatten # 打散
=> ["a", 1, 2, 3, 4]

irb(main):033:0> arr.each{|e| p e} # 正序
"a"
[1, 2]
[3, 4]
irb(main):034:0> arr.reverse_each{|e| p e} # 逆序
[3, 4]
[1, 2]
"a"

irb(main):036:0> arr.each_with_index{|e,i| p [i,e]} # 打印带索引
[0, "a"]
[1, [1, 2]]
[2, [3, 4]]

irb(main):038:0> arr=[1,-1,2,3,-4]
=> [1, -1, 2, 3, -4]
irb(main):039:0> arr.sort # 排序
=> [-4, -1, 1, 2, 3]
irb(main):040:0> arr.select{|e| e>0} # 按条件选择
=> [1, 2, 3]
irb(main):041:0> arr << nil  # 追加nil
=> [1, -1, 2, 3, -4, nil]
irb(main):042:0> arr.compact # 去掉nil
=> [1, -1, 2, 3, -4]

irb(main):043:0> arr.any?{|e| e<0} # 是否有小于0的值
=> true
```

### hash
**创建**
```ruby
# 引用
irb(main):044:0> a={key:'value'} # 这种情况下key是sybol类型，所以取它的值时a[:key]
=> {:key=>"value"}
irb(main):045:0> b =a
=> {:key=>"value"}
irb(main):046:0> b.object_id
=> 70368301765400
irb(main):047:0> a.object_id
=> 70368301765400
irb(main):049:0> a[:key]='foo'
=> "foo"
irb(main):050:0> b
=> {:key=>"foo"}

# 指定初始值
irb(main):053:0> h=Hash.new(3)
=> {}
irb(main):054:0> h[0]
=> 3
irb(main):055:0> h[1]
=> 3
irb(main):056:0> h
=> {}

#初始值只是一份引用，当中途改变时，后面创建的也都会改变
irb(main):057:0> h = Hash.new([])
=> {}
irb(main):058:0> h[:a]<<1
=> [1]
irb(main):059:0> h[:b]
=> [1]

# 生成不同的值，与array类似，要使用block来实现
irb(main):060:0> h =Hash.new{|h,k| h[k]=[]}
=> {}
irb(main):061:0> h[:a] << 1
=> [1]
irb(main):062:0> h
=> {:a=>[1]}
irb(main):063:0> h[:b]
=> []
irb(main):064:0> h
=> {:a=>[1], :b=>[]}

irb(main):065:0> h[:c]=3 # 赋值
=> 3
irb(main):066:0> h
=> {:a=>[1], :b=>[], :c=>3}
irb(main):067:0> h.delete(:b) # 删除
=> []
irb(main):068:0> h
=> {:a=>[1], :c=>3}
irb(main):069:0> h.assoc(:c) # 同时取key,value
=> [:c, 3]
irb(main):070:0> h.empty? # 是否为空
=> false
irb(main):071:0> h.has_value?(2) # 是否有某值
=> false
irb(main):072:0> h.has_key?(:c)  # 是否有某键
=> true
irb(main):073:0> h.keys  #　所有的键
=> [:a, :c]
irb(main):074:0> h.values  # 所有值
=> [[1], 3]
irb(main):075:0> h.to_a  # 转成数组
=> [[:a, [1]], [:c, 3]]
irb(main):076:0> h2={d:4}
=> {:d=>4}
irb(main):077:0> h.merge(h2)  # 合并
=> {:a=>[1], :c=>3, :d=>4}
# 遍历 ，遍历的顺序是插入的顺序
irb(main):079:0> h.each{|k,v| p [k,v]}  # 遍历键值
[:a, [1]]
[:c, 3]
=> {:a=>[1], :c=>3}
irb(main):080:0> h.each_key {|k| p k} # 遍历键
:a
:c
=> {:a=>[1], :c=>3}
irb(main):081:0> h.each_value {|v| p v}  # 遍历值
[1]
3
=> {:a=>[1], :c=>3}

irb(main):082:0> h.select{|k| k==:a}
=> {:a=>[1]}
```

### set
```ruby
irb(main):105:0> require 'set'  # 需要导入
=> true
irb(main):106:0> Set.new [1,2] # 创建
=> #<Set: {1, 2}>
irb(main):107:0> s = _
=> #<Set: {1, 2}>
irb(main):108:0> s.add('foo')
=> #<Set: {1, 2, "foo"}>
# 运算
irb(main):110:0> b = Set.new [2,3,4]
=> #<Set: {2, 3, 4}>
irb(main):111:0> s & b  # 交集
=> #<Set: {2}>
irb(main):112:0> s | b # 并集
=> #<Set: {1, 2, "foo", 3, 4}>
irb(main):113:0> s <= b  # 是否是b的子集
=> false
irb(main):114:0> c = Set.new [2,3]
=> #<Set: {2, 3}>
irb(main):115:0> c <= b
=> true
```
### range
有..（闭区间） 和 ...（开区间） 
```ruby
irb(main):119:0> r = 1..2
=> 1..2
irb(main):120:0> r.include?(2)
=> true
irb(main):121:0> a=[1,2,3,4]
=> [1, 2, 3, 4]
irb(main):122:0> a[1..2]
=> [2, 3]
```

### Method
#运算符作为方法名
```ruby
arr = [1, 2, 3]
def arr.+(num)
  self.dup << num
end

p arr +4
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
### 文件操作
File.rename(oldname,newname)
File.delete()
require FileUtils
FileUtils.cp()

Dir.open()

dir = Dir.open()
while filename = dir.read
p filename

Dir.mkdir('temp')
Dir.delete()

require "date"
Date.new


### 迭代器

### mixin
- 模块的(类)方法永远不能被 “混入”
- include 派到实例方法中
- extend 派到类方法中

```ruby
module First
  first = 1

  def greet
    p 'hello'
  end
end

module Second
  second = 2

  def self.smile
    p 'smile'
  end
end

class People
  # include First
  extend First
  extend Second

  def eat
    p 'eat'
  end
end

p = People.new
p.greet
# p.smile
People.smile
```
当使用`include First`时，只能使用p.greet,而如果使用extend则只能通过`Person.greet`调用,而对于module Second中的smile方法，是无法混入的