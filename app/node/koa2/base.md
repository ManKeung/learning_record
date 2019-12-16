# 初识koa

* 基本示例

```bash
# 安装 koa
yarn add koa
```

```js
const kao = require('koa')

const app = new kao()

// 中间件
app.use(async ctx => {
    ctx.body = 'hello koa'
})

app.listen(3000)
```

* 引入路由

```bash
# 安装路由
yarn add koa-router
```

```js
// 引入模块
const kao = require('koa')
const Router = require('koa-router')

// 实例化
const app = new kao()
const router = new Router()

// 配置路由
// ctx上下文 context 包含了request和response等信息
router.get('/', async ctx => {
    ctx.body = '这是首页' // 返回数据 相当于原生里面res.writeHead() res.end()
}).get('/news', async ctx => {
    ctx.body = '这是一个新闻页面'
})

// 启动路由
app
    .use(router.routes()) // 路由启动
    .use(router.allowedMethods()) // 可以配置也可以不配置，建议配置
    // router.allowedMethods() 作用： 这是官方文档的推荐用法, 我们可以
    // 看到 router.allowedMethods() 用在了路由匹配 router.routes() 之后, 所以在当所有
    // 路由中间件最后调用.此时根据 ctx.status 设置 response 响应头

// 端口
app.listen(3000)
```

* 获取get参数值

```js
// 引入模块
const kao = require('koa')
const router = require('koa-router')() // 引入和实例化

// 实例化
const app = new kao()

router.get('/', async ctx => {
    ctx.body = '这是首页'
})

router.get('/test', async ctx => {
    // 从ctx读取get传值
    console.log(ctx.query) // 获取的对象 用的最多的方式
    console.log(ctx.querystring) // 获取的是一个字符串
    console.log(ctx.url) // 读取url地址

    console.log('*************')

    // ctx里面的request里面获取get传值
    console.log(ctx.request.query)
    console.log(ctx.request.querystring)
    console.log(ctx.request.url)

    ctx.body = 'test'
})

app
    .use(router.routes())
    .use(router.allowedMethods())

app.listen(3000)
```

* 动态路由

```js
// 引入模块
const kao = require('koa')
const router = require('koa-router')() // 引入和实例化

// 实例化
const app = new kao()

router.get('/', async ctx => {
    ctx.body = '这是首页'
})

router.get('/test/:aid', async ctx => {
    // 获取动态路由的传值
    const params = ctx.params
    ctx.body = `test动态路由aid: ${params.aid}`
})

router.get('/package/:aid/:cid', async ctx => {
    const params = ctx.params
    ctx.body = `package/${params.aid}/${params.cid}`
})

app
    .use(router.routes())
    .use(router.allowedMethods())

app.listen(3000)
```

___
> 共同学习，共同进步