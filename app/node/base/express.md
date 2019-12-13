# 模拟express

* express_route.js

```js
const url = require('url')

// 封装方法改变res  绑定res.send()
const changeRes = (res) => {

    res.send = (data) => {

        res.writeHead(200, {
            "Content-Type": "text/html;charset='utf-8'"
        })

        res.end(data)
    }
}

//暴露的模块
const Server = () => {


    const G = this /*全局变量*/

    //处理get和post请求
    this._get = {}

    this._post = {}



    const app = (req, res) => {


        changeRes(res)

        //获取路由
        let pathname = url.parse(req.url).pathname
        if (!pathname.endsWith('/')) {
            pathname = pathname + '/'
        }

        //获取请求的方式 get  post
        let method = req.method.toLowerCase()


        if (G['_' + method][pathname]) {

            if (method == 'post') {
                /*执行post请求*/

                let postStr = ''
                req.on('data', (chunk) => {

                    postStr += chunk
                })
                req.on('end', (err, chunk) => {

                    req.body = postStr /*表示拿到post的值*/


                    //G._post['dologin'](req,res)

                    G['_' + method][pathname](req, res) /*执行方法*/

                })



            } else {
                /*执行get请求*/
                G['_' + method][pathname](req, res) /*执行方法*/

            }

        } else {

            res.end('no router')
        }

    }

    app.get = (string, callback) => {
        if (!string.endsWith('/')) {
            string = string + '/'
        }
        if (!string.startsWith('/')) {
            string = '/' + string
        }
        //    /login/
        G._get[string] = callback

    }

    app.post = (string, callback) => {
        if (!string.endsWith('/')) {
            string = string + '/'
        }
        if (!string.startsWith('/')) {
            string = '/' + string

        }
        //    /login/
        G._post[string] = callback

        //G._post['dologin']=function(req,res){
        //
        //}
    }

    return app

}

module.exports = Server()
```

* 主程序

```js
const http = require('http')
const ejs = require('ejs')
const app = require('./model/express_route.js')

console.log(app)
http.createServer(app).listen(8000)

app.get('/', (req, res) => {

    let msg = '这是数据库的数据'
    ejs.renderFile('views/index.ejs', {
        msg
    }, (err, data) => {

        res.send(data)
    })
})
```
___
> 共同学习，共同进步