# Nodejs

## mondodb

* 安装

```bash
yarn add mogodb
```
* 示例

```js
const MongoDB = require('mongodb')
const MongoClient = MongoDB.MongoClient
const ObjectID = MongoDB.ObjectID

// 定义链接数据库地址
const url = 'mongodb://localhost:27017'
const dbName = 'mktest'
const id = '5df7495bfce5440e879ecc72'
const objectID = new ObjectID(id) // mongodb里面查询 _id 把字符串转换成对象
console.log(typeof objectID)

// 链接数据库
MongoClient.connect(url, { useUnifiedTopology: true }, (err, client) => {
    if (err) {
        console.log('数据库连接失败')
        client.close()
        return
    }

    const db = client.db(dbName) // 获取db对象
    // 查询
    // db.collection('order').find().toArray((err, docs) => {
    //     if (err) {
    //         console.log('获取数错误')
    //         client.close()
    //         return
    //     }

    //     console.log(docs)
    //     client.close()
    // })
    // 插入
    // const json = {name: 'mankeung', age: 16, sex: '男'}
    // db.collection('user').insertOne(json, (err, result) => {
    //     if (err) {
    //         console.log('新增失败')
    //         return
    //     }
    //     console.log(result)
    //     client.close()
    // })
    // 修改
    // const json1 = {name: 'mankeung'}
    // const json2 = {age: 28}
    // db.collection('user').updateOne(json1, {
    //     $set: json2
    // }, (err, result) => {
    //     if (err) {
    //         console.log('修改错误')
    //         return
    //     }
    //     console.log(result)
    //     client.close()
    // })

    // 删除
    // const json = {name: 'mankeung'}
    // db.collection('user').remove(json, (err, result) => {
    //     if (err) {
    //         console.log('删除失败')
    //         return
    //     }
    //     console.log(result)
    //     client.close()
    // })

    db.collection("order").aggregate([{
            $lookup: {
                from: "order_item",
                localField: "order_id",
                foreignField: "order_id",
                as: "items"
            }
        },
        {
            $match: {
                "all_price": {
                    $gte: 90
                }
            }
        }

    ]).toArray(function (_err, docs) {
        console.log(docs)
        client.close()
    })
})
```

## mongoose

* 安装

```bash
yarn add mongoose
```

* 引入mongoose

```js
const mongoose = require('mongoose')
mongoose.connect('mongodb://localhost/test')
// 如果有账户密码需要采用下面的连接方式：
mongoose.connect('mongodb://eggadmin:123456@localhost:27017/eggcms')
```

### 定义Schema

数据库中的 Schema， 为数据库对象的集合。 schema 是 mongoose 里会用到的一种数据模式，可以理解为表结构的定义；每个 schema 会映射到 mongodb 中的一个 collection，它不具备操作数据库的能力

```js
const UserSchema=mongoose.Schema({
name: String,
age: Number,
status: 'number'
})
```

### 创建数据模型

定义好了 Schema，接下就是生成 Model。model 是由 schema 生成的模型，可以对数据库的操作。

>注意：mongoose.model 里面可以传入两个参数也可以传入三个参数

mongoose.model（参数 1:模型名称（首字母大写），参数 2:Schema）
mongoose.model（参数 1:模型名称（首字母大写），参数 2:Schema，参数 3:数据库集合名称）

如果传入2个参数的话:这个模型会和模型名称相同的复数的数据库建立连接：如通过下面方法创建模型，那么这个模型将会操作 users 这个集合

如果传入3个参数的话:模型默认操作第三个参数定义的集合名称

```js
const User=mongoose.model('User', UserSchema)
```

### 查找数据

```js
User.find({}, (err,docs) => {
    if(err){
        console.log(err)
        return
    }
    console.log(docs)
})
```

### 增加数据

```js
const u = new User({ //实例化模型 传入增加的数据
    name: 'lisi2222333',
    age: 20,
    status: true
})
u.save()
```

### 修改数据

```js
User.updateOne({ name: 'lisi2222' }, { name: '哈哈哈' }, (err, res) => {
    if(err){
        console.log(err)
        return
    }
    console.log('成功')
})
```

### 删除数据

```js
User.deleteOne({ _id: '5b72ada84e284f0acc8d318a' }, function (err) {
    if (err) {
        console.log(err)
        return
    }
    // deleted at most one tank document
    console.log('成功')
})
```

### 保存成功查找

```js
const u = new User({
    name: 'lisi2222333',
    age: 20,
    status: true //类型转换
})
u.save(function (err, docs) {
    if (err) {
        console.log(err)
        return
    }
    //console.log(docs)
    User.find({}, function (err, docs) {
        if (err) {
            console.log(err)
            return
        }
        console.log(docs)
    })
})
```

### mongoose预定义模式修饰符

lowercase、uppercase 、trim mongoose 提供的预定义模式修饰符，可以对我们增加的数据进行一些格式化。

```js
const UserSchema = mongoose.Schema({
    name: {
        type: String,
        trim: true
    },
    age: Number,
    status: {
        type: Number,
        default: 1
    }
})
```

### Mongoose Getters与Setters

除了mongoose内置的修饰符以外，我们还可以通过set（建议使用）修饰符在增加数据的时候对数据进行格式化。也可以通过 get（不建议使用）在 实例获取数据的时候对数据进行格式化。

```js
const NewsSchema = mongoose.Schema({
    title: "string",
    author: String,
    pic: String,
    redirect: {
        type: String,
        set(url) {
            if (!url) return url;
            if (url.indexOf('http://') != 0 && url.indexOf('https://') != 0) {
                url = 'http://' + url;
            }
            return url;
        }
    },
    content: String,
    status: {
        type: Number,
        default: 1
    }
})
```

```js
const NewsSchema = mongoose.Schema({
    title: "string",
    author: String,
    pic: String,
    redirect: {
        type: String,
        set(url) {
            if (!url) return url;
            if (url.indexOf('http://') != 0 && url.indexOf('https://') != 0) {
                url = 'http://' + url;
            }
            return url;
        },
        get: function (url) {
            if (!url) return url;
            if (url.indexOf('http://') != 0 && url.indexOf('https://') != 0) {
                url = 'http://' + url;
            }
            return url;
        }
    },
    content: String,
    status: {
        type: Number,
        default: 1
    }
})
```

### Mongoose索引

索引是对数据库表中一列或多列的值进行排序的一种结构，可以让我们查询数据库变得更
快。MongoDB 的索引几乎与传统的关系型数据库一模一样，这其中也包括一些基本的查询
优化技巧。

mongoose 中除了以前创建索引的方式，我们也可以在定义 Schema 的时候指定创建索引。

```js
const DeviceSchema = new mongoose.Schema({
    sn: {
        type: Number,
        // 唯一索引
        unique: true
    },
    name: {
        type: String,
        // 普通索引
        index: true
    }
})
```

### [https://mongoosejs.com/docs/queries.html

+ Model.deleteMany()
+ Model.deleteOne()
+ Model.find()
+ Model.findById()
+ Model.findByIdAndDelete()
+ Model.findByIdAndRemove()
+ Model.findByIdAndUpdate()
+ Model.findOne()
+ Model.findOneAndDelete()
+ Model.findOneAndRemove()
+ Model.findOneAndUpdate()
+ Model.replaceOne()
+ Model.updateMany()
+ Model.updateOne()

### 扩展Mongoose CURD方法

```js
const mongoose = require('./db.js')
const UserSchema = mongoose.Schema({
    name: {
        type: String
    },
    age: Number,
    status: {
        type: Number,
        default: 1
    }
})
// 静态方法
UserSchema.statics.findByUid = function (uid, cb) {
    this.find({
        "_id": uid
    }, function (err, docs) {
        cb(err, docs)
    })
}
// 实例方法
UserSchema.methods.print = function () {
    console.log('这是一个实例方法')
    console.log(this)
}
module.exports = mongoose.model('User', UserSchema, 'user')
```

### Mongoose校验参数

参数 | 描述
--- | ---
required | 表示这个数据必须传入
max | 用于 Number 类型数据，最大值
min | 用于 Number 类型数据，最小值
enum | 枚举类型，要求数据必须满足枚举值 enum: ['0', '1', '2']
match | 增加的数据必须符合 match（正则）的规则
maxlength | 最大值
minlength | 最小值

```js
const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    age: {
        type: Number,
        // 是否必须的校验器
        required: true,
        // 数字类型的最大值校验器
        max: 120,
        // 数字类型的最小值校验器
        min: 0
    },
    status: {
        type: String,
        // 设置字符串的可选值
        enum: ['0', '1', '2']
    },
    phone: {
        type: Number,
        match: /^\d{11}$/
    },
    desc: {
        type: String,
        maxlength: 20,
        minlength: 10
    }
})
```

### Mongoose自定义的验证器

在缺省情况下创建的索引均不是唯一索引。下面的示例将创建唯一索引，如：

```js
const UserSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
    },
    age: {
        type: Number,
        // 是否必须的校验器
        required: true,
        // 数字类型的最大值校验器
        max: 120,
        // 数字类型的最小值校验器
        min: 0
    },
    status: {
        type: String,
        // 设置字符串的可选值
        enum: ['0', '1', '2']
    },
    phone: {
        type: Number,
        match: /^\d{11}$/
    },
    desc: {
        type: String,
        // 自定义的验证器，如果通过验证返回 true，没有通过则返回 false
        validate: function (desc) {
            return desc.length >= 10
        }
    }
})
```

### Mongoose (populate)[https://mongoosejs.com/docs/populate.html]

* 关联查询

1. 定义ref

```js
const ArticleSchema = new Schema({
    title: {
        type: String,
        unique: true
    },
    cid: {
        type: Schema.Types.ObjectId,
        ref: 'ArticleCate' //model 的名称
    },
    /*分类 id*/
    author_id: {
        type: Schema.Types.ObjectId,
        ref: 'User'
    },
    /*用户的 id*/
    author_name: {
        type: String
    },
    descripton: String,
    content: String
})
```

2. 关联查询

```js
ArticleModel.find({}).populate('cid').populate('author_id').exec(function (err, docs) {
    console.log(docs)
})
```

___
> 共同学习，共同进步