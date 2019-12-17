# 基本使用

## 创建数据库

* 清屏

```bash
cls
```

* 查看所有数据库列表

```bash
show dbs
```

* 使用数据库/创建数据库

```bash
use mktest
```

> 没有数据库就创建

* 显示当前的数据集合(相当于mysql表)

```bash
show collections
```

* 删除数据库

```bash
db.dropDatabase()
```

> 当前所在的数据库

* 创建集合

```bash
db.createCollection('user')
```

* 删除集合

```bash
db.COLLECTION_NAME.drop()
# db.user.drop()
```

## 插入数据

```bash
db.user.insert({name: 'zhangsan'})
```

## 删除数据

```bash
db.user.remove({name: 'zhangsan'})
```

## 更新数据

* 查找名字叫做小明的，把年龄更改为16岁

```bash
db.student.update({name: '小明'}, {$set: {age: 16}})
```

* 查找数学成绩是70，把年龄更改为33岁

```bash
db.student.update({score.shuxue: 70}, {$set: {age: 33}})
```

* 更改所有匹配项目

```bash
db.student.update({sex: '男'}, {$set: {age: 33}}, {multi: true})
```

* 完整替换

```bash
db.student.update({name: '小明'}, {name: '大明', age: 16})
```

* 全部更新

```bash
db.users.update({name: 'Lisi'}, {$inc: {age: 50}}, false, true)
# 相当于
# update users set age = age + 50 where name = ‘Lisi’
```

```bash
db.users.update({name: 'Lisi'}, {$inc: {age: 50}, $set: {name: 'hoho'}}, false, true)
# 相当于
# update users set age = age + 50, name = ‘hoho’ where name = ‘Lisi’
```

* 只更新一条

```bash
db.col.update({count: {$gt: 10} } , {$inc: {count: 1}}, false, false)
```

## **查询**

* 查询所有

```bash
db.user.find()
```

* 查询去掉后的当前聚集集合中的某列的重复数据

```bash
db.user.distinct('name')
```

* 查询 age = 22 的记录

```bash
db.user.find({age: 22})
```

* 查询 age > 22 的记录

```bash
db.user.find({age: {$gt: 22}})
# $gte 大于等于
```

* 查询 age < 22  的记录

```bash
db.userInfo.find({age: {$lt: 22}})
# $lte 小于等于
```

* 查询 age >= 23 并且 age <= 26

```bash
db.userInfo.find({age: {$gte: 23, $lte: 26}})
```

* 查询 name 中包含 mongo 的数据 模糊查询用于搜索

```bash
db.userInfo.find({name: /mongo/})
```

* 查询 name 中以 mongo 开头的

```bash
db.userInfo.find({name: /^mongo/})
```

* 查询指定列 name 、age 数据

```bash
db.userInfo.find({}, {name: 1, age: 1})
```

* 查询指定列 name 、age 数据, age > 25

```bash
db.userInfo.find({age: {$gt: 25}}, {name: 1, age: 1})
```

* 按照年龄排序 1 升序 -1 降序

```bash
db.userInfo.find().sort({age: 1})
```

* 查询 name = zhangsan, age = 22 的数据

```bash
db.userInfo.find({name: 'zhangsan', age: 22})
```

* 查询前 5 条数据

```bash
db.userInfo.find().limit(5)
```

* 查询 10 条以后的数据

```bash
db.userInfo.find().skip(10)
```

* 查询在 5-10 之间的数据

```bash
db.userInfo.find().limit(10).skip(5)
# 可用于分页，limit 是 pageSize，skip 是第几页*pageSize
```

* or 与 查询

```bash
db.userInfo.find({$or: [{age: 22}, {age: 25}]})
```

* findOne 查询第一条数据

```bash
db.userInfo.findOne()
# db.userInfo.find().limit(1)
```

* 查询某个结果集的记录条数 统计数量

```bash
db.userInfo.find({age: {$gte: 25}}).count()
# 如果要返回限制之后的记录数量，要使用 count(true)或者 count(非 0)
# db.users.find().skip(10).limit(5).count(true)
```

## 索引

索引是对数据库表中一列或多列的值进行排序的一种结构， 可以让我们查询数据库变得
更快。MongoDB 的索引几乎与传统的关系型数据库一模一样，这其中也包括一些基本的查询优化技巧。

### 创建索引的命令

```bash
db.user.ensureIndex({username: 1}
```

### 获取当前集合的索引

```bash
db.user.getIndexes()
```

### 删除索引的命令是

```bash
db.user.dropIndex({username: 1})
```

### 复合索引

```bash
# 数字 1 表示 username 键的索引按升序存储，-1 表示 age 键的索引按照降序方式存储。
db.user.ensureIndex({username: 1, age: -1})
```

```bash
# 创建索引时为其指定索引名
db.user.ensureIndex({username: 1},{name: 'userindex'}
```

### 唯一索引

```bash
db.user.ensureIndex({userid: 1}, {unique: true})

# 创建复合唯一索引
# db.user.ensureIndex({userid: 1, age: 1}, {unique: true})
```

### 索引的一些参数

Parameter | Type | Description
---- | ---- | ----
background | Boolean | 建索引过程会阻塞其他数据库操作，background可以指定以后台方式创建索引，即增加啊"background"可选参数。"background"默认值为false
unique | Boolean | 建立的索引是否唯一。指定true创建唯一索引，默认false
name | String | 索引名称，如果未指定，MongoDB的通过链接索引的字段名和排序顺序生成索引名称
dropDups | Boolean | 在建立唯一索引时是否删除重复记录，指定true创建唯一索引，默认false

如果在为已有数据的文档创建索引时，可以执行下面的命令，以使 MongoDB 在后台创
建索引，这样的创建时就不会阻塞其他操作。但是相比而言，以阻塞方式创建索引，会使整个创建过程效率更高，但是在创建时 MongoDB 将无法接收其他的操作。

```bash
db.user.ensureIndex({username: 1}, {background: true})
```

## 数据的导出导入

### 导出

```bash
mongodump -h dbhost -d dbname -o dbdirectory
```

### 导出

```bash
mongorestore -h dbhost -d dbname path
```

___
> 共同学习，共同进步