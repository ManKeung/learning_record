# socket

```bash
# 安装
yarn add koa-socket
```

* 示例

```js
const Koa = require('koa'),
    router = require('koa-router')(),
    views = require('koa-views'),
    url = require('url')

const IO = require('koa-socket')
const io = new IO()

const app = new Koa()
io.attach(app)

app.use(views('views', {
    extension: 'ejs' // 应用ejs模板引擎
}))

router.get('/', async (ctx) => {
    let title = '你好ejs'
    await ctx.render('index', {
        title
    })
})

app._io.on('connection', socket => {
    console.log('建立连接了')

    let roomid = url.parse(socket.request.url, true).query.roomid // 获取房间号/ 获取桌号
    // console.log(roomid)
    socket.join(roomid) // 加入房间/加入分组

    socket.on('addCart', function (data) {
        console.log(data)
        // socket.emit('serverEmit','我接收到增加购物车的事件了')  // 发给指定用户
        // app._io.emit('serverEmit','我接收到增加购物车的事件了')  // 广播
        // app._io.to(roomid).emit('serverEmit','我接收到增加购物车的事件了')
        socket.broadcast.to(roomid).emit('serverEmit', '我接收到增加购物车的事件了')
    })
})

app.use(router.routes()) // 路由启动
app.use(router.allowedMethods())
app.listen(3000)

/*使用步骤
    1、安装
    cnpm i -S koa-socket

    2、引入
    const IO = require( 'koa-socket' )

    3、实例化const io = new IO()

    4、
    io.attach( app )

    5、配置服务端
    app._io.on( 'connection', socket => {
    console.log('建立连接了');
    })

    6、
    <script src="http://localhost:3000/socket.io/socket.io.js"></script>
    <script>
    var socket=io.connect('http://localhost:3000/')
    </script>
 * */
```

```html
<!-- index01.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>socket.io</title>
    <script src="http://192.168.0.3:3000/socket.io/socket.io.js"></script>
</head>
<body>
<h1>socket.io的多房间1111</h1>
<input type="button" value="加入购物车" onclick="addCart()"><br>


</body>
</html>

<script type="text/javascript">

    //和服务器建立长连接
    var socket = io.connect('http://192.168.0.3:3000?roomid=1');

    //接收服务器返回的信息
    socket.on('serverEmit',function(data){

        console.log(data);
    });

    function addCart(){
        socket.emit('addCart','addCart');
    }

</script>
```

```html
<!-- .index02.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>socket.io</title>
    <script src="http://192.168.0.3:3000/socket.io/socket.io.js"></script>
</head>
<body>
<h1>socket.io的多房间222</h1>
<input type="button" value="加入购物车" onclick="addCart()"><br>


</body>
</html>

<script type="text/javascript">

    //和服务器建立长连接
    var socket = io.connect('http://192.168.0.3:3000?roomid=2');

    //接收服务器返回的信息
    socket.on('serverEmit',function(data){

        console.log(data);
    });

    function addCart(){
        socket.emit('addCart','addCart');
    }

</script>
```

```html
<!-- index03.html -->
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>socket.io</title>
    <script src="http://192.168.0.3:3000/socket.io/socket.io.js"></script>
</head>
<body>
<h1>socket.io的多房间3333</h1>
<input type="button" value="加入购物车" onclick="addCart()"><br>


</body>
</html>

<script type="text/javascript">

    //和服务器建立长连接
    var socket = io.connect('http://192.168.0.3:3000?roomid=1');

    //接收服务器返回的信息
    socket.on('serverEmit',function(data){

        console.log(data);
    });

    function addCart(){
        socket.emit('addCart','addCart');
    }

</script>
```
___
> 共同学习，共同进步