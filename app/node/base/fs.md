# 文件操作

* 检查是文件还是目录

```js
const fs = require('fs')

fs.stat('index.js', (err, stats) => {
    if (err) {
        console.log(err)
        return
    }
    console.log('文件: ', stats.isFile())
    console.log('目录: ', stats.isDirectory())
})
```

* 创建目录

```js
const fs = require('fs')

/*
接收参数
path 将创建的目录路径
mode          目录权限（读写权限），默认0777
callback      回调，传递异常参数err
*/
fs.mkdir('css', (err) => {
    if (err) {
        console.log(err)
        return
    }
    console.log('创建目录成功')
})
```

* 创建写入文件

```js
const fs = require('fs')

//filename      (String)            文件名称
//data        (String | Buffer)    将要写入的内容，可以使字符串 或 buffer数据。
//options        (Object)           option数组对象，包含：
//· encoding   (string)            可选值，默认 ‘utf8′，当data使buffer时，该值应该为 ignored。
//· mode         (Number)        文件读写权限，默认值 438
//· flag            (String)            默认值 ‘w'
//callback {Function}  回调，传递一个异常参数err。
fs.writeFile('t.txt', '你好nodejs！', err => {
    if (err) {
        console.log(err)
        return
    }
    console.log('创建写入文件成功')
})
```

* 追加文件

```js
const fs = require('fs')

fs.appendFile('t.txt', '\n这是写入内容', err => {
    if (err) {
        console.log(err)
        return
    }
    console.log('追加写入成功')
})
```

* 读取文件

```js
const fs = require('fs')

fs.readFile('t.txt', (err, data) => {
    if (err) {
        console.log(err)
        return
    }
    // console.log(data)
    console.log(data.toString())
})
```

* 读取目录

```js
const fs = require('fs')

fs.readdir('html', (err, data) => {
    if (err) {
        console.log(err)
        return
    }
    console.log(data)
})
```

* 重命名

```js
const fs = require('fs')

fs.rename('html/new.html', 'html/index.html', err => {
    if (err) {
        console.log(err)
        return
    }
    console.log('修改名字成功')
})

/* ************ */

const fs = require('fs')

fs.rename('t.txt', 'html/t1.txt', err => {
    if (err) {
        console.log(err)
        return
    }
    console.log('剪切成功')
})
```

* 删除目录

```js
const fs = require('fs')

fs.rmdir('t', err => {
    if (err) {
        console.log(err)
        return
    }
    console.log('删除目录成功')
})
```

> 注意目录不为空报错

* 删除文件

```js
const fs = require('fs')

fs.unlink('txt.txt', err => {
    if (err) {
        console.log(err)
        return
    }
    console.log('删除文件成功')
})
```

* 流的方式读取文件

```js
const fs = require('fs')

let readStream = fs.createReadStream('txt.txt')

let str = '' // 保存数据
let count = 0 // 次数

readStream.on('data', chunk => {
    str += chunk
    count++
})

// 读取完成
readStream.on('end', chunk => {
    console.log(str)
    console.log(count)
})

// 读取失败
readStream.on('error', err => {
    console.log(err)
})
```

* 流的方式写入

```js
const fs = require('fs')

let data = '我是从数据库获取的数据，我要保存起来\n'

// 创建一个可以写入的流，写入到文件 output.txt 中
let writerStream = fs.createWriteStream('out.txt')

for (let i=0; i<1000; i++) {
    writerStream.write(data, 'utf-8')
}

// 标记写入完成
writerStream.end()

// 成功
writerStream.on('finish', () => {
    console.log('写入完成')
})

// 失败
writerStream.on('error', () => {
    console.log('写入失败')
})
```

* 管道读写操作

```js
const fs = require('fs')

// 创建一个可读流
let readerStream = fs.createReadStream('txt.txt')

// 创建一个可写流
let writerStream = fs.createWriteStream('output01.txt')

// 管道读写操作
// 读取 input.txt 文件内容，并将内容写入到 output.txt 文件中
readerStream.pipe(writerStream)

console.log("程序执行完毕")
```

## 应用

* 判断服务器上面有没有upload目录。没有创建这个目录。   （图片上传）

```js
const fs = require('fs')

fs.stat('upload', (err, stats) => {
    if (err) { // 没有目录
        console.log('没有目录正在创建')
        fs.mkdir('upload', error => {
            if (error) {
                console.log(error)
                return
            }
            console.log('创建目录成功')
        })
    } else {
        console.log('目录已经存在')
        console.log(stats.isDirectory())
    }
})
```

* 找出html目录下面的所有的目录， 然后打印出来

```js
const fs = require('fs')

fs.readdir('html', (err, files) => {
    if (err) {
        console.log(err)
        return
    }
    // 判断是目录还是文件夹
    console.log(files)
    for (let i = 0; i < files.length; i++) { // 循环判断是目录还是文件
        fs.stat(`html/${files[i]}`, (error, stats) => {
            if (error) {
                console.log(error)
                return
            }
            if (stats.isDirectory()) {
                console.log(files[i])
            }
        })
    }
})
```

* 递归参数创建目录

```js
const fs = require('fs')

fs.stat('public/upload/users', {recursive: true}, (err, stats) => {
    if (err) {
        console.log('没文件夹')
        fs.mkdirSync('public/upload/users', {recursive: true}, err => {
            if (err) {
                console.log(err)
                return
            }
            console.log('创建目录成功')
        })
        return
    }
    console.log(stats.isDirectory())
})
```

___
> 共同学习，共同进步