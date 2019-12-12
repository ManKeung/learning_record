# 字符串的扩展

## 字符的 Unicode 表示法

```js
"\u0061"
// "a"
// 这种表示法只限于码点在\u0000~\uFFFF之间的字符。超出这个范围的字符，必须用两个双字节的形式表示。
"\uD842\uDFB7"
// "𠮷"

"\u20BB7"
// " 7"
```

```js
"\u{20BB7}"
// "𠮷"

"\u{41}\u{42}\u{43}"
// "ABC"

let hello = 123;
hell\u{6F} // 123

'\u{1F680}' === '\uD83D\uDE80'
// true

// 有了这种表示法之后，JavaScript 共有 6 种方法可以表示一个字符。
'\z' === 'z'  // true
'\172' === 'z' // true
'\x7A' === 'z' // true
'\u007A' === 'z' // true
'\u{7A}' === 'z' // true
```

## 字符串的遍历器接口

```js
for (let codePoint of 'foo') {
    console.log(codePoint)
}
// "f"
// "o"
// "o"

// 除了遍历字符串，这个遍历器最大的优点是可以识别大于0xFFFF的码点，传统的for循环无法识别这样的码点。
let text = String.fromCodePoint(0x20BB7);

for (let i = 0; i < text.length; i++) {
    console.log(text[i]);
}
// " "
// " "

for (let i of text) {
    console.log(i);
}
// "𠮷"
```

## 模板字符串

```js
// 字符串中嵌入变量
let name = "Bob", time = "today";
`Hello ${name}, how are you ${time}?`
```

## String.fromCodePoint()

```js
// es5
// 不能识别码点大于0xFFFF的字符
String.fromCharCode(0x20BB7)
// "ஷ"

// es6
String.fromCodePoint(0x20BB7)
// "𠮷"
String.fromCodePoint(0x78, 0x1f680, 0x79) === 'x\uD83D\uDE80y'
// true
```

## String.raw()

ES6 还为原生的 String 对象

```js
String.raw`Hi\n${2+3}!`
// 实际返回 "Hi\\n5!"，显示的是转义后的结果 "Hi\n5!"

String.raw`Hi\u000A!`;
// 实际返回 "Hi\\u000A!"，显示的是转义后的结果 "Hi\u000A!"

// 如果原字符串的斜杠已经转义，那么String.raw()会进行再次转义。
String.raw`Hi\\n`
// 返回 "Hi\\\\n"

String.raw`Hi\\n` === "Hi\\\\n" // true
```

```js
// `foo${1 + 2}bar`
// 等同于
String.raw({ raw: ['foo', 'bar'] }, 1 + 2) // "foo3bar"

// 作为函数，String.raw()的代码实现基本如下。
String.raw = function (strings, ...values) {
    let output = '';
    let index;
    for (index = 0; index < values.length; index++) {
        x] + values[index];
    }

    output += strings.raw[index]
    return output;
}
```

## codePointAt()

```js
// es5
var s = "𠮷";

s.length // 2
s.charAt(0) // ''
s.charAt(1) // ''
s.charCodeAt(0) // 55362
s.charCodeAt(1) // 57271

// es6
let s = '𠮷a';

s.codePointAt(0) // 134071
s.codePointAt(1) // 57271

s.codePointAt(2) // 97
```

## normalize()

```js
'\u01D1'==='\u004F\u030C' //false

'\u01D1'.length // 1
'\u004F\u030C'.length // 2

'\u01D1'.normalize() === '\u004F\u030C'.normalize()
// true
```

## includes(), startsWith(), endsWith()

includes()：返回布尔值，表示是否找到了参数字符串。
startsWith()：返回布尔值，表示参数字符串是否在原字符串的头部。
endsWith()：返回布尔值，表示参数字符串是否在原字符串的尾部

```js
let s = 'Hello world!';

s.startsWith('Hello') // true
s.endsWith('!') // true
s.includes('o') // true

// 第二个参数，表示开始搜索的位置。
let s = 'Hello world!';

s.startsWith('world', 6) // true
s.endsWith('Hello', 5) // true
s.includes('Hello', 6) // false
```

## repeat()

repeat方法返回一个新字符串，表示将原字符串重复n次

```js
// 参数如果是小数，会被取整。
// 如果repeat的参数是负数或者Infinity，会报错。
// 如果参数是 0 到-1 之间的小数，则等同于 0，这是因为会先进行取整运算。0 到-1 之间的小数，取整以后等于-0，repeat视同为 0。
'x'.repeat(3) // "xxx"
'hello'.repeat(2) // "hellohello"
'na'.repeat(0) // ""
```

## padStart()，padEnd()

padStart()用于头部补全，padEnd()用于尾部补全。

```js
'x'.padStart(5, 'ab') // 'ababx'
'x'.padStart(4, 'ab') // 'abax'

'x'.padEnd(5, 'ab') // 'xabab'
'x'.padEnd(4, 'ab') // 'xaba'
```

## trimStart()，trimEnd()

trimStart()消除字符串头部的空格，trimEnd()消除尾部的空格。

```js
const s = '  abc  ';

s.trim() // "abc"
s.trimStart() // "abc  "
s.trimEnd() // "  abc"
```

___
> 共同学习，共同进步