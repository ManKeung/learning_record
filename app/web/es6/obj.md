# 对象的扩展

## 属性的简洁表示法

ES6 允许在大括号里面，直接写入变量和函数，作为对象的属性和方法。

```js
const foo = 'bar';
const baz = {foo};
baz // {foo: "bar"}

// 等同于
const baz = {foo: foo};

function f(x, y) {
  return {x, y};
}

// 等同于

function f(x, y) {
  return {x: x, y: y};
}

f(1, 2) // Object {x: 1, y: 2}

const o = {
  method() {
    return "Hello!";
  }
};

// 等同于

const o = {
  method: function() {
    return "Hello!";
  }
};
```

```js
let birth = '2000/01/01';

const Person = {

  name: '张三',

  //等同于birth: birth
  birth,

  // 等同于hello: function ()...
  hello() { console.log('我的名字是', this.name); }

};
```

性的赋值器（setter）和取值器（getter）

```js
const cart = {
    _wheels: 4,

    get wheels () {
        return this._wheels;
    },

    set wheels (value) {
        if (value < this._wheels) {
            throw new Error('数值太小了！');
        }
        this._wheels = value;
    }
}
```

## 属性名表达式

```js
// 方法一
obj.foo = true;

// 方法二
obj['a' + 'bc'] = 123;
```

```js
let lastWord = 'last word';

const a = {
    'first word': 'hello',
    [lastWord]: 'world'
};

a['first word'] // "hello"
a[lastWord] // "world"
a['last word'] // "world"
```

## 方法的 name 属性

```js
const person = {
    sayName() {
        console.log('hello!');
    },
};

person.sayName.name   // "sayName"
```

## 属性的可枚举性和遍历

* 可枚举性

```js
let obj = { foo: 123 };
Object.getOwnPropertyDescriptor(obj, 'foo')
//  {
//    value: 123,
//    writable: true,
//    enumerable: true,
//    configurable: true
//  }
```

* 属性的遍历

+ for...in
    - for...in循环遍历对象自身的和继承的可枚举属性（不含 Symbol 属性）。

+ Object.keys(obj)
    - Object.keys返回一个数组，包括对象自身的（不含继承的）所有可枚举属性（不含 Symbol 属性）的键名。

+ Object.getOwnPropertyNames(obj)
    - Object.getOwnPropertyNames返回一个数组，包含对象自身的所有属性（不含 Symbol 属性，但是包括不可枚举属性）的键名。

+ Object.getOwnPropertySymbols(obj)
    - Object.getOwnPropertySymbols返回一个数组，包含对象自身的所有 Symbol 属性的键名。

+ Reflect.ownKeys(obj)
    - Reflect.ownKeys返回一个数组，包含对象自身的所有键名，不管键名是 Symbol 或字符串，也不管是否可枚举。

## super 关键字

super，指向当前对象的原型对象

```js
const proto = {
    foo: 'hello'
};

const obj = {
    foo: 'world',
        find() {
    return super.foo;
    }
};

Object.setPrototypeOf(obj, proto);
obj.find() // "hello"
```

## 对象的扩展运算符

* 解构赋值

```js
let { x, y, ...z } = { x: 1, y: 2, a: 3, b: 4 };
x // 1
y // 2
z // { a: 3, b: 4 }
```

* 扩展运算符

```js
let z = { a: 3, b: 4 };
let n = { ...z };
n // { a: 3, b: 4 }
```

## 链判断运算符

```js
a?.b
// 等同于
a == null ? undefined : a.b

a?.[x]
// 等同于
a == null ? undefined : a[x]

a?.b()
// 等同于
a == null ? undefined : a.b()

a?.()
// 等同于
a == null ? undefined : a()
```

* 短路机制

```js
a?.[++x]
// 等同于
a == null ? undefined : a[++x]
```

* delete 运算符

```js
delete a?.b
// 等同于
a == null ? undefined : delete a.b
```

* 括号的影响

```js
(a?.b).c
// 等价于
(a == null ? undefined : a.b).c
```

* 报错场合

```js
// 构造函数
new a?.()
new a?.b()

// 链判断运算符的右侧有模板字符串
a?.`{b}`
a?.b`{c}`

// 链判断运算符的左侧是 super
super?.()
super?.foo

// 链运算符用于赋值运算符左侧
a?.b = c
```

* 右侧不得为十进制数值

## Null 判断运算符

读取对象属性的时候，如果某个属性的值是null或undefined，有时候需要为它们指定默认值。常见做法是通过||运算符指定默认值。

```js
const headerText = response.settings.headerText || 'Hello, world!';
const animationDuration = response.settings.animationDuration || 300;
const showSplashScreen = response.settings.showSplashScreen || true;
```

ES2020 引入了一个新的 Null 判断运算符??。它的行为类似||，但是只有运算符左侧的值为null或undefined时，才会返回右侧的值。

```js
const headerText = response.settings.headerText ?? 'Hello, world!';
const animationDuration = response.settings.animationDuration ?? 300;
const showSplashScreen = response.settings.showSplashScreen ?? true;
```

## Object.is()

Object.is就是部署这个算法的新方法。它用来比较两个值是否严格相等，与严格比较运算符（===）的行为基本一致

```js
Object.is('foo', 'foo')
// true
Object.is({}, {})
// false
```

不同之处只有两个：一是+0不等于-0，二是NaN等于自身。

```js
+0 === -0 //true
NaN === NaN // false

Object.is(+0, -0) // false
Object.is(NaN, NaN) // true
```

## Object.assign()

* 基本用法

```js
const target = { a: 1 };

const source1 = { b: 2 };
const source2 = { c: 3 };

Object.assign(target, source1, source2);
target // {a:1, b:2, c:3}
```

### 注意点

* 浅拷贝

Object.assign方法实行的是浅拷贝，而不是深拷贝。也就是说，如果源对象某个属性的值是对象，那么目标对象拷贝得到的是这个对象的引用。

```js
const obj1 = {a: {b: 1}};
const obj2 = Object.assign({}, obj1);

obj1.a.b = 2;
obj2.a.b // 2
```

* 同名属性的替换

对于这种嵌套的对象，一旦遇到同名属性，Object.assign的处理方法是替换，而不是添加。

```js
const target = { a: { b: 'c', d: 'e' } }
const source = { a: { b: 'hello' } }
Object.assign(target, source)
// { a: { b: 'hello' } }
```

* 数组的处理

Object.assign可以用来处理数组，但是会把数组视为对象。

```js
Object.assign([1, 2, 3], [4, 5])
// [4, 5, 3]
```

* 取值函数的处理

Object.assign只能进行值的复制，如果要复制的值是一个取值函数，那么将求值后再复制。

```js
const source = {
  get foo() { return 1 }
};
const target = {};

Object.assign(target, source)
// { foo: 1 }
```

### 常见用途

* 为对象添加属性

```js
class Point {
    constructor(x, y) {
        Object.assign(this, {x, y});
    }
}
```

* 为对象添加方法

```js
Object.assign(SomeClass.prototype, {
  someMethod(arg1, arg2) {
    ···
  },
  anotherMethod() {
    ···
  }
});

// 等同于下面的写法
SomeClass.prototype.someMethod = function (arg1, arg2) {
    ···
};
SomeClass.prototype.anotherMethod = function () {
    ···
};
```

* 克隆对象

```js
// 不过，采用这种方法克隆，只能克隆原始对象自身的值，不能克隆它继承的值。
function clone(origin) {
    return Object.assign({}, origin);
}

// 保持继承链，可以采用下面的代码
function clone(origin) {
    let originProto = Object.getPrototypeOf(origin);
    return Object.assign(Object.create(originProto), origin);
}
```

* 合并多个对象

```js
const merge =
  (target, ...sources) => Object.assign(target, ...sources);

// 合并后返回一个新对象
const merge =
  (...sources) => Object.assign({}, ...sources);
```

* 为属性指定默认值

```js
const DEFAULTS = {
    logLevel: 0,
    outputFormat: 'html'
};

function processContent(options) {
    options = Object.assign({}, DEFAULTS, options);
    console.log(options);
  // ...
}
```

## Object.getOwnPropertyDescriptors()

```js
const obj = {
  foo: 123,
  get bar() { return 'abc' }
};

Object.getOwnPropertyDescriptors(obj)
// { foo:
//    { value: 123,
//      writable: true,
//      enumerable: true,
//      configurable: true },
//   bar:
//    { get: [Function: get bar],
//      set: undefined,
//      enumerable: true,
//      configurable: true } }
```

## __proto__属性，Object.setPrototypeOf()，Object.getPrototypeOf()

* __proto__属性

```js
// es5 的写法
const obj = {
    method: function() { ... }
};
obj.__proto__ = someOtherObj;

// es6 的写法
var obj = Object.create(someOtherObj);
obj.method = function() { ... };
```

## Object.keys()，Object.values()，Object.entries()

* Object.keys()

```js
var obj = { foo: 'bar', baz: 42 };
Object.keys(obj)
// ["foo", "baz"]
```
ES2017 引入了跟Object.keys配套的Object.values和Object.entries，作为遍历一个对象的补充手段，供for...of循环使用。

```js
let {keys, values, entries} = Object;
let obj = { a: 1, b: 2, c: 3 };

for (let key of keys(obj)) {
    console.log(key); // 'a', 'b', 'c'
}

for (let value of values(obj)) {
    console.log(value); // 1, 2, 3
}

for (let [key, value] of entries(obj)) {
    console.log([key, value]); // ['a', 1], ['b', 2], ['c', 3]
}
```

* Object.values()

```js
const obj = { foo: 'bar', baz: 42 };
Object.values(obj)
// ["bar", 42]
```

* Object.entries()

```js
const obj = { foo: 'bar', baz: 42 };
Object.entries(obj)
// [ ["foo", "bar"], ["baz", 42] ]
```

## Object.fromEntries()

Object.fromEntries()方法是Object.entries()的逆操作，用于将一个键值对数组转为对象。

```js
Object.fromEntries([
  ['foo', 'bar'],
  ['baz', 42]
])
// { foo: "bar", baz: 42 }
```

```js
// 例一
const entries = new Map([
  ['foo', 'bar'],
  ['baz', 42]
]);

Object.fromEntries(entries)
// { foo: "bar", baz: 42 }

// 例二
const map = new Map().set('foo', true).set('bar', false);
Object.fromEntries(map)
// { foo: true, bar: false }
```

```js
Object.fromEntries(new URLSearchParams('foo=bar&baz=qux'))
// { foo: "bar", baz: "qux" }
```

___
> 共同学习，共同进步