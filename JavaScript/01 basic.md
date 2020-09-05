
## 基础
### import
```js
//1 直接编写,就将其放在html的<head>标签内 
<script> 
    alert('hello world') # alert（）实际为window.alert() 
</script> 
//2 导入文件 
<script src="hello.js"></script> 
<script language="javascript" type="text/javascript"></script> 
```
### variable
js中var 定义的变量没法通过{}锁定作用域，而let是块级作用域。
```js
//1、声明变量时不用声明变量类型. 可以使用var,let关键字; 
var a; 
a=3; 

#2、一行可以声明多个变量.并且可以是不同类型 
var name="andy, age=20, job="geologist"; 

#3、声明变量时,如果没有使用var 那么它是全局变量 

#4、变量命名,首字符只能是字母,下划线,$美元符 三选一，余下的字符可以是下划线、美元符号或任何字母或数字字符且区分大小写，x与X是两个变量. 
```

### constant
常量 ：直接在程序中出现的数据值 
标识符： 
- 由不以数字开头的字母、数字、下划线(_)、美元符号($)组成 
- 常用于表示函数、变量等的名称 
- 例如：_abc,$abc,abc,abc123是标识符，而1abc不是 
- JavaScript语言中代表特定含义的词称为保留字，不允许程序再定义为标识符 

### data type
number     -----  数值 
boolean    -----  布尔值 
string     -----  字符串 
undefined  -----  undefined 
null       -----   null  

#### number
不区分整型数值和浮点型数值; 所有数字都采用64位浮点格式存储，相当于Java和C语言中的double格式.能表示的最大值是±1.7976931348623157 x 10308,能表示的最小值是±5 x 10 -324 
整数： 
   在JavaScript中10进制的整数由数字的序列组成 
   精确表达的范围是 -9007199254740992 (-253) 到 9007199254740992 (253) 
   超出范围的整数，精确度将受影响 

浮点数： 
   使用小数点记录数据 
   例如：3.4，5.6 
   使用指数记录数据 
   例如：4.3e23 = 4.3 x 1023 
   
16进制和8进制数的表达: 
   16进制数据前面加上0x，16进制数是由0-9,A-F等16个字符组成;
   八进制前面加0;8进制数 由0-7等8个数字组成 
   16进制和8进制与2进制的换算: 
   2进制: 1111 0011 1101 0100   <-----> 16进制:0xF3D4 <-----> 10进制:62420 
   2进制: 1 111 001 111 010 100 <-----> 8进制:0171724 

#### string 
是由Unicode字符、数字、标点符号组成的序列；字符串常量首尾由单引号或双引号括起；JavaScript中没有字符类型；常用特殊字符在字符串中的表达；字符串中部分特殊字符必须加上右划线\；常用的转义字符 \n:换行 \':单引号 \":双引号 \\:右划线 

#### boolean
Boolean类型仅有两个值：true和false，也代表1和0，实际运算中true=1,false=0.布尔值也可以看作on/off、yes/no、1/0对应true/false.Boolean值主要用于JavaScript的控制语句，例如： 
```js
if (x==1){ 
      y=y+1; 
}else{ 
      y=y-1; 
      } 
```
#### null/undefined
Null 与undefined类型： 
- Undefined类型:Undefined 类型只有一个值，即 undefined。当声明的变量未初始化时，该变量的默认值是 undefined。当函数无明确返回值时，返回的也是值 "undefined"; 
- Null类型:另一种只有一个值的类型是 Null，它只有一个专用值 null，即它的字面量。值 undefined 实际上是从值 null 派生来的，因此 ECMAScript 把它们定义为相等的。 

尽管这两个值相等，但它们的含义不同。undefined 是声明了变量但未对其初始化时赋予该变量的值，null 则用于表示尚未存在的对象（在讨论 typeof 运算符时，简单地介绍过这一点）。如果函数或方法要返回的是对象，那么找不到该对象时，返回的通常是 null。 

### operator
 ` +   -    *    /     %       ++        --`
  
比较运算符： 
    >   >=   <    <=    !=    ==    ===   !== 

逻辑运算符：与，或，非 
     &&   ||   ！

赋值运算符： 
    =  +=   -=  *=   /= 

字符串运算符： 
    +  连接，两边操作数有一个或两个是字符串就做连接运算 

注意1: 自加自减 
假如x=2，那么x++表达式执行后的值为3，x--表达式执行后的值为1；i++相当于i=i+1，i--相当于i=i-1；
递增和递减运算符可以放在变量前也可以放在变量后：--i 

#### NaN
NaN:属于Number类型的一个特殊值,当遇到将字符串转成数字无效时,就会得到一个NaN数据
```js
var d="andy"; 
d=+d; 
alert(d);//NaN
alert(typeof(d));//Number 
```
//NaN特点:
```js
var n=NaN; 
alert(n>3); 
alert(n<3); 
alert(n==3); 
alert(n==NaN); 
alert(n!=NaN); 
```
//NaN参与的所有的运算都是false,除了!= 


#### compare
```
 >   >=   <    <=    !=    ==    ===   !==
```
用于控制语句时
```js
if (2>1){       //  3  0  false null undefined ［］ 
    console.log("条件成立!") 
}
```
等号和非等号的同类运算符是全等号和非全等号。这两个运算符所做的与等号和非等号相同，只是它们在检查相等性前，不执行类型转换。 
console.log(2==2); 
console.log(2=="2"); 
console.log(2==="2"); 
console.log(2!=="2"); 

#### alert
```js
var bResult = "Blue" < "alpha"; 
alert(bResult); //输出 true 
```
在上面的例子中，字符串 "Blue" 小于 "alpha"，因为字母 B 的字符代码是 66，字母 a 的字符代码是 97。比较数字和字符串 

另一种棘手的状况发生在比较两个字符串形式的数字时，比如： 
```js
var bResult = "25" < "3"; 
alert(bResult); //输出 "true" 
```
上面这段代码比较的是字符串 "25" 和 "3"。两个运算数都是字符串，所以比较的是它们的字符代码（"2" 的字符代码是 50，"3" 的字符代码是 51）。 
不过，如果把某个运算数改为数字，那么结果就有趣了： 
```js
var bResult = "25" < 3; 
alert(bResult); //输出 "false" 
```
这里，字符串 "25" 将被转换成数字 25，然后与数字 3 进行比较，结果不出所料。 
总结： 
> 比较运算符两侧如果一个是数字类型,一个是其他类型,会将其类型转换成数字类型. 
> 比较运算符两侧如果都是字符串类型,比较的是最高位的asc码,如果最高位相等,继续取第二位比较. 

等性运算符：执行类型转换的规则如下： 
> 如果一个运算数是 Boolean 值，在检查相等性之前，把它转换成数字值。false 转换成 0，true 为 1。  
> 如果一个运算数是字符串，另一个是数字，在检查相等性之前，要尝试把字符串转换成数字。  
> 如果一个运算数是对象，另一个是字符串，在检查相等性之前，要尝试把对象转换成字符串。  
> 如果一个运算数是对象，另一个是数字，在检查相等性之前，要尝试把对象转换成数字。  
在比较时，该运算符还遵守下列规则： 
>值 null 和 undefined 相等。  
> 在检查相等性时，不能把 null 和 undefined 转换成其他值。  
> 如果某个运算数是 NaN，等号将返回 false，非等号将返回 true。  
> 如果两个运算数都是对象，那么比较的是它们的引用值。如果两个运算数指向同一对象，那么等号返回 true，否则两个运算数不等。

### control flow

#### order
```js
<script> 
console.log(“星期一”); 
console.log(“星期二”); 
console.log(“星期三”); 
</script> 
```

#### condition
```js
if (表达式){ 
   语句１; 
   ...... 
   } else{ 
   语句２; 
   ..... 
   } 
)

var score=window.prompt("您的分数:"); 
if (score>90){ 
    ret="优秀"; 
}else if (score>80){ 
    ret="良"; 
}else if (score>60){ 
    ret="及格"; 
}else { 
    ret = "不及格"; 
}

switch(x){ 
    case 1:y="星期一";    break; 
    case 2:y="星期二";    break; 
    case 3:y="星期三";    break; 
    case 4:y="星期四";    break; 
    case 5:y="星期五";    break; 
    case 6:y="星期六";    break; 
    case 7:y="星期日";    break; 
    default: y="未定义"; 
} 
```
#### loop
```js
var i=1; 
while (i<=7) { 
    document.write("<H"+i+">hello</H "+i+"> "); 
    document.write("<br>"); 
    i++; 
}
```

### exception

```js
try { 
    //这段代码从上往下运行，其中任何一个语句抛出异常该代码块就结束运行 
} 
catch (e) { 
    // 如果try代码块中抛出了异常，catch代码块中的代码就会被执行。 
    //e是一个局部变量，用来指向Error对象或者其他抛出的对象 
} 
finally { 
     //无论try中代码是否有异常抛出（甚至是try代码块中有return语句），finally代码块中始终会被执行。 
} 
//注：主动抛出异常 throw Error('xxxx') 
```

### output
```js
//这里的输出类似于python的print,意思是输出数据，方便编程时查看： 

//方式一： 
window.alert("a");//这里window可以省略不写 

//方式二： 
window.write("b"); 

方式三： 
innerHTML//写入到HTML元素 

方式四： 
console.log()// 输出到浏览器控制台  
```