# 应用缓存

HTML5 引入了应用程序缓存，这意味着 web 应用可进行缓存，并可在没有因特网连接时进行访问。

* 实例

```html
<!DOCTYPE HTML>
<html manifest="demo.appcache">

<body>
文档内容......
</body>

</html>
```

* Manifest 文件
    + manifest 文件可分为三个部分：
        1. CACHE MANIFEST - 在此标题下列出的文件将在首次下载后进行缓存
        2. NETWORK - 在此标题下列出的文件需要与服务器的连接，且不会被缓存
        3. FALLBACK - 在此标题下列出的文件规定当页面无法访问时的回退页面（比如 404 页面）


* 实例 - 完整的 Manifest 文件

```appcache
CACHE MANIFEST
# 2012-02-21 v1.0.0
/theme.css
/logo.gif
/main.js

NETWORK:
login.php

FALLBACK:
/html/ /offline.html
```

>  "#" 开头的是注释行，但也可满足其他用途。应用的缓存会在其 manifest 文件更改时被更新。如果您编辑了一幅图片，或者修改了一个 JavaScript 函数，这些改变都不会被重新缓存。更新注释行中的日期和版本号是一种使浏览器重新缓存文件的办法。
> 浏览器对缓存数据的容量限制可能不太一样（某些浏览器设置的限制是每个站点 5MB）。


___
> 共同学习，共同进步