# 基本使用

## 公共命令

* 查看所有

```bash
keys *
```

* 删除指定key

```bash
del key
```

* 删除所有

```bash
flushall
```

* 查看类型

```bash
type key
```

* 设置键有效期

```bash
expire key seconds
```

* 查看有效时间

```bash
# 以秒为单位
# (integer) -2 没有这个键
# (integer) -1 一直有效
ttl key
```

## 字符串

* 普通设置

```bash
set key value
```

* 设置并加过期时间

```bash
set key value EX 30 # 表示30秒过期
# 方式二
# setex key seconds value
```

* 设置多个值

```bash
set key1 value1 key2 value2 ...
```

* 追加值

```bash
append key value
```

* 获取值

```bash
get key
```

* 设置值每次加1

```bash
incr key
```

## 列表

Redis 列表是简单的字符串列表，按照插入顺序排序。你可以添加一个元素到列表的头部（左边）或者尾部（右边）

* 列表右侧增加值

```bash
rpush key value
```

* 列表左侧增加值

```bash
lpush key value
```

* 右侧删除值

```bash
rpop key
```

* 左侧删除值

```bash
lpop key
```

* 删除指定元素
    - 将列表中前count次出现的值为value的元素移除
    - count > 0: 从头往尾移除
    - count < 0: 从尾往头移除
    - count = 0: 移除所有

```bash
lrem key count value
```

* 获取数据

```bash
lrange key start stop
# lrange key 0 -1 全部
# lrange key 0 0 第一个
```

* 在指定元素的前或后插⼊新元素

```bash
linsert key before 或 after 现有元素 新元素
```

* 设置指定索引位置的元素值

```bash
# 索引可以是负数，表示尾部开始计数，如-1表示最后⼀个元素
lset key index value
```

## 集合

### 无需集合

Redis的Set是String类型的无序集合。集合成员是唯一的，这就意味着集合中不能出现重复的数据。

* 增加数据

```bash
sadd key value
```

* 删除

```bash
srem key value
```

* 获取值

```bash
smembers key
```

### 有序集合

sorted set，有序集合
元素为string类型
元素具有唯⼀性，不重复
每个元素都会关联⼀个double类型的score，表示权重，通过权重将元素从⼩到⼤排序
说明：没有修改操作

* 增加

```bash
zadd key score1 member1 score2 member2 ...
```

* 获取

```bash
zrange key start stop
```

* 删除

```bash
zrem key member1 member2 ...
# 删除权重在指定范围的元素
zremrangebyscore key min max
```

## 哈希

Redis hash是一个string类型的field和value的映射表，hash特别适合用于存储对象。

* 设置

```bash
hset key field value field value...
# 设置键 user的属性name为itheima
hset user name itheima
```

* 获取

```bash
# 获取指定键所有的属性
hgetall key

# 获取⼀个属性的值
hget key field

# 获取多个属性的值
hmget key field1 field2 ...

# 获取所有属性的值
hvals key
```

* 删除

```bash
# 删除属性，属性对应的值会被⼀起删除
hdel key field1 field2...
```

___
> 共同学习，共同进步