# SCSS

## sass基本语法

1. sass编译
	1. 一次编译
	`sass 需要编译的文件 编译后的文件`
	2. 单文件监听
	`sass --watch common.scss:xx.css`
	3. 文件夹监听
	`sass --watch 文件名名称（要监听的文件夹）：编译到哪儿（编译后的位置）`
	4. 自动搜索（windows cmd 命令大全）
		- dir 查看当前目录文件
		- cd 打开文件 cd a cd a.txt cd .. 上一层
		- cls 清除当前品目
		- ctrl + c 是否终止操作 y / n
		- 按上下箭头 使用你最近使用的几个命令
	5. 编译模式
		- 语法
	`sass --watch 文件夹 : 文件夹 --stye nested 默认 / expanded css纵向写法 / compact 横向 / compressed 压缩（所有代码压缩成一行代码）`

2. sass注释
	- // 注释不会被编译
	- /\* 属于css注释，会被编译出来\*/

3. 变量(可以存 css单位、颜色、文字)
	- 语法
	`$变量:参数`
	- 实例
```scss
	$width:300px;
	$color:yellowgreen pink;
	div {
		width: $width;
		height: $width;
		background-color: nth($color,1);
		// nth(那个变量，第几个) 1 2 ...（**不是从0开始**）
	}
```
	- 变量作用域 和js中的 作用域一样

4. 嵌套（标签可以怎么嵌套就能怎么嵌套）
	- 语法
```scss
	ul {
		$lh:30px;
		li {
			height:$lh;
		 	a {
				color: red;
				margin-top: ($lh - 12px) / 2; // 遵循css3规则 运算符 前后空格分开 
		 }
	}
}
```

	- ~~属性嵌套（要用 : 区分）~~
```scss
	.box {
    //复合样式
    font:{
      style:normal;
      weight: bold;
      size: 14px;
      family: $ms;
    }

    margin: {
      top:12px;
      right: 12px;
      bottom: 12px;
      left: 12px;
    }
	}

```

	- 跳出根
```scss
	.news {
		@at-root .news_title {
			width: 10px;
		}
		.news_content {
			width: 20px;
		}
	}

// 单个跳出

	.news{
  //@at-root .news_title{
  //    width: 10px;
  //  }
  //@at-root .news_content{
  //    width: 20px;
  //  }

  @at-root {
    .news_title{
      width: 10px;
    }
    .abc{
      width: 10px;
    }
  }
}

// 一组跳出

```
	- 带入上一层选择器（不带父级）
```scss
.box{
  width: 200px;
  &_cont{
    width: 400px;
    &_abc{
      width: 200px;
    }
  }
}

& === 上一层选择器 --> .box_cont .box_cont_abc
```

5. 混合
	- 基本语法
```scss
@mixin opa() {
	opacity: .5;
	filter: alpha(opacity=50);
}
// 不带参数

@mixin opa($opa) {
	opacity: $opa / 100;
	filter: alpha(opacity=$opa);
}
// 带参数，必须传参数

@mixin opa($opa:50) {
	opacity: $opa / 100;
	filter: alpha(opacity=$opa);
}
// 传参数就是传的数，不传就是默认值50 可以自己设定

.demo{
	@include opa();
}

/**
 * @mixin 声明
 *
 * @include 是调用 @mixin 所声明的东西
 */
```

	- 参数不确定
```scss
@mixin shadow($shadow...){
  box-shadow: $shadow;
}
/**
 * ... 代表参数不确定
 * 可任意传
 */
```

6. if else判断
	- 语法
```scss
@mixin sj($fx:top,$size:10px,$color:red){

  @if ($fx == top) {
    border-color: transparent transparent $color transparent;
    border-style: dashed dashed solid dashed;
  }
  @else if($fx == right){
    border-color: transparent transparent transparent $color;
    border-style: dashed dashed dashed solid;
  }
  @else if($fx == bottom){
    border-color: $color transparent transparent transparent ;
    border-style: solid dashed dashed dashed ;
  }
  @else if($fx == left){
    border-color: transparent $color transparent transparent ;
    border-style: dashed solid dashed dashed ;
  }

  width: 0;
  height: 0;
  overflow: hidden;
  border-width: $size;

}

.demo{
  @include sj($fx:bottom,$color:yellowgreen);
}
```

	- if条件 not 非 | or 或 | and 与 | == 等于 | != 不等于
	**写兼容很适用（css3）**

7. 继承

	- 语法
```scss
.fl{
  float: left;
}

.box{
  width: 300px;
  height: 300px;
  @extend .fl;
}
.box2{
  @extend .box;
}
```

	- % 占位选择器（在用到的时候 才会被编译出来）
```scss
%clearfix{
  *zoom:1;
  &:after,
  &:before{
    content: '';
    display: table;
  }
  &:after{
    clear: both;
  }
}

.abc{
  width: 300px;
  @extend %clearfix;
}
```

8. \# 字符串插值

	- 语法
```scss
$icon:'../images/icon/';
$img:'../images/';
$sina:'http://img2.sina.com.cn/2016-11-21/qiaobusi/images/icon/';

//  #{变量名}

.content{
  background: url(#{$sina}/a.jpg) left top no-repeat;
}
```

9. sass中的运算 运算符的前后 必须要有空格

	- 语法
```scss
.ys{
  color: #F00 + 255;
  width: $width / 2;

  $fs:12px;
  $lh:24px;

  font: #{$fs}/#{$lh} "Microsoft YaHei","微软雅黑";
}
```

10. for循环

	- 语法
```scss
$max:10;
$min:5;
//sass
//  <=
@for $i from $min through $max{
    .item_#{$i}{
      background-position: -($i - 1) * 20px 0;
    }
}

// <
@for $i from 1 to 10{
  .demo_#{$i}{
    background-position: -($i - 1) * 20px 0;
  }
}
```

11. while

	- 语法
```scss
$a:5;
@while($a >= 1){
  .aaa_#{$a}{
    width: 20px * $a;
  }
  $a:$a - 1;
}
```

12. each

	- 语法
```scss
$icon_name:user,pass,checked,select;
@each $i in $icon_name{
  .icon_#{$i}{
    width: 10px;
  }
}
```

13. 三目

	- 语法
```scss
if($condition, $if true, $if false)

if(true, 1px, 2px) --> 1px
if(false, 1px, 2px) -->2px
```

___
> 共同学习，共同进步