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

### Math

### Function

BOM

DOM