# 提升

## 对象

JavaScript 中的所有事物都是对象：字符串、数值、数组、函数...
此外，JavaScript 允许自定义对象。

* 创建对象

```js
// 1
person = new Object()
person.firstname = 'man'
person.lastname = 'keung'
person.age = 18
person.eyecolor = 'black'
// 2
person={firstname:"John",lastname:"Doe",age:50,eyecolor:"blue"};
// 3
function person(firstname,lastname,age,eyecolor)
{
    this.firstname=firstname;
    this.lastname=lastname;
    this.age=age;
    this.eyecolor=eyecolor;
}
var myFather=new person("John","Doe",50,"blue");
var myMother=new person("Sally","Rally",48,"green");
```

* 把方法添加到 JavaScript 对象

```js
function person(firstname,lastname,age,eyecolor)
{
    this.firstname=firstname;
    this.lastname=lastname;
    this.age=age;
    this.eyecolor=eyecolor;

    this.changeName=changeName;
    function changeName(name)
    {
        this.lastname=name;
    }
}
```

* JavaScript for...in 循环

```js
for (variable in object)
{
    执行的代码……
}
```

## prototype

```js
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
}

var myFather = new Person("John", "Doe", 50, "blue");
var myMother = new Person("Sally", "Rally", 48, "green");
```

* 我们也知道在一个已存在的对象构造器中是不能添加新的属性的

```js
Person.nationality = "English"; // error
```

* prototype 继承

1. prototype 继承

```js
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
}
Person.prototype.nationality = "English";
```

2. 给对象的构造函数添加新的方法

```js
function Person(first, last, age, eyecolor) {
  this.firstName = first;
  this.lastName = last;
  this.age = age;
  this.eyeColor = eyecolor;
}

Person.prototype.name = function() {
  return this.firstName + " " + this.lastName;
};
```

## Date

```js
var d = new Date()
var d = new Date(milliseconds)
var d = new Date(dateString)
var d = new Date(year, month, day, hours, minutes, seconds, milliseconds)
```


方法 | 描述
--- | ---
getDate() | 从 Date 对象返回一个月中的某一天 (1 ~ 31)。
getDay() | 从 Date 对象返回一周中的某一天 (0 ~ 6)。
getFullYear() | 从 Date 对象以四位数字返回年份。
getHours() | 返回 Date 对象的小时 (0 ~ 23)。
getMilliseconds() | 返回 Date 对象的毫秒(0 ~ 999)。
getMinutes() | 返回 Date 对象的分钟 (0 ~ 59)。
getMonth() | 从 Date 对象返回月份 (0 ~ 11)。
getSeconds() | 返回 Date 对象的秒数 (0 ~ 59)。
getTime() | 返回 1970 年 1 月 1 日至今的毫秒数。
getTimezoneOffset() | 返回本地时间与格林威治标准时间 (GMT) 的分钟差。
getUTCDate() | 根据世界时从 Date 对象返回月中的一天 (1 ~ 31)。
getUTCDay() | 根据世界时从 Date 对象返回周中的一天 (0 ~ 6)。
getUTCFullYear() | 根据世界时从 Date 对象返回四位数的年份。
getUTCHours() | 根据世界时返回 Date 对象的小时 (0 ~ 23)。
getUTCMilliseconds() | 根据世界时返回 Date 对象的毫秒(0 ~ 999)。
getUTCMinutes() | 根据世界时返回 Date 对象的分钟 (0 ~ 59)。
getUTCMonth() | 根据世界时从 Date 对象返回月份 (0 ~ 11)。
getUTCSeconds() | 根据世界时返回 Date 对象的秒钟 (0 ~ 59)。
parse() | 返回1970年1月1日午夜到指定日期（字符串）的毫秒数。
setDate() | 设置 Date 对象中月的某一天 (1 ~ 31)。
setFullYear() | 设置 Date 对象中的年份（四位数字）。
setHours() | 设置 Date 对象中的小时 (0 ~ 23)。
setMilliseconds() | 设置 Date 对象中的毫秒 (0 ~ 999)。
setMinutes() | 设置 Date 对象中的分钟 (0 ~ 59)。
setMonth() | 设置 Date 对象中月份 (0 ~ 11)。
setSeconds() | 设置 Date 对象中的秒钟 (0 ~ 59)。
setTime() | setTime() 方法以毫秒设置 Date 对象。
setUTCDate() | 根据世界时设置 Date 对象中月份的一天 (1 ~ 31)。
setUTCFullYear() | 根据世界时设置 Date 对象中的年份（四位数字）。
setUTCHours() | 根据世界时设置 Date 对象中的小时 (0 ~ 23)。
setUTCMilliseconds() | 根据世界时设置 Date 对象中的毫秒 (0 ~ 999)。
setUTCMinutes() | 根据世界时设置 Date 对象中的分钟 (0 ~ 59)。
setUTCMonth() | 根据世界时设置 Date 对象中的月份 (0 ~ 11)。
setUTCSeconds() | setUTCSeconds() 方法用于根据世界时 (UTC) 设置指定时间的秒字段。
toDateString() | 把 Date 对象的日期部分转换为字符串。
toISOString() | 使用 ISO 标准返回字符串的日期格式。
toJSON() | 以 JSON 数据格式返回日期字符串。
toLocaleDateString() | 根据本地时间格式，把 Date 对象的日期部分转换为字符串。
toLocaleTimeString() | 根据本地时间格式，把 Date 对象的时间部分转换为字符串。
toLocaleString() | 据本地时间格式，把 Date 对象转换为字符串。
toString() | 把 Date 对象转换为字符串。
toTimeString() | 把 Date 对象的时间部分转换为字符串。
toUTCString() | 根据世界时，把 Date 对象转换为字符串。 实例：
var today = new Date();
var UTCstring = today.toUTCString();
UTC()	根据世界时返回 1970 年 1 月 1 日 到指定日期的毫秒数。
valueOf()	返回 Date 对象的原始值。

## 数组

方法 | 描述
--- | ---
concat() | 连接两个或更多的数组，并返回结果。
copyWithin() | 从数组的指定位置拷贝元素到数组的另一个指定位置中。
entries() | 返回数组的可迭代对象。
every() | 检测数值元素的每个元素是否都符合条件。
fill() | 使用一个固定值来填充数组。
filter() | 检测数值元素，并返回符合条件所有元素的数组。
find() | 返回符合传入测试（函数）条件的数组元素。
findIndex() | 返回符合传入测试（函数）条件的数组元素索引。
forEach() | 数组每个元素都执行一次回调函数。
from() | 通过给定的对象中创建一个数组。
includes() | 判断一个数组是否包含一个指定的值。
indexOf() | 搜索数组中的元素，并返回它所在的位置。
isArray() | 判断对象是否为数组。
join() | 把数组的所有元素放入一个字符串。
keys() | 返回数组的可迭代对象，包含原始数组的键(key)。
lastIndexOf() | 搜索数组中的元素，并返回它最后出现的位置。
map() | 通过指定函数处理数组的每个元素，并返回处理后的数组。
pop() | 删除数组的最后一个元素并返回删除的元素。
push() | 向数组的末尾添加一个或更多元素，并返回新的长度。
reduce() | 将数组元素计算为一个值（从左到右）。
reduceRight() | 将数组元素计算为一个值（从右到左）。
reverse() | 反转数组的元素顺序。
shift() | 删除并返回数组的第一个元素。
slice() | 选取数组的的一部分，并返回一个新数组。
some() | 检测数组元素中是否有元素符合指定条件。
sort() | 对数组的元素进行排序。
splice() | 从数组中添加或删除元素。
toString() | 把数组转换为字符串，并返回结果。
unshift() | 向数组的开头添加一个或更多元素，并返回新的长度。
valueOf() | 返回数组对象的原始值。

## math

* 对象属性

属性 | 描述
--- | ---
E | 返回算术常量 e，即自然对数的底数（约等于2.718）。
LN2 | 返回 2 的自然对数（约等于0.693）。
LN10 | 返回 10 的自然对数（约等于2.302）。
LOG2E | 返回以 2 为底的 e 的对数（约等于 1.4426950408889634）。
LOG10E | 返回以 10 为底的 e 的对数（约等于0.434）。
PI | 返回圆周率（约等于3.14159）。
SQRT1_2 | 返回 2 的平方根的倒数（约等于 0.707）。
SQRT2 | 返回 2 的平方根（约等于 1.414）。

* math对象方法

方法 | 描述
--- | ---
abs(x) | 返回 x 的绝对值。
acos(x) | 返回 x 的反余弦值。
asin(x) | 返回 x 的反正弦值。
atan(x) | 以介于 -PI/2 与 PI/2 弧度之间的数值来返回 x 的反正切值。
atan2(y,x) | 返回从 x 轴到点 (x,y) 的角度（介于 -PI/2 与 PI/2 弧度之间）。
ceil(x) | 对数进行上舍入。
cos(x) | 返回数的余弦。
exp(x) | 返回 Ex 的指数。
floor(x) | 对 x 进行下舍入。
log(x) | 返回数的自然对数（底为e）。
max(x,y,z,...,n) | 返回 x,y,z,...,n 中的最高值。
min(x,y,z,...,n) | 返回 x,y,z,...,n中的最低值。
pow(x,y) | 返回 x 的 y 次幂。
random() | 返回 0 ~ 1 之间的随机数。
round(x) | 四舍五入。
sin(x) | 返回数的正弦。
sqrt(x) | 返回数的平方根。
tan(x) | 返回角的正切。

___
> 共同学习，共同进步