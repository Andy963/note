## template_folder
1. 在渲染模版的时候，默认会从项目根目录下的`templates`目录下查找模版。
2. 如果不想把模版文件放在`templates`目录下，那么可以在`Flask`初始化的时候指定`template_folder`来指定模版的路径。

在使用`render_template`渲染模版的时候，可以传递关键字参数。以后直接在模版中使用就可以了。
 如果你的参数过多，那么可以将所有的参数放到一个字典中，然后在传这个字典参数的时候，使用两个星号，将字典打散成关键参数。

## 自动加载模板
`app.config['TEMPLATES_AUTO_RELOAD']=True`

## url_for

模版中的`url_for`跟我们后台视图函数中的`url_for`使用起来基本是一模一样的。也是传递视图函数的名字，也可以传递参数。
使用的时候，需要在`url_for`左右两边加上一个`{{ url_for('func') }}`, 
传参数：`<p><a href="{{ url_for('login',ref='/',id='1') }}">登录</a></p>`


## filter：
### 什么是过滤器，语法是什么：
1. 有时候我们想要在模版中对一些变量进行处理，那么就必须需要类似于Python中的函数一样，可以将这个值传到函数中，然后做一些操作。在模版中，过滤器相当于是一个函数，把当前的变量传入到过滤器中，然后过滤器根据自己的功能，再返回相应的值，之后再将结果渲染到页面中。
2. 基本语法：`{{ variable|过滤器名字 }}`。使用管道符号`|`进行组合。

### 常用过滤器：
#### default
使用方式`{{ value|default('默认值') }}`。如果value这个`key`不存在，那么就会使用`default`过滤器提供的默认值。如果你想使用类似于`python`中判断一个值是否为False（例如：None、空字符串、空列表、空字典等），那么就必须要传递另外一个参数`{{ value|default('默认值',boolean=True) }}`。当指定`boolean=True`时，如果value为False则就使用默认值。
可以使用`or`来替代`default('默认值',boolean=True)`。例如：`{{ signature or '此人很懒，没有留下任何说明' }}`。

1. `safe`过滤器：可以关闭一个字符串的自动转义。
2. `escape`过滤器：对某一个字符串进行转义。
3. `autoescape`标签，可以对他里面的代码块关闭或开启自动转义。
    ```jinja2
    {% autoescape off/on %}
        ...代码块
    {% endautoescape %}
    ```
    

```Jinja2

abs(value)：返回一个数值的绝对值。示例：-1|abs
default(value,default_value,boolean=false)：如果当前变量没有值，则会使用参数中的值来代替。示例：name|default('xiaotuo')——如果name不存在，则会使用xiaotuo来替代。boolean=False默认是在只有这个变量为undefined的时候才会使用default中的值，如果想使用python的形式判断是否为false，则可以传递boolean=true。也可以使用or来替换。
escape(value)或e：转义字符，会将<、>等符号转义成HTML中的符号。示例：content|escape或content|e。
first(value)：返回一个序列的第一个元素。示例：names|first
format(value,*arags,**kwargs)：格式化字符串。比如：

{{ "%s" - "%s"|format('Hello?',"Foo!") }}
将输出：Helloo? - Foo!
last(value)：返回一个序列的最后一个元素。示例：names|last。

length(value)：返回一个序列或者字典的长度。示例：names|length。
join(value,d=u'')：将一个序列用d这个参数的值拼接成字符串。
safe(value)：如果开启了全局转义，那么safe过滤器会将变量关掉转义。示例：content_html|safe。
int(value)：将值转换为int类型。
float(value)：将值转换为float类型。
lower(value)：将字符串转换为小写。
upper(value)：将字符串转换为小写。
replace(value,old,new)： 替换将old替换为new的字符串。
truncate(value,length=255,killwords=False)：截取length长度的字符串。
striptags(value)：删除字符串中所有的HTML标签，如果出现多个空格，将替换成一个空格。
trim：截取字符串前面和后面的空白字符。
string(value)：将变量转换成字符串。
wordcount(s)：计算一个长字符串中单词的个数。
```

### 自定义模版过滤器：
过滤器本质上就是一个函数。如果在模版中调用这个过滤器，那么就会将这个变量的值作为第一个参数传给过滤器这个函数，然后函数的返回值会作为这个过滤器的返回值。需要使用到一个装饰器：`@app.template_filter('cut')`
```python
@app.template_filter('cut')
def cut(value):
    value = value.replace("hello",'')
    return value
```
```html
<p>{{ article|cut }}</p>
```

#### 时间处理(距离现在多长时间）

```python

@app.template_filter('handle_time')
def handle_time(time):
    """
    time距离现在的时间间隔
    1. 如果时间间隔小于1分钟以内，那么就显示“刚刚”
    2. 如果是大于1分钟小于1小时，那么就显示“xx分钟前”
    3. 如果是大于1小时小于24小时，那么就显示“xx小时前”
    4. 如果是大于24小时小于30天以内，那么就显示“xx天前”
    5. 否则就是显示具体的时间 2017/10/20 16:15
    """
    if isinstance(time,datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif timestamp>=60 and timestamp < 60*60:
            minutes = timestamp / 60
            return "%s分钟前" % int(minutes)
        elif timestamp >= 60*60 and timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return '%s小时前' % int(hours)
        elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
            days = timestamp / (60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time
```

## if
`if`条件判断语句必须放在`{% if statement %}`中间，并且还必须有结束的标签`{% endif %}`。和`python`中的类似，可以使用`>，<，<=，>=，==，!=`来进行判断，也可以通过`and，or，not，()`来进行逻辑合并操作。

## for
在`jinja2`中的`for`循环，跟`python`中的`for`循环基本上是一模一样的。也是`for...in...`的形式。并且也可以遍历所有的序列以及迭代器。但是唯一不同的是，`jinja2`中的`for`循环没有`break`和`continue`语句。

```Jinja2

<table border="1">
    <tbody>
        {% for x in range(1,10) %}
            <tr>
                {% for y in range(1,10) if y <= x %}
                    <td>{{ y }}*{{ x }}={{ x*y }}</td>
                {% endfor %}
            </tr>
        {% endfor %}
    </tbody>
</table>
```

## 宏：
模板中的宏跟python中的函数类似，可以传递参数，但是不能有返回值，可以将一些经常用到的代码片段放到宏中，然后把一些不固定的值抽取出来当成一个变量。
使用宏的时候，参数可以为默认值。相关示例代码如下：
1. 定义宏：
    ```html
    {% macro input(name, value='', type='text') %}
    <input type="{{ type }}" name="{{ name }}" value="{{
    value }}">
    {% endmacro %}
    ```
2. 使用宏：
    ```html
    <p>{{ input('username') }}</p>
    <p>{{ input('password', type='password') }}</p>
    ```

### 导入宏：
1. `import "宏文件的路径" as xxx`。
2. `from '宏文件的路径' import 宏的名字 [as xxx]`。
3. 宏文件路径，不要以相对路径去寻找，都要以`templates`作为绝对路径去找。
4. 如果想要在导入宏的时候，就把当前模版的一些参数传给宏所在的模版，那么就应该在导入的时候使用`with context`。示例：`from 'xxx.html' import input with context`。这样就能将当前模板中的变量经过宏渲染后再传回来，类似于django中的inclusion_tag

```jinja2

{% from "macros.html" import input as input_field %}
{% import "macros/macros.html" as macros with context %}

<table>
        <tbody>
            <tr>
                <td>用户名：</td>
                <td>{{ macros.input('username') }}</td>
            </tr>
            <tr>
                <td>密码：</td>
                <td>{{ macros.input("password",type="password") }}</td>
            </tr>
            <tr>
                <td></td>
                <td>{{ macros.input(value="提交",type="submit") }}</td>
            </tr>
        </tbody>
    </table>
```

## include标签：
1. 这个标签相当于是直接将指定的模版中的代码复制粘贴到当前位置。
2. `include`标签，如果想要使用父模版中的变量，直接用就可以了，不需要使用`with context`。
3. `include`的路径，也是跟`import`一样，直接从`templates`根目录下去找，不要以相对路径去找。

## set/with 

### set语句：
在模版中，可以使用`set`语句来定义变量。示例如下：
```html
{% set username='知了课堂' %}
<p>用户名：{{ username }}</p>
```
一旦定义了这个变量，那么在后面的代码中，都可以使用这个变量，就类似于Python的变量定义是一样的。

### `with`语句：
`with`语句定义的变量，只能在`with`语句块中使用，超过了这个代码块，就不能再使用了。示例代码如下：
```html
{% with classroom = 'zhiliao1班' %}
<p>班级：{{ classroom }}</p>
{% endwith %}
```
`with`语句也不一定要跟一个变量，可以定义一个空的`with`语句，以后在`with`块中通过`set`定义的变量，就只能在这个`with`块中使用了：
```html
{% with %}
    {% set classroom = 'zhiliao1班' %}
    <p>班级：{{ classroom }}</p>
{% endwith %}
```
## 静态文件：
加载静态文件使用的是`url_for`函数。然后第一个参数需要为`static`，第二个参数需要为一个关键字参数`filename='路径'`。示例：
```html
{{ url_for("static",filename='xxx') }}
```
路径查找，要以当前项目的`static`目录作为根目录。

## 模版继承

### 为什么需要模版继承：
模版继承可以把一些公用的代码单独抽取出来放到一个父模板中。以后子模板直接继承就可以使用了。这样可以重复性的代码，并且以后修改起来也比较方便。

### 模版继承语法：
使用`extends`语句，来指明继承的父模板。父模板的路径，也是相对于`templates`文件夹下的绝对路径。示例代码如下：
`{% extends "base.html" %}`。

### block语法：
一般在父模版中，定义一些公共的代码。子模板可能要根据具体的需求实现不同的代码。这时候父模版就应该有能力提供一个接口，让父模板来实现。从而实现具体业务需求的功能。
在父模板中：
```html
{% block block的名字 %}
{% endblock %}
```
在子模板中：
```html
{% block block的名字 %}
子模板中的代码
{% endblock %}
```

### 调用父模版代码block中的代码：
默认情况下，子模板如果实现了父模版定义的block。那么子模板block中的代码就会覆盖掉父模板中的代码。如果想要在子模板中仍然保持父模板中的代码，那么可以使用`{{ super() }}`来实现。示例如下：
父模板：
```html
{% block body_block %}
        <p style="background: red;">这是父模板中的代码</p>
    {% endblock %}
```
子模板：
```html
{% block body_block %}
    {{ super() }}
    <p style="background: green;">我是子模板中的代码</p>
{% endblock %}
```

### 调用另外一个block中的代码：
如果想要在另外一个模版中使用其他模版中的代码。那么可以通过`{{ self.其他block名字() }}`就可以了。示例代码如下：
```html
{% block title %}
    知了课堂首页
{% endblock %}

{% block body_block %}
    {{ self.title() }}
    <p style="background: green;">我是子模板中的代码</p>
{% endblock %}
```

### 其他注意事项：
1. 子模板中的代码，第一行，应该是`extends`。
2. 子模板中，如果要实现自己的代码，应该放到block中。如果放到其他地方，那么就不会被渲染。

## 宏案例

base.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="{{ url_for('static',filename='css/base.css') }}">
    <link rel="stylesheet" href="{{ url_for("static",filename='css/item.css') }}">
    <title>{% block title %}{% endblock %}</title>
    {% block head %}{% endblock %}
</head>
<body>
    <div class="container">
        <div class="search-group">
            <input type="text" class="search-input" placeholder="搜索...">
        </div>
        {% block body %}{% endblock %}
    </div>
</body>
</html>
```

index.html
```html
{% extends 'base.html' %}
{% from "macros.html" import itemGroup,listGroup %}

{% block body %}
    {{ listGroup("电影",movies,1) }}
    {{ listGroup("电视剧",tvs,2) }}
{% endblock %}
```
macro.html
```jinja2
{# itemGroup的宏 #}
{% macro itemGroup(thumbnail,title,rating) %}
    <div class="item-group">
        <img src="{{ thumbnail }}" alt="" class="thumbnail">
        <p class="item-title">{{ title }}</p>
        <p class="item-rating">
            {% set lights = ((rating|int)/2)|int %}
            {% set halfs = (rating|int)%2 %}
            {% set grays = 5 - lights - halfs %}
            {% for light in range(0,lights) %}
                <img src="{{ url_for("static",filename='images/rate_light.png') }}" alt="">
            {% endfor %}
            {% for half in range(0,halfs) %}
                <img src="{{ url_for('static',filename='images/rate_half.jpg') }}" alt="">
            {% endfor %}
            {% for gray in range(0,grays) %}
                <img src="{{ url_for('static',filename='images/rate_gray.png') }}" alt="">
            {% endfor %}
            {{ rating }}
        </p>
    </div>
{% endmacro %}


{# listGroup的宏 #}
{% macro listGroup(module_title,items,category=category) %}
    <div class="item-list-group">
        <div class="item-list-top">
            <span class="module-title">{{ module_title }}</span>
{#            /list/1/#}
{#            /list/?category=1#}
            <a href="{{ url_for("item_list",category=category) }}" class="more-btn">更多</a>
        </div>
        <div class="list-group">
            {% for item in items[0:3] %}
                {{ itemGroup(item.thumbnail,item.title,item.rating) }}
            {% endfor %}
        </div>
    </div>
{% endmacro %}
```

list.html
```html
{% extends 'base.html' %}
{% from "macros.html" import itemGroup %}

{% block body %}
    {% for item in items %}
        {{ itemGroup(item.thumbnail,item.title,item.rating) }}
    {% endfor %}
{% endblock %}
```

### flash
flash 即flask中的闪现
使用：
在视图函数中调用 flash(message, category)
在模板中使用get_flashed_messages()
```jinja2

{% set message = get_flash_message() %} # 此时message变量的范围是当前block,如果又定义了另一个block，则无法使用

{% with message = get_flash_message() %}
  message 的有效范围为with语句内部
{% endwith %}
```

```