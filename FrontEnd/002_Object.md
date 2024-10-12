## object


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
JavaScript 中提供了四种不同的方法来创建 Date 对象

```js
//方法1：不指定参数 
var nowd1=new Date(); 
// Fri Sep 15 2023 13:48:10 GMT+0800 (China Standard Time)
alert(nowd1.toLocaleString( )); 

//方法2：参数为日期字符串 
var nowd2=new Date("2004/3/20 11:12"); 
alert(nowd2.toLocaleString( )); // '3/20/2004, 11:12:00 AM'
nowd2.toLocalDateString() // '3/20/2004'
nowd2.toLocalTimeString() // '11:12:00 AM'
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

#### property

Date中主要包含两个属性：constructor， prototype

##### constructor

返回构造函数

```js
d = new Date()
d.constructor
ƒ Date() { [native code] }
```

##### prototype

通过该属性您可以向对象中添加属性和方法,通过prototype添加的方法可以被所有实例共享

```js
// 定义一个构造函数
function Person(name) {
    this.name = name;
}

// 给Person的原型添加一个方法
Person.prototype.sayHello = function() {
    console.log("Hello, my name is " + this.name);
}

// 创建一个Person的实例
var alice = new Person("Alice");

// 调用原型中的方法
alice.sayHello();  // 输出：Hello, my name is Alice
```

在对象上直接添加方法,它会在所有实例上进行拷贝，从而占用更多内存。

```js
let obj = {};
obj.sayHello = function() {
    console.log("Hello, world!");
};
obj.sayHello();  // 输出："Hello, world!"
```

在构造函数内部添加方法, 这种与直接在对象上添加方法一样，新添加的方法会在所有实例上拷贝。

```js
function Person(name) {
    this.name = name;
    this.sayHello = function() {
        console.log("Hello, my name is " + this.name);
    };
}

let alice = new Person("Alice");
alice.sayHello();  // 输出："Hello, my name is Alice"
```

#### method

```js
function getDate(sep = '-') {
    let today = new Date();
    let y = today.getFullYear();
    let m = today.getMonth() + 1;
    let d = today.getDate();
    if (m >= 1 && m <= 9) {
        m = '0' + m;
    }

    if (d >= 0 && d <= 9) {
        d = '0' + d;
    }

    return `${y}${sep}${m}${sep}${d}`;

}
```

##### getDate()  
获取日 

```js
var date = new Date();
var day = date.getDate();
console.log(day); // 15
```

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
