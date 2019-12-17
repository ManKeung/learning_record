# mongoose示例

## 基本操作

```js
// 引入
const mongoose = require('mongoose')

// 建立连接
mongoose.connect('mongodb://localhost:27017/mktest', {
    useUnifiedTopology: true,
    useNewUrlParser: true
})

const db = mongoose.connection

// 失败警告
db.on('error', console.error.bind(console, 'connection error'))
// 连接成功提醒
db.once('open', () => {
    console.log('we are connected!')
})

// 数据类型
const types = mongoose.Schema.Types

// 操作users表（集合） 定义schema Schema里面的对象和数据库表里面的字段需要一一对应
const UserSchema = mongoose.Schema({
    name: types.String,
    age: types.Number,
    sex: types.String,
    subject: types.Mixed
})

// 定义数据库模型 操作数据库
// model里面的第一个参数 要注意：1首字母大写  2、要和数据库表（集合 ）名称对应  这个模型会和模型名称相同的复数的数据库表建立连接
// const User = mongoose.model('User', UserSchema) // 默认会操作 users表（集合）
const User = mongoose.model('User', UserSchema, 'user')

// 增
// const u = new User({
//     name: '闺女',
//     age: 0,
//     sex: '女',
//     subject: {
//         shuxue: 90,
//         yingyu: 85,
//         yuwen: 90
//     }
// })
// u.save().then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

// 删
// User.deleteOne({name: '123'}).then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

// 改
// User.updateOne({name: '闺女'}, {age: 1}).then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

// 查
User.find({age: {$gt: 1}}).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 模块化

* app.js

```js
const UserModel = require('./mongoose/userinfo')
const OrderModel = require('./mongoose/order')

const user = new UserModel({
    name: '老许',
    age: 40
})

// user.save().then(_data => {
//     UserModel.find().then(data => {
//         console.log(data)
//     }).catch(err => {
//         console.log(`数据查找失败${err}`)
//     })
// }).catch(err => {
//     console.log(`数据增加失败:${err}`)
// })
OrderModel.find().then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* db.js

```js
const mongoose = require('mongoose')
exports.types = mongoose.Schema.Types

mongoose.connect('mongodb://localhost:27017/mktest', {
    useUnifiedTopology: true,
    useNewUrlParser: true,
    useCreateIndex: true
}).then(data => {
    console.log(`数据库连接成功${data}`)
}).catch(err => {
    console.log(`数据库连接失败${err}`)
})

exports.mongoose = mongoose
```


* userinfo.js

```js
const {mongoose, types} = require('./db')

const UserInfoSchema = mongoose.Schema({
    name: types.String,
    age: types.Number,
    sex: {
        type: types.String,
        default: '男'
    }
})

module.exports = mongoose.model('UserInfo', UserInfoSchema, 'userinfo')
```

* order.js

```js
const {mongoose, types} = require('./db')

const OrderSchema = mongoose.Schema({
    order_id: types.String,
    uid: types.Number,
    trade_no: types.String,
    all_price: types.Number,
    all_num: types.Number
})

module.exports = mongoose.model('Order', OrderSchema, 'order')
```

* 性能测试

```js
console.time('user')
const UserModel = require('./mongoose/userinfo')
console.timeEnd('user')

console.time('order')
const Order = require('./mongoose/order')
console.timeEnd('order')

console.time('user2')
const UserModel2 = require('./mongoose/userinfo')
console.timeEnd('user2')
```

* 模型参数约定

```js
const {mongoose, types} = require('./db')

// mongoose数据校验:用户通过mongoose给mongodb数据库增加数据的时候，对数据的合法性进行的验证
// mongoose里面定义Schema:字段类型，修饰符、默认参数 、数据校验都是为了数据库数据的一致性
// Schema，为数据库对象的集合,每个schema会映射到mongodb中的一个collection,定义Schema可以理解为表结构的定义

const PersonSchema = mongoose.Schema({
    name: {
        type: types.String, // 指定类型
        trim: true, // 修饰符
        required: true
    },
    sn: {
        type: types.String,
        index: true, // 索引
        set(val) { // 自定义修饰符
            return `mk:${val}`
        },
        maxlength: 10,
        minlength: 4,
        // match: /^sn(.*)/,
        // validate: (sn) => {
        //     return sn.length >= 4
        // }
    },
    age: {
        type: types.Number,
        min: 0,
        max: 240,
    },
    status: {
        type: types.String,
        default: 'success', // 默认值
        enum: ['success', 'error'] // status的值必须在 对应的数组里面  注意枚举是用在String
    }
})

module.exports = mongoose.model('Person', PersonSchema, 'person')
```

## 关联查询

```js
const OrderModel = require('./mongoose/order')

// order表关联order_item
// OrderModel.find().then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

// order表关联order_item
OrderModel.aggregate([
    {
        $lookup: {
            from: 'order_item',
            localField: 'order_id',
            foreignField: 'order_id',
            as: 'items'
        }
    },
    {
        $match: {all_price: {$gte: 90}}
    }
]).then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

## 三表关联

* app.js

```js
const ArticleModel = require('./mongoose/article')

// 查询文章信息
// ArticleModel.find().then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

// 两表关联
// ArticleModel.aggregate([
//     {
//         $lookup: {
//             from: 'articlecate',
//             localField: 'cid',
//             foreignField: '_id',
//             as: 'cate'
//         }
//     }
// ]).then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })

// 三个表关联查询
ArticleModel.aggregate([
    {
        $lookup: {
            from: "articlecate",
            localField: "cid",
            foreignField: "_id",
            as: "cate"
        }
    }, {
        $lookup: {
            from: "user",
            localField: "author_id",
            foreignField: "_id",
            as: "user"
        }
    }
]).then(data => {
    console.log(JSON.stringify(data))
}).catch(err => {
    console.log(err)
})
```

* add.js

```js
const ArticleCateModel = require('./mongoose/articlecate')
const UserModel = require('./mongoose/user')
const ArticleModel = require('./mongoose/article')

// 分类的增加
// const cate = new ArticleCateModel({
//     title: '国内新闻',
//     description: '国内新闻'
// })

// cate.save().then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })
// id 5df86b3c1074f23f10a6a800

// 增加用户
// const user = new UserModel({
//     username: 'lisi',
//     password: '123456',
//     name: '李四',
//     age: 20,
//     sex: '男',
//     tel: 10086
// })

// user.save().then(data => {
//     console.log(data)
// }).catch(err => {
//     console.log(err)
// })
// id 5df86bcf4956d93f5083fd97

const article = new ArticleModel()
article.title = '这是一个国内新闻11111111'
article.cid = '5df86b3c1074f23f10a6a800' /*国内新闻*/
article.author_id = '5df86bcf4956d93f5083fd97'
article.author_name = '张三'
article.description = '这是一个国内新闻11111111 此处省略300字'
article.content = '习近平访问美国 这是一个国内新闻11111111'

article.save().then(data => {
    console.log(data)
}).catch(err => {
    console.log(err)
})
```

* user.js

```js
const {mongoose, types} = require('./db')
const Schrma = mongoose.Schema

const UserSchema = new Schrma({
    username: {
        type: types.String,
        unique: true
    },
    password: types.String,
    name: types.String,
    age: types.Number,
    sex: types.String,
    tel: types.Number,
    status: {
        type: types.Number,
        default: 1
    }
})

module.exports = mongoose.model('User', UserSchema, 'user')
```

* article.js

```js
const {mongoose, types} = require('./db')
const Schrma = mongoose.Schema

const ArticleSchema = new Schrma({
    title: {
        type: types.String,
        unique: true
    },
    cid: {
        type: types.ObjectId
    },
    author_id: {
        type: types.ObjectId
    },
    author_name: {
        type: types.String
    },
    description: types.String,
    content: types.String
})

module.exports = mongoose.model('Article', ArticleSchema, 'article')
```

* articlecate.js

```js
const {mongoose, types} = require('./db')
const Schrma = mongoose.Schema

const ArticleCateSchema = new mongoose.Schema({
    title: {
        type: types.String,
        unique: true
    },
    descripton: types.String,
    addtime: {
        type: Date,
        default: new Date()
    }
})

module.exports = mongoose.model('ArticleCate', ArticleCateSchema, 'articlecate')
```

### populate

* app.js

```js
// 注意使用 populate需要引入用到的model
const ArticleCateModel = require('./mongoose/articlecate')
const ArticleModel = require('./mongoose/article.js')
const UserModel = require('./mongoose/user.js')

// 文章表和 分类表的关联
ArticleModel.find().populate('cid').exec().then(data => {
    console.log(JSON.stringify(data))
}).catch(err => {
    console.log(err)
})

// 三个表关联
ArticleModel.find({}).populate('cid').populate('author_id').exec().then(data => {
    console.log(JSON.stringify(data))
}).catch(err => {
    console.log(err)
})
```

* article.js

```js
const {mongoose, types} = require('./db')
const Schrma = mongoose.Schema

const ArticleSchema = new Schrma({
    title: {
        type: types.String,
        unique: true
    },
    cid: {
        type: types.ObjectId,
        ref: 'ArticleCate' //cid和 文章分类建立关系。   model
    },
    author_id: {
        type: types.ObjectId,
        ref: 'ArticleCate' //cid和 文章分类建立关系。   model
    },
    author_name: {
        type: types.String
    },
    description: types.String,
    content: types.String
})

module.exports = mongoose.model('Article', ArticleSchema, 'article')
```

___
> 共同学习，共同进步