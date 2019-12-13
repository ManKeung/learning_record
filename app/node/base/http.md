# 初识服务

```js
// 1. 引入http模块
const http = require('http')

// 2. 用http模块创建服务

/*
request 获取url信息
response 浏览器返回响应信息
 */

http.createServer((request, response) => {
    console.log('***********')
    // console.log(request)
    console.log('***********')
    // 发送HTTP头部
    // HTTP状态值: 200:ok
    // 设置HTTP头部，状态码是200，文件类型html，字符集是url
    response.writeHead(200, {'Content-Type': 'text/html;charset="utf-8"'})
    response.write('hello world')
    response.write('I am is nodejs')
    response.end() // 结束响应
}).listen(8000)
```
* url模块获取get参数

```js
// 引入模块
const http = require('http')
const url = require('url')

// 用http模块创建服务

/*
request 获取url信息
response 浏览器返回响应信息
 */

http.createServer((request, response) => {
    // http://localhost:8000/new?aid=123 拿到 aid
    // http://localhost:8000/new?aid=123&cid=3 拿到 aid cid
    // console.log(request.url)
    // const query = url.parse(request.url, true)
    // console.log(query)
    // 发送HTTP头部
    // HTTP状态值: 200:ok
    // 设置HTTP头部，状态码是200，文件类型html，字符集是url
    response.writeHead(200, {'Content-Type': 'text/html;charset="utf-8"'})
    if (request.url != '/favicon.ico') {
        const result = url.parse(request.url, true) // 第一个参数是地址    第二个参数是true的话表示把get传值转换成对象
        console.log('aid=' + result.query.aid)
        console.log('cid=' + result.query.cid)
    }
    response.write('hello world')
    response.write('I am is nodejs')
    response.end() // 结束响应
}).listen(8000)
```

* supervisor改代码自动重启web服务

```bash
yarn add supervisor -D
supervisor index.js
```

* 模块化

1. config.js

```js
// 方式一
let str = 'this isconfig'
export.str = str // 导出

// 导入
const {str} = require('./config')

// 方式２
let str = 'this isconfig'
module.exports = str // 导出默认模块

// 导入
const config = require('./config')
```

> 默认在目录下面没有，没有的话nodejs会在node_modules里面找这个模块
> 找 package.json 入口文件 "main": "nav.js"

___
> 共同学习，共同进步