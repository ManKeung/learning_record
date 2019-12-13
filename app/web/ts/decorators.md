# 装饰器

* 命令

```bash
tsc --target ES5 --experimentalDecorators
```

* tsconfig.json

```json
{
    "compilerOptions": {
        "target": "ES5",
        "experimentalDecorators": true
    }
}
```

## 类装饰器

```ts
// 参数params就是被装饰的类HttpClient
function log(params: any) {
    console.log(params)  // class HttpClient
}
@log
class Test {
    constructor() {

    }
}
```

* 动态扩展属性属性和方法

```ts
function log(params: Function) {
    params.prototype.url = 'xxx'
    params.prototype.getUrl = () => {
        console.log(params.prototype.url)
    }

}
@log
class Test {
    [x: string]: any
    name: string
    constructor() {
        this.name = 'mk'
    }
}

const a = new Test()
a.getUrl()
console.log(a.name)
```

* 装饰器工厂：闭包

```ts
function log(params: string) {
    return (target: Function) => {
        target.prototype.url = params
    }
}
@log('mankeung')
class Test {
    [x: string]: any
    constructor() {
    }
}

const a = new Test()
console.log(a.url)

// 如果不想给装饰器传参，可以把参数声明为可选参数，但使用装饰器时仍然不能丢失小括号！
function log(params?: string) {
    return (target: Function) => {
        target.prototype.url = params || '默认'
    }
}
@log()
class Test {
    [x: string]: any
    constructor() {
    }
}
```

* 重载构造函数

```ts
function log(target: any) {
    return class extends target {
        url = 'change url'
        getUrl() {
            console.log('getUrl', this.url)
        }
    }
}
@log
class Test {
    public url:string|undefined
    constructor() {
        this.url = 'init url'
    }
    getUrl() {
        console.log(this.url)
    }
}

const a = new Test()
a.getUrl()
```

* 修改类的定义

```ts
function fn<T extends {new(...args:any[]):{}}>(constructor: T): T {
    class Ps extends constructor {
        age: number = 20; // 扩展一个类型为number的属性age
    }

    return Ps
}

@fn
class Person {
    [x: string]: any;
}

let p = new Person(); // 装饰之后的Person已经变成了Ps
console.log(p.age)
```

```ts
function fn (v: number) {
    return <T extends { new(...args: any[]): {} }>(constructor: T): T => {
        class Ps extends constructor {
            age: number = v; // 扩展一个类型为number的属性age
        }

        return Ps
    }
}

@fn(10)
class Person {
    [x: string]: any;
}

@fn(20)
class Cat {
    [x: string]: any;
}

let p = new Person(); // 装饰之后的Person已经变成了Ps
console.log(p.age)
let c = new Cat();
console.log(c.age)
```

## 属性的装饰

```ts
function log(params:any) {
    return function(target:any, attr:any) {
        console.log(target)
        console.log(attr)
        target[attr] = params // 通过原型对象修改属性值 = 装饰器传入的参数
        target.api = 'xxx' // 扩展属性
        target.run = function() { // 扩展方法
            console.log('run ...')
        }
    }
}

class Test {
    @log('https://www.mkimq.com')
    public url:any|undefined
    constructor() {}
    getUrl() {
        console.log(this.url)
    }
}

const t:any = new Test()
t.getUrl()
console.log(t.api)
t.run()
```

## 方法的装饰

```ts
function get(params: any) {
    console.log(params) // 装饰器传入的参数：http://baidu.com
    return function (target: any, methodName: any, desc: any) {
        console.log(target)  // { constructor:f, getData:f }
        console.log(methodName)  // getData
        console.log(desc)  // {value: ƒ, writable: true, enumerable: false, configurable: true} value就是方法体
        /* 修改被装饰的方法 */
        //1. 保存原方法体
        var oldMethod = desc.value
        //2. 重新定义方法体
        desc.value = function (...args: any[]) {
            //3. 把传入的数组元素都转为字符串
            let newArgs = args.map((item) => {
                return String(item)
            })
            //4. 执行原来的方法体
            oldMethod.apply(this, newArgs)
            // 等效于 oldMethod.call(this, ...newArgs)
        }
    }
}
class HttpClient {
    constructor() { }
    @get('http://baidu.com')
    getData(...args: any[]) {
        console.log('getData: ', args)
    }
}
var http = new HttpClient()
http.getData(1, 2, true)  // getData: ["1", "2", "true"]
```

## 方法参数装饰器

```ts
function logParams(params: any) {
    console.log(params)  // 装饰器传入的参数：uuid
    return function (target: any, methodName: any, paramIndex: any) {
        console.log(target)  // { constructor:f, getData:f }
        console.log(methodName)  // getData
        console.log(paramIndex)  // 0
    }
}
class HttpClient {
    constructor() { }
    getData(@logParams('uuid') uuid: any) {
        console.log(uuid)
    }
}
```

> 注意：参数装饰器只能用来监视一个方法的参数是否被传入
> 参数装饰器在Angular中被广泛使用,特别是结合reflect-metadata库来支持实验性的Metadata API
> 参数装饰器的返回值会被忽略

## 装饰器的执行顺序

* 装饰器组合：TS支持多个装饰器同时装饰到一个声明上，语法支持从左到右，或从上到下书写

```ts
@f @g x

@f
@g
x
```

* 在TypeScript里，当多个装饰器应用在一个声明上时会进行如下步骤的操作
    + 由上至下依次对装饰器表达式求值
    + 求值的结果会被当作函数，由下至上依次调用

* 不同装饰器的执行顺序：属性装饰器 > 方法装饰器 > 参数装饰器 > 类装饰器

```ts
function logClz11(params: string) {
    return function (target: any) {
        console.log('logClz11')
    }
}
function logClz22(params?: string) {
    return function (target: any) {
        console.log('logClz22')
    }
}
function logAttr(params?: string) {
    return function (target: any, attrName: any) {
        console.log('logAttr')
    }
}
function logMethod(params?: string) {
    return function (target: any, methodName: any, desc: any) {
        console.log('logMethod')
    }
}
function logParam11(params?: any) {
    return function (target: any, methodName: any, paramIndex: any) {
        console.log('logParam11')
    }
}
function logParam22(params?: any) {
    return function (target: any, methodName: any, paramIndex: any) {
        console.log('logParam22')
    }
}

@logClz11('http://baidu.com')
@logClz22()
class HttpClient {
    @logAttr()
    public url: string | undefined

    constructor() { }

    @logMethod()
    getData() {
        console.log('get data')
    }

    setData(@logParam11() param1: any, @logParam22() param2: any) {
        console.log('set data')
    }
}
// logAttr --> logMethod --> logParam22 --> logParam11 --> logClz22 --> logClz11
```

___
> 共同学习，共同进步