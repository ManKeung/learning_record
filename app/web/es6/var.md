# let 和 const 命令

## let

ES6 新增了let命令，用来声明变量。它的用法类似于var，但是所声明的变量，只在let命令所在的代码块内有效。

```js
// let命令，用来声明变量。用法类似于var，但声明的变量只在代码块内有效
{
    let a = 10;
    var b = 1;
}

a // ReferenceError: a is not defined.
b // 1
```

```js
{
    for(let i = 0; i < 10; i++) {
    // ...
    }

    // console.log(i); // 报错 let 换成 var i=10

    var a = [];

    for(var i = 0; i < 10; i++) {
    a[i] = function() {
        console.log(i);
    };
    }

    a[6]();
}

{
    var a = [];

    for(let i = 0; i < 10; i++) {
    a[i] = function() {
        console.log(i);
    };
    }

    a[6]();

    // 明函数内部的变量i与循环变量i不在同一个作用域，有各自单独的作用域。
    for(let i = 0; i < 3; i++) {
    let i = 'abc';
    console.log(i);
    }
}
```

* 不存在变量提升

```js
{
    // var 的情况
    console.log(foo); // 输出 undefined
    var foo = 2;

    // let 的情况
    console.log(bar); // 报错ReferenceError
    let bar = 2;
}
```

* 暂时性死区

```js
{
    var tmp = 123;

    // 只要块级作用域内存在let命令，它所声明的变量就“绑定”（binding）这个区域，不再受外部的影响。
    if(true) {
    tmp = 'abc'; // ReferenceError
    let tmp;
    }

    if(true) {
    // TDZ开始
    tmp = 'abc'; // ReferenceError
    console.log(tmp); // ReferenceError

    let tmp; // TDZ结束
    console.log(tmp); // undefined

    tmp = 123;
    console.log(tmp); // 123
    }
}
```

* 不允许重复声明

```js
{
    // let不允许在相同作用域内，重复声明同一个变量。
    // 报错
    function funa() {
    let a = 10;
    var a = 1;
    }

    // 报错
    function funb() {
    let a = 10;
    let a = 1;
    }

    // 不能在函数内部重新声明参数
    function func(arg) {
    let arg; // 报错
    }

    function fund(arg) {
    {
        let arg; // 不报错
    }
    }
}
```

* 块级作用域

```js
{
    var tmp = new Date();

    function f() {
    console.log(tmp);
    if(false) {
        var tmp = 'hello world';
    }
    }

    f();

    var s = 'hello';

    for(var i=0; i<s.length; i++) {
    console.log(s[i]);
    }

    console.log(i);
}

{
    function f1() {
    let n = 5;

    if(true) {
        let n = 10;
    }

    console.log('n = ', n);
    }

    f1();
}
```

## const

* 基本用法

```js
{
    const PI = 3.1415;
    console.log(`PI = ${PI}`);
    // PI = 3; // TypeError: Assignment to constant variable

    {
        if(true) {
            const MAX = 5;
        }

        // MAX; // ReferenceError: MAX is not defined
    }

    {
        var message = 'Hello!';
        let age = 25;

        // 以下两行都会报错
        // const message = 'Goodbye!';
        // const age = 30;
    }
}

```

* 本质

```js
{
    const foo = {};

    foo.prop = 123;
    console.log(`foo.prop = ${foo.prop}`);

    // foo = {}; // TypeError: Assignment to constant variable

        { // 对象冻结，应该使用Object.freeze方法
        const foo = Object.freeze({});

        // 常规模式时，下面一行不起作用；
        // 严格模式时，该行报错
        // foo.prop = 123;
    }

    {
        // 对象彻底冻结的函数
        var constantize = (obj) => {
            Object.freeze(obj);
            Object.keys(obj).forEach((key, i) => {
            if(typeof obj[key] === 'object') {
                constantize(obj[key]);
            }
            });
        };
    }
}
```

* 顶层对象的属性

```js
window.a = 1;
console.log(`a = ${a}`);

a = 2;
console.log(`window.a = ${window.a}`);
```

* globalThis对象

JavaScript 语言存在一个顶层对象，它提供全局环境（即全局作用域），所有代码都是在这个环境中运行。但是，顶层对象在各种实现里面是不统一的。
    - 浏览器里面，顶层对象是window，但 Node 和 Web Worker 没有window。
    - 浏览器和 Web Worker 里面，self也指向顶层对象，但是 Node 没有self。
    - Node 里面，顶层对象是global，但其他环境都不支持。

```js
// 方法一
(typeof window !== 'undefined'
   ? window
   : (typeof process === 'object' &&
      typeof require === 'function' &&
      typeof global === 'object')
     ? global
     : this);

// 方法二
var getGlobal = function () {
    if (typeof self !== 'undefined') { return self; }
    if (typeof window !== 'undefined') { return window; }
    if (typeof global !== 'undefined') { return global; }
    throw new Error('unable to locate global object');
};
```

___
> 共同学习，共同进步