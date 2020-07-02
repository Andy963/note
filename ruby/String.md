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