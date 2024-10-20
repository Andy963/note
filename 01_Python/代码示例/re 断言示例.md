### look around:

- look forward

```python

In [12]: txt = "i love python, i love regex"
# 后面是python的Love
In [13]: pattern = re.compile("love\s(?=python)")
# 所以这里只能匹配出第一个love, 因为第二个love后面接的regex
In [14]: pattern.search(txt)
Out[14]: <re.Match object; span=(2, 7), match='love '>
# 后面不是python的Love
In [15]: pattern = re.compile("love\s(?!python)")
# 通过索引可以看到，匹配的是第二个love, 因为第一个Love后面接的是python
In [16]: pattern.search(txt)
Out[16]: <re.Match object; span=(17, 22), match='love '>
# 后面既不能是python也不能是love
In [17]: pattern = re.compile("love\s(?!python|regex)")

In [18]: pattern.search(txt)
```

the word after "?=" or "?!" will not consuming characters. the first one `love\s(?=python)` means only match the word love which is followed by python.
if i change the "?=" to "?!" means not match, so the result is the "love" folled by regex

- look back/behind

```python
# 肯定型后视断言，这里的<= 可以理解为在当前位置回退几个字符，看是否能匹配上内部的模式
# 这里的内部的模式即pattern in the brackets, but remmber the pattern lenght is
# accurate, but not variable(a.*, a{3,4} is not allowed)
In [72]: text = "love regex or hate regex, can't ignore regex"

In [73]: pattern = re.compile("(?<=(love|hate)\s)regex")

In [74]: pattern.findall(text)
Out[74]: ['love', 'hate']

# negetive look back, which is oppoiste to the up one
In [94]: pattern = re.compile("(?<!love\s)regex")

In [95]: pattern.findall(text)
Out[95]: ['regex', 'regex']

# i don't known why this negetive lookbehind not work even if i change the 
# the inside mode to a or anything else.
In [96]: pattern = re.compile("(?<!(love|hate)\s)regex")
In [97]: pattern.findall(text)
Out[97]: ['']

```

the word after ?<= will only match the word  has hate or love before regex.  and ?<! not match. but there is sth confusing: when i use "love|hate" why it return "" ? 
