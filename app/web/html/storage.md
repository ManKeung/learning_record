# web存储

## localStorage 和 sessionStorage

localStorage - 用于长久保存整个网站的数据，保存的数据没有过期时间，直到手动去除。
sessionStorage - 用于临时保存同一窗口(或标签页)的数据，在关闭窗口或标签页之后将会删除这些数据。

```js
if(typeof(Storage)!=="undefined")
{
    // 是的! 支持 localStorage  sessionStorage 对象!
    // 一些代码.....
} else {
    // 抱歉! 不支持 web 存储。
}
```

* 不管是 localStorage，还是 sessionStorage，可使用的API都相同，常用的有如下几个（以localStorage为例）：
     - 保存数据：localStorage.setItem(key,value);
     - 读取数据：localStorage.getItem(key);
     - 删除单个数据：localStorage.removeItem(key);
     - 删除所有数据：localStorage.clear();
     - 得到某个索引的key：localStorage.key(index);


___
> 共同学习，共同进步