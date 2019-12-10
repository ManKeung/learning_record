# html基本

## 基本文档

```html
<!DOCTYPE html>
<html>
<head>
<title>文档标题</title>
</head>
<body>
可见文本...
</body>
</html>
```

## meta

+ 页面关键词
	`<meta name="keywords" conten="you tags">`

+ 页面描述
	`<meta name="description" conten="150 words">`

+ 搜索引擎索引方式
	`<meta name="robots" conten="index,follow">`
	- all：文件将被检索，且页面上的链接可以被查询
	- none：文件将不被检索，且页面上的链接不可以被查询
	- index：文件将被检索
	- follow：页面上的链接可以被查询
	- noindex：文件将不被检索
	- nofollow：页面上的链接不可以被查询

+ 页面重定和刷新
	`<meta http-equiv="refresh" conten="0;url=">`

+ 其他
	`<meta name="author" content="author name" /> <!-- 定义网页作者 -->`
	`<meta name="google" content="index,follow" />`
	`<meta name="googlebot" content="index,follow" />`
	`<meta name="verify" content="index,follow" />`

+ 移动设备
	`<meta name="viewport" content="width=device-width, initial-scale=1.0,maximum-scale=1.0, user-scalable=no"/> <!-- 'width=device-width' 会导致 iPhone 5 添加到主屏后以 WebApp 全屏模式打开页面时出现黑边  -->`

+ WebApp全屏模式
	`<meta name="apple-mobile-web-app-capable" content="yes" /> <!-- 启用 WebApp 全屏模式 -->`

+ 隐藏状态栏/设置状态栏颜色
	`<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent" />`

+ 添加到主屏后的标题
	`<meta name="apple-mobile-web-app-title" content="标题">`

+ 忽略数字自动识别为电话号码
	`<meta content="telephone=no" name="format-detection" />`

+忽略识别邮箱
	`<meta content="email=no" name="format-detection" />`

+ 申明编码
	`<meta charset='utf-8' />`

+ 优先使用 IE 最新版本和 Chrome
	`<meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />`
	<!-- 关于X-UA-Compatible -->
	`<meta http-equiv="X-UA-Compatible" content="IE=6" ><!-- 使用IE6 -->`
	`<meta http-equiv="X-UA-Compatible" content="IE=7" ><!-- 使用IE7 -->`
	`<meta http-equiv="X-UA-Compatible" content="IE=8" ><!-- 使用IE8 -->`

+ 禁止浏览器从本地计算机的缓存中访问页面内容
	`<meta http-equiv="Pragma" content="no-cache">`

+ 浏览器不会自动调整文件的大小,也就是说是固定大小,不会随着浏览器拉伸缩放。
	`<meta name="MobileOptimized" content="240"/>`

## 基本标签

```html
<h1>最大的标题</h1>
<h2> . . . </h2>
<h3> . . . </h3>
<h4> . . . </h4>
<h5> . . . </h5>
<h6>最小的标题</h6>
<p>这是一个段落。</p>
<br> （换行）
<hr> （水平线）
<!-- 这是注释 -->
```

## 文本格式化

```html
<b>粗体文本</b>
<code>计算机代码</code>
<em>强调文本</em>
<i>斜体文本</i>
<kbd>键盘输入</kbd> 
<pre>预格式化文本</pre>
<small>更小的文本</small>
<strong>重要的文本</strong>
<abbr> （缩写）
<address> （联系信息）
<bdo> （文字方向）
<blockquote> （从另一个源引用的部分）
<cite> （工作的名称）
<del> （删除的文本）
<ins> （插入的文本）
<sub> （下标文本）
<sup> （上标文本）
```

## 链接

```html
普通的链接：<a href="http://www.example.com/">链接文本</a>
图像链接： <a href="http://www.example.com/"><img src="URL" alt="替换文本"></a>
邮件链接： <a href="mailto:webmaster@example.com">发送e-mail</a>
书签：
<a id="tips">提示部分</a>
<a href="#tips">跳到提示部分</a>
```

## 图片

```html
<img src="URL" alt="替换文本" height="42" width="42">
```

## 样式/区块

```html
<style type="text/css">
h1 {color:red;}
p {color:blue;}
</style>
<div>文档中的块级元素</div>
<span>文档中的内联元素</span>
```

## 无序列表

```html
<ul>
    <li>项目</li>
    <li>项目</li>
</ul>
```

## 有序列表

```html
<ol>
    <li>第一项</li>
    <li>第二项</li>
</ol>
```

## 定义列表

```html
<dl>
  <dt>项目 1</dt>
    <dd>描述项目 1</dd>
  <dt>项目 2</dt>
    <dd>描述项目 2</dd>
</dl>
```

## 表格

```html
<table border="1">
  <tr>
    <th>表格标题</th>
    <th>表格标题</th>
  </tr>
  <tr>
    <td>表格数据</td>
    <td>表格数据</td>
  </tr>
</table>
```

## 框架

```html
<iframe src="demo_iframe.htm"></iframe>
```

## 表单

```html
<form action="demo_form.php" method="post/get">
<input type="text" name="email" size="40" maxlength="50">
<input type="password">
<input type="checkbox" checked="checked">
<input type="radio" checked="checked">
<input type="submit" value="Send">
<input type="reset">
<input type="hidden">
<select>
<option>苹果</option>
<option selected="selected">香蕉</option>
<option>樱桃</option>
</select>
<textarea name="comment" rows="60" cols="20"></textarea>
</form>
```

## 脚本

```html
<script>
document.write("Hello World!")
</script>
<noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>
```

## 字符实体

* 结合音标符

音标符 | 字符 | Construct | 输出结果
--- | --- | --- | ---
  ̀	 | a | a&#768; | à
  ́	 | a | a&#769; | á
̂	| a | a&#770; | â
  ̃	 | a | a&#771; | ã
  ̀	 | O | O&#768; | Ò
  ́	 | O | O&#769; | Ó
̂	| O | O&#770; | Ô
  ̃	 | O | O&#771; | Õ

## 字符实体

显示结果 | 描述 | 实体名称 | 实体编号
--- | --- | --- | ---
 | 空格 | &nbsp; | &#160;
< | 小于号 | &lt; | &#60;
\> | 大于号 | &gt; | &#62;
& | 和号 | &amp; | &#38;
" | 引号 | &quot; | &#34;
' | 撇号 | &apos; (IE不支持) | &#39;
￠ | 分 | &cent; | &#162;
£ | 镑 | &pound; | &#163;
¥ | 人民币/日元 | &yen; | &#165;
€ | 欧元 | &euro; | &#8364;
§ | 小节 | &sect; | &#167;
© | 版权 | &copy; | &#169;
® | 注册商标 | &reg; | &#174;
™ | 商标 | &trade; | &#8482;
× | 乘号 | &times; | &#215;
÷ | 除号 | &divide; | &#247;

___
> 共同学习，共同进步