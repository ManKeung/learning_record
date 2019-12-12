# Generator

* 基本概念

```js
function* helloWorldGenerator() {
    yield 'hello'
    yield 'world'
    return 'ending'
}

let hw = helloWorldGenerator()
console.log(hw.next())
console.log(hw.next())
console.log(hw.next())
console.log(hw.next())
```

* 用同步的流程来表示异步的操作

```js
function request() {
    return new Promise(function (resolve, reject) {
        setTimeout(function () {
            resolve("拿到的数据")
        }, 1000)
    });
}

function* gen() {
    yield request()
    yield request()
    yield request()
}
let it = gen();
it.next().value.then(function (data) {
    console.log(data, 1)
    return it.next().value
}).then(function (data) {
    console.log(data, 2)
    return it.next().value
}).then(function (data) {
    console.log(data, 3)
})
```

___
> 共同学习，共同进步