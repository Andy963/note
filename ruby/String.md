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

#### length & size
获取字符串长度与size相同
```ruby
irb(main):001:0> p 'just'.length
4
=> 4
irb(main):002:0> 'just'.size
=> 4
```

#### 索引
```ruby
irb(main):004:0> 'ruby'[0]
=> "r"
irb(main):005:0> 'ruby'[1]
=> "u"
```
#### 字符串拼接
```ruby
irb(main):006:0> 'hello' + 'world'
=> "helloworld"
irb(main):007:0> 'hello' << 'world'
=> "helloworld"
irb(main):008:0> 'hello'.concat('world')
=> "helloworld"
```
+ 拼接不会改变原有对象，但 << ,concat会改变原有对象

```ruby
reverse
include？
index
sub(source,to) # 替换
size
to_sym
```
#### printf & sprintf
```ruby
irb(main):001:0> n = 123
=> 123
irb(main):002:0> printf("%d\n",n)
123
=> nil
irb(main):003:0> printf("%4d\n", n)
 123
=> nil
irb(main):004:0> printf("%04d\n", n)
0123
=> nil
irb(main):005:0> printf("%+d\n", n)
+123
=> nil

irb(main):006:0> n = "Ruby"
=> "Ruby"
irb(main):007:0> printf("Hello,%s!\n", n)
Hello,Ruby!
=> nil
irb(main):008:0> printf("Hello,%8s!\n", n)
Hello,    Ruby!
=> nil
irb(main):009:0> printf("Hello,%-8s!\n", n)
Hello,Ruby    !
=> nil
```
printf会将内容输出到控制台，而sprintf会将内容转成字符串对象
```ruby
irb(main):010:0> sprintf("%d", 123)
=> "123"
irb(main):011:0> sprintf("%d", 123).class
=> String
irb(main):012:0> p sprintf("%04d", 123)
"0123"
=> "0123"
irb(main):013:0> p sprintf("%+d", 123)
"+123"
=> "+123"
irb(main):014:0> p sprintf("Hello,%s!\n", n)
"Hello,Ruby!\n"
=> "Hello,Ruby!\n"
irb(main):015:0> p sprintf("Hello,%8s!\n", n)
"Hello,    Ruby!\n"
=> "Hello,    Ruby!\n"
irb(main):016:0> p sprintf("Hello,%-8s!\n", n)
"Hello,Ruby    !\n"
=> "Hello,Ruby    !\n"
```

#### 字符串比较
使用== 与！=
```ruby
irb(main):017:0> 'aa'=='aa'
=> true
irb(main):019:0> 'aa'=='ab'
=> false
irb(main):020:0>
```
另外大小比较时是由字符编码的顺序决定
```ruby
irb(main):020:0> 'aaa' < 'b'
=> true
```

#### split
```ruby
irb(main):021:0> str = "高桥:gaoqiao:1234567:000-123-4567"
=> "高桥:gaoqiao:1234567:000-123-4567"
irb(main):022:0> str.split(/:/)
=> ["高桥", "gaoqiao", "1234567", "000-123-4567"]
irb(main):023:0> str.split(':')
=> ["高桥", "gaoqiao", "1234567", "000-123-4567"]
```
#### chop & chomp
chop 删除最后一个字符，chomp则只删除行尾的换行符.另外有chop!,chomp!在原字符串上操作
```ruby
irb(main):024:0> str='abcd'
=> "abcd"
irb(main):025:0> str.chop
=> "abc"
irb(main):026:0> str.chomp
=> "abcd"
irb(main):027:0> str='abc\n'
=> "abc\\n"
irb(main):028:0> str.chomp
=> "abc\\n"
irb(main):029:0> str.chop
=> "abc\\"
irb(main):030:0> str="abc\n"
=> "abc\n"
irb(main):031:0> str.chomp
=> "abc"
irb(main):032:0> str="abc\n"
=> "abc\n"
irb(main):033:0> str.chop
=> "abc"
```

#### 检索
找到字符时返回首个字符的索引
```ruby
irb(main):034:0> str='abcde'
=> "abcde"
irb(main):035:0> str.index('b')
=> 1
irb(main):036:0> str.rindex('b')
=> 1
```