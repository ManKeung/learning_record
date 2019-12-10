# HTML5

HTML5是HTML最新的修订版本，2014年10月由万维网联盟（W3C）完成标准制定。
HTML5的设计目的是为了在移动设备上支持多媒体。
HTML5 简单易学。

* 完美的 Shiv 解决方案

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>渲染 HTML5</title>
  <!--[if lt IE 9]>
  <script src="http://cdn.static.runoob.com/libs/html5shiv/3.7/html5shiv.min.js"></script>
  <![endif]-->
</head>

<body>

<h1>我的第一篇文章</h1>

<article>
学的不仅是技术，更是梦想！！！
</article>

</body>
</html>
```

## 全局属性

* accesskey

设置访问元素的键盘快捷键。

```html
<!-- 提示： 各种浏览器下accesskey快捷键的使用方法：
IE浏览器
按住Alt键，点击accesskey定义的快捷键(焦点将移动到链接)，再按回车.
FireFox浏览器
按住Alt+Shift键，点击accesskey定义的快捷键.
Chrome浏览器
按住Alt键，点击accesskey定义的快捷键.
Opera浏览器
按住Shift键，点击esc，出现本页定义的accesskey快捷键列表可供选择.
Safari浏览器
按住Alt键，点击accesskey定义的快捷键. -->
<a href="//www.runoob.com/html/html-tutorial.html" accesskey="h">HTML 教程</a><br>
<a href="//www.runoob.com/css/css-tutorial.html" accesskey="c">CSS 教程</a>
```

* class

规定元素的类名（classname）

* id

规定元素的唯一 id

* style

规定元素的行内样式（inline style）

* title

规定元素的额外信息（可在工具提示中显示）

* contenteditable

规定是否可编辑元素的内容。

```html
<!-- true(可编辑) | false(不可编辑) -->
<p contenteditable="true">这是一个可编辑段落。</p>
```

* contextmenu

指定一个元素的上下文菜单。当用户右击该元素，出现上下文菜单

```html
<!-- 目前只有 Firefox 浏览器支持 contextmenu 属性。 -->
<div contextmenu="mymenu">

<menu type="context" id="mymenu">
  <menuitem label="Refresh"></menuitem>
  <menuitem label="Twitter"></menuitem>
</menu>

</div>
```

* data-*

用于存储页面的自定义数据

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>document</title>
<script>
function showDetails(animal)
{
	var animalType = animal.getAttribute("data-animal-type");
	alert("The " + animal.innerHTML + " is a " + animalType + ".");
}
</script>
</head>
<body>

<h1>物种</h1>
<p>点击一个物种，看看它是什么类型：</p>

<ul>
  <li onclick="showDetails(this)" id="owl" data-animal-type="bird">Owl</li>
  <li onclick="showDetails(this)" id="salmon" data-animal-type="fish">Salmon</li>
  <li onclick="showDetails(this)" id="tarantula" data-animal-type="spider">Tarantula</li>
</ul>

</body>
</html>
```

* dir

设置元素中内容的文本方向。

```html
<bdo dir="rtl">文本方向从右到左!</bdo>
<!-- ltr	默认。从左向右的文本方向。
rtl	从右向左的文本方向。
auto	让浏览器根据内容来判断文本方向。仅在文本方向未知时推荐使用。 -->
```

* draggable

指定某个元素是否可以拖动

```html
<!-- true	规定元素是可拖动的。
false	规定元素是不可拖动的。
auto	使用浏览器的默认特性。 -->
<!DOCTYPE HTML>
<html>
<head>
<meta charset="utf-8">
<title>document</title>
<style type="text/css">
#div1 {width:350px;height:70px;padding:10px;border:1px solid #aaaaaa;}
</style>
<script type="text/javascript">
function allowDrop(ev)
{
	ev.preventDefault();
}

function drag(ev)
{
	ev.dataTransfer.setData("Text",ev.target.id);
}

function drop(ev)
{
	var data=ev.dataTransfer.getData("Text");
	ev.target.appendChild(document.getElementById(data));
	ev.preventDefault();
}
</script>
</head>
<body>

<div id="div1" ondrop="drop(event)" ondragover="allowDrop(event)"></div>
<br />
<p id="drag1" draggable="true" ondragstart="drag(event)">这是一段可移动的段落。请把该段落拖入上面的矩形。</p>
```

* dropzone

指定是否将数据复制，移动，或链接，或删除

```html
<!-- copy	拖动数据会导致被拖数据产生副本。
move	拖动数据会导致被拖数据移动到新位置。
link	拖动数据会生成指向原始数据的链接。 -->
<!-- 没有主流浏览器支持 dropzone 属性。 -->
<div dropzone="copy"></div>
```

* hidden

hidden 属性规定对元素进行隐藏。

```html
<p hidden>这是一段隐藏的段落。</p>
```

* lang

设置元素中内容的语言代码。

```html
<p lang="en">这是一个段落。</p>
```

* spellcheck

检测元素是否拼写错误

```html
<!-- true	规定应当对元素的文本进行拼写检查。
false	规定不应对元素的文本进行拼写检查。 -->
<p contenteditable="true" spellcheck="true">这是可编辑的段落。请试着编辑文本。</p>
```

* tabindex

设置元素的 Tab 键控制次序。

```html
<a href="//www.runoob.com//" tabindex="2"> runoob.com 菜鸟教程</a><br />
<a href="//www.google.com/" tabindex="1">Google</a><br />
<a href="//www.microsoft.com/" tabindex="3">Microsoft</a>
```

* translate

指定是否一个元素的值在页面载入时是否需要翻译

```html
<!-- 目前没有主流浏览器支持 translate 属性。 -->
<p translate="no">这个段落不能翻译。</p>
<p>这个段落可以被翻译</p>
```

## 新元素

### canvas

标签定义图形，比如图表和其他图像。该标签基于 JavaScript 的绘图 API

```html
<canvas id="myCanvas"></canvas>
<script type="text/javascript">
var canvas=document.getElementById('myCanvas');
var ctx=canvas.getContext('2d');
ctx.fillStyle='#FF0000';
ctx.fillRect(0,0,80,100);
</script>
```

### 新多媒体元素

* audio

定义音频内容

```html
<audio controls>
  <source src="horse.ogg" type="audio/ogg">
  <source src="horse.mp3" type="audio/mpeg">
  您的浏览器不支持 audio 元素。
</audio>
```

* video

定义视频（video 或者 movie）

```html
<video width="320" height="240" controls>
    <source src="movie.mp4" type="video/mp4">
    <source src="movie.ogg" type="video/ogg">
    您的浏览器不支持 video 标签。
</video>
```

* source

定义多媒体资源`<video>`和 `<audio>`

```html
<audio controls>
    <source src="horse.ogg" type="audio/ogg">
    <source src="horse.mp3" type="audio/mpeg">
    您的浏览器不支持 audio 元素。
</audio>
```

* embed

定义嵌入的内容，比如插件。

```html
<embed src="helloworld.swf">
```

* track

为诸如`<video>`和`<audio>`元素之类的媒介规定外部文本轨道。

```html
<!-- IE 10、Opera 和 Chrome 浏览器支持 <track> 标签。 -->
<video width="320" height="240" controls>
<source src="forrest_gump.mp4" type="video/mp4">
<source src="forrest_gump.ogg" type="video/ogg">
<track src="subtitles_en.vtt" kind="subtitles" srclang="en"
label="English">
<track src="subtitles_no.vtt" kind="subtitles" srclang="no"
label="Norwegian">
</video>
```

### 新表单元素

* datalist

定义选项列表。请与 input 元素配合使用该元素，来定义 input 可能的值。

```html
<input list="browsers">
<datalist id="browsers">
  <option value="Internet Explorer">
  <option value="Firefox">
  <option value="Chrome">
  <option value="Opera">
  <option value="Safari">
</datalist>
```

* output

定义不同类型的输出，比如脚本的输出。

```html
<form oninput="x.value=parseInt(a.value)+parseInt(b.value)">0
  <input type="range" id="a" value="50">100
  +<input type="number" id="b" value="50">
  =<output name="x" for="a b"></output>
</form>
```

### 新的语义和结构元素

标签 | 描述
--- | ---
`<article>` | 定义页面独立的内容区域。
`<aside>` | 定义页面的侧边栏内容。
`<bdi>` | 允许您设置一段文本，使其脱离其父元素的文本方向设置。
`<command>` | 定义命令按钮，比如单选按钮、复选框或按钮
`<details>` | 用于描述文档或文档某个部分的细节
`<dialog>` | 定义对话框，比如提示框
`<summary>` | 标签包含 details 元素的标题
`<figure>` | 规定独立的流内容（图像、图表、照片、代码等等）。
`<figcaption>` | 定义 `<figure>` | 元素的标题
`<footer>` | 定义 section 或 document 的页脚。
`<header>` | 定义了文档的头部区域
`<mark>` | 定义带有记号的文本。
`<meter>` | 定义度量衡。仅用于已知最大和最小值的度量。
`<nav>` | 定义导航链接的部分。
`<progress>` | 定义任何类型的任务的进度。
`<ruby>` | 定义 ruby 注释（中文注音或字符）。
`<rt>` | 定义字符（中文注音或字符）的解释或发音。
`<rp>` | 在 ruby 注释中使用，定义不支持 ruby 元素的浏览器所显示的内容。
`<section>` | 定义文档中的节（section、区段）。
`<time>` | 定义日期或时间。
`<wbr>` | 规定在文本中的何处适合添加换行符。

___
> 共同学习，共同进步