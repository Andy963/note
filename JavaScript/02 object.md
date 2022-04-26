## object
在JavaScript中除了null和undefined以外其他的数据类型都被定义成了对象，也可以用创建对象的方法定义变量，String、Math、Array、Date、RegExp都是JavaScript中重要的内置对象，在JavaScript程序大多数功能都是基于对象实现的.
```js
<script language="javascript"> 
var aa=Number.MAX_VALUE;  
//利用数字对象获取可表示最大数 
var bb=new String("hello JavaScript");  
//创建字符串对象 
var cc=new Date(); 
//创建日期对象 
var dd=new Array("星期一","星期二","星期三","星期四");  
//数组对象 
</script> 
```

### string
#### create
字符串创建(两种方式) 
```js
//变量 = “字符串” 
//字串对象名称 = new String (字符串) 
var str1="hello world"; 
var str1= new String("hello word"); 
```

#### attr && method
x.length         －－－－获取字符串的长度 
x.toLowerCase()        －－－－转为小写 
x.toUpperCase()        －－－－转为大写 
x.trim()               －－－－去除字符串两边空格
x.charAt(index)       －－－－获取指定位置字符，其中index为要获取的字符索引 
x.charCodeAt(index)       -------返回指定索引位置的unicode的值 
x.fromCharCode()                   ------将unicode转换成字符串 
x.localcompare(y)           ----------用本地特定的顺序来比较两个字符串 
x.indexOf(findstr,index) －－－－查询字符串位置 
x.match(regexp)         －－－－match返回匹配字符串的数组，如果没有匹配则返回null 
x.search(regexp)        －－－－search返回匹配字符串的首字符位置索引 
x.substr(start, length) －－－－start表示开始位置，length表示截取长度 
x.substring(start, end) －－－－end是结束位置 
x.slice(start, end) －－－－切片操作字符串， 与python类似，左包右不包

反转字符串: 利用数组的reverse方法
```js
function reverseString(str) {
    return str.split("").reverse().join("");
}
reverseString("hello");
#ref:https://leetcode-cn.com/problems/palindrome-number/submissions/
```
#### format
字符串格式化通常有两种方式，用+，以及ES6中的反引号
```js
var name = 'andy'
var s0 = 'hello ' + name
var s = `Hello ${name}`
console.log(s)
```
### array
 js中数组的特性 
- js中的数组可以装任意类型,没有任何限制. 
- js中的数组,长度是随着下标变化的.用到多长就有多长.
#### create
```js
//创建方式1: 
var arrname = [元素0,元素1,….];          // var arr=[1,2,3]; 
//创建方式2: 
var arrname = new Array(元素0,元素1,….); // var test=new Array(100,"a",true); 
//创建方式3: 
var arrname = new Array(长度);  
//  初始化数组对象: 
    var cnweek=new Array(7); 
    cnweek[0]="星期日"; 
    cnweek[1]="星期一";  
    cnweek[6]="星期六"; 
```
two demension array
```js
var cnweek=new Array(7); 
for (var i=0;i<=6;i++){ 
    cnweek[i]=new Array(2); 
} 
cnweek[0][0]="星期日"; 
cnweek[0][1]="Sunday"; 
cnweek[1][0]="星期一"; 
cnweek[1][1]="Monday"; 
... 
cnweek[6][0]="星期六"; 
cnweek[6][1]="Saturday"; 
```

#### attr && method
##### join
```js
var arr1=[1, 2, 3, 4, 5, 6, 7]; 
var str1=arr1.join("-"); 
alert(str1);  //结果为"1-2-3-4-5-6-7"  
```
##### concat 
```js
x.concat(value,...)    －－－－  
var a = [1,2,3]; 
var b=a.concat(4,5) ; 
alert(a.toString());  //返回结果为1,2,3             
alert(b.toString());  //返回结果为1,2,3,4,5,相当于+ 
```
##### reverse/sort
array sort并不是按数字大小，而是ascii
```js
var arr1=[32, 12, 111, 444]; 
arr1.sort() // [111, 12, 32, 444]
arr1.reverse //[444, 32, 12, 111]
```
sort(func)中可以传入一个函数来决定排序规则
```js
function intSort(a,b){ 
    if (a>b){ 
        return 1;//-1 
    } 
    else if(a<b){ 
        return -1;//1 
    } 
    else { 
        return 0 
    } 
} 

arr.sort(intSort); 
alert(arr); 
```
##### slice /splice
x.slice(start, end) 
start表示开始位置索引 end是结束位置下一数组元素索引编号 
//第一个数组元素索引为0 
//start、end可为负数，-1代表最后一个数组元素 
//end省略则相当于从start位置截取以后所有数组元素

x. splice(start, deleteCount, value, ...) 
splice的主要用途是对数组指定位置进行删除和插入 start表示开始位置索引 deleteCount删除数组元素的个数 value表示在删除位置插入的数组元素 value参数可以省略  

##### push/pop
数组的push和pop： 
push pop这两个方法模拟的是一个栈操作 x.push(value, ...)  压栈 x.pop()弹栈       
value可以为字符串、数字、数组等任何值 push是将value值添加到数组x的结尾 pop是将数组x的最后一个元素删除 

##### shift/unshift
x.unshift(value,...) x.shift() 
value可以为字符串、数字、数组等任何值 unshift是将value值插入到数组x的开始位置 shift是将数组x的第一个元素删除

### Date
#### create
```js
//方法1：不指定参数 
var nowd1=new Date(); 
alert(nowd1.toLocaleString( )); 

//方法2：参数为日期字符串 
var nowd2=new Date("2004/3/20 11:12"); 
alert(nowd2.toLocaleString( )); 
var nowd3=new Date("04/03/20 11:12"); 
alert(nowd3.toLocaleString( )); 

//方法3：参数为毫秒数 
var nowd3=new Date(5000); 
alert(nowd3.toLocaleString( )); 
alert(nowd3.toUTCString()); 

//方法4：参数为年月日小时分钟秒毫秒 
var nowd4=new Date(2004,2,20,11,12,0,300); 
alert(nowd4.toLocaleString( ));//毫秒并不直接显示 
```
#### method
getDate()                 获取日 
getDay ()                 获取星期 
getMonth ()               获取月（0-11） 
getFullYear ()            获取完整年份 
getYear ()                获取年 
getHours ()               获取小时 
getMinutes ()             获取分钟 
getSeconds ()             获取秒 
getMilliseconds ()        获取毫秒 
getTime ()                返回累计毫秒数(从1970/1/1午夜)

example
```js
function getCurrentDate(){ 
        //1. 创建Date对象 
        var date = new Date(); //没有填入任何参数那么就是当前时间 
        //2. 获得当前年份 
        var year = date.getFullYear(); 
        //3. 获得当前月份 js中月份是从0到11. 
        var month = date.getMonth()+1; 
        //4. 获得当前日 
        var day = date.getDate(); 
        //5. 获得当前小时 
        var hour = date.getHours(); 
        //6. 获得当前分钟 
        var min = date.getMinutes(); 
        //7. 获得当前秒 
        var sec = date.getSeconds(); 
        //8. 获得当前星期 
        var week = date.getDay(); //没有getWeek 
        // 2014年06月18日 15:40:30 星期三 
        return year+"年"+changeNum(month)+"月"+day+"日 "+hour+":"+min+":"+sec+" "+parseWeek(week); 
    } 
//解决 自动补齐成两位数字的方法 
    function changeNum(num){ 
    if(num < 10){ 
        return "0"+num; 
    }else{ 
        return num; 
    } 

} 
//将数字 0~6 转换成 星期日到星期六 
    function parseWeek(week){ 
    var arr = ["星期日","星期一","星期二","星期三","星期四","星期五","星期六"]; 
    //             0      1      2      3 ............. 
    return arr[week]; 
} 

 alert(getCurrentDate()); 
```
#### set 
设置日期和时间 
setDate(day_of_month)       设置日 
setMonth (month)                 设置月 
setFullYear (year)               设置年 
setHours (hour)         设置小时 
setMinutes (minute)     设置分钟 
setSeconds (second)     设置秒 
setMillliseconds (ms)       设置毫秒(0-999) 
setTime (allms)     设置累计毫秒(从1970/1/1午夜)

#### transfer
日期和时间的转换: 
getTimezoneOffset():8个时区×15度×4分/度=480; 
返回本地时间与GMT的时间差，以分钟为单位 
toUTCString() 
返回国际标准时间字符串 
toLocalString() 
返回本地格式时间字符串 
Date.parse(x) 
返回累计毫秒数(从1970/1/1午夜到本地时间) 
Date.UTC(x) 
返回累计毫秒数(从1970/1/1午夜到国际时间) 

### Math
Math对象的方法在使用时需要带上Math.方法名 

abs(x)    返回数的绝对值。 
exp(x)    返回 e 的指数。 
floor(x)  对数进行下舍入。 
log(x)    返回数的自然对数（底为e）。 
max(x,y)    返回 x 和 y 中的最高值。 
min(x,y)    返回 x 和 y 中的最低值。 
pow(x,y)    返回 x 的 y 次幂。 
random()    返回 0 ~ 1 之间的随机数。 
round(x)    把数四舍五入为最接近的整数。 
sin(x)    返回数的正弦。 
sqrt(x)    返回数的平方根。 
tan(x)    返回角的正切。 

### Function
#### define
```js
function 函数名 (参数){  
    //函数体; 
    return 返回值; 
} 

var 函数名 = new Function("参数1","参数n","function_body"); 
// 虽然由于字符串的关系，第二种形式写起来有些困难，但有助于理解函数只不过是一种引用类型，它们的行为与用 Function 类明确创建的函数行为是相同的
```
注意：js的函数加载执行与python不同，它是整体加载完才会执行，所以执行函数放在函数声明上面或下面都可以：即当函数的调用在函数声明前时并不会报错

#### attr
##### length
ECMAScript 定义的属性 length 声明了函数期望的参数个数。 alert(func1.length) 

##### arguments
```js
function add(a,b){ 

        console.log(a+b);//3 
        console.log(arguments.length);//2 
        console.log(arguments);//[1,2] 

} 
    add(1,2) 

arguments指参数 

------------------arguments的用处1 ------------------ 
    function nxAdd(){ 
        var result=0; 
        for (var num in arguments){ 
            result+=arguments[num] 
        } 
        alert(result) 

} 

nxAdd(1,2,3,4,5) 

//     ------------------arguments的用处2 ------------------ 

function f(a,b,c){ 
        if (arguments.length!=3){ 
            throw new Error("function f called with "+arguments.length+" arguments,but it just need 3 arguments") 
        } 
        else { 
            alert("success!") 
        } 
    } 

f(1,2,3,4,5) 
```
##### anonymous function
```js
   var func = function(arg){ 
        return "tony"; 
    } 

// 匿名函数的应用 
    (function(){ 
        alert("tony"); 
    } )() 

(function(arg){ 
        console.log(arg); 
    })('123') 
```
BOM

DOM