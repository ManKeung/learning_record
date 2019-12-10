# CSS3

## 边框

* 圆角

```css
div {
    border: 2px solid red;
    border-radius: 25px;
}
```

* 盒阴影

```css
div {
    box-shadow: 10px 10px 5px #888888;
}
```

* 边界图片

```css
div {
    border-image:url(border.png) 30 30 round;
}
```

## 字体

```html
<style>
@font-face
{
    font-family: myFirstFont;
    src: url(sansation_light.woff);
}

div
{
    font-family:myFirstFont;
}
</style>
```

## 2D转换

* 转换属性

Property | 描述
--- | ---
transform | 适用于2D或3D转换的元素
transform-origin | 允许您更改转化元素位置

* 2D 转换方法


函数 | 描述
--- | ---
matrix(n,n,n,n,n,n) | 定义 2D 转换，使用六个值的矩阵。
translate(x,y) | 定义 2D 转换，沿着 X 和 Y 轴移动元素。
translateX(n) | 定义 2D 转换，沿着 X 轴移动元素。
translateY(n) | 定义 2D 转换，沿着 Y 轴移动元素。
scale(x,y) | 定义 2D 缩放转换，改变元素的宽度和高度。
scaleX(n) | 定义 2D 缩放转换，改变元素的宽度。
scaleY(n) | 定义 2D 缩放转换，改变元素的高度。
rotate(angle) | 定义 2D 旋转，在参数中规定角度。
skew(x-angle,y-angle) | 定义 2D 倾斜转换，沿着 X 和 Y 轴。
skewX(angle) | 定义 2D 倾斜转换，沿着 X 轴。
skewY(angle) | 定义 2D 倾斜转换，沿着 Y 轴。

## 3D转换

* 转换属性

属性 | 描述
--- | ---
transform | 向元素应用 2D 或 3D 转换。
transform-origin | 允许你改变被转换元素的位置。
transform-style | 规定被嵌套元素如何在 3D 空间中显示。
perspective | 规定 3D 元素的透视效果。
perspective-origin | 规定 3D 元素的底部位置。
backface-visibility | 定义元素在不面对屏幕时是否可见。

* 转换方法

函数 | 描述
--- | ---
matrix3d(n,n,n,n,n,n,
n,n,n,n,n,n,n,n,n,n) | 定义 3D 转换，使用 16 个值的 4x4 矩阵。
translate3d(x,y,z) | 定义 3D 转化。
translateX(x) | 定义 3D 转化，仅使用用于 X 轴的值。
translateY(y) | 定义 3D 转化，仅使用用于 Y 轴的值。
translateZ(z) | 定义 3D 转化，仅使用用于 Z 轴的值。
scale3d(x,y,z) | 定义 3D 缩放转换。
scaleX(x) | 定义 3D 缩放转换，通过给定一个 X 轴的值。
scaleY(y) | 定义 3D 缩放转换，通过给定一个 Y 轴的值。
scaleZ(z) | 定义 3D 缩放转换，通过给定一个 Z 轴的值。
rotate3d(x,y,z,angle) | 定义 3D 旋转。
rotateX(angle) | 定义沿 X 轴的 3D 旋转。
rotateY(angle) | 定义沿 Y 轴的 3D 旋转。
rotateZ(angle) | 定义沿 Z 轴的 3D 旋转。
perspective(n) | 定义 3D 转换元素的透视视图。

## 过渡

* 过渡属性

属性 | 描述
--- | ---
transition | 简写属性，用于在一个属性中设置四个过渡属性。
transition-property | 规定应用过渡的 CSS 属性的名称。
transition-duration | 定义过渡效果花费的时间。默认是 0。
transition-timing-function | 规定过渡效果的时间曲线。默认是 "ease"。
transition-delay | 规定过渡效果何时开始。默认是 0。

值 | 描述
--- | ---
linear | 规定以相同速度开始至结束的过渡效果（等于 cubic-bezier(0,0,1,1)）。
ease | 规定慢速开始，然后变快，然后慢速结束的过渡效果（cubic-bezier(0.25,0.1,0.25,1)）。
ease-in | 规定以慢速开始的过渡效果（等于 cubic-bezier(0.42,0,1,1)）。
ease-out | 规定以慢速结束的过渡效果（等于 cubic-bezier(0,0,0.58,1)）。
ease-in-out | 规定以慢速开始和结束的过渡效果（等于 cubic-bezier(0.42,0,0.58,1)）。
cubic-bezier(n,n,n,n) | 在 cubic-bezier函数中定义自己的值。可能的值是 0 至 1 之间的数值。

## 动画

* CSS3的动画属性

属性 | 描述
--- | ---
@keyframes | 规定动画。
animation | 所有动画属性的简写属性，除了 animation-play-state | 属性。
animation-name | 规定 @keyframes 动画的名称。
animation-duration | 规定动画完成一个周期所花费的秒或毫秒。默认是 0。
animation-timing-function | 规定动画的速度曲线。默认是 "ease"。
animation-fill-mode | 规定当动画不播放时（当动画完成时，或当动画有一个延迟未开始播放时），要应用到元素的样式。
animation-delay | 规定动画何时开始。默认是 0。
animation-iteration-count | 规定动画被播放的次数。默认是 1。
animation-direction | 规定动画是否在下一周期逆向地播放。默认是 "normal"。
animation-play-state | 规定动画是否正在运行或暂停。默认是 "running"。

```css
@keyframes myfirst
{
    0%   {background: red; left:0px; top:0px;}
    25%  {background: yellow; left:200px; top:0px;}
    50%  {background: blue; left:200px; top:200px;}
    75%  {background: green; left:0px; top:200px;}
    100% {background: red; left:0px; top:0px;}
}
@keyframes myfirst
{
    from {background: red;}
    to {background: yellow;}
}

div
{
    animation: myfirst 5s linear 2s infinite alternate;
}
```

## 多列

* 多列属性

属性 | 描述
--- | ---
column-count | 指定元素应该被分割的列数。
column-fill | 指定如何填充列
column-gap | 指定列与列之间的间隙
column-rule | 所有 column-rule-* 属性的简写
column-rule-color | 指定两列间边框的颜色
column-rule-style | 指定两列间边框的样式
column-rule-width | 指定两列间边框的厚度
column-span | 指定元素要跨越多少列
column-width | 指定列的宽度
columns | 设置 column-width 和 column-count 的简写

## flex

```css
father {
	display: flex;
	flex-direction: row; // 排列方式 决定主轴方向
	flex-wrap: nowrap; // 换行
	justify-content: flex-end; // 水平对齐方式
	align-items: center; // 垂直对齐方式
	align-content: center; // 多行对齐方式 注意：需要多行才行 多根轴线对齐方式
}

```

属性 | 参数 | 描述
---- | ---- | ----
display | flex | 给某个开启弹性布局
flex-direction | row | 水平方向，起点在左端（默认值）
flex-direction | row-reverse | 水平方向，起点在右端
flex-direction | column | 垂直方向，起点在上沿
flex-direction | column-reverse | 垂直方向，起点在下沿
flex-wrap | nowrap | 单行
flex-wrap | wrap | 换行（宽度不够自动换行，前提不参加收缩）
flex-wrap | wrap-reverse | 换行并反转
justify-content | flex-start | 左对齐
justify-content | flex-end | 右对齐
justify-content | center | 居中对齐
justify-content | space-between | 两端对齐（之间间隔相等）
justify-content | space-around | 每个项目两侧的间隔相等
align-items | flex-start | 起点对齐
align-items | flex-end | 终点对齐
align-items | center | 中点对齐
align-items | baseline | 基线对齐
align-items | stretch | 默认值（未设置高度或设为auto，将占满容器的高度）
align-content | flex-start | 左对齐
align-content | flex-end | 右对齐
align-content | center | 居中对齐
align-content | space-between | 两端对齐（之间间隔相等）
align-content | space-around | 每个项目两侧的间隔相等
align-content | stretch | 轴线占满整个交叉轴

+ 当这两个属性遇到了
  flex-direction: column / column-reverse  整个顺序就都变了

```
father children {
	flex: 1;
	flex-shrink: 0; // 为复杂布局而生 缩小比例
	flex-grow: 1; // 扩展比例
	align-self: flex-end; // 允许单个项目有与其他项目不一样的对齐方式
	flex-basis: 500px; // 最小分配空间
}

```

属性 | 参数 | 描述
---- | ---- | ----
flex | number | **均分**宽度 number（阿拉伯数字） 份
flex-shrink | number | 此时剩余空间不足时都等比例缩小，0 表示不参加收缩比例；若没写该属性，则为 1；number：1 2 3 ...
flex-grow | number | 剩余空间是正值的时，伸缩项目相对于伸缩容器里其他伸缩项目能分配到空间比例，若没写该属性，则为0 ，0代表不参与扩展
align-self | auto | 默认值auto，表示继承父级元素的align-items，如果没有父级，则等同于stretch
align-self | flex-start |
align-self | flex-end |
align-self | center |
align-self | baseline |
align-self | stretch |
flex-basis | number | 再分配之前，页已经分配得到空间（最小空间）


+ 剩余不足等比缩小计算公式
`剩余宽度：总体宽度 - 自适应两个元素的宽度的和`
`缩小后的：(每个元素的实际宽度 / 总宽度) * 剩余宽度`

+ align-self 属性 对应align-items

+ **缩写方式**
` flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]`
```
flex:1 0 500px;<!-- 可以写两个参数 -->

```

### flex兼容性问题

```
 解决UC、微信兼容性问题
 安卓平台的uc和微信
 	要加-webkit-
  	display: flex;
    display: -webkit-box;
    flex: 1;
    -webkit-box-flex: 1;
    -moz-box-flex: 1;
    box-flex: 1;
    webkit、moz、原生

    align-items: center;
    -webkit-box-align: center;
    flex-direction: column;
    box-orient: vertical;
    webkit、moz、原生

```

## user-modify

+ 语法
`div {-webkit-user-modify: read-write;}`

参数 | 描述
---- | ----
read-only | 只读
read-write | 内容可读写
read-write-plaintext-only | 内容可读写，但富粘贴的文本格式会丢失

## user-select

+ 语法
`div {-webkit-user-select: read-write;}`

参数 | 描述
---- | ----
auto | 用户可选内容
none | 不可选
text | 可选文本

## [~~倒影~~](http://www.w3chtml.com/css3/properties/border/box-reflect.html)

+ 语法
```

box-reflect：none | <direction> <offset>? <mask-box-image>?<direction> = above | below | left | right
<offset> = <length> | <percentage>
<mask-box-image> = none | <url> | <linear-gradient> | <radial-gradient> | <repeating-linear-gradient> | <repeating-radial-gradient>
默认值：none

```

参数 | 描述
---- | ----
none | 无倒影
above<direction> | 指定倒影在对象的上边
below<direction> | 指定倒影在对象的下边
left<direction> | 指定倒影在对象的左边
right<direction> | 指定倒影在对象的右边
offset | 可以是数字或者百分比,zh指倒影与对象之间的间隔 可以为负值
url | 使用绝对或相对地址指定遮罩图像
渐变 | 用渐变做遮罩层

+ 示例
	1. `div {-webkit-box-reflect: <direction>;} // 可取 above below left right`
	2. `div {-webkit-box-reflect: left 10px;} // 也可写百分比`
	3. `div {-webkit-box-reflect: left 10px -webkit-linear-gradient(top,rgba(250,250,250,0),rgba(250,250,250,.0) 30%,rgba(250,250,250,0.3));} // 可以线性 径向 重复`
	4. `div {-webkit-box-reflect: left 10px url(a/b/img.png);}`

## ~~滤镜~~

+ 语法
`filter: none | blur() | brightness() | contrast() | drop-shadow() | grayscale() | hue-rotate() | invert() | opacity() | saturate() | sepia() | url();`

参数 | 描述
---- | ----
none | 无SVG滤镜效果
blur | 模糊效果 px
brightness | 亮度 %/number
contrast | 对比度 %/number
grayscale | 灰度 %/number
hue-rotate | 色相旋转 deg
invert | 反色 %/number
opacity | 透明度 %/number
saturate | 饱和度 %/number
sepia | 褐色成都 %/number
drop-shadow | 阴影 (x y radius color)

## 移动端布局

* 纯粹的移动端

+ 不需要考虑任何PC上的展示效果

1. ~~百分比（不推荐使用）~~
2. **rem**
3. **viewpoint**
4. *无宽布局（不是说永远都不给宽度）*

* viewport

+ 可视区尺寸

移动设备上的viewport就是设备的屏幕上能用来显示我们的网页的那一块区域
浏览器上(也可能是一个app中的webview)用来显示网页的那部分区域
它可能比浏览器的可视区域要大，也可能比浏览器的可视区域要小。
默认情况下，手机网页采用980px的宽

+ 语法
`<meta name="viewport" id="viewport" content="width=375,initial-scale=1,user-scalable=1">`

+ content 参数

参数 | 描述
---- | ----
width | viewport的宽度(数值/device-width) 可以是具体数值
height | viewport的高度(数值/device-height) 可以是具体数值
initial-scale | 初始缩放比例 任意值
user-scalable | 是否允许用户缩放(yes/no)/(0/1)
maximum-scale | 最大缩放比例
minimum-scale | 最小缩放比例
~~target-densitydpi~~ | 仅供了解

+ ~~target-densitydpi~~
`一个屏幕像素密度是由屏幕分辨率决定的，通常定义为每英寸点的数量（dpi）。Android支持三种屏幕像素密度：低像素密度，中像素密度，高像素密度。一个低像素密度的屏幕每英寸上的像素点更少，而一个高像素密度的屏幕每英寸上的像素点更多。Android Browser和WebView默认屏幕为中像素密度。`

取值 | 描述
---- | ----
device-dpi | 使用设备原本的 dpi 作为目标 dp。 不会发生默认缩放
high-dpi | 使用hdpi 作为目标 dpi。 中等像素密度和低像素密度设备相应缩小
medium-dpi | 使用mdpi作为目标 dpi。 高像素密度设备相应放大， 像素密度设备相应缩小。 这是默认的target density.
low-dpi | 使用mdpi作为目标 dpi。中等像素密度和高像素密度设备相应放大

* ios专用属性

1. 是否进入webapp全屏模式
	`<meta name="apple-mobile-web-app-capable" content="yes">`
2. 禁止iPhone把数字识别为电话
	`<meta name="format-detection" content="telephone=no" >`
3.  添加主屏后的标题
	`<meta name="apple-mobile-web-app-title" content="标题">`
4. 添加主屏后的图标
	`<link rel="apple-touch-icon-precomposed" href="/57x57-phone.png">`
	- 规格：1. iPhone、iTouch默认57\*57-必要；2. iPad72\*72-可没有，推荐添加Retina iPhone和Retina iTounch，114\*114像素，可以没有但推荐有；3. Retina iPad，144\*144像素，可以没有但推荐有

+ **移动端注意事项**
	1. A点击有黑色背景
	`-webkit-tap-heighlight-color:transparent;`
	2. 禁用iPhone中Safari的字号自动调整
	`html{-webkit-text-size-adjust:none;}`

* css单位

+ 尺寸

单位 | 描述
---- | ----
%	| 百分比
in | 英寸
cm | 厘米
mm | 毫米
**em** |1em 等于当前的字体尺寸。2em 等于当前字体尺寸的两倍。例如，如果某元素以 12pt 显示，那么 2em 是24pt。在 CSS 中，em 是非常有用的单位，因为它可以自动适应用户所使用的字体。
ex | 一个 ex 是一个字体的 x-height。 (x-height 通常是字体尺寸的一半。)
pt | 磅 (1 pt 等于 1/72 英寸)
pc | 12 点活字 (1 pc 等于 12 点)
px | 像素 (计算机屏幕上的一个点)
**rem** | 相对单位，可理解为”root em”, 相对根节点html的字体大小来计算，CSS3新加属性
vw | viewpoint width，视窗宽度，1vw等于视窗宽度的1%
vh | viewpoint height，视窗高度，1vh等于视窗高度的1%
vmin | vw和vh中较小的那个
vmax| vw和vh中较大的那个

> **em  的字体大小 是根据父级的字体大小来计算的 如果父级没有字体大小，往上找，找到了就用 找不到 默认 16px**


+ 颜色

单位 | 描述
---- | ----
(颜色名) | 颜色名称 (比如 red)
rgb(x,x,x) | RGB 值 (比如 rgb(255,0,0))
rgb(x%, x%, x%) | RGB 百分比值 (比如 rgb(100%,0%,0%))
rgba(x,x,x,o) | 代表透明度
\#rrggbb | 十六进制数 (比如 #ff0000)

+ retina图片适配问题

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>图片适配</title>
    <meta name="viewport" id="viewport" content="width=375,initial-scale=1,user-scalable=0">
    <style>
        div{
            width: 100px;
            height: 100px;
            /*border: solid 2px red;*/
            margin-bottom: 10px;
        }
        .div1{
            background: url(icon@3x.png) 0 0 no-repeat;
        }
        .div2{
            background: url(icon.png) 0 0 no-repeat;
            background-image: -webkit-image-set(url(icon.png) 1x,url(icon@2x.png) 2x);
        }
        .div3{
            background: url(icon@3x.png) 0 0 no-repeat;
            background-image: -webkit-image-set(url(icon.png) 1x,url(icon@2x.png) 2x,url(icon@3x.png) 3x);
        }

    </style>
</head>
<body>
    <!--retina  2倍 或者 3倍的屏幕-->
    <div class="div1"></div>
    <div class="div2"></div>
    <div class="div3"></div>

    <img src="icon.png" alt="">
    <img src="icon.png" srcset="icon@2x.png 2x" alt="">
</body>
</html>

```

+ -webkit-image-set 设置 让retina的屏幕 看图片更清晰

+ img 引入的图
`<img src="pic.png" srcset="pic@2x.png 2x">`

+ ~~base 64~~
	- 把图片转成 64进制的编码
	- 语法
	`div { background-image:url("data:image/png;base64,编码");}`

* 移动端页面

+ 适配（兼容），适应各个不同的设备
+ 浏览器、微信（通过转发朋友圈）、QQ（内置浏览器）、UC
	- \*米、华\*会有部分兼容问题
+ 不需要考虑兼容pc、pad
+ 有的公司会把pc版和手机版分开来做
	- 数据交互量很大

* **rem布局（所有机型）**

+ 示例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>rem布局</title>
    <meta name="viewport" id="viewport" content="width=device-width,initial-scale=1,user-scalable=0">
    <script>
        alert(window.screen.width);
        var _html = document.getElementsByTagName('html')[0];
        var ch = document.documentElement.clientWidth;
        if(ch>640) {
            _html.style.fontSize = '40px';
            /*最大是40*/
        }
        else{
            _html.style.fontSize = ch / 16 + 'px';
            /*ch / 16 份数*/
        }
    </script>
    <style>
        html{
            font-size: 30px;
        }
        .box{
            width: 7.5rem;
            height: 7.5rem;
            background-color: yellowgreen;
        }
    </style>
</head>
<body>
    <div class="box"></div>

<!--
    有一个300的元素，在 414 保持 300
                    375     300？减小多少？

    640（iphone5 的320来的）  /  750(根据iphone 6)  /  1000+
        如果可视区的尺寸 比640（页面大小） 要大  页面只显示640
        如果小的话，会按照一个比例来缩放。
        40 - HTML的 font-size

        640 / 40 = 16 份 ， 每一份最大是40

    750
        50
        750 / 50 = 15

    适配：
        1 通过rem的方式来进行适配
'

        640的页面 分成了 64份  每份最大是10

        元素大小现在是 315  = 多少  31.5rem ？
-->
</body>
</html>

```

* ~~viewpoint布局（主流机型）~~

+ 缩放比例
	- 屏幕的尺寸  / 网页的尺寸（设计图的尺寸）
+ 机型兼容
+ js写法
	1. 引入js文件
	`<script src="mobile-util.js"></script> // 必须在meta标签下`
	2. 定宽：对应meta 标签写法
	`<meta name="viewport" content="width=640">`
+ [viewport切图注意事项](https://www.zhihu.com/question/25308946
 "参考")
	- 640/750 正常切
	- 1242(iphone 6p 做的三倍图)/1125(iphone6 做的三倍图)/960(iphone5 做的三倍)
+ [转rem](http://www.520ued.com/tools/rem "px-->rem")

##### rem/viewpoint布局引入js

+ 代码

```js
/**
 * 该 JS 中，包含常用的 UA 判断、页面适配、search 参数转 键值对。
 * 该 JS 应在 head 中尽可能早的引入，减少重绘。
 *
 * fixScreen 方法根据两种情况适配，该方法自动执行。
 *      1. 定宽： 对应 meta 标签写法 --
            <meta name="viewport" content="width=750">
 *         该方法会提取 width 值，主动添加 scale 相关属性值。
 *         注意： 如果 meta 标签中指定了 initial-scale， 该方法将不做处理（即不执行）。
 *
 *      2. REM: 不用写 meta 标签，该方法根据 dpr 自动生成，并在 html 标签中加上 data-dpr 和 font-size 两个属性值。
 *         该方法约束：IOS 系统最大 dpr = 3，其它系统 dpr = 1，页面每 dpr 最大宽度（即页面宽度/dpr） = 750，REM 换算比值为 16。
 *         对应 css 开发，任何弹性尺寸均使用 rem 单位，rem 默认宽度为 视觉稿宽度 / 16;
 *         scss 中 $ppr(pixel per rem) 变量写法 -- $ppr: 750px/16/1rem;
 *         元素尺寸写法 -- html { font-size: $ppr*1rem; } body { width: 750px/$ppr; }。
 */
window.mobileUtil = (function(win, doc) {
	var UA = navigator.userAgent,
		isAndroid = /android|adr/gi.test(UA),
		isIos = /iphone|ipod|ipad/gi.test(UA) && !isAndroid, // 据说某些国产机的UA会同时包含 android iphone 字符
		isMobile = isAndroid || isIos;  // 粗略的判断

	return {
		isAndroid: isAndroid,
		isIos: isIos,
		isMobile: isMobile,

        isNewsApp: /NewsApp\/[\d\.]+/gi.test(UA),
		isWeixin: /MicroMessenger/gi.test(UA),
		isQQ: /QQ\/\d/gi.test(UA),
		isYixin: /YiXin/gi.test(UA),
		isWeibo: /Weibo/gi.test(UA),
		isTXWeibo: /T(?:X|encent)MicroBlog/gi.test(UA),

		tapEvent: isMobile ? 'tap' : 'click',

		/**
		 * 缩放页面
		 */
		fixScreen: function() {
            var metaEl = doc.querySelector('meta[name="viewport"]'),
                metaCtt = metaEl ? metaEl.content : '',
                matchScale = metaCtt.match(/initial\-scale=([\d\.]+)/),
			    matchWidth = metaCtt.match(/width=([^,\s]+)/);

            if ( !metaEl ) { // REM
                var docEl = doc.documentElement,
                    maxwidth = docEl.dataset.mw || 750, // 每 dpr 最大页面宽度
                    dpr = isIos ? Math.min(win.devicePixelRatio, 3) : 1,
                    scale = 1 / dpr,
                    tid;

                docEl.removeAttribute('data-mw');
                docEl.dataset.dpr = dpr;
                metaEl = doc.createElement('meta');
                metaEl.name = 'viewport';
                metaEl.content = fillScale(scale);
                docEl.firstElementChild.appendChild(metaEl);

                var refreshRem = function() {
                    var width = docEl.getBoundingClientRect().width;
                    if (width / dpr > maxwidth) {
                        width = maxwidth * dpr;
                    }
                    var rem = width / 16;
                    docEl.style.fontSize = rem + 'px';
                };

                win.addEventListener('resize', function() {
                    clearTimeout(tid);
                    tid = setTimeout(refreshRem, 300);
                }, false);
                win.addEventListener('pageshow', function(e) {
                    if (e.persisted) {
                        clearTimeout(tid);
                        tid = setTimeout(refreshRem, 300);
                    }
                }, false);

                refreshRem();
            } else if ( isMobile && !matchScale && ( matchWidth && matchWidth[1] != 'device-width' ) ) { // 定宽
                var	width = parseInt(matchWidth[1]),
                    iw = win.innerWidth || width,
                    ow = win.outerWidth || iw,
                    sw = win.screen.width || iw,
                    saw = win.screen.availWidth || iw,
                    ih = win.innerHeight || width,
                    oh = win.outerHeight || ih,
                    ish = win.screen.height || ih,
                    sah = win.screen.availHeight || ih,
                    w = Math.min(iw,ow,sw,saw,ih,oh,ish,sah),
                    scale = w / width;

                if ( scale < 1 ) {
                    metaEl.content = metaCtt + ',' + fillScale(scale);
                }
            }

            function fillScale(scale) {
                return 'initial-scale=' + scale + ',maximum-scale=' + scale + ',minimum-scale=' + scale + ',user-scalable=no';
            }
		},

		/**
		 * 转href参数成键值对
		 * @param href {string} 指定的href，默认为当前页href
		 * @returns {object} 键值对
		 */
		getSearch: function(href) {
			href = href || win.location.search;
			var data = {},reg = new RegExp( "([^?=&]+)(=([^&]*))?", "g" );
			href && href.replace(reg,function( $0, $1, $2, $3 ){
				data[ $1 ] = $3;
			});
			return data;
		}
	};
})(window, document);

// 默认直接适配页面
mobileUtil.fixScreen();

```

### 响应式

+ 一套网站，兼容N多设备（pc、pad、移动端、IE6~8）
	- 必须共享一套HTML结构，样式不同而已，通过设备的分辨率来自动切换样式
+ 只是用于简单的页面：博客、新闻、简单的公司门户（公司小网站）
+ 需要兼容的尺寸
	- pc 普屏 1000（放的显示器 - 1024\*768）
	- pc 宽屏 1190/1200/1210/1600 分辨率 1366\*768 / 1440\*768 / 1920\*1080
	-pad 768 横屏和竖屏 1024\*768 / 768\*1024
	-phone 分辨率就都不一定了

#### 媒体查询

+ 语法
```

声明：@media
条件：min-width、height/max-width、height设备类型

min-width 最小宽度 >=
max-width 最大宽度 <=

原则：永远从 最小的设备写起 （phone > pad > pc > pc宽屏）

and 并且
	not 不是
	only 不支持的忽略
	device-width/min、max
	device-width / min-device-width / max-device-width

@media (orientation: landscape) 横屏
@media (orientation: portrait) 竖屏

<!-- >= 768 -->
@media (min-width:768px) {
	div {
		width:600px;
	}
}

<!-- >=1000 && <= 1200 -->
@media (min-width:1000px) and (max-width:1200px) {
	div {
		width:800px;
	}
}

<!-- 不是 屏幕 -->
@media (min-width:768px) not screen {
	div {
		width:600px;
	}
}

```

[媒体类型](http://www.runoob.com/cssref/css3-pr-mediaquery.html "媒体类型") | 描述
---- | ----
all | 用于所有的媒体设备
aural | 用于语音和音频合成器
braille | 用于盲人用点字法触觉回馈设备
embossed | 用于分页的盲人用点字法打印机
handheld | 用于小的手持的设备
print | 用于打印机
projection | 用于方案展示，比如幻灯片
screen | 用于电脑显示器
tty | 用于使用固定密度字母栅格的媒体，比如电传打字机和终端
tv | 用于电视机类型的设备

+ 响应式样式表的引用
	1. common.css 公共样式（手机样式）
	2. ~~ie.css ie低版本兼容样式（一般不兼容ie低版本）~~
	3. pad.css pad样式
	4. pc.css 普屏pc样式
	5. pc-w.css 宽屏pc样式
> **css文件命名可随自己**

	- 语法
```

<link rel="stylesheet" href="style/common.css" type="text/css">
<link rel="stylesheet" href="style/pad.css" type="text/css" media="(min-width:768px)">
<link rel="stylesheet" href="style/pc.css" type="text/css" media="(min-width:1000px)">
<link rel="stylesheet" href="style/pc-w.css" type="text/css" media="(min-width:1190px)">


```

#### IE版本判断

+ IE对HTML注释做了一些扩展，使之可以支持条件判断表达式

条件 | 描述
---- | ----
[if IE] | 判断是否IE
[if IE 7] | 判断是否是IE7
[if !IE] | 判断是否不是IE
[if lt IE 5.5] | 判断是否是IE5.5 以下版本。  (<)
[if lte IE 6] | 判断是否等于IE6 版本或者以下 (<=)
[if gt IE 5] | 判断是否IE5以上版本  （> ）
[if gte IE 7] | 判断是否 IE7 版本或者以上
[if !(IE 7)] | 判断是否不是IE7
[if (gt IE 5)&(lt IE 7)] | 判断是否大于IE5， 小于IE7
[if (IE 6)&#124;(IE 7)] | 判断是否IE6 或者 IE7 | &#124; === |

+ 示例

```html
<!--[if IE]><p>You are using Internet Explorer.</p><![endif]-->
<!--[if !IE]><p>You are not using Internet Explorer.</p><![endif]>
<!--[if IE 7]><p>Welcome to Internet Explorer 7!</p><![endif]-->
<!--[if !(IE 7)]><p>You are not using version 7.</p><![endif]-->
<!--[if gte IE 7]><p>You are using IE 7 or greater.</p><![endif]-->
<!--[if (IE 5)]><p>You are using IE 5 (any version).</p><![endif]-->
<!--[if (gte IE 5.5)&(lt IE 7)]><p>You are using IE 5.5 or IE 6.</p><![endif]-->
<!--[if lt IE 5.5]><p>Please upgrade your version of Internet Explorer.</p><![endif]-->
<!--[if IE]><p>You are using Internet Explorer.</p><![endif]-->
<!--[if !IE]><p>You are not using Internet Explorer.</p><![endif]>
<!--[if IE 7]><p>Welcome to Internet Explorer 7!</p><![endif]-->
<!--[if !(IE 7)]><p>You are not using version 7.</p><![endif]-->
<!--[if gte IE 7]><p>You are using IE 7 or greater.</p><![endif]-->
<!--[if (IE 5)]><p>You are using IE 5 (any version).</p><![endif]-->
<!--[if (gte IE 5.5)&(lt IE 7)]><p>You are using IE 5.5 or IE 6.</p><![endif]-->
<!--[if lt IE 5.5]><p>Please upgrade your version of Internet Explorer.</p><![endif]-->

```

> **注：IE5 以下的版本不支持这种注释扩展**

___
> 共同学习，共同进步