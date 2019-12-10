# 正则表达式

1. 什么是正则表达式
	+ 规则、模式
	+ 强大的字符串匹配工具
	+ 是一种正常人类很难读懂的文字

2. RegExp对象
	+ JS风格 —— new RegExp('a',i);
	+ perl风格 —— /a/i

```js
var str = 'abcdef';
//var re = new RegExp('a', 'i');
var re = /a/i;

console.log(re.test(str));
```

3. search
    + 字符串搜索
    + 忽略大小写: i -> ignore
    + 判断浏览器类型

```js
//alert(window.navigator.userAgent);
if(window.navigator.userAgent.search(/firefox/i)!=-1)
{
    alert('ff');
}
else if(window.navigator.userAgent.search(/chrome/i)!=-1)
{
    alert('chrome');
}
else if(window.navigator.userAgent.search(/msie 9/i)!=-1)
{
    alert('IE9');
}
```

4. match
	+ 获取匹配的项目
		- 量词：+
		- 量词变化：\d、\d\d和\d+
		- 全局匹配：g——global
		- 例子：找出所有数字

```js
var str = 'sdf e443 fedef 55 66gg 333226455 dff';
var re = /\d+/g;
console.log(str.match(re));
```

5. replace
	+ 替换所有匹配
		- 返回替换后的字符串
		- 例子：敏感词过滤
		- | 或则

```js
var str='abacdAef';
console.log(str.replace(/a/gi, 'T'));
var re = /(13)(\d)(\d{8})/;
var phone = '13170132937';
var arr = phone.match(re)
console.log(phone.replace(re, '$1$2********'));
console.log(arr)
/* [
  '13170132937',
  '13',
  '1',
  '70132937',
  index: 0,
  input: '13170132937',
  groups: undefined
] */
```

6. 任意字符
	+ [abc]
    + 范围
		- [a-z]、[0-9] 
	+ 排除
		- [^a] ^除了
	+ 组合
		- [a-z0-9A-Z]

```js
var str='1b2 abc 1c2 ee';

//或者

var re=/1[abc]2/g;
//var re=/1a2|1b2|1c2/;

console.log(str.match(re));
```

7. 转义字符
	+ .（点）——任意字符
	+ \d、\w、\s 数字 数字字母下划线[a-z0-9_A-Z] 空白
	+ \D、\W、\S 除了数字 除了数字字母下划线 除了空白字符

8. 常用量词
	+ {n,} 至少n次
	+ \* 任意次 {0,} 建议不用
	+ ？ 零次或一次 {0,1}
	+ \+ 一次或任意次{1,}
	+ {n} 正好n次

9. 头尾
	+ ^ 开头
	+ $ 结尾

10. 匹配中文：[\u4e00-\u9fa5]

11. 单词边界：\b

12. 分组
    + 捕获型　　　-　()
    + 非捕获型　　-　(?:)
    + 正向前瞻型　-　(?=)
    + 反向前瞻型　-　(?!)

* 分组
    + 正则表达式匹配kidkidkid: `/kidkidkid/`
    + 优雅写法：`/(kid){3}/`
> ()就是一个分组

* 候选

一个分组中，可以有多个候选表达式，用|分隔

```js
var reg = /I love (him|her|it)/;
reg.test('I love him')  // true
reg.test('I love her')  // true
reg.test('I love it')  // true
reg.test('I love them') // false
```

> 这里的|相当于“或”的意思。

* 捕获与引用

被正则表达式匹配（捕获）到的字符串会被暂存起来。其中，由分组捕获的串会从1开始编号，于是我们可以引用这些串：

```js
var reg = /(\d{4})-(\d{2})-(\d{2})/
var date = '2010-04-12'
reg.test(date)
RegExp.$1 // 2010
RegExp.$2 // 04
RegExp.$3 // 12
```

> $1引用了第一个被捕获的串，$2是第二个，依次类推。

* 与replace配合

```js
var reg = /(\d{2}).(\d{2})\/(\d{4})/
var date = '12.21/2012'

date = date.replace(reg, '$3-$1-$2') // date = 2012-12-21
```

将违禁词转换为等字数的星号是一个常见功能。比如文本是kid is a doubi，其中kid与doubi是违禁词，那么转换后应该为*** is a *****。我们可以这么写：

```js
var reg = /(kid|doubi)/g
var str = 'kid is a doubi'

str = str.replace(reg, function(word){
  return word.replace(/./g, '*')
})
```

* 嵌套分组的捕获

如果碰到类似/((kid) is (a (doubi)))/的嵌套分组，捕获的顺序是什么？

```js
var reg = /((kid) is (a (doubi)))/
var str = "kid is a doubi"

reg.test( str ) // true

RegExp.$1 // kid is a doubi
RegExp.$2 // kid
RegExp.$3 // a doubi
RegExp.$4 // doubi
```

* 反向引用

正则表达式里也能进行引用，这称为反向引用

```js
var reg = /(\w{3}) is \1/

reg.test('kid is kid') // true
reg.test('dik is dik') // true
reg.test('kid is dik') // false
reg.test('dik is kid') // false
```

> \1引用了第一个被分组所捕获的串，换言之，表达式是动态决定的

注意，如果编号越界了，则会被当成普通的表达式

```js
var reg = /(\w{3}) is \6/;

reg.test( 'kid is kid' ); // false
reg.test( 'kid is \6' );  // true
```

* 非捕获型分组

有时候，我们只是想分个组，而没有捕获的需求，则可以使用非捕获型分组，语法为左括号后紧跟?:

```js
var reg = /(?:\d{4})-(\d{2})-(\d{2})/
var date = '2012-12-21'
reg.test(date)

RegExp.$1 // 12
RegExp.$2 // 21
```

> 这个例子中，(?:\d{4})分组不会捕获任何串，所以$1为(\d{2})捕获的串

* 正向与反向前瞻型分组

就好像你站在原地，向前眺望：
正向前瞻型分组 - 你前方是什么东西吗？
负向前瞻型分组 - 你前方不是什么东西吗？

太拗口了，我喜欢称之为肯定表达式与否定表达式。先举个正向前瞻的例子

```js
var reg = /kid is a (?=doubi)/

reg.test('kid is a doubi') // true
reg.test('kid is a shabi') // false
```

而负向前瞻则刚好相反

```js
var reg = /kid is a (?!doubi)/

reg.test('kid is a doubi') // false
reg.test('kid is a shabi') // true
```

如果前瞻型分组也不会捕获值。那么它与非捕获型的区别是什么？

```js
var reg, str = "kid is a doubi"

reg = /(kid is a (?:doubi))/
reg.test(str)
RegExp.$1 // kid is a doubi

reg = /(kid is a (?=doubi))/
reg.test(str)
RegExp.$1 // kis is a
```

> 可见，非捕获型分组匹配到的串，仍会被外层的捕获型分组捕获到，但前瞻型却不会。当你需要参考后面的值，又不想连它一起捕获时，前瞻型分组就派上用场了。
> 最后，JS不支持后瞻型分组。
___
> 共同学习，共同进步