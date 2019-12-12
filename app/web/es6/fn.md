# 函数的扩展

## 函数参数的默认值

* 基本用法

```js
// es5
function log(x, y) {
    y = y || 'World';
    console.log(x, y);
}

log('Hello') // Hello World
log('Hello', 'China') // Hello China
log('Hello', '') // Hello World

// es6
function log(x, y = 'World') {
    console.log(x, y);
}

log('Hello') // Hello World
log('Hello', 'China') // Hello China
log('Hello', '') // Hello
```

* 与解构赋值默认值结合使用

```js
function foo({x, y = 5}) {
    console.log(x, y);
}

foo({}) // undefined 5
foo({x: 1}) // 1 5
foo({x: 1, y: 2}) // 1 2
foo() // TypeError: Cannot read property 'x' of undefined

function foo({x, y = 5} = {}) {
    console.log(x, y);
}

foo() // undefined 5
```

* 参数默认值的位置

```js
// 例一
function f(x = 1, y) {
    return [x, y];
}

f() // [1, undefined]
f(2) // [2, undefined])
f(, 1) // 报错
f(undefined, 1) // [1, 1]

// 例二
function f(x, y = 5, z) {
    return [x, y, z];
}

f() // [undefined, 5, undefined]
f(1) // [1, 5, undefined]
f(1, ,2) // 报错
f(1, undefined, 2) // [1, 5, 2]

function foo(x = 5, y = 6) {
    console.log(x, y);
}

foo(undefined, null)
// 5 null
```

* 函数的 length 属性

```js
(function (a) {}).length // 1
(function (a = 5) {}).length // 0
(function (a, b, c = 5) {}).length // 2

(function(...args) {}).length // 0

// 如果设置了默认值的参数不是尾参数，那么length属性也不再计入后面的参数了。
(function (a = 0, b, c) {}).length // 0
(function (a, b = 1, c) {}).length // 1
```

* 作用域

```js
var x = 1;

function f(x, y = x) {
    console.log(y);
}

f(2) // 2

let x = 1;

function f(y = x) {
    let x = 2;
    console.log(y);
}

f() // 1
```

```js
// 全局变量x不存在，就会报错。
function f(y = x) {
    let x = 2;
    console.log(y);
}

f() // ReferenceError: x is not defined

// 这样写，也会报错
var x = 1;

function foo(x = x) {
    // ...
}

foo() // ReferenceError: x is not defined
```

* 应用

利用参数默认值，可以指定某一个参数不得省略，如果省略就抛出一个错误。

```js
function throwIfMissing() {
    throw new Error('Missing parameter');
}

function foo(mustBeProvided = throwIfMissing()) {
    return mustBeProvided;
}

foo()
// Error: Missing parameter
```

## rest参数

ES6 引入 rest 参数（形式为...变量名），用于获取函数的多余参数，这样就不需要使用arguments对象了。rest 参数搭配的变量是一个数组，该变量将多余的参数放入数组中。

```js
function add(...values) {
    let sum = 0;

    for (var val of values) {
        sum += val;
    }

    return sum;
}

add(2, 5, 3) // 10
```

## name属性

```js
const bar = function baz() {};

// ES5
bar.name // "baz"

// ES6
bar.name // "baz"
```

## 箭头函数

* 基本用法

ES6 允许使用“箭头”（=>）定义函数。

```js
var f = v => v;

// 等同于
var f = function (v) {
    return v;
}
```

如果箭头函数不需要参数或需要多个参数，就使用一个圆括号代表参数部分。

```js
var f = () => 5;
// 等同于
var f = function () { return 5 };

var sum = (num1, num2) => num1 + num2;
// 等同于
var sum = function(num1, num2) {
    return num1 + num2;
};
```

如果箭头函数的代码块部分多于一条语句，就要使用大括号将它们括起来，并且使用return语句返回。

```js
var sum = (num1, num2) => { return num1 + num2; }
```

由于大括号被解释为代码块，所以如果箭头函数直接返回一个对象，必须在对象外面加上括号，否则会报错。

```js
// 报错
let getTempItem = id => { id: id, name: "Temp" };

// 不报错
let getTempItem = id => ({ id: id, name: "Temp" });
```

如果箭头函数只有一行语句，且不需要返回值，可以采用下面的写法，就不用写大括号了。

```js
let fn = () => void doesNotReturn();
```

箭头函数可以与变量解构结合使用。

```js
const full = ({ first, last }) => first + ' ' + last;

// 等同于
function full(person) {
    return person.first + ' ' + person.last;
}
```

* 使用注意点
    1. 函数体内的this对象，就是定义时所在的对象，而不是使用时所在的对象。
    2. 不可以当作构造函数，也就是说，不可以使用new命令，否则会抛出一个错误。
    3. 不可以使用arguments对象，该对象在函数体内不存在。如果要用，可以用 rest 参数代替。
    4. 不可以使用yield命令，因此箭头函数不能用作 Generator 函数。

## 尾调用优化

```js
function f(x){
    return g(x);
}
```

以下三种情况，都不属于尾调用

```js
// 情况一
function f(x){
    let y = g(x);
    return y;
}

// 情况二
function f(x){
    return g(x) + 1;
}

// 情况三
function f(x){
    g(x);
}
```

尾递归

函数调用自身，称为递归。如果尾调用自身，就称为尾递归。

```js
function factorial(n) {
    if (n === 1) return 1;
    return n * factorial(n - 1);
}

factorial(5) // 120
```

递归函数的改写

```js
function factorial(n, total = 1) {
    if (n === 1) return total;
    return factorial(n - 1, n * total);
}

factorial(5) // 120
```

## 函数参数的尾逗号

```js
function clownsEverywhere(
    param1,
    param2,
) { /* ... */ }

clownsEverywhere(
    'foo',
    'bar',
);
```

## Function.prototype.toString()

```js
function /* foo comment */ foo () {}

foo.toString()
// "function /* foo comment */ foo () {}"
```

## catch 命令的参数省略

```js
try {
    // ...
} catch (err) {
    // 处理错误
}

try {
    // ...
} catch {
    // ...
}
```

___
> 共同学习，共同进步