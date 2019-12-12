# 数值的扩展

## 二进制和八进制表示法

ES6 提供了二进制和八进制数值的新的写法，分别用前缀0b（或0B）和0o（或0O）表示。

```js
0b111110111 === 503 // true
0o767 === 503 // true
```

将0b和0o前缀的字符串数值转为十进制，要使用Number方法。

```js
Number('0b111')  // 7
Number('0o10')  // 8
```

## Number.isFinite(), Number.isNaN()

Number.isFinite()用来检查一个数值是否为有限的（finite），即不是Infinity。

```js
Number.isFinite(15); // true
Number.isFinite(0.8); // true
Number.isFinite(NaN); // false
Number.isFinite(Infinity); // false
Number.isFinite(-Infinity); // false
Number.isFinite('foo'); // false
Number.isFinite('15'); // false
Number.isFinite(true); // false
```

> 注意，如果参数类型不是数值，Number.isFinite一律返回false。

Number.isNaN()用来检查一个值是否为NaN。

```js
Number.isNaN(NaN) // true
Number.isNaN(15) // false
Number.isNaN('15') // false
Number.isNaN(true) // false
Number.isNaN(9/NaN) // true
Number.isNaN('true' / 0) // true
Number.isNaN('true' / 'true') // true
```

> 参数类型不是NaN，Number.isNaN一律返回false。

传统的全局方法isFinite()和isNaN()的区别在于，传统方法先调用Number()将非数值的值转为数值，再进行判断，而这两个新方法只对数值有效，Number.isFinite()对于非数值一律返回false, Number.isNaN()只有对于NaN才返回true，非NaN一律返回false。

```js
isFinite(25) // true
isFinite("25") // true
Number.isFinite(25) // true
Number.isFinite("25") // false

isNaN(NaN) // true
isNaN("NaN") // true
Number.isNaN(NaN) // true
Number.isNaN("NaN") // false
Number.isNaN(1) // false
```

## Number.parseInt(), Number.parseFloat()

ES6 将全局方法parseInt()和parseFloat()，移植到Number对象上面，行为完全保持不变。

```js
// ES5的写法
parseInt('12.34') // 12
parseFloat('123.45#') // 123.45

// ES6的写法
Number.parseInt('12.34') // 12
Number.parseFloat('123.45#') // 123.45
// 这样做的目的，是逐步减少全局性方法，使得语言逐步模块化。
```

## Number.isInteger()

Number.isInteger()用来判断一个数值是否为整数。

```js
Number.isInteger(25) // true
Number.isInteger(25.1) // false

// JavaScript 内部，整数和浮点数采用的是同样的储存方法，所以 25 和 25.0 被视为同一个值。
Number.isInteger(25) // true
Number.isInteger(25.0) // true
// 参数不是数值，Number.isInteger返回false。
```

> 对数据精度的要求较高，不建议使用Number.isInteger()判断一个数值是否为整数。

## Number.EPSILON

ES6 在Number对象上面，新增一个极小的常量Number.EPSILON。根据规格，它表示 1 与大于 1 的最小浮点数之间的差。

对于 64 位浮点数来说，大于 1 的最小浮点数相当于二进制的1.00..001，小数点后面有连续 51 个零。这个值减去 1 之后，就等于 2 的 -52 次方。

```js
Number.EPSILON === Math.pow(2, -52)
// true
Number.EPSILON
// 2.220446049250313e-16
Number.EPSILON.toFixed(20)
// "0.00000000000000022204"
```

Number.EPSILON可以用来设置“能够接受的误差范围”。比如，误差范围设为 2 的-50 次方（即Number.EPSILON * Math.pow(2, 2)），即如果两个浮点数的差小于这个值，我们就认为这两个浮点数相等。

```js
5.551115123125783e-17 < Number.EPSILON * Math.pow(2, 2)
// true

// 为浮点数运算，部署了一个误差检查函数。
function withinErrorMargin (left, right) {
  return Math.abs(left - right) < Number.EPSILON * Math.pow(2, 2);
}

0.1 + 0.2 === 0.3 // false
withinErrorMargin(0.1 + 0.2, 0.3) // true

1.1 + 1.3 === 2.4 // false
withinErrorMargin(1.1 + 1.3, 2.4) // true
```

## 安全整数和 Number.isSafeInteger()

JavaScript 能够准确表示的整数范围在-2^53到2^53之间（不含两个端点），超过这个范围，无法精确表示这个值。

```js
Math.pow(2, 53) // 9007199254740992

9007199254740992  // 9007199254740992
9007199254740993  // 9007199254740992

Math.pow(2, 53) === Math.pow(2, 53) + 1
// true
// 上面代码中，超出 2 的 53 次方之后，一个数就不精确了。
```

ES6 引入了Number.MAX_SAFE_INTEGER和Number.MIN_SAFE_INTEGER这两个常量，用来表示这个范围的上下限。

```js
Number.MAX_SAFE_INTEGER === Math.pow(2, 53) - 1
// true
Number.MAX_SAFE_INTEGER === 9007199254740991
// true

Number.MIN_SAFE_INTEGER === -Number.MAX_SAFE_INTEGER
// true
Number.MIN_SAFE_INTEGER === -9007199254740991
// true
```

Number.isSafeInteger()则是用来判断一个整数是否落在这个范围之内。

```js
Number.isSafeInteger('a') // false
Number.isSafeInteger(null) // false
Number.isSafeInteger(NaN) // false
Number.isSafeInteger(Infinity) // false
Number.isSafeInteger(-Infinity) // false

Number.isSafeInteger(3) // true
Number.isSafeInteger(1.2) // false
Number.isSafeInteger(9007199254740990) // true
Number.isSafeInteger(9007199254740992) // false

Number.isSafeInteger(Number.MIN_SAFE_INTEGER - 1) // false
Number.isSafeInteger(Number.MIN_SAFE_INTEGER) // true
Number.isSafeInteger(Number.MAX_SAFE_INTEGER) // true
Number.isSafeInteger(Number.MAX_SAFE_INTEGER + 1) // false
```

## Math 对象的扩展

* Math.trunc()

Math.trunc方法用于去除一个数的小数部分，返回整数部分。

```js
Math.trunc(4.1) // 4
Math.trunc(4.9) // 4
Math.trunc(-4.1) // -4
Math.trunc(-4.9) // -4
Math.trunc(-0.1234) // -0

// 对于非数值，Math.trunc内部使用Number方法将其先转为数值。
Math.trunc('123.456') // 123
Math.trunc(true) //1
Math.trunc(false) // 0
Math.trunc(null) // 0

// 对于空值和无法截取整数的值，返回NaN。
Math.trunc(NaN);      // NaN
Math.trunc('foo');    // NaN
Math.trunc();         // NaN
Math.trunc(undefined) // NaN

// 对于没有部署这个方法的环境，可以用下面的代码模拟。
Math.trunc = Math.trunc || function(x) {
  return x < 0 ? Math.ceil(x) : Math.floor(x);
};
```

* Math.sign()

Math.sign方法用来判断一个数到底是正数、负数、还是零。对于非数值，会先将其转换为数值。

返回五种值。
    - 参数为正数，返回+1；
    - 参数为负数，返回-1；
    - 参数为 0，返回0；
    - 参数为-0，返回-0;
    - 其他值，返回NaN。

```js
Math.sign(-5) // -1
Math.sign(5) // +1
Math.sign(0) // +0
Math.sign(-0) // -0
Math.sign(NaN) // NaN

// 如果参数是非数值，会自动转为数值。对于那些无法转为数值的值，会返回NaN。
Math.sign('')  // 0
Math.sign(true)  // +1
Math.sign(false)  // 0
Math.sign(null)  // 0
Math.sign('9')  // +1
Math.sign('foo')  // NaN
Math.sign()  // NaN
Math.sign(undefined)  // NaN

// 对于没有部署这个方法的环境，可以用下面的代码模拟。
Math.sign = Math.sign || function(x) {
  x = +x; // convert to a number
  if (x === 0 || isNaN(x)) {
    return x;
  }
  return x > 0 ? 1 : -1;
};
```

* Math.cbrt()

Math.cbrt方法用于计算一个数的立方根。

```js
Math.cbrt(-1) // -1
Math.cbrt(0)  // 0
Math.cbrt(1)  // 1
Math.cbrt(2)  // 1.2599210498948734

// 对于非数值，Math.cbrt方法内部也是先使用Number方法将其转为数值
Math.cbrt('8') // 2
Math.cbrt('hello') // NaN

// 对于没有部署这个方法的环境，可以用下面的代码模拟。
Math.cbrt = Math.cbrt || function(x) {
  var y = Math.pow(Math.abs(x), 1/3);
  return x < 0 ? -y : y;
};
```

* Math.clz32()

Math.clz32()方法将参数转为 32 位无符号整数的形式，然后返回这个 32 位值里面有多少个前导 0。

```js
Math.clz32(0) // 32
Math.clz32(1) // 31
Math.clz32(1000) // 22
Math.clz32(0b01000000000000000000000000000000) // 1
Math.clz32(0b00100000000000000000000000000000) // 2
```

左移运算符（<<）与Math.clz32方法直接相关。

```js
Math.clz32(0) // 32
Math.clz32(1) // 31
Math.clz32(1 << 1) // 30
Math.clz32(1 << 2) // 29
Math.clz32(1 << 29) // 2
```

对于小数，Math.clz32方法只考虑整数部分。

```js
Math.clz32(3.2) // 30
Math.clz32(3.9) // 30
```

对于空值或其他类型的值，Math.clz32方法会将它们先转为数值，然后再计算。

```js
Math.clz32() // 32
Math.clz32(NaN) // 32
Math.clz32(Infinity) // 32
Math.clz32(null) // 32
Math.clz32('foo') // 32
Math.clz32([]) // 32
Math.clz32({}) // 32
Math.clz32(true) // 31
```

* Math.imul()

Math.imul方法返回两个数以 32 位带符号整数形式相乘的结果，返回的也是一个 32 位的带符号整数。

```js
Math.imul(2, 4)   // 8
Math.imul(-1, 8)  // -8
Math.imul(-2, -2) // 4
```

* Math.fround()
Math.fround方法返回一个数的32位单精度浮点数形式。

对于32位单精度格式来说，数值精度是24个二进制位（1 位隐藏位与 23 位有效位），所以对于 -224 至 224 之间的整数（不含两个端点），返回结果与参数本身一致。

```js
Math.fround(0)   // 0
Math.fround(1)   // 1
Math.fround(2 ** 24 - 1)   // 16777215

// 对于没有部署这个方法的环境，可以用下面的代码模拟。
Math.fround = Math.fround || function (x) {
  return new Float32Array([x])[0];
};
```

* Math.hypot()

Math.hypot方法返回所有参数的平方和的平方根。

```js
Math.hypot(3, 4);        // 5
Math.hypot(3, 4, 5);     // 7.0710678118654755
Math.hypot();            // 0
Math.hypot(NaN);         // NaN
Math.hypot(3, 4, 'foo'); // NaN
Math.hypot(3, 4, '5');   // 7.0710678118654755
Math.hypot(-3);          // 3
```

> 如果参数不是数值，Math.hypot方法会将其转为数值。只要有一个参数无法转为数值，就会返回 NaN。

## 对数方法

* Math.expm1()

Math.expm1(x)返回 ex - 1，即Math.exp(x) - 1。

```js
Math.expm1(-1) // -0.6321205588285577
Math.expm1(0)  // 0
Math.expm1(1)  // 1.718281828459045

// 对于没有部署这个方法的环境，可以用下面的代码模拟。
Math.expm1 = Math.expm1 || function(x) {
  return Math.exp(x) - 1;
};
```

* Math.log1p()

Math.log1p(x)方法返回1 + x的自然对数，即Math.log(1 + x)。如果x小于-1，返回NaN。

```js
Math.log1p(1)  // 0.6931471805599453
Math.log1p(0)  // 0
Math.log1p(-1) // -Infinity
Math.log1p(-2) // NaN

// 对于没有部署这个方法的环境，可以用下面的代码模拟。
Math.log1p = Math.log1p || function(x) {
  return Math.log(1 + x);
};
```

* Math.log10()

Math.log10(x)返回以 10 为底的x的对数。如果x小于 0，则返回 NaN。

```js
Math.log10(2)      // 0.3010299956639812
Math.log10(1)      // 0
Math.log10(0)      // -Infinity
Math.log10(-2)     // NaN
Math.log10(100000) // 5

// 对于没有部署这个方法的环境，可以用下面的代码模拟
Math.log10 = Math.log10 || function(x) {
  return Math.log(x) / Math.LN10;
};
```

* Math.log2()

Math.log2(x)返回以 2 为底的x的对数。如果x小于 0，则返回 NaN。

```js
Math.log2(3)       // 1.584962500721156
Math.log2(2)       // 1
Math.log2(1)       // 0
Math.log2(0)       // -Infinity
Math.log2(-2)      // NaN
Math.log2(1024)    // 10
Math.log2(1 << 29) // 29

// 对于没有部署这个方法的环境，可以用下面的代码模拟
Math.log2 = Math.log2 || function(x) {
  return Math.log(x) / Math.LN2;
};
```

## 双曲函数方法

Math.sinh(x) 返回x的双曲正弦（hyperbolic sine）
Math.cosh(x) 返回x的双曲余弦（hyperbolic cosine）
Math.tanh(x) 返回x的双曲正切（hyperbolic tangent）
Math.asinh(x) 返回x的反双曲正弦（inverse hyperbolic sine）
Math.acosh(x) 返回x的反双曲余弦（inverse hyperbolic cosine）
Math.atanh(x) 返回x的反双曲正切（inverse hyperbolic tangent）

## 指数运算符

ES2016 新增了一个指数运算符（**）。

```js
2 ** 2 // 4
2 ** 3 // 8
```

这个运算符的一个特点是右结合，而不是常见的左结合。多个指数运算符连用时，是从最右边开始计算的。

```js
// 相当于 2 ** (3 ** 2)
2 ** 3 ** 2
// 512
```

指数运算符可以与等号结合，形成一个新的赋值运算符（**=）。

```js
let a = 1.5;
a **= 2;
// 等同于 a = a * a;

let b = 4;
b **= 3;
// 等同于 b = b * b * b;`js
```

注意，V8 引擎的指数运算符与Math.pow的实现不相同，对于特别大的运算结果，两者会有细微的差异。

```js
Math.pow(99, 99)
// 3.697296376497263e+197

99 ** 99
// 3.697296376497268e+197
```
___
> 共同学习，共同进步