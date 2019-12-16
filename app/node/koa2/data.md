# 连接数据库

## mongodb

```bash
# 安装
yarn add mongodb
```

* 示例

```js
// app.js
const Koa = require('koa')
const router = require('koa-router')()
const render = require('koa-art-template')
const bodyParser = require('koa-bodyparser')
const path = require('path')
const DB = require('./model/db')

const app = new Koa()

// 配置post提交数据的中间件
app.use(bodyParser())

// 配置 koa-art-template模板引擎
render(app, {
    root: path.join(__dirname, 'views'), // 视图的位置
    extname: '.html', // 后缀名
    debug: process.env.NODE_ENV !== 'production' // 是否开启调试模式
})

router
    .get('/', async (ctx) => {
        let list = await DB.find('user')
        await ctx.render('index', {
            list
        })
    })
    .get('/edit', async (ctx) => {
        // 通过get传过来的id来获取用户信息
        let id = ctx.query.id
        let data = await DB.find('user', {
            '_id': DB.getObjectId(id)
        })
        // 获取用户信息
        await ctx.render('edit', {
            list: data[0]
        })
    })
    .post('/doEdit', async (ctx) => {
        let id = ctx.request.body.id
        let username = ctx.request.body.username
        let age = ctx.request.body.age
        let sex = ctx.request.body.sex
        let status = ctx.request.body.status
        let data = await DB.update('user', {
            '_id': DB.getObjectId(id)
        }, {
            username,
            age,
            sex,
            status
        })
        try {
            if (data.result.ok) {
                ctx.redirect('/')
            }
        } catch (error) {
            console.log(error)
            ctx.redirect('/add')
            return
        }
    })
    .get('/add', async (ctx) => {
        await ctx.render('add')
    })
    .post('/doAdd', async (ctx) => {
        // 获取表单提交的数据
        let data = await DB.insert('user', ctx.request.body)
        try {
            if (data.result.ok) {
                ctx.redirect('/')
            }
        } catch (error) {
            console.log(error)
            ctx.redirect('/add')
            return
        }
    })
    .get('/delete', async (ctx) => {
        let id = ctx.query.id
        let data = await DB.remove('user', {
            '_id': DB.getObjectId(id)
        })
        try {
            if (data.result.ok) {
                ctx.redirect('/')
            }
        } catch (error) {
            console.log(error)
            ctx.redirect('/')
            return
        }
    })

app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

```js
// config.js
// 配置文件
const app = {
    dbUrl: 'mongodb://localhost:27017',
    dbName: 'Koa'
}

module.exports = app
```

```js
// db.js
const MongoDB = require('mongodb')
const MongoClient = MongoDB.MongoClient
const ObjectID = MongoDB.ObjectID

const Config = require('./config')

class Db {
    static getInstance() {
        // 单例
        if (!Db.instance) {
            Db.instance = new Db()
        }
        return Db.instance
    }

    constructor() {
        this.dbClient = '' // 属性 放db对象
        this.connect() // 实例化的时候就链接数据库
    }

    connect() {
        // 连接数据库
        return new Promise((resolve, reject) => {
            if (!this.dbClient) {
                // 解决数据库多次链接的问题
                MongoClient.connect(Config.dbUrl, { useNewUrlParser: true }, (err, client) => {
                    if (err) {
                        reject(err)
                    } else {
                        this.dbClient = client.db(Config.dbName)
                        resolve(this.dbClient)
                    }
                })
            } else {
                resolve(this.dbClient)
            }
        })
    }

    find(collectionName, json) {
        return new Promise((resolve, reject) => {
            this.connect().then((db) => {
                let result = db.collection(collectionName).find(json)
                result.toArray(function (err, docs) {
                    if (err) {
                        reject(err)
                        return
                    }
                    resolve(docs)
                })
            })
        })
    }

    update(collectionName, json1, json2) {
        return new Promise((resolve, reject) => {
            this.connect().then((db) => {
                db.collection(collectionName).updateOne(json1, {
                    $set: json2
                }, (err, result) => {
                    if (err) {
                        reject(err)
                        return
                    }
                    resolve(result)
                })
            })
        })
    }

    insert(collectionName, json) {
        return new Promise((resolve, reject) => {
            this.connect().then((db) => {
                db.collection(collectionName).insertOne(json, function (err, result) {
                    if (err) {
                        reject(err)
                        return
                    }
                    resolve(result)
                })
            })
        })
    }

    remove(collectionName, json) {
        return new Promise((resolve, reject) => {
            this.connect().then((db) => {
                db.collection(collectionName).removeOne(json, function (err, result) {
                    if (err) {
                        reject(err)
                        return
                    }
                    resolve(result)
                })
            })
        })
    }

    getObjectId(id) {
        // mongodb里面查询 _id 把字符串转换成对象
        return new ObjectID(id)
    }
}

module.exports = Db.getInstance()
```

## mysql

```bash
# 安装
yarn add mysql
```

```js
const mysql = require('mysql')

// 建立连接的方法
function __connection() {
    const connection = mysql.createConnection({
        host: 'localhost',
        user: 'root',
        password: '12345678',
        database: 'koacms'
    })
    connection.connect()
    return connection
}

exports.query = function (sql, parmas = null) {
    // 1.获取数据库连接对象
    const connection = __connection()
    return new Promise(function (reject, resolve) {
        // 2、执行sql语句
        connection.query(sql, parmas, function (error, results, fields) {
            if (error) throw error
            reject(results)

        })
        // 3、关闭连接
        connection.end()
    })
}

```

## redis

```bash
# 安装
yarn add ioredis
```

```js
const router = require('koa-router')()
const Redis = require('ioredis')
const redis = new Redis({
    host: '127.0.0.1', // 安装好的redis服务器地址
    port: 80, // 端口
    prefix: 'sam:', // 存诸前缀
    ttl: 60 * 60 * 23, // 过期时间
    db: 0
})
router.get('/', async function (ctx, next) {
    redis.set("test", "kwg kwg kwg")
    const doc = await
    redis.get("test", function (err, doc) {
        return doc
    })
    ctx.body = doc

})

module.exports = router
```

___
> 共同学习，共同进步