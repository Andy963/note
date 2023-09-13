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

##### length

 返回字符串长度
```js
console.log(name.length);
```
##### indexOf()

indexof方法返回字符串中指定文本首次出现的索引（位置

```js
let names = 'zhou wu zheng '
console.log(names.indexOf('z'));
console.log(names.lastIndexOf('z'));

```

当未找到指定文本时，两者均返回-1
通常我们判断字符串中是否有某个字符会通过索引是否为-1,但其实，我们也可以通`includes`

```js
let name = 'zhou abc'
console.log(name.includes('zh'))
// true
```

##### search() 

search方法搜索特定值的字符串，并返回匹配的位置

```js
let names = 'zhou wu zheng '
console.log(names.search('u')); // 3
```

search 可以使用正则

```js
let name = 'zhou abc '
reg = new RegExp('ab')
reg.test(name)
//true
```

##### slice

```js
var str = "Apple, Banana, Mango";
var res = str.slice(7,13);
```

如果某个参数为负，则从字符串的结尾开始计数。
如果省略第二个参数，则该方法将裁剪字符串的剩余部分

##### substring
substring方法与slice 类似，但它不能接受负数作为索引


##### substr() depricate
substr与slice 类似，但第二个参数规定提取字符串的长度
```js
let names = 'zhou wu zheng '
console.log(names.substr(3,4));
//u wu 
```
当忽略第二个参数时，会取第一个参数位置之后所有的字符
当第一个参数 为负，则从结尾开始取

##### replace
```js
str = "Please visit Microsoft!";
var n = str.replace("Microsoft", "W3School");
```
默认情况下，replace 只替换第一个匹配的，且默认情况区分大小写
使用正则的i，使其对大小写不敏感
```js
str = "Please visit Microsoft!";
var n = str.replace(/MICROSOFT/i, "W3School");
```
使用正则的g,使其替换所有
```js
str = "Please visit Microsoft and Microsoft!";
var n = str.replace(/Microsoft/g, "W3School");
console.log(n);
//Please visit W3School and W3School!
```

##### toUpperCase()/toLowerCase()

```js
var text1 = "Hello World!";       // 字符串
var text2 = text1.toUpperCase();  // text2 是被转换为大写的 text1
var text1 = "Hello World!";       // 字符串
var text2 = text1.toLowerCase();  // text2 是被转换为小写的 text1
```
##### concat()

连接两个或者多个字符串
```js
var text1 = "Hello";
var text2 = "World";
text3 = text1.concat(" ",text2);
```
##### String.trim()

去掉两边的空格

```js
var str = "       Hello World!        ";
console.log(str.trim());
```

##### charAt()

返回字符串中指定下标（位置）的字符串
```js
var str = "HELLO WORLD";
str.charAt(0);            // 返回 H
```
##### charCodeAt()

返回字符串中指定索引的字符 unicode 编码
```js
var str = "HELLO WORLD";
str.charCodeAt(0);         // 返回 72
```
##### Property Access

属性访问
```js
var str = "HELLO WORLD";
str[0];                   // 返回 H
```

它让字符串看起来像是数组（其实并不是）
如果找不到字符，[ ] 返回 undefined，而 charAt() 返回空字符串。
它是只读的。<u>**str[0] = "A" 不会产生错误（但也不会工作！）**</u>

##### split

将字符串转换成数组

```js
var txt = "a,b,c,d,e";   // 字符串
console.log(txt.split(","));          // 用逗号分隔
console.log(txt.split(" "));          // 用空格分隔
console.log(txt.split("|"));          // 用竖线分隔

[ 'a', 'b', 'c', 'd', 'e' ]
[ 'a,b,c,d,e' ]
[ 'a,b,c,d,e' ]
```

当用于分割的字符不存在时，则将字符串作为整体放在数组中。这与省略分割符相同，这与python语言中不同，python中默认使用空格
当分割符为“”时，返回是间隔单个字符的数组

```js
var txt = "a,b,c,d,e";   // 字符串
console.log(txt.split(""));          // 用逗号分隔
[
  'a', ',', 'b',
  ',', 'c', ',',
  'd', ',', 'e'
]
```

##### string2Number

there is a trick that we can convert a string num to real number: `"90" -0` it will convert `"90"` to `90`

```js
let a = parseInt('90')
typeof(a) // number

// 浮点数据则是使用parseFloat
// 与之类似的还有Number

typeof(Number('90')) // number
```

#### format
字符串格式化通常有两种方式，用+，以及ES6中的反引号
```js
var name = 'andy'
var s0 = 'hello ' + name
var s = `Hello ${name}`
console.log(s)
```

### Array
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

attr && method

#### join

```js
var arr1=[1, 2, 3, 4, 5, 6, 7]; 
var str1=arr1.join("-"); 
alert(str1);  //结果为"1-2-3-4-5-6-7"  
```

#### concat 

```js
x.concat(value,...)    －－－－  
var a = [1,2,3]; 
var b=a.concat(4,5) ; 
alert(a.toString());  //返回结果为1,2,3             
alert(b.toString());  //返回结果为1,2,3,4,5,相当于+ 
```

#### copyWithin

copyWithin(targetIndex, startIndex,endIndex )

```js

const fruits = ["Banana", "Orange", "Apple", "Mango", "Kiwi"];
fruits.copyWithin(2, 0, 2);
// 结果：["Banana", "Orange", "Banana", "Orange", "Kiwi"]


const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.copyWithin(2, 0);
// 结果：["Banana", "Orange", "Banana", "Orange"]

let evenNumbers= [2,4,6,8];
evenNumbers.copyWithin(-1);
// 结果：[2, 4, 6, 2]
```

它的一种应用场景是原地修改数组的元素

#### entries
返回数组的可迭代对象,该对象包含数组中每个索引的键值对

```js
const arr = ['a', 'b', 'c'];

const iterator = arr.entries();

for (let e of iterator) {
  console.log(e);
}

// [0, 'a']
// [1, 'b'] 
// [2, 'c']

```

entries()方法的常见应用场景包括:

1. 遍历数组时获取每个元素的索引。
2. 将数组转化为Map。例如:

```js
const map = new Map(arr.entries()); 
```

3. 遍历对象属性时获取键名。例如:

```js
const obj = { foo: 'bar' }; 

for (let [key, value] of Object.entries(obj)) {
  console.log(key, value);
}

// 'foo' 'bar'
```

entries与python中的enumerate[[004_函数与类#enumerate]]有相似之处，也有不同之处。
entries在获取迭代器时会立即计算所有值，且不接受任何参数，无法指定起始索引值。

#### every

用于数组中的所有元素是否都满足某个测试函数

```js
const numbers = [12, 25, 18, 130, 44];
const isAllNumbersGreaterThan10 = numbers.every(num => num > 10);
console.log(isAllNumbersGreaterThan10); // 输出：true
```

常见使用场景：
- 检查数组所有元素是否都满足某个条件
- 判断数组是具有某个统一的格式或者结构

python中有类似的all() [[004_函数与类#all]]方法，两者都可以判断可迭代对象的所有元素是否都计算为True
但 every 仅可用于数组，但all可用于任意可迭代对象，every,all 都会找到第一个false就短路返回，

#### fill

```js
const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.fill("Kiwi");
// 结果：["Kiwi", "Kiwi", "Kiwi", "Kiwi"]

arr = new Array(8).fill(false)
//arr [false, false, false,false, false, false,false, false ]

const fruits = ["Banana", "Orange", "Apple", "Mango"];
fruits.fill("Kiwi", 2, 4);
// 结果：["Banana", "Orange", "Kiwi", "Kiwi"]

```

#### filter

```js
let arr = [56, 15, 48, 3, 7];
let newArr = arr.filter(function (value, index, array) {
    return value % 2 === 0;
});
console.log(newArr)

// 去除空值
let  newrr = ['','',1,2,3]
var newArr = newrr.filter(item => item)
console.log(newArr)
//[1,2,3]  因为'' 被认为为false 的值
```

#### find

find 返回符合传入函数条件的第一个数组元素

```js
arr = [1, 2, 3, 4, 5]
let result = arr.find(item => item > 3);
console.log(result);  // 输出：4
```

注意它是只返回符合条件的第一个元素，而filter会返回所有元素

#### findIndex
返回符合传入数组条件的数组第一个元素的索引，如果没有返回-1

#### forEach

数组中每个元素都执行一次回调函数, 函数有三个参数

```js
array.forEach(callbackFn(currentValue, index, arr), thisValue)
- currentValue - 数组中当前被处理的元素
- index - 当前元素的索引
- arr - 数组本身
```

通常情况下，只会用到第一个参数：

```js
const numbers = [1, 2, 3, 4];

let sum = 0;
numbers.forEach(function(n) {
  sum += n; 
});

console.log(sum); // 10
```

#### from

from 从一个类数组或可迭代对象创建一个新的浅拷贝的数组实例 `Array.from(arrayLike, mapFn, thisArg)` 
- arrayLike - 想要转换成数组的类数组对象或可迭代对象。
- mapFn - 可选,新数组中的每个元素会执行该回调函数。
- thisArg - 可选,执行回调函数 mapFn 时 this 对象。

```js
var myArr = Array.from('RUNOOB');
console.log(myArr);  // 输出：[ 'R', 'U', 'N', 'O', 'O', 'B' ]

var arr = Array.from([1, 2, 3], x => x * 10);
console.log(arr);  // 输出：[10, 20, 30]

```

#### includes

判断一个数组是否包含一个指定的值，如果是返回true,否则 返回false

```js
[1, 2, 3].includes(2); // 返回 true
[1, 2, 3].includes(4); // 返回 false
```

#### indexOf

搜索数组中元素，返回它所在的位置。它与findIndex的区别是： indexOf 用于查找 数组中特定的元素，而findIndex则接收一个函数作为参数。但如果不存在的元素，两者都会返回-1

```js
let arr = [1, 2, 3, 4, 5];
console.log(arr.indexOf(3));  // 输出：2

```

#### isArray

isarray用于确定传递的数值是否是一个数组，它不检查原型链，也不依赖于它所附加的构造函数，对于使用数组字面量语法或者Array构造函数创建的值，它都返回true

```js
console.log(Array.isArray([1, 2, 3]));  // 输出：true
console.log(Array.isArray('Runoob'));  // 输出：false
```

下面内容来自claude2 未验证

```js
- instanceof 可以判断对象的类型,但可能由于多窗口而失败
- Array.isArray() 只检测数组,但不会失败

所以 Array.isArray() 是更可靠地判断数组的方法。

注意,它在存在 iframes 的情况下也可以正常工作,而 instanceof 会失败。

例如:


let iframe = document.createElement('iframe');
document.body.appendChild(iframe);
let iArray = window.frames[window.frames.length-1].Array;

let arr = [1, 2, 3]; 

// 在 iframe 中创建的数组
console.log(arr instanceof iArray); // false  

// 正确的方法  
console.log(Array.isArray(arr)); // true
```

主要用于数据类型检查，避免出现错误。

#### join

Array.join(sep)

```js
let fruits = ['apple', 'banana', 'cherry'];
let result = fruits.join(); // 默认使用逗号作为分隔符
console.log(result); // 输出 "apple,banana,cherry"
```

功能上它与Python中字符串的join[[002_数据运算与类型#join]]是一样的，但区别是python中是字符串内建方法

#### keys

返回数组每个索引的迭代对象

```js
let fruits = ['apple', 'banana', 'cherry'];
let keys = fruits.keys();

for (let key of keys) {
  console.log(key); // 输出 "0", "1", "2"
}
```

它与[[002_Object#entries]] 的不同之处在于，它只返回索引，而entries会返回索引和值

#### lastIndexOf

它用于从数组的末尾开始向前查找指定元素，并返回它的索引。如果没有找到元素，则返回-1

` array.lastIndexOf(item, start) `  `item`是必需的，指定要搜索的元素。`start`是可选的，指定从哪个位置开始搜索

```js
let fruits = ['apple', 'banana', 'cherry', 'apple', 'banana'];
let index = fruits.lastIndexOf('apple'); 
console.log(index); // 输出 "3"
```

lastIndexOf 类似python中字符串的 rindex方法[[002_数据运算与类型#rindex]]

#### map

`map()`方法是数组的一个内置方法，它创建一个新数组，其结果是该数组中的每个元素都调用一个提供的函数后返回的结果 `array.map(function(currentValue, index, arr), thisValue)
`
```js
let numbers = [1, 2, 3, 4];
let squares = numbers.map(x => x * x);
console.log(squares); // 输出 "[1, 4, 9, 16]"
```

它与forEach的不同在于：forEach不会返回一个新的数组,而python中map[[004_函数与类#map]] 是 一个内建函数
#### reverse/sort

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

#### slice /splice
x.slice(start, end) 
start表示开始位置索引 end是结束位置下一数组元素索引编号 
//第一个数组元素索引为0 
//start、end可为负数，-1代表最后一个数组元素 
//end省略则相当于从start位置截取以后所有数组元素

```js
let fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry'];
let someFruits = fruits.slice(1, 3);
console.log(someFruits); // 输出 ["banana", "cherry"]
```

x. splice(start, deleteCount, value, ...) 
splice的主要用途是对数组指定位置进行删除和插入 start表示开始位置索引 deleteCount删除数组元素的个数 value表示在删除位置插入的数组元素 value参数可以省略  

```js
a = ['a','b','c']
(3) ['a', 'b', 'c']
a.splice(1,0,'d') // 从索引为1的位置开始删除，删除0个，并用'd'来替换
[]
a 
(4) ['a', 'd', 'b', 'c']
// 第三个元素是要添加的元素
```

#### push/pop
数组的push和pop： 
push pop这两个方法模拟的是一个栈操作 x.push(value, ...)  压栈 x.pop()弹栈       
value可以为字符串、数字、数组等任何值 push是将value值添加到数组x的结尾 pop是将数组x的最后一个元素删除 

push 返回新数组的长度， pop返回删除的那个元素

```js
let fruits = ['apple', 'banana'];
let newLength = fruits.push('cherry');
console.log(fruits); // 输出 ["apple", "banana", "cherry"]
console.log(newLength); // 输出 3

let fruits = ['apple', 'banana', 'cherry'];
let lastFruit = fruits.pop();
console.log(fruits); // 输出 ["apple", "banana"]
console.log(lastFruit); // 输出 "cherry"
```

#### shift/unshift
x.unshift(value,...) x.shift() 
value可以为字符串、数字、数组等任何值 unshift是将value值插入到数组x的开始位置 shift是将数组x的第一个元素删除

unshift 会返回新数组的长度， shift 删除数组的第一个元素

```js
let fruits = ['banana', 'cherry'];
let newLength = fruits.unshift('apple');
console.log(fruits); // 输出 ["apple", "banana", "cherry"]
console.log(newLength); // 输出 3

let fruits = ['apple', 'banana', 'cherry'];
let firstFruit = fruits.shift();
console.log(fruits); // 输出 ["banana", "cherry"]
console.log(firstFruit); // 输出 "apple"
```

#### reduce


```js
let numbers = [1, 2, 3, 4];
let sum = numbers.reduce((total, num) => total + num, 0);
console.log(sum); // 输出 "10"
```

#### reduceRight

`reduceRight()`方法与`reduce()`方法类似，但它是从数组的末尾开始向前应用函数，而不是从开始处

#### some

查看是否有满足条件的元素，是则返回true, 否则 返回false

```js
array.some(function(currentValue, index, arr), thisValue)
let numbers = [1, 2, 3, 4];
let hasNegativeNumbers = numbers.some(num => num < 0);
console.log(hasNegativeNumbers); // 输出 "false"

```
#### toString

将数组转化成字符串,注意，它把逗号也带上了

```js
let fruits = ['apple', 'banana', 'cherry'];
let str = fruits.toString();
console.log(str); // 输出 "apple,banana,cherry"
```

#### valueOf

获取数组的原始值

```js
let numbers = [1, 2, 3, 4];
let originalValue = numbers.valueOf(); // [1, 2, 3, 4]
let stringValue = numbers.toString(); // "1,2,3,4"
let sum = numbers.reduce((total, num) => total + num, 0); // 10
```

#### Array 解构

```js
let [a,b,c] = ['1',2,3] // 声明同时解构
;[d,c,e,f=10] = [1,3,5] // 前边加";"告诉后面是一个独立的句子，并且f设置了默认值
【g,h,i=i] = [1,2] // i如有有赋新值，则使用新值，如果没有赋值则使用原来的值。
```
#### 合并两个数组并同时去重
经常会有这种需求，比如在页面进行勾选时，有时需要与已经勾选的列表进行合并（某些情况下勾选一个会添加多个子项），此时就存在合并的情况，以前我都是通过循环，判断的方式
在ES6中可以使用下面的方法进行：

```js
a = [1,2,3]
b = [2,3,4]
d = Array.from(new Set([...a,...b]))
(4) [1, 2, 3, 4]
```

其实就是通过set去重，然后将set转成array




### Obj

```js
let obj = {'name':'andy', 'age':18}

let {addresss} = obj // 没有的属性，返回undefined
let {name:a, age:b address:d='花果山'} = obj // 给name 取别名，这样可以通过a访问name, 而address则既有别名，又有默认值

```

#### Obj has key

```js
// in 操作符会查找整个原型链, 如果只想看是否对象本身包含，就使用hasOwnPorperty
const myObj = { key: 'value' };
if ('key' in myObj) {
  console.log('key exists in myObj');
}

// 查看本身是否包含某个属性
const myObj = { key: 'value' };
if (myObj.hasOwnProperty('key')) {
  console.log('key exists in myObj');
}

// 查看某个对象的属性列表使用keys
const myObj = { key: 'value' };
if (Object.keys(myObj).includes('key')) {
  console.log('key exists in myObj');
}



```
### Obj copy

obj copy 属于浅复制

```js
const obj = {'name':'andy',age:18}

const obj2 = Object.assign({}, obj)

const obj3 = {}
Object.assign(obj3, obj)

// Object.assign 将第二个参数的属性复制到第一个参数中
// 如果{}已经有属性，如果新的属性也有则会覆盖，如果新属性中没有，则保持不变
const obj4={}
obj4 = {...obj3}
```

### Map

Obj 的键只能是字符串或者符号symbol，如果传入一个对象,js会自动将它转为字符
Map任何类型的对象都可以是数据的key

```js
const mp = new Map();
const obj = {'age':18};
// 设置
mp.set('name', 'Andy');
mp.set(obj, 'age')
mp.set(NaN, 'hello')
// 取
mp.get('name');
mp.get(obj) // 这里取必须用obj,不能像obj取对象可以传任意对象如{}
mp.get(NaN)
mp.size // 获取map中键值对的数量

// 删除
mp.delete(NaN)
//是否包含key
mp.has(key) // return ture, false
mp.clear() // 清空

// map 转数组
let arr = Array.from(mp); // [['name':'Andy']]
arr = [...mp] // 这种方式也可以

// 从二维数组构建map
const mp2 = new Map([['name','andy']])

// 遍历 map

for (let entry of mp2){ // let [key, val] of mp2 也可以
	const [key, val] = entry;
	console.log(key, val);
}

mp2.forEach(key, val){ // 如果有第三个参数，那么第三个参数是mp2本身
	console.log(key, val)
}

mp.keys() // 获取所有的key 与python中的dict类似，返回的结果是一个迭代器
mp.values()
```

### set
集合，与数组类似，不同点在于set中不能存重复数据

```js
const set = new Set()

// 添加数据 
set.add(10);

// 是否包含
set.has(10)

// 删除
set.delete(10)

// 遍历 
for(let item of set){
	console.log(item)
}

// 如果想按顺序取，如取第一个，第二个，只能先将其转成数组
let arr =  Array.from(set) // [...set]

// 去重
const arr = [1,3,3,4,2];
const set2 = new Set(arr); 
const arr2 = [...set2] // 转加数组
```

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

arguments是一个类数组对象，但不是数组，无法调用数组的方法如forEach

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

可变参数：

```js

const f = function(...args){
	return args.reduce((a,b) => a+b)
}

const f3 = function(){
	for(let v in arguments){
		console.log(n);
	}
    for(let w of arguments){
      console.log(w);
    }
}
```

可变参数名字可以自己定义
可变参数本身就是一个数组，可直接使用数组方法

#### apply & call

```js
function fn(){
	console.log('函数被调用了');
}
fn.call();
fn.apply();
```

还可以指定函数中的this, call, apply 的第一个参数将成为函数中的 `this`
通过call方法调用函数，函数的实参直接在第一个参数后一个一个列出来
通过apply方法调用函数，函数的实参需要通过一个数组传递

#### bind
bind 返回一个新的函数， 函数中this 由bind第一个参数决定（无法修改）
bind：
	- 为新函数绑定this
	- 为新函数绑定参数

```js
function fn(a,b,c){
	console.log(a,b,c);
}

const obj = {name:"andy"};
const newFn = fn.bind(obj, 10)
// newFn的this永远为obj, 且a参数绑定为10，不需要传，且传的参数也不会分配给a,在python中为partial 偏函数
```

但箭头函数比较特殊，它的this不受apply,call, bind影响，只与外部作用域有关。并且箭头函数中没有arguments

#### anonymous function
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

如果函数的参数或者返回值是函数，则其为高阶函数。 参数是函数意味着可以动态的传递参数

## class

#### 属性

```js

class Person{
	/* 
		 类的代码块默认就是严格模式，是用来设置对象的属性的，不是什么代码都能写的
	*/
	name='p' // Person的实例属性name, 实例属性只能通过实例访问
	static age = 18 // 静态（类）属性，只能通过类本身去访问
}

p = new Person()
p.name = 'andy'
p.age = '18'
```


#### 方法

```js
class Person{
	name='p' // Person的实例属性name, 实例属性只能通过实例访问
	static age = 18 // 静态（类）属性，只能通过类本身去访问
	// sayhello = function(){}  添加方法的一种方式
	sayhello(){
		console.log('hello');
		// 方法内部可以使用this,this代表当前实例
	}
	// 同样有static 方法，需要通过类来调用
	static test(){
		// static方法只能类调用，并且它的this指向类，而非类对象
	}
}

```

#### 构造函数

```js

class Person{
	// 类中可以添加一个特殊的方法constructor
	// 该方法称为构造函数
	constructor(name, age, gender){
		console.log('构造函数', name, age, gender)
		this.name = name
		this.age = age
		this.gender = gender
	}
}

 /* #file_name 将属性变成私有属性，私有属性只能在类内部访问，并且需要先声明*/

class Person{
	#name;
	#age 
	constructor(name, age){
		this.#name = name;
		this.#age = age
	}
	/*暴露接口给外面使用*/
	getName(){
		return this.#name
	}
	setName(name){
		this.#name = name
	}
	/*get, set 新的使用方式*/
	get age(){
		return this.#age;
	}
	set age(age){
		this.#age = age
	}
}
```

#### 继承

```js

class Animal{
	constructor(name){
		this.name = name;
	}
	sayHello(){
		console.log('Animal is speaking');
	}
}

class Dog extends Animal{

}

/* 如果要重写构造方法，则需要使用super()*/ 

class Cat extends Animal{
	constructor(name){
		super(name)
	}
}

// 方法调用父类的方法
super.sayHello()
```

#### 原型对象

对象中存储属性的地方有两个：对象自身，原型对象prototype

```
对象自身： 直接通过对象所添加的属性，位于对象自身中
		   在类中通过 x= y 的形式添加的属性，位于对象自身中 

原型对象： 对象中有一些内容会存储到其他的对象里（原型对象）这个属性叫__proto__
		   原型对象也负责为对象存储属性，当我们访问对象中属性时，会优先访问对象中
		   属性，如果自身中不存在，则会去原型对象中去寻找
		   会添加原型对象的情况：
		    1. 在类中通过 xxx(){}方式添加的方法
		    2. 主动向原型中添加的属性或方法。
```

不要通过类的实例去修改原型：
	- 通过一个对象影响所有同类对象，不合适
	- 修改原型要先创建实例
	- 危险
正确做法：
    通过类的prototype属性，来访问实例的原型，也可以赋值
```js

class Person{
	name = 'Andy'
	age = 19

	sayHello(){
		console.log('hello world');l
	}
}

Person.prototype.fly = () = > {
	console.log('I am flying.');
}
```

instanceof 
hasOwnProperty && in 
```js
console.log('sayHello' in p); // 无论属性是在对象自身还是在原型中，都会返回true
console.log(p.hasOwnPorperty('name')) // 检查对象自身是否有name属性 不推荐

console.log(Object.hasOwn(对象，属性名))
```


## RegExp

let reg = new RegExp("a", 'i')
reg = /a/i, //  /正则/匹配模式

```js
// 反转义
let reg = /\w/
let reg = new RegExp("\\w")

let reg2 = /a/
let res = reg2.test('abc')
```
