# 路由

* 文件拆分

```js
// index.js
const http = require('http')
const router = require('./model/router')

const app = http.createServer((req, res) => {
    router.statics(req, res, 'static')
})

app.listen(8000)
```

```js
// router.js
const fs = require('fs')
const path = require('path')
const url = require('url')

const getMime = (extname, callback = () => '无回调函数') => {
    fs.readFile('./mime.json', (err, data) => {
        if (err) {
            console.log('mime.json文件不存在')
            return
        }

        const Mimes = JSON.parse(data.toString())
        const result = Mimes[extname] || 'txt/html'

        callback(result)
    })
}

exports.statics = (req, res, staticpath='static') => {
    let pathname = url.parse(req.url).pathname

    if (pathname === '/') {
        pathname = '/index.html' // 默认加载首页
    }

    // 获取文件后缀名
    const extname = path.extname(pathname)

    if (pathname !== '/favicon.ico') { // 过滤请求
        fs.readFile(`${staticpath}${pathname}`, (err, data) => {
            if (err) {
                fs.readFile(`${staticpath}/404.html`, (err, data) => {
                    if (err) {
                        console.log(err)
                        return
                    }
                    res.writeHead(404, {'Content-Type': 'text/html;charset="utf-8"'})
                    res.end(data)
                })
                return
            }

            getMime(extname, mime => {
                res.writeHead(200, {'Content-Type': `${mime};charset='utf-8'`})
                res.end(data)
            })
        })
    }
}
```

## 模板引擎

* 安装ejs

```bash
yarn add ejs
```

* 主程序

```js
const http = require('http')
const url = require('url')
// const router = require('./model/router')
const ejs = require('ejs')
const fs = require('fs')

// 路由: 指的就是针对不同请求的 URL， 处理不同的业务逻辑。
http.createServer((req, res) => {
    res.writeHead(200, {
        "Content-Type": "text/html;charset='utf-8'"
    })
    // get还是post请求
    // console.log(req.method)
    let method = req.method.toLowerCase()
    let pathname = url.parse(req.url).pathname

    // console.log(pathname)

    if (pathname === '/login') {
        // 把数据渲染到模板上面
        ejs.renderFile('views/form.ejs', {}, (err, data) => {
            res.end(data)
        })
    } else if (pathname === '/dologin' && method === 'get') { // 执行登录操作
        // get获取数据
        console.log(url.parse(req.url, true).query)
        res.end('dologin get')
    } else if (pathname === '/dologin' && method === 'post') {
        let postStr = ''
        req.on('data', (chunk) => {
            postStr += chunk
        })
        req.on('end', (err, chunk) => {
            // res.end(postStr)
            fs.appendFile('login.txt', postStr + '\n', (err) => {

                if (err) {
                    console.log(err)
                    return
                }
                console.log('写入数据成功')
            })

            res.end('<script>alert("登录成功");history.back();</script>')
        })
    } else {
        ejs.renderFile('views/index.ejs', {}, (err, data) => {
            res.end(data)
        })
    }
}).listen(8000)
```

* 模板语法

```ejs
<%=msg%> // 读取值
<%-h%> // 把变量h字符串不转义
<% for(let i=0; i<list.length;i++) {%>
    <h2><%=list[i]%></h2>
<% } %>
```

___
> 共同学习，共同进步