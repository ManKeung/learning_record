# bom

## window

所有浏览器都支持 window 对象。它表示浏览器窗口。
所有 JavaScript 全局对象、函数以及变量均自动成为 window 对象的成员。
全局变量是 window 对象的属性。
全局函数是 window 对象的方法。

* window尺寸
    + 对于Internet Explorer、Chrome、Firefox、Opera 以及 Safari：`window.innerHeight - 浏览器窗口的内部高度(包括滚动条);window.innerWidth - 浏览器窗口的内部宽度(包括滚动条)`
    + 对于 Internet Explorer 8、7、6、5:
    `document.documentElement.clientHeight;document.documentElement.clientWidth`
    + 或者
    `document.body.clientHeight;document.body.clientWidth`

```js
var w=window.innerWidth
|| document.documentElement.clientWidth
|| document.body.clientWidth;

var h=window.innerHeight
|| document.documentElement.clientHeight
|| document.body.clientHeight;
```

* 其他window方法
    - window.open() - 打开新窗口
    - window.close() - 关闭当前窗口
    - window.moveTo() - 移动当前窗口
    - window.resizeTo() - 调整当前窗口的尺寸

* 定义全局变量与在 window 对象上直接定义属性差别
    + 全局变量不能通过 delete 操作符删除；而 window 属性上定义的变量可以通过 delete 删除
    + 访问未声明的变量会抛出错误，但是通过查询 window 对象，可以知道某个可能未声明的变量是否存在。
    + 有些自执行函数里面的变量，想要外部也访问到的话，在 window 对象上直接定义属性。

## window screen

window.screen对象在编写时可以不使用 window 这个前缀。

* screen.availWidth - 可用的屏幕宽度
* screen.width - 屏幕宽度
* screen.availHeight - 可用的屏幕高度
* screen.height - 屏幕高度
* screen.colorDepth - 色彩深度
* screen.pixelDepth - 色彩分辨率: 24

> 可用宽高以像素计，减去界面特性，比如窗口任务栏。

## window location

* location.hostname 返回 web 主机的域名
* location.pathname 返回当前页面的路径和文件名
* location.port 返回 web 主机的端口 （80 或 443）
* location.protocol 返回所使用的 web 协议（http: 或 https:）
* location.href 属性返回当前页面的 URL。
* location.assign() 方法加载新的文档。


> window.location.assign(url) ： 加载 URL 指定的新的 HTML 文档。 就相当于一个链接，跳转到指定的url，当前页面会转为新页面内容，可以点击后退返回上一个页面。
> window.location.replace(url) ： 通过加载 URL 指定的文档来替换当前文档 ，这个方法是替换当前窗口页面，前后两个页面共用一个窗口，所以是没有后退返回上一页的


## window history

* history.back() - 与在浏览器点击后退按钮相同
* history.forward() - 与在浏览器中点击向前按钮相同
* history.go() 这个方法来实现向前，后退的功能。

## window navigator

```html
<div id="example"></div>
<script>
txt = "<p>浏览器代号: " + navigator.appCodeName + "</p>";
txt+= "<p>浏览器名称: " + navigator.appName + "</p>";
txt+= "<p>浏览器版本: " + navigator.appVersion + "</p>";
txt+= "<p>启用Cookies: " + navigator.cookieEnabled + "</p>";
txt+= "<p>硬件平台: " + navigator.platform + "</p>";
txt+= "<p>用户代理: " + navigator.userAgent + "</p>";
txt+= "<p>用户代理语言: " + navigator.systemLanguage + "</p>";
document.getElementById("example").innerHTML=txt;
</script>
```

* 来自 navigator 对象的信息具有误导性，不应该被用于检测浏览器版本，这是因为
    - navigator 数据可被浏览器使用者更改
    - 一些浏览器对测试站点会识别错误
    - 浏览器无法报告晚于浏览器发布的新操作系统

* 浏览器检测

由于 navigator 可误导浏览器检测，使用对象检测可用来嗅探不同的浏览器。

由于不同的浏览器支持不同的对象，您可以使用对象来检测浏览器。例如，由于只有 Opera 支持属性 "window.opera"，您可以据此识别出 Opera。

## 弹窗

可以在 JavaScript 中创建三种消息框：警告框、确认框、提示框。

* 警告框

```js
// window.alert('alert msg');
alert('alert msg');
```

* 确认框

```js
var r=confirm("按下按钮");
if (r==true)
{
    x="你按下了\"确定\"按钮!";
}
else
{
    x="你按下了\"取消\"按钮!";
}
```

* 提示框

```js
var person=prompt("请输入你的名字","Harry Potter");
if (person!=null && person!="")
{
    x="你好 " + person + "! 今天感觉如何?";
    document.getElementById("demo").innerHTML=x;
}
```

* 换行

```js
alert('hello\nhow are you?');
```

## 记时事件

* setInterval() 方法

```js
setInterval("javascript function", milliseconds);
```

* clearInterval() 方法

```html
<p id="demo"></p>
<button onclick="myStopFunction()">停止</button>
<script>
var myVar=setInterval(function(){myTimer()},1000);
function myTimer(){
    var d=new Date();
    var t=d.toLocaleTimeString();
    document.getElementById("demo").innerHTML=t;
}
function myStopFunction(){
    clearInterval(myVar);
}
</script>
```

* setTimeout() 方法

```js
myVar= window.setTimeout("javascript function", milliseconds);
```

* clearTimeout() 方法

```js
var myVar;

function myFunction()
{
    myVar=setTimeout(function(){alert("Hello")},3000);
}

function myStopFunction()
{
    clearTimeout(myVar);
}
```

## cookie

* 创建cookie

```js
document.cookie="username=John Doe";
// 您还可以为 cookie 添加一个过期时间（以 UTC 或 GMT 时间）。默认情况下，cookie 在浏览器关闭时删除：
document.cookie="username=John Doe; expires=Thu, 18 Dec 2043 12:00:00 GMT";
// 您可以使用 path 参数告诉浏览器 cookie 的路径。默认情况下，cookie 属于当前页面。
document.cookie="username=John Doe; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/";
```

* 读取cookie

```js
var x = document.cookie;
```

* 修改cookie

```js
// 修改 cookie 类似于创建 cookie
document.cookie="username=John Smith; expires=Thu, 18 Dec 2043 12:00:00 GMT; path=/";
```

* 删除cookie

```js
// 只需要设置 expires 参数为以前的时间即可
document.cookie = "username=; expires=Thu, 01 Jan 1970 00:00:00 GMT";
```

```js
function setCookie(cname,cvalue,exdays){
    var d = new Date();
    d.setTime(d.getTime()+(exdays*24*60*60*1000));
    var expires = "expires="+d.toGMTString();
    document.cookie = cname+"="+cvalue+"; "+expires;
}
function getCookie(cname){
    var name = cname + "=";
    var ca = document.cookie.split(';');
    for(var i=0; i<ca.length; i++) {
        var c = ca[i].trim();
        if (c.indexOf(name)==0) { return c.substring(name.length,c.length); }
    }
    return "";
}
function checkCookie(){
    var user=getCookie("username");
    if (user!=""){
        alert("欢迎 " + user + " 再次访问");
    }
    else {
        user = prompt("请输入你的名字:","");
          if (user!="" && user!=null){
            setCookie("username",user,30);
        }
    }
}
```

___
> 共同学习，共同进步