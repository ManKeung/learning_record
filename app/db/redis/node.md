# nodejs

```bash
yarn add ioredis
```

## 基本使用

```js
// db.js
const Redis = require('ioredis')

const redis = {
    port: 6379,
    host: 'localhost',
    family: 4,
    db: 0
}

module.exports = new Redis(redis)
```

* 查看所有

```js
redis.keys('*').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 删除指定key

```js
redis.del('test').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 删除所有

```js
redis.flushall().then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 查看类型

```js
redis.type('test').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 设置键有效期

```js
redis.expire('test', 60).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 字符串

* 普通设置

```js
const redis = require('./redis/db')

redis.set('test', 'haha').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 设置并加过期时间

```js
redis.set('exp', '123', 'EX', 60).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

```js
redis.setex('exp2', 60, '过期时间60').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 追加

```js
redis.append('str', 'xixi')then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取值

```js
redis.get('str').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 设置每次加1

```js
redis.incr('num').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 列表

* 列表右侧增加值

```js
redis.rpush('arr', 'a').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 列表左侧增加值

```js
redis.lpush('arr', 'b').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 右侧删除值

```js
redis.rpop('arr').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 左侧删除值

```js
redis.lpop('arr').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 删除指定元素

```js
// 参数
// key count value
// 将列表中前count次出现的值为value的元素移除
// count > 0: 从头往尾移除
// count < 0: 从尾往头移除
// count = 0: 移除所有
redis.lrem('arr', 0, 'mk1').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取值

```js
redis.lrange('arr', 0, 2).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 在指定元素的前或后插⼊新元素

```js
// key before 或 after 现有元素 新元素
redis.linsert('arr', 'BEFORE', 'mk0', 'mankeng').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 设置指定索引位置的元素值

```js
redis.lset('arr', 0, 'mq').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 无需集合

* 设置

```js
redis.sadd('s', '无序集合').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 删除

```js
redis.srem('s', '无序集合').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取值

```js
redis.smembers('s').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 有序集合

* 设置

```js
redis.zadd('ss', [1, 2]).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取

```js
redis.zrange('ss', 0, -1).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 删除

```js
redis.zrem('ss', '2').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 删除权重在指定范围的元素

```js
redis.zremrangebyscore('ss', 0, 10).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 哈希

* 设置

```js
redis.hset('user', 'age', 18, 'name', 'mankeung').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取指定键所有的属性

```js
redis.hgetall('user').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取⼀个属性的值

```js
redis.hget('user', 'name').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取多个属性的值

```js
redis.hmget('user', ['age', 'name']).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 获取所有属性的值

```js
redis.hvals('user').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* 删除

```js
redis.hdel('user', 'age').then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 发布订阅

* pub.js

```js
const redis = require('./redis/db')

redis.publish('news', 'Hello world!')
redis.publish('music', 'Hello again!')
```

* sub.js

```js
const redis = require('./redis/db')

redis.subscribe('news', 'music')

redis.on('message', function (channel, message) {
    // 收到消息 Hello world! from channel news
    // 收到消息 Hello again! from channel music
    console.log('Receive message %s from channel %s', message, channel)
})

// 还有一个是事件叫做`messageBuffer`,和message是一样的
// 返回buffer，替代字符串
redis.on('messageBuffer', function (channel, message) {
    // Both `channel` and `message` are buffers.
})
```

## 管道流水线

```js
const redis = require('./redis/db')

const pipeline = redis.pipeline()

pipeline.set('msg', 'mankeung').get('msg').exec().then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 事务

```js
const redis = require('./redis/db')

const multi = redis.multi()

multi.set('foo').set('foo', 'new value').exec().then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

___
> 共同学习，共同进步