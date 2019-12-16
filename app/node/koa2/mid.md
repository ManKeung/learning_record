# 中间件

* 应有级中间件

```js
const Koa = require('koa')
const router = require('koa-router')()
const app = new Koa()

// Koa中间件
//匹配任何路由  ，如果不写next，这个路由被匹配到了就不会继续向下匹配
/*
app.use(async (ctx)=>{
    ctx.body='这是一个中间件'
})
* */

// 匹配路由之前打印日期
app.use(async (_ctx, next) => {
    console.log(new Date())
    await next()
})

router
    .get('/', async ctx => {
        ctx.body = '首页'
    })
    .get('/news', async ctx => {
        ctx.body = '新闻'
    })

app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

* 路由级中间件

```js
const Koa = require('koa')
const router = require('koa-router')()
const app = new Koa()

app.use(async (_ctx, next) => {
    console.log(new Date())
    await next()
})

router
    .get('/', async ctx => {
        ctx.body = '首页'
    })
    // 匹配到news路由继续向下匹配路由
    .get('/news', async (_ctx, next) => {
        console.log('这是一个新闻')
        await next()
    })
    .get('/news', async ctx => {
        ctx.body = '新闻'
    })

app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

* 错误处理中间件

```js
const Koa = require('koa')
const router = require('koa-router')()
const app = new Koa()

app.use(async (ctx, next) => {
    console.log('这是一个中间件01')
    await next()
    if (ctx.status === 404) {
        ctx.status = 404
        ctx.body = '这是一个404页面'
    } else {
        console.log(ctx.url)
    }
})

router
    .get('/', async ctx => {
        ctx.body = '首页'
    })

app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

* 中间件执行流程

```js
const Koa = require('koa')
const router = require('koa-router')()
const app = new Koa()

// 匹配任何路由  ，如果不写next，这个路由被匹配到了就不会继续向下匹配
// www.域名.com/news
app.use(async (_ctx, next) => {
    console.log('1、这是第一个中间件01')
    await next()
    console.log('5、匹配路由完成以后又会返回来执行中间件')
})

app.use(async (_ctx, next) => {
    console.log('2、这是第二个中间件02')
    await next()
    console.log('4、匹配路由完成以后又会返回来执行中间件')
})

router
    .get('/', async ctx => {
        ctx.body = '首页'
    })
    .get('/news', async (ctx) => {
        console.log('3、匹配到了news这个路由')
        ctx.body = '这是一个新闻'
    })


app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)

/*
// /
1、这是第一个中间件01
2、这是第二个中间件02
4、匹配路由完成以后又会返回来执行中间件
5、匹配路由完成以后又会返回来执行中间件
// /news
1、这是第一个中间件01
2、这是第二个中间件02
3、匹配到了news这个路由
4、匹配路由完成以后又会返回来执行中间件
5、匹配路由完成以后又会返回来执行中间件 */
```

___
> 共同学习，共同进步