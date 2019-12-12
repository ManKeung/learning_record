# Promise

## 基本用法

```js
const promise = new Promise((resolve, reject) => {
    if (Math.random() * 10 > 5) {
        resolve('success')
    } else {
        reject('error')
    }
})

promise.then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
}).finally(() => {
    console.log('不管promise最后的状态，在执行完then或catch指定的回调函数以后，都会执行finally方法指定的回调函数。')
})
```

* 异步加载图片

```js
const loadImg = url => {
    return new Promise((resolve, reject) => {
        if (!url) {
            reject(new Error('url地址为空'))
            return
        }
        const img = new Image()
        img.src = url
        img.onload = () => {
            resolve(img)
        }
        img.onerror = (err) => {
            reject(new Error(`Could not load image at ${url}`))
            console.log(err)
        }
    })
}

loadImg('https://www.baidu.com/img/bd_logo1.png?where=super').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})

Promise.all([
    loadImg('https://www.baidu.com/img/bd_logo1.png?where=super'),
    loadImg(),
    loadImg('htp://www.baidu.com/01.png')
]).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})

const pall = Promise.race([
    loadImg('https://www.baidu.com/img/bd_logo1.png?where=super'),
    loadImg(),
    loadImg('htp://www.baidu.com/01.png')
])

pall.then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* allSettled/any

```js
const re1 = Promise.resolve(1)
const re2 = Promise.resolve(2)
const rej1 = Promise.reject(-1)
const rej2 = Promise.reject(-2)

const allSettledPromise = Promise.allSettled([re1, re2, rej1, rej2])
allSettledPromise.then(results => {
    console.log(results)
})

const anyPromise = Promise.any([re1, re2, rej1, rej2])
anyPromise.then(results => {
    console.log(results)
}).catch(err => {
    console.log(err)
})
```

___
> 共同学习，共同进步