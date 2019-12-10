# CSS

CSS 用于控制网页的样式和布局。
CSS3 是最新的 CSS 标准。
[兼容查询](https://www.caniuse.com "兼容查询")

## 选择器

* [元素选择符](http://css.doyoe.com/)

选择符 | 名称 | 版本 | 描述
---- | ---- | ---- | ----
* | 通配选择符 | CSS2 | 所有元素
E | 类型选择符 | CSS1 | 以文档语言类型作为选择符
E#myid | id选择符 | CSS1 | 以唯一标识符id属性等于myid的E对象作为选择符
E.myclass | class选择符 | CSS1 | 以class属性包含myclass的E对象作为选择符

* [关系选择符](http://css.doyoe.com/)

选择符 | 名称 | 版本 | 描述
---- | ---- | ---- | ----
E F | 包含选择符 | CSS1 | 选择所有被E元素包含的F元素
E>F | 子选择符 | CSS2 | 选择所有作为E元素的子元素F
E+F	| 相邻选择符 | CSS2 |	选择紧贴在E元素之后F元素
E~F	| 兄弟选择符 | CSS3 |	选择E元素所有兄弟元素F

* [属性选择符](http://css.doyoe.com/)

选择符 | 版本 | 描述
---- | ---- | ----
E[att] | CSS2	| 选择具有att属性的E元素
E[att="val"] | CSS2 |	选择具有att属性且属性值等于val的E元素
E[att~="val"]	| CSS2 | 选择具有att属性且属性值为一用空格分隔的字词列表，其中一个等于val的E元素
E[att^="val"]	| CSS3 | 选择具有att属性且属性值为以val开头的字符串的E元素
E[att$="val"]	| CSS3 | 选择具有att属性且属性值为以val结尾的字符串的E元素
E[att*="val"]	| CSS3 | 选择具有att属性且属性值为包含val的字符串的E元素
E[att&#124;="val"]	| CSS2 | 选择具有att属性且属性值为以val开头并用连接符"-"分隔的字符串的E元素，如果属性值仅为val，也将被选择 | (&#124; == |)

* [伪类选择符](http://css.doyoe.com/)

选择符 | 版本 | 描述
---- | ---- | ----
E:link | CSS1 | 设置超链接a在未被访问前的样式
E:visited | CSS1 | 设置超链接a在其链接地址已被访问过时的样式
E:hover	| CSS1/2 | 设置元素在其鼠标悬停时的样式
E:active | CSS1/2 | 设置元素在被用户激活（在鼠标点击与释放之间发生的事件）时的样式
E:focus | CSS1/2 | 设置元素在成为输入焦点（该元素的onfocus事件发生）时的样式
E:lang(fr) | CSS2 | 匹配使用特殊语言的E元素
E:not(s) | CSS3 | 匹配不含有s选择符的元素E
E:root | CSS3 | 匹配E元素在文档的根元素
E:first-child | CSS2 | 匹配父元素的第一个子元素E
E:last-child | CSS3	| 匹配父元素的最后一个子元素E
E:only-child | CSS3	| 匹配父元素仅有的一个子元素E
E:nth-child(n) | CSS3 | 匹配父元素的第n个子元素E （odd 奇数 even 偶数）
E:nth-last-child(n) | CSS3 | 匹配父元素的倒数第n个子元素E
E:first-of-type | CSS3 | 匹配同类型中的第一个同级兄弟元素E
E:last-of-type | CSS3 | 匹配同类型中的最后一个同级兄弟元素E
E:only-of-type | CSS3 | 匹配同类型中的唯一的一个同级兄弟元素E
E:nth-of-type(n) | CSS3 | 匹配同类型中的第n个同级兄弟元素E
E:nth-last-of-type(n) | CSS3 | 匹配同类型中的倒数第n个同级兄弟元素E
E:empty | CSS3 | 匹配没有任何子元素（包括text节点）的元素E
E:checked | CSS3 | 匹配用户界面上处于选中状态的元素E(用于input type为radio与checkbox时)
E:enabled | CSS3 | 匹配用户界面上处于可用状态的元素E
E:disabled | CSS3 | 匹配用户界面上处于禁用状态的元素E
E:target | CSS3 | 匹配相关URL指向的E元素
@page:first | CSS2 | 设置页面容器第一页使用的样式。仅用于@page规则
@page:left | CSS2 | 设置页面容器位于装订线左边的所有页面使用的样式。仅用于@page规则
@page:right	| CSS2 | 设置页面容器位于装订线右边的所有页面使用的样式。仅用于@page规则

* [伪对象选择符](http://css.doyoe.com/)

选择符 | 版本 | 描述
---- | ---- | ----
~~E:first-letter~~/E::first-letter | CSS1/3 | 设置对象内的第一个字符的样式
~~E:first-line~~/E::first-line | CSS1/3 | 设置对象内的第一行的样式
~~E:before~~/E::before | CSS2/3	| 设置在对象前（依据对象树的逻辑结构）发生的内容。用来和content属性一起使用
~~E:after~~/E::after | CSS2/3 | 设置在对象后（依据对象树的逻辑结构）发生的内容。用来和content属性一起使用
E::placeholder | CSS3 | 设置对象文字占位符的样式
E::selection | CSS3 | 设置对象被选择时的颜色

* 伪类伪元素

+ **伪类：hover focus 不会产生东西，只会执行一个样式而已**
+ **伪元素：在你的结构中添加一个元元素出来(::after ::before)，可以给他加任何的样式。（需要添加content才能看到，没有加content就等于没有加伪元素一样）**

+ 伪元素content

值 | 描述
---- | ----
string | 定义文本内容
~~url~~ | 定义url
**attr(x)** | 定义显示在该选择器之前或之后的选择器的属性

+ 示例
	1. `div::after {content: '';}`
	2. `div::after {content: url('./image.png');}`
	3. `div::after {content: attr(title);}`

___
> 共同学习，共同进步