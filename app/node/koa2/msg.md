# cookie和session

## cookie

* 基本使用

```js
const Koa = require('koa')
const router = require('koa-router')()
const render = require('koa-art-template')
const path = require('path')

const app = new Koa()

// 配置 koa-art-template模板引擎
render(app, {
    root: path.join(__dirname, 'views'), // 视图的位置
    extname: '.html', // 后缀名
    debug: process.env.NODE_ENV !== 'production' // 是否开启调试模式
})

router
    .get('/', async ctx => {
        // 正常就这样配置就能使用了
        /* ctx.cookies.set('userinfo', 'zhangsan', {
            maxAge: 60*1000*60
        }) */

        ctx.cookies.set('userinfo', 'zhangsan', {
            maxAge: 60* 1000 * 60,
            path: '/news', // 配置可以访问的页面
            // domain: '.aidu.com', // 正常情况不要设置 默认当前域名下面的所有页面都可以访问
            /*
                a.baidu.com
                b.baidu.com  共享cookie的数据
                express基础教程
            */
           httpOnly: true, // true表示这个cookie只有服务器端可以访问，false表示客户端（js），服务器端都可以访问
        })

        let list = {
            name: 'Mankeung'
        }

        await ctx.render('index', {
            list
        })
    })
    .get('/news', async ctx => {
        const userinfo = ctx.cookies.get('userinfo')
        let list = {
            name: userinfo
        }
        await ctx.render('news', {
            list
        })
    })


app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

### Koa中设置Cookie的值
ctx.cookies.set(name, value, [options])

### 通过 options 置 设置 cookie name  的 value :

options名称 | options值
--- | ---
maxAge | 一个数字表示从 Date.now()得到的毫秒数
expires | cookie 过期的 Date
path | cookie 路径, 默认是'/'
domain | cookie 域名
secure | 安全 cookie 默认false，设置成true表示只有https可以访问
httpOnly | 是否只是服务器可访问cookie, 默认是true
overwrite | 一个布尔值，表示是否覆盖以前设置的同名的cookie(默认是 false). 如果是 true, 在同一个请求中设置相同名称的所有Cookie（不管路径或域）是否在设置此 Cookie 时从Set-Cookie 标头中过滤掉。a boolean indicating whether to overwrite previously set cookies of the same name (false by default). If this is true, all cookies set during the same request with the same name (regardless of path or domain) are filtered out of the Set-Cookie header when setting this cookie.

### Koa 中获取 Cookie
ctx.cookies.get('name')

### Koa  中设置中文 Cookie

```
console.log(new Buffer('hello, world!').toString('base64'));// 转换成 base64 字符
串：aGVsbG8sIHdvcmxkIQ==
console.log(new Buffer('aGVsbG8sIHdvcmxkIQ==', 'base64').toString());// 还原 base
64 字符串：hello, world!
```

## session

```bash
# 安装
yarn add koa-session
```

```js
const Koa = require('koa')
const router = require('koa-router')()
const render = require('koa-art-template')
const session = require('koa-session')
const path = require('path')

const app = new Koa()

// 配置 koa-art-template模板引擎
render(app, {
    root: path.join(__dirname, 'views'), // 视图的位置
    extname: '.html', // 后缀名
    debug: process.env.NODE_ENV !== 'production' // 是否开启调试模式
})

// 配置session的中间件
app.keys = ['some secret hurr'] // cookie的签名
const CONFIG = {
    // 默认
    key: 'koa:sess',
    //  cookie的过期时间 【需要修改】
    maxAge: 10000,
    // (boolean) can overwrite or not (default true)    没有效果，默认
    overwrite: true,
    // true表示只有服务器端可以获取cookie
    httpOnly: true,
    // 默认 签名
    signed: true,
    // 在每次请求时强行设置 cookie，这将重置 cookie 过期时间（默认：false） 【需要修改】
    rolling: false,
    // (boolean) renew session when session is nearly expired 【需要修改】
    renew: true,
}
app.use(session(CONFIG, app))

router
    .get('/', async (ctx) => {
        // 获取session
        console.log(`/:${ctx.session.userinfo}`)
        ctx.body = '首页'
    })
    .get('/login', async (ctx) => {
        // 设置session
        ctx.session.userinfo = '张三'
        ctx.body = '登录'
    })
    .get('/news', async (ctx) => {
        console.log(`news:${ctx.session.userinfo}`)
        ctx.body = '新闻'
    })

app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

___
> 共同学习，共同进步