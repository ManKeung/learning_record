# Proxy

```js
// 原始数据
let obj = {
    time: '2017-03-11',
    name: 'net',
    _r: 123
};

// 代理商
let monitor = new Proxy(obj, {
    // 拦截对象属性
    get(target, key) {
        return target[key].replace('2017', '2018')
    },
    // 拦截对象设置shux
    set(target, key, value) {
        if (key === 'name') {
            return target[key] = value
        } else {
            return target[key]
        }
    },
    // 拦截key in objec操作
    has(target, key) {
        if (key === 'name') {
            return target[key]
        } else {
            return false
        }
    },
    // 拦截delete
    deleteProperty(target, key) {
        if (key.indexOf('_') > -1) {
            delete target[key]
            return true
        } else {
            return target[key]
        }
    },
    // 拦截Object.keys,Object.getOwnPropertySymbols,Object.getOwnPropertyNames
    ownKeys(target) {
        return Object.keys(target).filter(item => item != 'time')
    }
})

console.log('get', monitor.time)
monitor.name = 'mankeung';
console.log('set', monitor.name)
// console.log('has', 'name' in monitor, 'time' in monitor)
delete monitor.time;
// console.log('delete',monitor)
delete monitor._r;
// console.log('delete',monitor)
console.log('ownKeys', Object.keys(monitor))
```

___
> 共同学习，共同进步