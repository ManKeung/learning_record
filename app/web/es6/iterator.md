# Iterator

* 模拟next方法

```js
const it = makeIterator(['a', 'b'])

console.log(it.next()) // { value: "a", done: false }
console.log(it.next()) // { value: "b", done: false }
console.log(it.next()) // { value: undefined, done: true }

function makeIterator(array) {
    var nextIndex = 0
    return {
        next: function () {
            return nextIndex < array.length ? {
                value: array[nextIndex++],
                done: false
            } : {
                value: undefined,
                done: true
            };
        }
    }
}
```

* Symbol.iterator

```js
let arr = ['hello', 'world']
let map = arr[Symbol.iterator]()
console.log(map.next())
console.log(map.next())
console.log(map.next())

let obj = {
    start: [1, 3, 2],
    end: [7, 9, 8],
    [Symbol.iterator]() {
        let self = this;
        let index = 0;
        let arr = self.start.concat(self.end);
        let len = arr.length;
        return {
            next() {
                if (index < len) {
                    return {
                        value: arr[index++],
                        done: false
                    }
                } else {
                    return {
                        value: arr[index++],
                        done: true
                    }
                }
            }
        }
    }
}
for (let key of obj) {
    console.log(key)
}
```

___
> 共同学习，共同进步