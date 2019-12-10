# canvas

HTML5`<canvas>`元素用于图形的绘制，通过脚本 (通常是JavaScript)来完成.
`<canvas>`标签只是图形容器，您必须使用脚本来绘制图形。
你可以通过多种方法使用 canvas 绘制路径,盒、圆、字符以及添加图像。

* 创建画布

```html
<canvas id="myCanvas" width="200" height="100"
style="border:1px solid #000000;">
</canvas>
```

* 使用JavaScript来绘制图像

```js
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.fillStyle="#FF0000";
ctx.fillRect(0,0,150,75);
```

* canvas-路径

moveTo(x,y) 定义线条开始坐标
lineTo(x,y) 定义线条结束坐标

```js
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.moveTo(0,0);
ctx.lineTo(200,100);
ctx.stroke();
```

* canvas中绘制圆形

```js
// arc(x,y,r,start,stop)
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.beginPath();
ctx.arc(95,50,40,0,2*Math.PI);
ctx.stroke();
```

* Canvas - 文本

font - 定义字体
fillText(text,x,y) - 在 canvas 上绘制实心的文本
strokeText(text,x,y) - 在 canvas 上绘制空心的文本

```js
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
ctx.font="30px Arial";
ctx.fillText("Hello World",10,50);
```

* Canvas - 渐变

createLinearGradient(x,y,x1,y1) - 创建线条渐变
createRadialGradient(x,y,r,x1,y1,r1) - 创建一个径向/圆渐变

```js
// 创建一个线性渐变。使用渐变填充矩形:
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
// 创建渐变
var grd=ctx.createLinearGradient(0,0,200,0);
grd.addColorStop(0,"red");
grd.addColorStop(1,"white");
// 填充渐变
ctx.fillStyle=grd;
ctx.fillRect(10,10,150,80);

// 创建一个径向/圆渐变。使用渐变填充矩形：
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");

// 创建渐变
var grd=ctx.createRadialGradient(75,50,5,90,60,100);
grd.addColorStop(0,"red");
grd.addColorStop(1,"white");

// 填充渐变
ctx.fillStyle=grd;
ctx.fillRect(10,10,150,80);
```

* Canvas - 图像

drawImage(image,x,y)

```js
var c=document.getElementById("myCanvas");
var ctx=c.getContext("2d");
var img=document.getElementById("scream");
ctx.drawImage(img,10,10);
```

> [更多](https://www.runoob.com/tags/ref-canvas.html)

___
> 共同学习，共同进步