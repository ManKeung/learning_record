# Class

* 定义类

```js
class Point {
    constructor(x=1, y=2) {
        this.x = x
        this.y = y
    }

    toString() {
        return `(${this.x}, ${this.y})`
    }

    add() {
        return `x + y = ${this.x + this.y}`
    }
}

const point = new Point(2, 4)
console.log(point.toString())
console.log(point.x)
console.log(point.add())
```

* 静态方法

```js
class Foo {
    static classMethod() {
        return 'hello'
    }
}

console.log(Foo.classMethod())
```

* 静态属性

```js
class Foo {

}
Foo.prop = 1
console.log(Foo.prop)
```

* 继承

```js
class Point {
    constructor(x, y) {
        this.x = x
        this.y = y
    }
}

class ColorPoint extends Point {
    constructor(x, y color) {
        super(x, y)
        this.color = color
    }
}
```

* 单例模式

```js
// es5
var Singleton = function (name) {
    this.name = name
    //一个标记，用来判断是否已将创建了该类的实例
    this.instance = null
    console.log(name)
}
// 提供了一个静态方法，用户可以直接在类上调用
Singleton.getInstance = function (name) {
    // 没有实例化的时候创建一个该类的实例
    if (!this.instance) {
        this.instance = new Singleton(name)
    }
    // 已经实例化了，返回第一次实例化对象的引用
    return this.instance
}

var a = Singleton.getInstance('sven1')
var b = Singleton.getInstance('sven2')

// es6
class Singleton {
    constructor(name) {
        this.name = name
        this.instance = null
        console.log(name)
    }
    // 构造一个广为人知的接口，供用户对该类进行实例化
    static getInstance(name) {
        if (!this.instance) {
            this.instance = new Singleton(name)
        }
        return this.instance
    }
}

const a = Singleton.getInstance('sven1')
const b = Singleton.getInstance('sven1')
```

___
> 共同学习，共同进步