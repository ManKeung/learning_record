# 基础

## 用法

1. HTML 中的脚本必须位于`<script>` 与`</script>`标签之间。
2. 脚本可被放置在HTML页面的`<body>`和`<head>`部分中。
3. 也可以是单文件引入`<script src="file.js"></script>`

## 输出

JavaScript 可以通过不同的方式来输出数据：
    - 使用 window.alert() 弹出警告框。
    - 使用 document.write() 方法将内容写到 HTML 文档中。
    - 使用 innerHTML 写入到 HTML 元素。
    - 使用 console.log() 写入到浏览器的控制台。

## 语法

+ JavsScript对换行、缩进、空白不明感
+ 每一条语句末尾要加上分号，虽然分号不是必须加的，但是为了程序今后要压缩，如果不加分号，压缩之后将不能运行了
+ 所有符号都是英文的

## 注释

* 单行注释
```js
// 这是注释
```

* 多行注释
```js
/* 这是注释 */
```

## 变量

### 变量命名规则
	1. 变量命名必须以字母或是下标符号”\_”或者”$”为开头
	2. 变量名长度不能超过255个字符
	3. 变量名中不允许使用空格
	4. 不用使用脚本语言中保留的关键字及保留符号作为变量名
	5. 变量名区分大小写。(javascript是区分大小写的语言)
	6. 可读性——能看懂
	7. 规范性——符合规则

### 匈牙利命名法 类型前缀 首字母大写

类型 | 前缀 |	类型 | 示例
---- | ---- | ---- | ----
数组 | a | Array | aItems
布尔值 | b | Boolean | bIsComplete
整数 | i | Integer | iItemCount
浮点型 | f | Float | fPrice
函数 | fn | Function | fnHandler
对象 | o | Object | oDivl
正则表达式 | re | RegExp | reEmailCheck
字符串 | s | String | sUserName
变体变量 | v | Variant | vAnything

> 函数命名 驼峰命名 showDiv(){};

### 变量作用域

- 全局变量
	1. 在最外层声明的变量。
    2. 在函数体内部，但是没有声明var 的变量也是全局变量
- 局部变量
  	1. 在函数体内部的声明变量

## 数据类型

JavaScript 拥有动态类型。这意味着相同的变量可用作不同的类型：

```js
var x;               // x 为 undefined
var x = 5;           // 现在 x 为数字
var x = "John";      // 现在 x 为字符串
```

* 字符串

字符串可以是引号中的任意文本。您可以使用单引号或双引号：

```js
var str = "Hello";
var str = 'World';
```

* 数字

JavaScript 只有一种数字类型。数字可以带小数点，也可以不带：

```js
var num = 34.00;
var num = 34;
var num = 123e5; // 12300000
var num = 123e-5; // 0.00123
```

* 布尔

布尔（逻辑）只能有两个值：true 或 false

```js
var b = true;
var b = false;
```

* 数组

```js
// 1
var arr = new Array();
arr[0] = 'Hello';
arr[1] = 'World';
// 2
var arr = new Array('Hello', 'World');
// 3
var arr = ['Hello', 'World'];
```

* 对象

对象由花括号分隔。在括号内部，对象的属性以名称和值对的形式 (name : value) 来定义。属性由逗号分隔：

```js
var person = {
    name: 'mankeung',
    age: 18,
    phone: 10086
}

name = person.name
name = person['name']
```

* Undefined和Null

Undefined 这个值表示变量不含有值。
可以通过将变量的值设置为 null 来清空变量。

```js
peson = null;
```

* 声明变量名

可以使用关键词 "new" 来声明其类型

```js
var carname=new String;
var x=      new Number;
var y=      new Boolean;
var cars=   new Array;
var person= new Object;
```

## 函数

* 函数入口

```js
window.onload = function() {
    // 逻辑
}
```

* 自定义函数

```js
function fn() {
    console.log('this is fn!');
}
fn(); // 不调用函数，自己不执行
```

* 函数直接变量声明

```js
var fn = function() {
    console.log('this is fn!');
}
fn(); // 也需要调用
```

* 利用Function关键词声明

```js
var fn = new Function('console.log("this is Function")');
fn();
```

* 变量名提升

```js
// 函数体内部，声明变量，会把该声明提升到函数体的最顶端。 只提升变量声明，不赋值。
function fn() {
    console.log(num);
    var num = 20;
}
// 相当于
function fn() {
    var num;
    console.log(num);
    num = 20;
}
```

* 函数参数

```js
function fn(a, b) {
    // arguments是存储了函数传送过过来实参 arguments对象的长度是由实参个数而不是形参个数决定的
    console.log(fn.length); // 得到是 函数的形参的个数
    console.log(arguments.length); // 得到的是实参的个数
    if (fn.length === arguments.length) {
        console.log(a + b);
    } else {
        console.error('Err:参数不对');
    }
}
fn(1, 2);
fn(1, 2, 3);
/* arguments 对象
	+ arguments.length; // 返回的是 实参的个数
	+ arguments.callee; // 返回的是正在执行的函数。也是在函数体内使用。在使用函数递归调用时推荐使用arguments.callee代替函数名本身 */
```

* 回调函数

等函数执行完毕再去执行的函数 回调函数

* 立即执行函数

```js
// 独立的作用域，不会污染全局环境
(function() {
    // 逻辑
})()

// 对于当前作用域中，如果将window传入，就不用依赖全局对象了
(function(window, document) {
    var div = document.getElementById();
})(window, document);

(function aaa() {
    console.log(1111);
})();

var a = function() {
    console.log(2222)
}();

!function() {
    console.log(3333);
}();

+function() {
    console.log(4444);
}();
// 小括号
// 赋值操作
// 逻辑运算符
// 数字运算符
```

## 事件

事件三要素

1. 事件源 --> 触发者
2. 事件 --> 动作
3. 事件处理程序 --> = function(){}

> 事件源.事件 = function(){  事件处理函数 }

常用事件

事件 | 描述
--- | ---
onchange | HTML元素改变
onclick | 用户点击HTML元素
onmouseover | 用户在HTML元素上移动鼠标
onmouseout | 用户从一个HTML元素移开鼠标
onkeydown | 用户按下键盘按键
onload | 浏览器已加载完也页面

> [更多事件](https://www.runoob.com/jsref/dom-obj-event.html)

## 字符串

* 特殊字符

反斜杠是一个转义字符。 转义字符将特殊字符转换为字符串字符：

代码 | 输出
--- | ---
\' | 单引号
\" | 双引号
\\ | 反斜杠
\n | 换行
\r | 回车
\t | tab(制表符)
\b | 退格符
\f | 换页符

* 转化为字符串

```js
// 1 + ''
var a = 2 +'';
console.log(a, typeof a); // 2 string
// 2 String()
var num = 123;
console.log(typeof String(num), String(num));
// 3 toSting(基数)　基数就是进制 默认十进制
console.log(typeof num.toString(10), num.toString(10));
```

* 字符串属性
    1. 返回创建字符串属性的函数
    ```js
    var str = 'hello world';
    console.log(str.constructor)
    ```
    2. 返回字符串长度
    ```js
    var str = 'hello world';
    console.log(str.length)
    ```
    3. prototype允许您向对象添加属性和方法

* 返回指定索引位置的字符串

```js
var str = 'hello world';
console.log(str.charAt(0));
```

* 返回指定索引位置的字符串Unicode值

```js
var str = 'hello world';
console.log(str.charCodeAt(0));
```

* 连接两个或多个字符串

```js
var h = 'hello';
var w = 'world';
console.log(h.concat(w)); // helloworld
console.log(h.concat(' ', w)); // hello world
```

* 将Unicode转化为字符串

```js
console.log(String.fromCharCode(65)); // A
```

* 返回字符串中检查指定字符第一次出现的位置

```js
var str = 'hello world';
console.log(str.indexOf('l')); // 2
```

* 返回字符串中检查指定字符最后一次出现的位置

```js
var str = 'hello world';
console.log(str.lastIndexOf('l')); // 9
```

* 用本地特定的顺序来比较两个字符串

```js
var arr = [
    {brandName:'Andrew Marc',brandId:4},
    {brandName:'Armani Jeans',brandId:1},
    {brandName:'Ai Riders On The Storm',brandId:12},
    {brandName:'Armani Collezioni',brandId:20}
]
function fn(a,b){
    return a.brandName.localeCompare(b.brandName)
}
console.log(arr.sort(fn))
/* [
  { brandName: 'Ai Riders On The Storm', brandId: 12 },
  { brandName: 'Andrew Marc', brandId: 4 },
  { brandName: 'Armani Collezioni', brandId: 20 },
  { brandName: 'Armani Jeans', brandId: 1 }
] */
```

* 找到一个或多个正则表达式的匹配

```js
var str = 'The rain in SPAIN stays mainly in the plain';
var n = str.match(/ain/g);
console.log(n);
```

* 替换与正则表达式匹配的子串

```js
var str = 'The rain in SPAIN stays mainly in the plain';
var n = str.replace(/ain/g, '哈哈');
console.log(n);
```

* 检索与正则表达式相匹配的值

```js
var str = 'The rain in SPAIN stays mainly in the plain';
var n = str.search(/ain/g);
console.log(n);
```

* 提取字符串的片断，并在新的字符串中返回被提取的部分

```js
var str = 'Hello world!';
var n = str.slice(1,5); // (start, end)
console.log(n)
```

* 把字符串分割为子字符串数组

```js
var str = 'hello world';
var n = str.split(' ');
console.log(n)
```

* 从起始索引号提取字符串中指定数目的字符

```js
var str = 'Hello world!';
var n = str.substr(2,3); // (start, length) // 第二个参数不传　默认从起始位置取到最后
console.log(n);
```

* 提取字符串中两个指定的索引号之间的字符

```js
var str = 'hello world!';
console.log(str.substring(3)) // lo world!
console.log(str.substring(3, 7)) // lo w
```

* 根据本地主机的语言环境把字符串转换为小写

```js
var str = 'Runoob';
var res = str.toLocaleLowerCase();
console.log(res)
```

* 根据本地主机的语言环境把字符串转换为大写

```js
var str = 'Runoob';
var res = str.toLocaleUpperCase();
console.log(res)
```

* 把字符串转换为小写

```js
var str = 'Runoob';
var res = str.toLowerCase();
console.log(res)
```

* 把字符串转换为大写

```js
var str = 'Runoob';
var res = str.toUpperCase();
console.log(res)
```

* 返回字符串对象

```js
var str = 'Runoob';
var res = str.toString();
console.log(res)
```

* 去除字符串中的头尾空格

```js
var str = '       Runoob        ';
console.log(str.trim());
```

* 返回某个字符串对象的原始值

```js
var str = 'hello world';
console.log(str.valueOf());
```

* 网址编码

```js
var url = "http://www.itcast.cn?name=andy";
console.log(encodeURIComponent(url));  // 编码
var afterUrl = encodeURIComponent(url);
console.log(decodeURIComponent(afterUrl)); // 解码
```

## 运算符

* 算术运算符

y=5

运算符 | 描述　| 例子 | x运算结果 | y运算结果
--- | --- | --- | --- | ---
+ | 加法　| x=y+2 | 7 | 5
- | 减法 | x=y-2 | 3 | 5
* | 乘法 | x=y*2 | 10 | 5
/ | 除法 | x=y/2 | 2.5 | 5
% | 取模(取余) | x=y%2 | 1 | 5
++ | 前自增 | x=++y | 6 | 6
++ | 后自增 | x=y++ | 5 | 6
-- | 前自减 | x=--y | 4 | 4
-- | 后自减 | x=y-- | 5 | 4

* 赋值运算符

x=10,y=5

运算符 | 例子 | 等同于 | 运算结果
--- | --- | --- | ---
= | x=y | | x=51
+= | x+=y | x=x+y | x=15
-= | x-=y | x=x-y | x=5
*= | x*=y | x=x*y | x=50
/= | x/=y | x=x/y | x=2
%= | x%=y | x=x%y | x=0

* 逻辑操作符

符号 | ! | && | &#124;&#124;
---- | ---- | ---- | ----
描述 | 非 | 与 | 或

* 关系操作符

符号 | > | < | >= | <= | == | === | != | !==
---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ----
描述 | 大于 | 小于 | 大于等于 | 小于等于 | 等于 | 全等 | 不等 | 不全等

* 条件操作符

符号 | ?:
---- | ----
描述 | 三目运算符 相当于 if(){} else {};

运算符顺序
```
1  ()
2  !、-、++、--    (-10)  负号  正号
3 *、/、%
4 +、-         10-5
5 <、<=、<、>=
6 ==、!=、===、!==、
7 &&
8 ||
9?:
10 =、+=、-=、*=、/=、%=     赋值
```

## 流程控制

* 判断: if / switch / ?:
    + if
    ```js
    if(条件) { // 条件真就执行 假就执行 else里的语句

    } else {

    }
    // 可以多层嵌套
    if () {} if else()...else {}
    ```
    + switch
    ```js
    switch(变量) {
        case 值1:
            ...
            break;
        case 值2:
            ...
            break;
        default:
            不匹配默认执行;
    }
    ```
    + ?:三目运算符
    ```js
    条件 ? 真 执行 : 假 执行;
    ```

* 循环: while / for
    + while
    ```js
    // 1.
    while(条件)　{
        // 条件真执行
    }
    // 2.
    do {
        // do 里面不管真假 都执行 条件假 执行一次 条件真 继续执行do
    } while(条件);
    ```
    + for
    ```js
    for(初始值;条件;递增) {
        语句;
    }
    // 初始值-->条件真-->执行语句-->递增-->条件真-->执行语句-->...直到递增值不满足条件就不执行
    // 注意：初始值只执行一次
    ```

> 跳出：break、continue
>> break 跳出循环
>> continue 跳出当次循环 继续下次循环

## typeof

typeof 操作符来检测变量的数据类型

```js
typeof 'John'                // 返回 string
typeof 3.14                  // 返回 number
typeof false                 // 返回 boolean
typeof [1,2,3,4]             // 返回 object
typeof {name:'John', age:34} // 返回 object
```

* null

在 JavaScript 中 null 表示 "什么都没有"。
null是一个只有一个值的特殊类型。表示一个空对象引用。
你可以设置为 null 来清空对象

* undefined

在 JavaScript 中, undefined 是一个没有设置值的变量。
typeof 一个没有值的变量会返回 undefined。

* undefined 和 null 的区别

null 和 undefined 的值相等，但类型不等：

```js
typeof undefined             // undefined
typeof null                  // object
null === undefined           // false
null == undefined            // true
```

## 类型转换

* 5种不同的数据类型：
    1. string
    2. number
    3. boolean
    4. object
    5. function

* 3种对象类型：
    1. Object
    2. Date
    3. Array

* 2个不包含任何值的数据类型：
    1. null
    2. undefined

*  typeof 操作符来查看 JavaScript 变量的数据类型

```js
typeof "John"                 // 返回 string
typeof 3.14                   // 返回 number
typeof NaN                    // 返回 number
typeof false                  // 返回 boolean
typeof [1,2,3,4]              // 返回 object
typeof {name:'John', age:34}  // 返回 object
typeof new Date()             // 返回 object
typeof function () {}         // 返回 function
typeof myCar                  // 返回 undefined (如果 myCar 没有声明)
typeof null                   // 返回 object
```

* constructor 属性返回所有 JavaScript 变量的构造函数

```js
"John".constructor                 // 返回函数 String()  { [native code] }
(3.14).constructor                 // 返回函数 Number()  { [native code] }
false.constructor                  // 返回函数 Boolean() { [native code] }
[1,2,3,4].constructor              // 返回函数 Array()   { [native code] }
{name:'John', age:34}.constructor  // 返回函数 Object()  { [native code] }
new Date().constructor             // 返回函数 Date()    { [native code] }
function () {}.constructor         // 返回函数 Function(){ [native code] }
```

### 数字化为字符串

全局方法String()
该方法可用于任何类型的数字，字母，变量，表达式

```js
String(x)         // 将变量 x 转换为字符串并返回
String(123)       // 将数字 123 转换为字符串并返回
String(100 + 23)  // 将数字表达式转换为字符串并返回
```

Number 方法 toString() 也是有同样的效果

```js
x.toString()
(123).toString()
(100 + 23).toString()
```

方法 | 描述
--- | ---
toExponential()	| 把对象的值转换为指数计数法。
toFixed() | 把数字转换为字符串，结果的小数点后有指定位数的数字。
toPrecision() | 把数字格式化为指定的长度。

### 将布尔值转换为字符串

```js
String(false)        // 返回 "false"
String(true)         // 返回 "true"
false.toString()     // 返回 "false"
true.toString()      // 返回 "true"
```

### 将日期转换为字符串

```js
String(new Date())
obj = new Date()
obj.toString()
```

### 将字符串转换为数字

```js
Number("3.14")    // 返回 3.14
Number(" ")       // 返回 0
Number("")        // 返回 0
Number("99 88")   // 返回 NaN
```

方法 | 描述
--- | ---
parseFloat() | 解析一个字符串，并返回一个浮点数。
parseInt() | 解析一个字符串，并返回一个整数。

### 将布尔值转换为数字

```js
Number(false)     // 返回 0
Number(true)      // 返回 1
```

### 将日期转换为数字

```js
d = new Date();
Number(d);
d = new Date();
d.getTime();
```

### 自动转换类型

当 JavaScript 尝试操作一个 "错误" 的数据类型时，会自动转换为 "正确" 的数据类型

```js
5 + null    // 返回 5         null 转换为 0
"5" + null  // 返回"5null"   null 转换为 "null"
"5" + 1     // 返回 "51"      1 转换为 "1" 
"5" - 1     // 返回 4         "5" 转换为 5
```

### 自动转换为字符串

```js
document.getElementById("demo").innerHTML = myVar;

myVar = {name:"Fjohn"}  // toString 转换为 "[object Object]"
myVar = [1,2,3,4]       // toString 转换为 "1,2,3,4"
myVar = new Date()      // toString 转换为 "Fri Jul 18 2014 09:08:55 GMT+0200"
```

### 使用不同的数值转换为数字(Number), 字符串(String), 布尔值(Boolean)

原始值 | 转换为数字 | 转换为字符串 | 转换为布尔值
--- | --- | --- | ---
false | 0 | "false" | false
true | 1 | "true" | true
0 | 0 | "0"	| false
1 | 1 | "1" | true
"0" | 0 | "0" | true
"000" | 0 | "000" | true
"1" | 1 | "1" | true
NaN	| NaN | "NaN" | false
Infinity | Infinity | "Infinity" | true
-Infinity | -Infinity | "-Infinity" | true
"" | 0 | "" | false
"20" | 20 | "20" | true
"Runoob" | NaN | "Runoob" | true
[ ] | 0 | "" | true
[20] | 20 | "20" | true
[10,20] | NaN | "10,20" | true
["Runoob"] | NaN | "Runoob" | true
["Runoob","Google"] | NaN | "Runoob,Google" | true
function(){} | NaN | "function(){}" | true
{ } | NaN | "[object Object]" | true
null | 0 | "null" | false
undefined | NaN | "undefined" | false

## 错误

try 语句测试代码块的错误。
catch 语句处理错误。
throw 语句创建自定义错误。
finally 语句在 try 和 catch 语句之后，无论是否有触发异常，该语句都会执行。

语法

```js
try {
    ... // 异常抛出语句
} catch(e) {
    ... // 异常捕获与处理
} finally {
    ... // 有无异常都要执行
}
```

throw语句

throw 语句允许我们创建自定义错误。

```js
function add(a, b) {
    try {
        if (arguments.length != 2) throw '参数不对'
        if (isNaN(a) || isNaN(b)) throw '不是数字'
        console.log('a + b = ' + (a + b))
    } catch (err) {
        console.log(err)
    }
}
add()
add('1', 2)
add(1, 2)
```

## this关键字

* 面向对象语言中 this 表示当前对象的一个引用。
* 但在 JavaScript 中 this 不是固定不变的，它会随着执行环境的改变而改变。
    - 在方法中，this 表示该方法所属的对象。
    - 如果单独使用，this 表示全局对象。
    - 在函数中，this 表示全局对象。
    - 在函数中，在严格模式下，this 是未定义的(undefined)。
    - 在事件中，this 表示接收事件的元素。
    - 类似 call() 和 apply() 方法可以将 this 引用到任何对象。

## json

函数 | 描述
--- | ---
JSON.parse() | 用于将一个 JSON 字符串转换为 JavaScript 对象。
JSON.stringify() | 用于将 JavaScript 值转换为 JSON 字符串。

___
> 共同学习，共同进步