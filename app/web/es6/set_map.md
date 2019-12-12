# Set 和 Map 数据结构

## Set

* 增加

```js
let s = new Set();
s.add(1);
```

* 长度

```js
let s = new Set();
s.size
```

* 判断是否有无

```js
let s = new Set();
s.has(1);
```

* 删除

```js
let s = new Set();
s.delete(1);
```

* 清空

```js
let s = new Set();
s.clear();
```

* 遍历操作

```js
/* keys()：返回键名的遍历器
values()：返回键值的遍历器
entries()：返回键值对的遍历器
forEach()：使用回调函数遍历每个成员 */
let set = new Set(['red', 'green', 'blue']);

for (let item of set.keys()) {
    console.log(`key: ${item}`);
}

for (let item of set.values()) {
    console.log(`value: ${item}`);
}

for (let item of set.entries()) {
    console.log(`entries: ${item}`);
}

set.forEach((value, key) => console.log(`${key} : ${value}`));
```

* 应用

1. 去重

```js
let arr = [3, 5, 2, 2, 5, 3];
let unique = [...new Set(arr)];
console.log(unique);
```

2. 数组的map和filter方法也可以间接用于 Set 了

```js
let set = new Set([1, 2, 3]);
set = new Set([...set].map(x => x * 2));
// 返回Set结构：{2, 4, 6}

let set1 = new Set([1, 2, 3, 4, 5]);
set1 = new Set([...set1].filter(x => (x % 2) == 0));
// 返回Set结构：{2, 4}
```

3. Set 可以很容易地实现并集（Union）、交集（Intersect）和差集（Difference）

```js
let a = new Set([1, 2, 3]);
let b = new Set([4, 3, 2]);

// 并集
let union = new Set([...a, ...b]);
// Set {1, 2, 3, 4}

// 交集
let intersect = new Set([...a].filter(x => b.has(x)));
// set {2, 3}

// 差集
let difference = new Set([...a].filter(x => !b.has(x)));
// Set {1}
```

4. 遍历操作中改变原来的 Set 结构

```js
// 方法一
let set = new Set([1, 2, 3]);
set = new Set([...set].map(val => val * 2));
// set的值是2, 4, 6

// 方法二
let set1 = new Set([1, 2, 3]);
set1 = new Set(Array.from(set1, val => val * 2));
// set的值是2, 4, 6
```

## Map

* 增加

```js
const map = new Map();
map.set('foo', true);
```

* 长度

```js
const map = new Map();
map.set('foo', true);
map.size
```

* 判断有无

```js
const map = new Map();
map.set('foo', true);
map.has('foo');
```

* 删除

```js
const map = new Map();
map.set('foo', true);
map.delete('foo');
```

* 清空

```js
const map = new Map();
map.set('foo', true);
map.clear()
```

* 获取

```js
const map = new Map();
map.set('foo', true);
map.get('foo');
```

* 遍历方法

```js
/* keys()：返回键名的遍历器。
values()：返回键值的遍历器。
entries()：返回所有成员的遍历器。
forEach()：遍历 Map 的所有成员。 */
const map = new Map([
    ['F', 'no'],
    ['T', 'yes'],
]);

for (let key of map.keys()) {
    console.log(key);
}
// "F"
// "T"

for (let value of map.values()) {
    console.log(value);
}
// "no"
// "yes"

for (let item of map.entries()) {
    console.log(item[0], item[1]);
}
// "F" "no"
// "T" "yes"

for (let [key, value] of map.entries()) {
    console.log(key, value);
}
// "F" "no"
// "T" "yes"

// 等同于使用map.entries()
for (let [key, value] of map) {
    console.log(key, value);
}
// "F" "no"
// "T" "yes"
```

### 与其他数据结构的互相转换

* Map 转为数组

```js
const myMap = new Map()
    .set(true, 7)
    .set({foo: 3}, ['abc']);
[...myMap]
// [ [ true, 7 ], [ { foo: 3 }, [ 'abc' ] ] ]
```

* 数组 转为 Map

```js
new Map([
  [true, 7],
  [{foo: 3}, ['abc']]
])
// Map {
//   true => 7,
//   Object {foo: 3} => ['abc']
// }
```

* Map 转为对象

```js
function strMapToObj(strMap) {
    let obj = Object.create(null);
    for (let [k,v] of strMap) {
        obj[k] = v;
    }
    return obj;
}

const myMap = new Map()
    .set('yes', true)
    .set('no', false);
strMapToObj(myMap)
// { yes: true, no: false }
```

* 对象转为 Map

```js
function objToStrMap(obj) {
    let strMap = new Map();
    for (let k of Object.keys(obj)) {
        strMap.set(k, obj[k]);
    }
    return strMap;
}

objToStrMap({yes: true, no: false})
// Map {"yes" => true, "no" => false}
```

* Map 转为 JSON

```js
function strMapToJson(strMap) {
    return JSON.stringify(strMapToObj(strMap));
}

let myMap = new Map().set('yes', true).set('no', false);
strMapToJson(myMap)
// '{"yes":true,"no":false}'
```

* JSON 转为 Map

```js
function jsonToStrMap(jsonStr) {
    return objToStrMap(JSON.parse(jsonStr));
}

jsonToStrMap('{"yes": true, "no": false}')
// Map {'yes' => true, 'no' => false}
```

___
> 共同学习，共同进步