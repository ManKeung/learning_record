# Decorator

* 类的装饰

```js
@testable
class Test {}

function testable(target) {
    target.isTestable = true
}

console.log(Test.isTestable)

/****************************/
@decorator
class A {}

// 等同于

class A {}
A = decorator(A) || A;
```

* 增加参数

```js
function testable(isTestable) {
    return function(target) {
        target.isTestable = isTestable
    }
}

@testable(true)
class MyTestableClass {}
MyTestableClass.isTestable // true

@testable(false)
class MyClass {}
MyClass.isTestable // false
```

* 添加实例属性

```js
function testable(target) {
    target.prototype.isTestable = true
}

@testable
class MyTestableClass {}

let obj = new MyTestableClass()
obj.isTestable // true
```

* 把Foo对象的方法添加到了MyClass的实例上面

```js
// mixins.js
export function mixins(...list) {
  return function (target) {
    Object.assign(target.prototype, ...list)
  }
}

// main.js
import { mixins } from './mixins'

const Foo = {
    foo() { console.log('foo') }
};

@mixins(Foo)
class MyClass {}

let obj = new MyClass()
obj.foo() // 'foo'
```

* 方法的装饰

```js
class Person {
    @readonly
    name() {
        return `${this.first} ${this.last}`
    }
}

/*
target: 原型对象
name: 装饰的属性名
descriptor: 该属性的描述对象
*/
function readonly (target, name, descriptor) {
    // descriptor对象原来的值如下
    // {
    //   value: specifiedFunction,
    //   enumerable: false,
    //   configurable: true,
    //   writable: true
    // }
    descriptor.writable = false
    return descriptor
}
```

___
> 共同学习，共同进步