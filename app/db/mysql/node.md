# nodejs

```bash
yarn add mysql2
```

## 基本使用

```js
// app.js
const { pool } = require('./mysql/db')

// ? 占位符
const sql = 'SELECT * FROM `students` WHERE `name` = ?'

pool.query(sql, ['小乔'], (err, rows, _fields) => {
    if (err) {
        console.log(err)
        return
    }
    console.log(rows)
})

const sql2 = 'SELECT * FROM `students`'

pool.getConnection((err, conn) => {
    conn.query(sql2, (err, rows) => {
        console.log(rows)
    })
    // 完成后请不要忘记释放连接！(将连接返回到连接池中)
    // conn.release()
    pool.releaseConnection(conn)
})
```

```js
// db.js
const mysql = require('mysql2')

// 创建数据库
// const connection = mysql.createConnection({
//     host: 'localhost',
//     user: 'root',
//     password: '123456',
//     database: 'mktest',
//     charset: 'utf8'
// })

// connection.connect(err => {
//     if (err) {
//         console.log(`链接错误: ${err.stack}`)
//         return
//     }
//     console.log(`连接ID: ${connection.threadId}`)
// })

// 创建连接池
// 连接池有助于减少连接到MySQL服务器的时间， 通过重用以前的连接
// 可以避免查询的延迟， 减少建立新连接所带来的开销。
const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: '123456',
    database: 'mktest',
    charset: 'utf8',

    // 以下选项均为默认值（如果不需要变动可省略）
    waitForConnections: true, // 为true时，连接排队等待可用连接。为false将立即抛出错误
    connectionLimit: 10, // 单次可创建最大连接数
    queueLimit: 0 // 连接池的最大请求数，从getConnection方法前依次排队。设置为0将没有限制
})


// exports.conn = connection
exports.pool = pool
```

## 事务操作

```js
const { pool } = require('./mysql/db')

/**
 * 1、使用```pool.getConnection()```获取到连接对象```conn```
 * 2、使用```conn.beginTransaction()```声明开始事务操作
 * 3、使用```conn.rollback()```进行事务回滚
 * 4、使用```conn.commit()```进行事务提交
 */
pool.getConnection((err, conn) => {
    if (err) {
        console.log('pool.getConnection出错')
        return
    }
    conn.beginTransaction(err => {
        if (err) {
            console.log('开始事务错误')
            return
        }
        conn.query('UPDATE students SET gender=2 WHERE id=?', [4], (err, _rows) => {
            if (err) {
                return conn.rollback(_ => {
                    console.log('修改id=4性别为女回滚了')
                })
            }
            conn.query('SELECT * FROM students where id=4', (err, rows) => {
                if (err) {
                    return conn.rollback(_ => {
                        console.log('查询id=4的学生')
                    })
                }
                conn.commit(err => {
                    if (err) {
                        return conn.rollback(_ => {
                            console.log('提交事务失败')
                        })
                    }
                    console.log('success!')
                    console.log(rows)
                })
            })
        })
    })
})
```

## 分块查询

```js
const { pool } = require('./mysql/db')

const sql = 'SELECT * FROM `students`'

/**
 * 通过```conn.pause()```可暂停查询,当大量数据处理时很有用
 * 通过```conn.resume()```可继续查询，当处理完一段之后可通过该方法继续IO操作
 * @return {[type]}           [description]
 */
pool.getConnection((err, conn) => {
    if (err) {
        console.log('pool.getConnection出错了')
        return
    }
    let query = conn.query(sql)
    query.on('error', err => {
        // 错误处理
    })
    .on('fields', fields => {
        // 查询行段信息
    })
    .on('result', row => {
        // 暂停（row为查询的数据每查询到一行触发一次）
        conn.pause()
        // 继续查询
        conn.resume()
        console.log(row)
    })
    .on('end', _ => {
        conn.release()
        // 无论成功与否最后均会触发该事件
    })
})
```

## Promise用法

```js
async function main() {
    const mysql = require('mysql2/promise')
    const sql = 'SELECT * FROM `students`'

    // 创建链接
    const pool = await mysql.createPool({
        host: 'localhost',
        user: 'root',
        password: '123456',
        database: 'mktest',
        charset: 'utf8',

        // 以下选项均为默认值（如果不需要变动可省略）
        waitForConnections: true, // 为true时，连接排队等待可用连接。为false将立即抛出错误
        connectionLimit: 10, // 单次可创建最大连接数
        queueLimit: 0 // 连接池的最大请求数，从getConnection方法前依次排队。设置为0将没有限制
    })

    // 操作数据库
    const [rows, firlds] = await pool.execute(sql)
    console.log(rows)
}

main()
```

```js
// mysql2 新方法
const { pool } = require('./mysql/db')

const sql = 'SELECT * FROM `students`'

pool.promise().query(sql).then(([rows, fields]) => {
    console.log(rows)
}).catch(err => {
    console.log(err)
    pool.end()
})
```
___
> 共同学习，共同进步