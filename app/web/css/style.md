# 样式属性

## background

CSS背景属性用于定义HTML元素的背景

```css
background:bg-color bg-image position/bg-size bg-repeat bg-origin bg-clip bg-attachment initial|inherit;
```

* background-color

```css
body {
    background-color: 十六进制(#fff000) | RGB(rgb(255,0,0)) | RGBA(rgba(255,0,0,1)) | 颜色名称(red);
}
```

* background-image
    1. url('URL')
    ```css
    /* 图像的url */
    body {
        background-image: url('./logo.png');
    }
    ```
    2. none 无背景图像会显示，默认
    3. linear-gradient()
    ```css
    /* 线性渐变图像
    direction	用角度值指定渐变的方向（或角度）
    color-stop1, color-stop2,...	用于指定渐变的起止颜色
     background-image: linear-gradient(to right, red , blue);
     background-image: linear-gradient(180deg, red, blue);
     background-image: linear-gradient(to right, rgba(255,0,0,0), rgba(255,0,0,1));
     */
    body {
        background-image: linear-gradient(direction, color-stop1, color-stop2...)
    }
    ```
    4. radial-gradient()
    ```css
    /*
    径向渐变
    */
    body {
        background-image: radial-gradient(shape size at position, start-color, ..., last-color);
    }
    ```
    5. repeating-linear-gradient()
    ```css
    /*重复线性渐变
    background: repeating-linear-gradient(angle | to side-or-corner, color-stop1, color-stop2, ...);
    */
    body {
        background-image: repeating-linear-gradient(red, yellow 10%, green 20%);
    }
    ```
    6. repeating-radial-gradient()
    ```css
    /*重复的线性渐变
    background-image: repeating-radial-gradient(shape size at position, start-color, ..., last-color);
    */
    body {
        background-image: repeating-radial-gradient(red, yellow 10%, green 15%);
    }
    ```
    7. inherit 指定背景图像应该从父元素继承

值 | 描述
--- | ---
shape | 确定圆的类型:ellipse (默认): 指定椭圆形的径向渐变。circle ：指定圆形的径向渐变
size | 定义渐变的大小，可能值：farthest-corner (默认) : 指定径向渐变的半径长度为从圆心到离圆心最远的角closest-side ：指定径向渐变的半径长度为从圆心到离圆心最近的边closest-corner ： 指定径向渐变的半径长度为从圆心到离圆心最近的角farthest-side ：指定径向渐变的半径长度为从圆心到离圆心最远的边
position | 定义渐变的位置。可能值：center（默认）：设置中间为径向渐变圆心的纵坐标值。top：设置顶部为径向渐变圆心的纵坐标值。bottom：设置底部为径向渐变圆心的纵坐标值。
start-color, ..., last-color | 用于指定渐变的起止颜色。

Value | 描述
--- | ---
angle | 定义渐变的角度方向。从 0deg 到 360deg，默认为 180deg。
side-or-corner | 指定线性渐变的起始位置。由两个关键字组成：第一个为指定水平位置(left 或 right)，第二个为指定垂直位置（top 或bottom）。 顺序是随意的，每个关键字都是可选的。
color-stop1, color-stop2,... | 指定渐变的起止颜色，由颜色值、停止位置（可选，使用百分比指定）组成。

* background-position

背景图像的位置

值 | 描述
--- | ---
left top / left center / left bottom / right top / right center / right bottom / center top / center center / center bottom | 如果仅指定一个关键字，其他值将会是"center"
x% y% | 第一个值是水平位置，第二个值是垂直。左上角是0％0％。右下角是100％100％。如果仅指定了一个值，其他值将是50％。 。默认值为：0％0％
xpos ypos | 第一个值是水平位置，第二个值是垂直。左上角是0。单位可以是像素（0px0px）或任何其他 CSS单位。如果仅指定了一个值，其他值将是50％。你可以混合使用％和positions
inherit | 指定background-position属性设置应该从父元素继承

* background-size

背景图像的大小

```css
background-size: length|percentage|cover|contain;
```

值 | 描述
--- | ---
length | 设置背景图片高度和宽度。第一个值设置宽度，第二个值设置的高度。如果只给出一个值，第二个是设置为 auto(自动)
percentage | 将计算相对于背景定位区域的百分比。第一个值设置宽度，第二个值设置的高度。如果只给出一个值，第二个是设置为"auto(自动)"
cover | 此时会保持图像的纵横比并将图像缩放成将完全覆盖背景定位区域的最小大小。
contain | 此时会保持图像的纵横比并将图像缩放成将适合背景定位区域的最大大小。

* background-repeat

如何重复背景图像

值 | 说明
--- | ---
repeat | 背景图像将向垂直和水平方向重复。这是默认
repeat-x | 只有水平位置会重复背景图像
repeat-y | 只有垂直位置会重复背景图像
no-repeat | background-image不会重复
inherit	指定background-repea属性设置应该从父元素继承

* background-origin

背景图像的定位区域

值 | 描述
--- | ---
padding-box | 背景图像填充框的相对位置
border-box | 背景图像边界框的相对位置
content-box | 背景图像的相对位置的内容框

* background-clip

背景图像的绘画区域

值 | 说明
--- | ---
border-box | 默认值。背景绘制在边框方框内（剪切成边框方框）。
padding-box | 背景绘制在衬距方框内（剪切成衬距方框）。
content-box | 背景绘制在内容方框内（剪切成内容方框）。

* background-attachment

背景图像是否固定或者随着页面的其余部分滚动。

值 | 描述
scroll | 背景图片随着页面的滚动而滚动，这是默认的。
fixed | 背景图片不会随着页面的滚动而滚动。
local | 背景图片会随着元素内容的滚动而滚动。
initial |
 设置该属性的默认值。 阅读关于 initial 内容
inherit	| 指定 background-attachment 的设置应该从父元素继承。 阅读关于 inherit 内容

* background-blend-mode

混合模式

值 | 描述
--- | ---
normal | 默认值。设置正常的混合模式。
multiply | 正片叠底模式。
screen | 滤色模式。
overlay | 叠加模式。
darken | 变暗模式。
lighten | 变亮模式。
color-dodge | 颜色减淡模式。
saturation | 饱和度模式。
color | 颜色模式。
luminosity | 亮度模式。

## 文本

* 文本颜色

```css
body {
    color: #00ff00 | rgb(0,0,0) | rgba(0.0.0.1) | red;
}
```

* 文本对齐

```css
body {
    text-align: center(居中) | right | left | justify(每一行被展开为宽度相等) | inherit(父元素继承)
}
```

* 文本修饰

```css
body {
    text-decoration: none | underline(下划线) | underline wavy red(红色波浪形下划线) | line-through(过文本下的一条线) | blink(闪烁的文本) | inhrit
}
```

* 文本转换

```css
body {
    text-transform: none | capitalize(文本中的每个单词以大写字母开头。) | uppercase | lowercase | inherit
}
```

* 文本缩进

```css
body {
    text-indexnt: length | % |inherit
}
```

* 文本方向

```css
body {
    direction: ltr(默认。文本方向从左到右。) | rtl(文本方向从右到左) | inherit
}
```

* 字符间距

```css
body {
    letter-spacing: normal | length | inherit
}
```

* 行高

```css
body {
    line-height: normal | number | length | % | inherit
}
```

* 文本阴影

```css
/* text-shadow: h-shadow v-shadow blur color; */
body {
    text-shadow: 2px 2px #fff000;
}
```

值 | 描述
--- | ---
h-shadow | 必需。水平阴影的位置。允许负值。
v-shadow | 必需。垂直阴影的位置。允许负值。
blur | 可选。模糊的距离。
color | 可选。阴影的颜色。参阅 CSS 颜色值。

* 设置或返回文本是否被重写

```css
/* unicode-bidi 属性与 direction 属性一起使用，来设置或返回文本是否被重写，以便在同一文档中支持多种语言 */
body {
    direction:rtl;
    unicode-bidi:bidi-override;
}
```

值 | 描述
--- | ---
normal | 默认。不使用附加的嵌入层面。
embed | 创建一个附加的嵌入层面。
bidi-override | 创建一个附加的嵌入层面。重新排序取决于 direction 属性。
initial | 设置该属性为它的默认值。请参阅 initial。
inherit | 从父元素继承该属性。请参阅 inherit。

* 元素的垂直对齐

```css
body {
    vertical-align: text-top;
}
```

值 | 描述
--- | ---
baseline | 默认。元素放置在父元素的基线上。
sub | 垂直对齐文本的下标。
super | 垂直对齐文本的上标
top	| 把元素的顶端与行中最高元素的顶端对齐
text-top | 把元素的顶端与父元素字体的顶端对齐
middle | 把此元素放置在父元素的中部。
bottom | 把元素的底端与行中最低的元素的顶端对齐。
text-bottom | 把元素的底端与父元素字体的底端对齐。
length	|
% | 使用 "line-height" 属性的百分比值来排列此元素。允许使用负值。
inherit | 规定应该从父元素继承 vertical-align 属性的值。

* 元素中空白的处理方式

```css
body {
    white-space:nowrap;
}
```

值 | 描述
--- | ---
normal | 默认。空白会被浏览器忽略。
pre | 空白会被浏览器保留。其行为方式类似 HTML 中的 `<pre>` 标签。
nowrap | 文本不会换行，文本会在在同一行上继续，直到遇到 `<br>` 标签为止。
pre-wrap | 保留空白符序列，但是正常地进行换行。
pre-line | 合并空白符序列，但是保留换行符。
inherit	规定应该从父元素继承 white-space 属性的值。

* 字间距

```css
body {
    word-spacing:30px;
}
```

值 | 描述
--- | ---
normal | 默认。定义单词间的标准空间。
length | 定义单词间的固定空间。
inherit | 规定应该从父元素继承 word-spacing 属性的值。


## 字体

Property | 描述
--- | ---
font | 在一个声明中设置所有的字体属性
font-family | 指定文本的字体系列
font-size | 指定文本的字体大小
font-style | 指定文本的字体样式
font-variant | 以小型大写字体或者正常字体显示文本。
font-weight | 指定字体的粗细。

## 链接

```css
a:link {color:#000000;}      /* 未访问链接*/
a:visited {color:#00FF00;}  /* 已访问链接 */
a:hover {color:#FF00FF;}  /* 鼠标移动到链接上 */
a:active {color:#0000FF;}  /* 鼠标点击时 */
```

## 列表样式

属性 | 描述
--- | ---
list-style | 简写属性。用于把所有用于列表的属性设置于一个声明中
list-style-image | 将图象设置为列表项标志。
list-style-position | 设置列表中列表项标志的位置。
list-style-type | 设置列表项标志的类型。

## 边框

```css
body {
    /* border: width style color; */
    border: 1px solid red;
}
```

border-style样式 | 描述
--- | ---
none | 默认无边框
dotted | 定义一个点线边框
dashed | 定义一个虚线边框
solid | 定义实线边框
double | 定义两个边框。 两个边框的宽度和 border-width 的值相同
groove | 定义3D沟槽边框。效果取决于边框的颜色值
ridge | 定义3D脊边框。效果取决于边框的颜色值
inset | 定义一个3D的嵌入边框。效果取决于边框的颜色值
outset | 定义一个3D突出边框。 效果取决于边框的颜色值

* outline

轮廓（outline）是绘制于元素周围的一条线，位于边框边缘的外围，可起到突出元素的作用。
轮廓（outline）属性指定元素轮廓的样式、颜色和宽度。


## 显示

* 隐藏元素

```css
.hidden {
    /* visibility:hidden可以隐藏某个元素，但隐藏的元素仍需占用与未隐藏之前一样的空间。也就是说，该元素虽然被隐藏了，但仍然会影响布局。 */
    visibility: hidden;
}

.hidden {
    /* display:none可以隐藏某个元素，且隐藏的元素不会占用任何空间。也就是说，该元素不但被隐藏了，而且该元素原本占用的空间也会从页面布局中消失。 */
    display: none;
}
```

* 块级元素(block)特性：
    + 总是独占一行，表现为另起一行开始，而且其后的元素也必须另起一行显示;
    + 宽度(width)、高度(height)、内边距(padding)和外边距(margin)都可控制;

* 内联元素(inline)特性：
    + 和相邻的内联元素在同一行;
    + 宽度(width)、高度(height)、内边距的top/bottom(padding-top/padding-bottom)和外边距的top/bottom(margin-top/margin-bottom)都不可改变，就是里面文字或图片的大小;

* 块级元素主要有：
    + address , blockquote , center , dir , div , dl , fieldset , form , h1 , h2 , h3 , h4 , h5 , h6 , hr , isindex , menu , noframes , noscript , ol , p , pre , table , ul , li

* 内联元素主要有：
    + a , abbr , acronym , b , bdo , big , br , cite , code , dfn , em , font , i , img , input , kbd , label , q , s , samp , select , small , span , strike , strong , sub , sup ,textarea , tt , u , var

* 可变元素(根据上下文关系确定该元素是块元素还是内联元素)：
    + applet ,button ,del ,iframe , ins ,map ,object , script

* CSS中块级、内联元素的应用：
    + 利用CSS我们可以摆脱上面表格里HTML标签归类的限制，自由地在不同标签/元素上应用我们需要的属性。
    + 主要用的CSS样式有以下三个：
        - display:block  -- 显示为块级元素
        - display:inline  -- 显示为内联元素
        - display:inline-block -- 显示为内联块元素，表现为同行显示并可修改宽高内外边距等属性我们常将`<ul>`元素加上display:inline-block样式，原本垂直的列表就可以水平显示了。

## 定位

* static 定位

```css
/* 静态定位的元素不会受到 top, bottom, left, right影响。 */
body {
    position: static;
}
```

* fixed 定位

```css
/* 元素的位置相对于浏览器窗口是固定位置。
即使窗口是滚动的它也不会移动： */
body {
    position: fixed;
}
```

* relative 定位

```css
/* 相对定位元素的定位是相对其正常位置。 */
body {
    position: relative;
}
```

* absolute 定位

```css
/* 绝对定位的元素的位置相对于最近的已定位父元素，如果元素没有已定位的父元素，那么它的位置相对于<html>: */
body {
    position: absolute;
}
```

* sticky 定位

sticky 英文字面意思是粘，粘贴，所以可以把它称之为粘性定位。
position: sticky; 基于用户的滚动位置来定位。
粘性定位的元素是依赖于用户的滚动，在 position:relative 与 position:fixed 定位之间切换。
它的行为就像 position:relative; 而当页面滚动超出目标区域时，它的表现就像 position:fixed;，它会固定在目标位置。
元素定位表现为在跨越特定阈值前为相对定位，之后为固定定位。
这个特定阈值指的是 top, right, bottom 或 left 之一，换言之，指定 top, right, bottom 或 left 四个阈值其中之一，才可使粘性定位生效。否则其行为与相对定位相同。

```css
body {
    position: sticky;
}
```

* 剪辑一个绝对定位的元素

```css
img {
    position:absolute;
    clip:rect(0px,60px,200px,0px);
}
```

值 | 描述
--- | ---
shape | 设置元素的形状。唯一合法的形状值是：rect (top, right, bottom, left)
auto | 默认值。不应用任何剪裁。
inherit | 规定应该从父元素继承 clip 属性的值。

* cursor光标

值 | 描述
--- | ---
url | 需使用的自定义光标的 URL。注释：请在此列表的末端始终定义一种普通的光标，以防没有由 URL 定义的可用光标。
default | 默认光标（通常是一个箭头）
auto | 默认。浏览器设置的光标。
crosshair | 光标呈现为十字线。
pointer | 光标呈现为指示链接的指针（一只手）
move | 此光标指示某对象可被移动。
e-resize | 此光标指示矩形框的边缘可被向右（东）移动。
ne-resize | 此光标指示矩形框的边缘可被向上及向右移动（北/东）。
nw-resize | 此光标指示矩形框的边缘可被向上及向左移动（北/西）。
n-resize | 此光标指示矩形框的边缘可被向上（北）移动。
se-resize | 此光标指示矩形框的边缘可被向下及向右移动（南/东）。
sw-resize | 此光标指示矩形框的边缘可被向下及向左移动（南/西）。
s-resize | 此光标指示矩形框的边缘可被向下移动（北/西）。
w-resize | 此光标指示矩形框的边缘可被向左移动（西）。
text | 此光标指示文本。
wait | 此光标指示程序正忙（通常是一只表或沙漏）。
help | 此光标指示可用的帮助（通常是一个问号或一个气球）。

* overflow


值 | 描述
--- | ---
visible | 默认值。内容不会被修剪，会呈现在元素框之外。
hidden | 内容会被修剪，并且其余内容是不可见的。
scroll | 内容会被修剪，但是浏览器会显示滚动条以便查看其余的内容。
auto | 如果内容被修剪，则浏览器会显示滚动条以便查看其余的内容。
inherit | 规定应该从父元素继承 overflow 属性的值。

___
> 共同学习，共同进步