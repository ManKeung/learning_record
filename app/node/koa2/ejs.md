# 模板引擎

* 安装

```bash
yarn add koa-views ejs
```

* 示例

```js
// app.js
const Koa = require('koa')
const router = require('koa-router')()
const views = require('koa-views')

const app = new Koa()

// 配置模板引擎中间件
// app.use(views('views', { map: {html: 'ejs' }}))  //这样配置也可以  注意如果这样配置的话 模板的后缀名是.html
app.use(views('views', {
    extension: 'ejs' // 应用ejs模板引擎
}))

// 写一个中间件配置公共的信息
app.use(async (ctx, next) => {
    ctx.state = {
        userinfo: 'ManKeung'
    }
    await next() // 继续向下匹配路由
})

router
    .get('/', async ctx => {
        let title = '你好ejs'
        await ctx.render('index', {
            title
        })
    })
    .get('/news', async (ctx) => {
        let arr = [111, 2222, 3333, 4444]
        let content = '<h2>这是一个h2</h2>'
        let num = 123
        await ctx.render('news', {
            arr,
            content,
            num
        })
    })


app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

```html
<!-- index.ejs -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>首页</title>
</head>

<body>
    这是一个ejs模板引擎
    <%- include('public/header.ejs')-%>
    <hr />
    <h2><%=title%></h2>
    <h2><%=userinfo%></h2>
</body>

</html>
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>首页</title>
</head>

<body>
    这是一个ejs模板引擎
    <hr />
    <h2><%=title%></h2>
    <h2><%=userinfo%></h2>
</body>

</html>
```

```html
<!-- header.ejs -->
<h1 class="title">这是一个头部模块</h1>
```

```html
<!-- news.ejs -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>新闻</title>
</head>

<body>
    这是一个ejs循环渲染数据
    <hr />
    <ul>
        <!-- 循环 -->
        <% for(let i=0; i<arr.length; i++) {%>
        <li>
            <!-- 绑定数据 -->
            <%=arr[i]%>
        </li>
        <%}%>
    </ul>
    <hr/>
    <!-- 绑定html -->
<%-content%>-----<%=userinfo%>
        <!-- 条件判断 -->
        <%if(num>24){%>
        大于24
        <%} else {%>
        小于24
        <%}%>
</body>
</html>
```

## 获取post数据

* 原生node获取

```js
// app.js
const Koa = require('koa')
const router = require('koa-router')()
const views = require('koa-views')
const common = require('./model/common')

const app = new Koa()

app.use(views('views', {
    extension: 'ejs'
}))


router
    .get('/', async ctx => {
        await ctx.render('index')
    })
    // 接收post提交数据
    .post('/doAdd', async (ctx) => {
        // 原生nodejs 在koa中获取表单提交的数据
        let data = await common.getPostData(ctx)
        console.log(data)
        ctx.body = data
    })


app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

```js
// common.js
exports.getPostData = ctx => {
    // 获取数据 异步
    return new Promise((resolve, reject) => {
        try {
            let str = ''
            ctx.req.on('data', chunk => {
                str += chunk
            })
            ctx.req.on('end', _chunk => {
                resolve(str)
            })
        } catch(error) {
            reject(error)
        }
    })
}
```

```html
<!-- index.ejs -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>首页</title>
</head>

<body>
    <form action="/doAdd" method="post">
        用户名：<input type="text" name="username" />
        <br />
        <br />
        密码：<input type="password" name="password" />
        <br />
        <button type="submit">提交</button>
    </form>
</body>

</html>
```

* 第三方

```bash
# 安装
yarn add koa-bodyparser
```

```js
const Koa = require('koa')
const router = require('koa-router')()
const views = require('koa-views')
const bodyParser = require('koa-bodyparser')

const app = new Koa()

app.use(views('views', {
    extension: 'ejs'
}))

// 配置post bodyparser的中间件
app.use(bodyParser())


router
    .get('/', async ctx => {
        await ctx.render('index')
    })
    // 接收post提交数据
    .post('/doAdd', async (ctx) => {
        console.log(ctx.request.body)
        ctx.body = ctx.request.body // 获取表单提交的数据
    })


app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

## 静态web服务

```bash
# 安装
yarn add koa-static
```

* 示例

```js
const Koa = require('koa')
const router = require('koa-router')()
const views = require('koa-views')
const bodyParser = require('koa-bodyparser')
const static = require('koa-static')

const app = new Koa()

app.use(views('views', {
    extension: 'ejs'
}))

// 配置post bodyparser的中间件
app.use(bodyParser())

// http://localhost:3000/css/basic.css  首先去static目录找 ，如果能找到返回对应的文件，找不到 next()
// 配置静态web服务的中间件
// app.use(static('./static'))
app.use(static(__dirname + '/static'))
app.use(static(__dirname + '/public')) // koa静态资源中间件可以配置多个


router
    .get('/', async ctx => {
        await ctx.render('index')
    })
    // 接收post提交数据
    .post('/doAdd', async (ctx) => {
        console.log(ctx.request.body)
        ctx.body = ctx.request.body // 获取表单提交的数据
    })


app
    .use(router.routes())
    .use(router.allowedMethods())
    .listen(3000)
```

## art-template模板

```bash
# 安装
yarn add art-template koa-art-template
```

```js
// app.js
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
        // ctx.body = '首页'
        let list = {
            name: 'Mankeung',
            h: '<h2>这是一个h2</h2>',
            num: 20,
            arr: [111, 222, 333]
        }
        await ctx.render('index', {
            list
        })
    })
    .get('/news', async ctx => {
        let list = {
            name: 'Mankeung',
            h: '<h2>这是一个h2</h2>',
            num: 20,
            arr: [111, 222, 333]
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

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>首页</title>
</head>

<body>
    <h2>这是一个koa-art-template</h2>
    <hr />
    <!-- 绑定数据 -->
    <%=list.name%>
    <hr />
    <!-- 原文输出 -->
    <%-list.h%>
    <hr />
    <!-- 条件 -->
    <%if(list.num > 24) {%>
    大于24
    <%}else{%>
    小于24
    <%}%>
    <hr/>
    <!-- 循环数据 -->
    <ul>
    <%for(let i=0; i<list.arr.length; i++) {%>
    <li><%=list.arr[i]%></li>
    <%}%>
    </ul>
    <hr/>
    <!-- 子模块 -->
    <% include('./public/footer.html')%>
</body>

</html>
```

```html
<!-- news.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>新闻</title>
</head>

<body>
    <h2>这是一个koa-art-template news</h2>
    <hr />
    <!-- 绑定数据 -->
    {{list.name}}
    <hr />
    <!-- 绑定html -->
    {{@list.h}}
    <hr />
    <!-- 条件 -->
    {{if list.num > 24}}<strong>大于24</strong>{{else}}<strong>小于24</strong>{{/if}}
    <hr />
    <!-- 循环 -->
    <ul>
        {{each list.arr}}
        <li>{{$index}} --- {{$value}}</li>
        {{/each}}
    </ul>
    <hr />
    <!-- 子模块 -->
    {{include './public/footer.html'}}
</body>

</html>
```

```html
<!-- footer.html -->
<h1>这是一个底部</h1>
```

___
> 共同学习，共同进步