


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




#### 正则表达式
**创建**
- /ruby/
- %r{ruby}
- Regexp.new

www.rubular.com

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

**attr_accessor**
```ruby
class Test
  attr_accessor :name

  def initialize(name)
    @name = name
  end
  def say
    p name
  end
end

test = Test.new('andy')
test.name= 'jack'
test.say # "jack"

# attr_accessor等同于创造了两个方法
class Test
  def initialize(name)
    @name = name
  end

  def name
    @name
  end

  def name=(name)
    @name = name
  end

  def say
    p name
  end
end

test = Test.new('andy')
test.name = 'jack'
test.say # 'jack'
```

```ruby
class Point
  def initialize(x, y)
    #@x 实例变量
    # @@x 类变量
    # $x 全局变量
    # x 局部变量
    @x, @y = x, y
  end
end

p = Point.new(1,2)
p.x # 这样会出错，需要通过getter,setter来获取：attr_getter,attr_setter,attr_accessor
```

#### self
```ruby
class Point
  attr_accessor : x, :y

  def initialize(x, y)
    @x, @y = x, y
  end

  def first_quadrant?
    x > 0 && y > 0 # 等同于self.x或者@a
    # 但如果赋值则需要self.x=3,否则ruby不知道是局部变量还是实例变量
  end

  def self.second_quadrant?(x, y) # 定义类方法，self指class,如果在first_quadrant方法内使用self,指实例，在second_quadrant方法内指类
    x < 0 && y > 0
  end
  class <<self
    def foo # 赞同于self.foo
    end
    def bar
    end
  end
end

p = Point.new(1, 2)
puts p.y
```

#### 类变量
```ruby
class Person
  @@age = 1
  GENDRE = 'male'

  def talk
    p 'talk'
  end

end

p1 = Person.new
p p1.age #这样是获取不到的
需要作下面的修改
class Person
  @@age = 1
  GENDRE = 'male'

  def talk
    p 'talk'
  end

  def get_age
    @@age
  end
end

p1 = Person.new
p p1.get_age
#而对于GENDER 则可以通过Person::GENDER来获取 
```
#### 类方法
public,private,protected
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
```ruby
class BaseFoo
  def foo
    private_method
  end

  def private_method
    puts 'come to baseclass'
  end

  private :private_method
end

class Foo < BaseFoo
  def bar
    result = foo
    private_method(result)
  end

  def private_method(result = nil)
    puts 'come to subclass'
  end

  private :private_method
end

foo = Foo.new
foo.bar
#执行结果：
come to subclass
come to subclass
# 理论上是先执行BaseFoo的private_method,但因为子类重写了private_method，所以最终结果是子类的private_method执行了两次。在ruby中public,private,protected的类方法都可以被子类继承。
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

### block
block能获取当前环境下的所有变量，block中的return是指从包含当前block的方法中退出。
```ruby
def foo(&block)
  a = 2
  block.call(a)
end

foo { |a| puts a }  # 注意这里不能加括号
```

```ruby
def bar
  puts 'start of bar'
  x = 3
  yield x
  puts 'end of bar'
end

def foo
  puts 'start of foo'
  bar { |x| return if x > 0 }
  puts 'end of foo'
end

foo
#输出
start of foo
start of bar
```
### proc && lambda
proce 的行为更像block, lambda更像方法
```ruby
irb(main):075:0> p = Proc.new { |x,y| p x,y }
=> #<Proc:0x00007ffff26c0058@(irb):75>
irb(main):076:0> p.call(1)
1
nil
=> [1, nil]
irb(main):077:0> p.call(1,2)
1
2
=> [1, 2]
irb(main):078:0> p.call(1,2,3)
1
2
=> [1, 2]

irb(main):079:0> l = lambda { |x,y| p x,y }
=> #<Proc:0x00007ffff26633f8@(irb):79 (lambda)>
irb(main):080:0> l.call(1)
Traceback (most recent call last):
        3: from /usr/bin/irb:11:in `<main>'
        2: from (irb):80
        1: from (irb):79:in `block in irb_binding'
ArgumentError (wrong number of arguments (given 1, expected 2))
irb(main):081:0> l.call(1,2)
1
2
=> [1, 2]
irb(main):082:0> l.call(1,2,3)
Traceback (most recent call last):
        3: from /usr/bin/irb:11:in `<main>'
        2: from (irb):82
        1: from (irb):79:in `block in irb_binding'
ArgumentError (wrong number of arguments (given 3, expected 2))
```

### 文件操作

require FileUtils
FileUtils.cp()

```ruby
File.open('file.rb', 'r') do |f|
  while line = f.gets # f.getc 获取一个字符
    puts line
  end
end

File.open('test.rb','r') do |f|
  lines = f.readlines
end

File.readlines('file_util.rb') # 读取所有行
File.read('file_util.rb')  # 读取所有内容

File.open('test','w') do |f|
  f << 'hello'  # 追加
  f << 'world'
  f.puts 'hello'
  f.puts 'world'
end
```

#### File && Dir
**File**
```ruby
irb(main):053:0> full_name="/mnt/d/code/ruby/r1.rb"
=> "/mnt/d/code/ruby/r1.rb"
irb(main):054:0> File.basename(full_name) # 文件名
=> "r1.rb"
irb(main):055:0> File.basename(full_name,'.rb')  # 去年后缀的文件名
=> "r1"
irb(main):056:0> File.dirname(full_name)  # 文件夹路径
=> "/mnt/d/code/ruby"
irb(main):057:0> File.extname(full_name)  # 后缀名
=> ".rb"
irb(main):058:0> File.join('/mnt/d','code')  # 拼接
=> "/mnt/d/code"
irb(main):059:0> File.expand_path("~/ruyb")  # 
=> "/home/andy/ruyb"
irb(main):064:0> File.exist?('.zshrc') # 是否存在
=> true
irb(main):066:0> File.directory?('/home/andy')  # 是否是文件夹
=> true
irb(main):067:0> File.file?('.bashrc')  # 是否文件
=> true
irb(main):068:0> File.size('.bashrc')  # 文件大小
=> 3772
File.rename('oldname','newname')  # 重命名
File.delete('test.rb')  # 删除
File.symlink('test','old_test')

```
**Dir**
```ruby
irb(main):060:0> Dir.pwd  # 打印路径
=> "/home/andy"
irb(main):061:0> Dir.chdir('./')  # 切换目录
=> 0
irb(main):062:0> Dir.pwd
=> "/home/andy"
irb(main):063:0> Dir.entries('./')  # 遍历文件
=> [".", "..", ".bash_history", ".bash_logout", ".bashrc", ".cache", ".config", ".gem", ".gitconfig", ".ipython", ".jupyter", ".local", ".oh-my-zsh", ".pip", ".profile", ".python_history", ".shell.pre-oh-my-zsh", ".ssh", ".sudo_as_admin_successful", ".vim", ".viminfo", ".wget-hsts", ".zcompdump", ".zcompdump-Andy963-5.4.2", ".zsh_history", ".zshrc", "config", "proxychains-ng"]
irb(main):073:0> Dir['*config']  # 过滤文件
=> ["config"]
Dir.glob('/mnt/d/code/ruby/*.rb){|f| load f}
Dir.mkdir('tmp')  # 创建目录
Dir.rmdir('tmp')  # 删除目录

```

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

### exception
**raise**
raise 'some error message'
raise ArgumentError, 'error msg',caller

```ruby
irb(main):001:0> def foo
irb(main):002:1>   begin
irb(main):003:2>     raise TypeError, 'boom in foo', caller
irb(main):004:2>   rescue => e
irb(main):005:2>     puts e.send(:caller)
irb(main):006:2>   end
irb(main):007:1> end
=> :foo
irb(main):008:0> foo
(irb):1:in `foo'
(irb):8:in `irb_binding'
/usr/lib/ruby/2.5.0/irb/workspace.rb:85:in `eval'
/usr/lib/ruby/2.5.0/irb/workspace.rb:85:in `evaluate'
/usr/lib/ruby/2.5.0/irb/context.rb:380:in `evaluate'
/usr/lib/ruby/2.5.0/irb.rb:491:in `block (2 levels) in eval_input'
/usr/lib/ruby/2.5.0/irb.rb:623:in `signal_status'
/usr/lib/ruby/2.5.0/irb.rb:488:in `block in eval_input'
/usr/lib/ruby/2.5.0/irb/ruby-lex.rb:246:in `block (2 levels) in each_top_level_statement'
/usr/lib/ruby/2.5.0/irb/ruby-lex.rb:232:in `loop'
/usr/lib/ruby/2.5.0/irb/ruby-lex.rb:232:in `block in each_top_level_statement'
/usr/lib/ruby/2.5.0/irb/ruby-lex.rb:231:in `catch'
/usr/lib/ruby/2.5.0/irb/ruby-lex.rb:231:in `each_top_level_statement'
/usr/lib/ruby/2.5.0/irb.rb:487:in `eval_input'
/usr/lib/ruby/2.5.0/irb.rb:428:in `block in run'
/usr/lib/ruby/2.5.0/irb.rb:427:in `catch'
/usr/lib/ruby/2.5.0/irb.rb:427:in `run'
/usr/lib/ruby/2.5.0/irb.rb:383:in `start'
/usr/bin/irb:11:in `<main>'
=> nil
```
**实例**
```ruby
def factorial(n)
  raise TypeError unless n.is_a? Integer
  raise ArgumentError if n < 1
  return 1 if n == 1
  n * factorial(n - 1)
end

begin
  x = factorial(1)
rescue ArgumentError => e
  puts 'Try again with a value >=1'
rescue TypeError => e
  puts "Try again with an integer"
else
  puts x
ensure
  puts 'The process of factorial calculation is completeed'
end
```
### 日期与时间
DateTime < Date
Time

**Date**
```ruby
irb(main):010:0> require 'date'
irb(main):014:0> date = Date.today
=> #<Date: 2020-06-26 ((2459027j,0s,0n),+0s,2299161j)>
irb(main):015:0> date.year
=> 2020
irb(main):016:0> date.month
=> 6
irb(main):017:0> date.day
=> 26
irb(main):018:0> date.wday
=> 5
irb(main):019:0> date.prev_day
=> #<Date: 2020-06-25 ((2459026j,0s,0n),+0s,2299161j)>
irb(main):020:0> date.next_day
=> #<Date: 2020-06-27 ((2459028j,0s,0n),+0s,2299161j)>
irb(main):021:0> date.next_day.wday
=> 6
```
**DateTime**
```ruby
irb(main):034:0> DateTime.now.new_offset(Rational(-7,24))
=> #<DateTime: 2020-06-25T20:10:49-07:00 ((2459027j,11449s,310850000n),-25200s,2299161j)>
```

**Time**
```ruby
irb(main):024:0> time = Time.now
=> 2020-06-26 11:02:20 +0800
irb(main):025:0> time.year
=> 2020
irb(main):026:0> time.month
=> 6
irb(main):027:0> time.day
=> 26
irb(main):028:0> time.hour
=> 11
irb(main):029:0> time.min
=> 2
irb(main):030:0> time.sec
=> 20
irb(main):031:0> time.zone
=> "CST"
```

### Thread

```ruby
def foo
  10.times { puts "call foo at #{Time.now}" }
  sleep(0.5)
end

def bar
  10.times { puts "call bar at #{Time.now}" }
  sleep(0.5)
end

p '*' * 10 + 'start' + '*' * 10
t1 = Thread.new { foo() }
t2 = Thread.new { bar() }
t1.join
t2.join
p '*' * 10 + 'end' + '*' * 10
```

```ruby
count = 0
arr = []

10.times do |i|
  arr[i] = Thread.new {
    sleep(rand(0) / 10)
    Thread.current['count'] = count
    count += 1
  }
end

arr.each { |t| t.join; print t['count'], ',' }
puts "count=#{count}"
```
指定priority 使得分配的时间不同
```ruby
count1 = count2 = 0
a = Thread.new do
  loop { count1 += 1}
end
a.priority =1

b = Thread.new do
  loop { count2 += 1}
end

b.priority = -1
sleep(1)
puts count1,count2
```

**加锁**
```ruby
mutex = Mutex.new
count1 = count2 = 0
difference = 0
counter = Thread.new do
  loop do
    mutex.synchronize do
      count1 += 1
      count2 += 1
    end
  end
end

spy = Thread.new do
  loop do
    mutex.synchronize do
      difference += (count1 - count2).abs
    end
  end
end
sleep(1)
mutex.lock
puts "count1: #{count1}"
puts "count2: #{count2}"
puts "difference: #{difference}"

```

### module
module没有实例，我们使用时把module混合到类中使用。可以简单理解为把module的内容拷贝一份到类里面，成为类的一部分
```ruby
module FirstModule
  def say
    puts 'hello'
  end
end

class ModuleTest
  include FirstModule
end

test = ModuleTest.new
test.say
```

**相互嵌套**
```ruby
module Human
  class Boy
    def say
      puts 'Hey guys'
    end
  end
end

test = Human::Boy.new
test.say
```