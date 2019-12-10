# ajax

* 创建XMLHttpRequest对象

```js
var xmlhttp;
if (window.XMLHttpRequest)
{
    //  IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
    xmlhttp=new XMLHttpRequest();
}
else
{
    // IE6, IE5 浏览器执行代码
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
}
```

* 向服务器发送请求

```js
xmlhttp.open("GET","ajax_info.txt",true);
xmlhttp.send();
```

方法 | 描述
--- | ---
open(method,url,async) | 规定请求的类型、URL 以及是否异步处理请求。method：请求的类型；GET 或 POST url：文件在服务器上的位置async：true（异步）或 false（同步）
send(string) | 将请求发送到服务器。string：仅用于 POST 请求

* GET 还是 POST？

与 POST 相比，GET 更简单也更快，并且在大部分情况下都能用。

+ 然而，在以下情况中，请使用 POST 请求：
    - 无法使用缓存文件（更新服务器上的文件或数据库）
    - 向服务器发送大量数据（POST 没有数据量限制）
    - 发送包含未知字符的用户输入时，POST 比 GET 更稳定也更可靠

* get

```js
xmlhttp.open("GET","/try/ajax/demo_get.php",true);
xmlhttp.send();
// 为了避免这种情况，请向 URL 添加一个唯一的 ID：
xmlhttp.open("GET","/try/ajax/demo_get.php?t=" + Math.random(),true);
xmlhttp.send();
// 如果您希望通过 GET 方法发送信息，请向 URL 添加信息：
xmlhttp.open("GET","/try/ajax/demo_get2.php?fname=Henry&lname=Ford",true);
xmlhttp.send();
```

* post

```js
xmlhttp.open("POST","/try/ajax/demo_post.php",true);
xmlhttp.send();
// 如果需要像 HTML 表单那样 POST 数据，请使用 setRequestHeader() 来添加 HTTP 头。然后在 send() 方法中规定您希望发送的数据：
xmlhttp.open("POST","/try/ajax/demo_post2.php",true);
xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
xmlhttp.send("fname=Henry&lname=Ford");
```

方法 | 描述
--- | ---
setRequestHeader(header,value) | 向请求添加 HTTP 头。header: 规定头的名称 value: 规定头的值

* 服务器响应

如需获得来自服务器的响应，请使用 XMLHttpRequest 对象的 responseText 或 responseXML 属性。

属性 | 描述
--- | ---
responseText | 获得字符串形式的响应数据。
responseXML | 获得 XML 形式的响应数据。

* responseText属性

```js
document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
```

* responseXML 属性

```js
xmlDoc=xmlhttp.responseXML;
txt="";
x=xmlDoc.getElementsByTagName("ARTIST");
for (i=0;i<x.length;i++)
{
    txt=txt + x[i].childNodes[0].nodeValue + "<br>";
}
document.getElementById("myDiv").innerHTML=txt;
```

* onreadystatechange 事件

当请求被发送到服务器时，我们需要执行一些基于响应的任务。
每当 readyState 改变时，就会触发 onreadystatechange 事件。
readyState 属性存有 XMLHttpRequest 的状态信息。
下面是 XMLHttpRequest 对象的三个重要的属性：

属性 | 描述
--- | ---
onreadystatechange | 存储函数（或函数名），每当 readyState 属性改变时，就会调用该函数。
readyState | 存有 XMLHttpRequest 的状态。从 0 到 4 发生变化。0: 请求未初始化1: 服务器连接已建立2: 请求已接收3: 请求处理中4: 请求已完成，且响应已就绪
status | 200: "OK" 404: 未找到页面

```js
xmlhttp.onreadystatechange=function()
{
    if (xmlhttp.readyState==4 && xmlhttp.status==200)
    {
        document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    }
}
```

___
> 共同学习，共同进步