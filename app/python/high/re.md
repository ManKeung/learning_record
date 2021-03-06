# 正则表达式

## re模块操作

* 模块使用过程

```python
# 导入模块
import re

# 使用match方法匹配操作
result = re.match(正则表达式,要匹配的字符串)

# 如果上一步匹配到数据的话，可以使用group方法来提取数据
result.group()
```

* 匹配单个字符

字符 | 功能
--- | ---
. | 匹配任意1个字符（除了\n）
[ ] | 匹配[ ]中列举的字符
\d | 匹配数字，即0-9
\D | 匹配非数字，即不是数字
\s | 匹配空白，即 空格，tab键
\S | 匹配非空白
\w | 匹配单词字符，即a-z、A-Z、0-9、_
\W | 匹配非单词字符

* 匹配多个字符

字符 | 功能
--- | ---
* | 匹配前一个字符出现0次或者无限次，即可有可无
+ | 匹配前一个字符出现1次或者无限次，即至少有1次
? | 匹配前一个字符出现1次或者0次，即要么有1次，要么没有
{m} | 匹配前一个字符出现m次
{m,n} | 匹配前一个字符出现从m到n次

* 匹配开头结尾

字符 | 功能
--- | ---
^ | 匹配字符串开头
$ | 匹配字符串结尾

* 匹配分组

字符 | 功能
--- | ---
\| | 匹配左右任意一个表达式
(ab) | 将括号中字符作为一个分组
\num | 引用分组num匹配到的字符串
(?P<name>) | 分组起别名
(?P=name) | 引用别名为name分组匹配到的字符串

## 高级用法

* search

```python
import re

ret = re.search(r'\d+', '阅读次数为 9999')
print(ret.group())
# '9999'
```

* findall

```python
import re

ret = re.findall(r'\d+', 'python = 9999, c = 7890, c++ = 12345')
print(ret.group())
# ['9999', '7890', '12345']
```

* sub 将匹配到的数据进行替换

```python
import re

ret = re.sub(r'\d+', '998', 'python = 997')
print(ret)
# python = 998
```

* split 根据匹配进行切割字符串，并返回一个列表

```python
import re

ret = re.split(r':| ','info:xiaoZhang 33 shandong')
print(ret)
# ['info', 'xiaoZhang', '33', 'shandong']
```

* 例子

```python
import re
# re.match(正则表达式, 需要处理的字符串)
re.match(r"hello", "hello world")
re.match(r"hello", "Hello world")
re.match(r"[hH]ello", "Hello world")
re.match(r"[hH]ello", "hello world")
re.match(r"速度与激情1", "速度与激情1")
re.match(r"速度与激情1", "速度与激情2")
re.match(r"速度与激情\d", "速度与激情2")
re.match(r"速度与激情\d", "速度与激情3")
re.match(r"速度与激情\d", "速度与激情5")
ret = re.match(r"速度与激情\d", "速度与激情5")
ret.group()
ret = re.match(r"速度与激情\d", "速度与激情8")
ret.group()
ret = re.match(r"速度与激情\d", "速度与激情88")
ret.group()
ret = re.match(r"速度与激情\d", "速度与激情8")
ret.group()
ret = re.match(r"速度与激情\d", "速度与激情9")
ret.group()
ret = re.match(r"速度与激情[12345678]", "速度与激情1")
ret.group()
re.match(r"速度与激情[12345678]", "速度与激情1").group()
re.match(r"速度与激情[12345678]", "速度与激情2").group()
re.match(r"速度与激情[12345678]", "速度与激情3").group()
re.match(r"速度与激情[12345678]", "速度与激情8").group()
re.match(r"速度与激情[12345678]", "速度与激情9").group()
re.match(r"速度与激情[12345678]", "速度与激情9")
re.match(r"速度与激情[1-8]", "速度与激情3")
re.match(r"速度与激情[1-8]", "速度与激情5")
re.match(r"速度与激情[1-8]", "速度与激情1")
re.match(r"速度与激情[1-8]", "速度与激情8")
re.match(r"速度与激情[1-8]", "速度与激情0")
re.match(r"速度与激情[1-8]", "速度与激情9")
re.match(r"速度与激情[123678]", "速度与激情1")
re.match(r"速度与激情[123678]", "速度与激情2")
re.match(r"速度与激情[123678]", "速度与激情3")
re.match(r"速度与激情[123678]", "速度与激情6")
re.match(r"速度与激情[123678]", "速度与激情8")
re.match(r"速度与激情[123678]", "速度与激情4")
re.match(r"速度与激情[1-36-8]", "速度与激情1")
re.match(r"速度与激情[1-36-8]", "速度与激情2")
re.match(r"速度与激情[1-36-8]", "速度与激情3")
re.match(r"速度与激情[1-36-8]", "速度与激情4")
re.match(r"速度与激情[1-36-8]", "速度与激情5")
re.match(r"速度与激情[1-36-8]", "速度与激情6")
re.match(r"速度与激情[1-36-8]", "速度与激情7")
re.match(r"速度与激情[1-36-8]", "速度与激情8")
re.match(r"速度与激情[1-8abcd]", "速度与激情8")
re.match(r"速度与激情[1-8abcd]", "速度与激情8").group()
re.match(r"速度与激情[1-8abcd]", "速度与激情a").group()
re.match(r"速度与激情[1-8abcd]", "速度与激情b").group()
re.match(r"速度与激情[1-8abcd]", "速度与激情d").group()
re.match(r"速度与激情[1-8abcd]", "速度与激情e").group()
re.match(r"速度与激情[1-8a-d]", "速度与激情e").group()
re.match(r"速度与激情[1-8a-z]", "速度与激情e").group()
re.match(r"速度与激情[1-8a-zA-Z]", "速度与激情E").group()
re.match(r"速度与激情\w", "速度与激情E").group()
re.match(r"速度与激情\w", "速度与激情e").group()
re.match(r"速度与激情\w", "速度与激情4").group()
re.match(r"速度与激情\w", "速度与激情_").group()
re.match(r"速度与激情\w", "速度与激情=").group()
re.match(r"速度与激情\w", "速度与激情！").group()
re.match(r"速度与激情\w", "速度与激情哈").group()
re.match(r"速度与激情 \d", "速度与激情 1").group()
re.match(r"速度与激情\s\d", "速度与激情 1").group()
re.match(r"速度与激情\s\d", "速度与激情\t1").group()
re.match(r"速度与激情.", "速度与激情1").group()
re.match(r"速度与激情.", "速度与激情a").group()
re.match(r"速度与激情.", "速度与激情A").group()
re.match(r"速度与激情.", "速度与激情_").group()
re.match(r"速度与激情.", "速度与激情哈").group()
re.match(r"速度与激情.", "速度与激情！").group()
re.match(r"速度与激情.", "速度与激情#").group()
re.match(r"速度与激情\d\d", "速度与激情12").group()
re.match(r"速度与激情\d\d", "速度与激情1").group()
re.match(r"速度与激情\d{1,2}", "速度与激情1").group()
re.match(r"速度与激情\d{1,2}", "速度与激情2").group()
re.match(r"速度与激情\d{1,2}", "速度与激情12").group()
re.match(r"速度与激情\d{1,3}", "速度与激情12").group()
re.match(r"速度与激情\d{1,3}", "速度与激情123").group()
re.match(r"速度与激情\d{1,3}", "速度与激情1").group()
re.match(r"速度与激情\d{1,3}", "速度与激情12").group()
re.match(r"\d{11}", "12345678901").group()
re.match(r"\d{11}", "1234567890").group()
re.match(r"\d{11}", "123456780").group()
re.match(r"\d{11}", "123456A78901").group()
re.match(r"021-\d{8}", "021-12345678").group()
re.match(r"021-?\d{8}", "02112345678").group()
re.match(r"021-?\d{8}", "021-12345678").group()
re.match(r"\d{3}-?\d{8}", "021-12345678").group()
re.match(r"\d{3,4}-?\d{8}", "021-12345678").group()
re.match(r"\d{3,4}-?\d{8}", "0531-12345678").group()
re.match(r"\d{3,4}-?\d{8}", "0532-12345678").group()
re.match(r"\d{3,4}-?\d{7,8}", "0532-12345678").group()
re.match(r"\d{3,4}-?\d{7,8}", "0532-1234567").group()
html_content = """fdsf
kasdjfkjasdkfjkasdjfjahsdufhawufhausdhfuahsdf
asdjfhjjasdhf
asdfasd'fas
df
asd
fas
df
asd
fa
sdf
asdf"""
print(html_content)
re.match(r".*", html_content).group()
re.match(r".*", html_content, re.S).group()
re.match(r".*", "a").group()
re.match(r".*", "a1").group()
re.match(r".*", "").group()
re.match(r".+", "a").group()
re.match(r".+", "ab").group()
re.match(r".+", "abaksdjfkjasdkfjaksdjfkajsdfkjs").group()
re.match(r".+", "").group()
re.match(r"\d{3}", "123").group()
re.match(r"\d{3}", "12").group()
re.match(r"\d{3}", "123456789").group()
re.match(r"[a-zA-Z0-9_]{4,20}@163\.com$", "laowang@163.com")
re.match(r"[a-zA-Z0-9_]{4,20}@163\.com$", "laowang@163.com").group()
re.match(r"[a-zA-Z0-9_]{4,20}@163|126\.com$", "laowang@163.com").group()
re.match(r"[a-zA-Z0-9_]{4,20}@163|126\.com$", "126.com").group()
re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "126.com").group()
re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "laowang@126.com").group()
re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "laowang@163.com").group()
re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "laowang@163.com").group()
re.match(r"[a-zA-Z0-9_]{4,20}@(163|126)\.com$", "laowang@163.com").group(1)
re.match(r"([a-zA-Z0-9_]{4,20})@(163|126)\.com$", "laowang@163.com").group(1)
re.match(r"([a-zA-Z0-9_]{4,20})@(163|126)\.com$", "laowang@163.com").group(2)
re.match(r"([a-zA-Z0-9_]{4,20})@(163|126)\.com$", "laowang@163.com").group(3)
html_str = "<h1>hahahah</h1>"
re.match(r"<\w*>.*</\w*>", html_str)
re.match(r"<\w*>.*</\w*>", html_str).group()
html_str = "<h1>hahahah</h2>"
re.match(r"<\w*>.*</\w*>", html_str).group()
re.match(r"<(\w*)>.*</\1>", html_str).group()
html_str = "<h1>hahahah</h1>"
re.match(r"<(\w*)>.*</\1>", html_str).group()
html_str = "<body><h1>hahahah</h1></body>"
re.match(r"<(\w*)><(\w*)>.*</\1></\2>", html_str).group()
re.match(r"<(\w*)><(\w*)>.*</\2></\1>", html_str).group()
re.match(r"<(?P<p1>\w*)><(?P<p2>\w*)>.*</(?P=p2)></(?P=p1)>", html_str).group()
re.search(r"\d+", "阅读次数为 9999").group()
re.search(r"\d+", "阅读次数为 9999, 点赞数为:100").group()
re.search(r"\d+", "阅读次数为 9999, 点赞数为:100").group(1)
re.search(r"\d+", "阅读次数为 9999, 点赞数为:100").group(2)
re.search(r"^\d+", "阅读次数为 9999, 点赞数为:100").group(2)
re.findall(r"\d+", "python = 9999, c = 7890, c++ = 12345")
re.sub(r"\d+", '998', "python = 997")
re.sub(r"\d+", '998', "python = 997, c++ = 1024")
html_str = """
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>职位诱惑：<br>机器学习相关项目，完全新技术驱动，互联网公司，工作氛围好，扁平管理，有技术大牛带<br><br>职位描述：<br>配合架构师和机器学习专家，完成项目的编码、测试和上线。<br><br>我们期望：<br>1.&nbsp;211院校计算机相关专业本科以上学历；<br>2.&nbsp;有扎实的编程和计算机基础，熟悉常用算法和数据结构。<br>3.&nbsp;具有很强的问题解决能力，综合知识（或者通过搜索能快速掌握知识）强，了解前端、网络、多线程、数据库、Web开发等知识。<br>4.&nbsp;2年以上工作经验（Python或者JAVA方向，如果编程能力特别过硬可以放开语言要求）；<br><br>工作内容：<br>1.&nbsp;根据业务需求进行需求分析和代码编写；<br>2.&nbsp;结合系统实现对代码进行充分的自测，以及配合测试工程师联合进行测试；<br>3.&nbsp;配合机器学习算法专家进行代码编写</p>
        </div>
    </dd>
"""
re.sub(r"<.*>", "", html_str)
re.sub(r"<\w*>", "", html_str)
re.match(r"\w", " ")
re.match(r"\w", "a")
re.match(r"\w", "_")
re.sub(r"<[^>]*>", "", html_str)
html_str = """
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>职位诱惑：<br>机器学习相关项目，完全新技术驱动，互联网公司，工作氛围好，扁平管理，有技术大牛带<br><br>职位描述：<br>配合架构师和机器学习专家，完成项目的编码、测试和上线。<br><br>我们期望：<br>1.&nbsp;211院校计算机相关专业本科以上学历；<br>2.&nbsp;有扎实的编程和计算机基础，熟悉常用算法和数据结构。<br>3.&nbsp;具有很强的问题解决能力，综合知识（或者通过搜索能快速掌握知识）强，了解前端、网络、多线程、数据库、Web开发等知识。<br>4.&nbsp;2年以上工作经验（Python或者JAVA方向，如果编程能力特别过硬可以放开语言要求）；<br><br>工作内容：<br>1.&nbsp;根据业务需求进行需求分析和代码编写；<br>2.&nbsp;结合系统实现对代码进行充分的自测，以及配合测试工程师联合进行测试；<br>3.&nbsp;配合机器学习算法专家进行代码编写</p>
        </div>
    </dd>
"""
re.sub(r"<[^>]*>|\s", "", html_str)
re.sub(r"<[^>]*>|\s|&nbsp;", "", html_str)
re.sub(r"<.*>", "", html_str)
re.sub(r"<\w*>", "", html_str)
re.sub(r"<.*?>", "", html_str)
s = "This is a number 234-235-22-423"
re.match(r".*\d{3}-\d{3}-\d{2}-\d{3}", s).group()
re.match(r".*(\d{3}-\d{3}-\d{2}-\d{3})", s).group()
re.match(r".*(\d{3}-\d{3}-\d{2}-\d{3})", s).group(1)
re.match(r".*(\d+-\d+-\d+-\d+)", s).group()
re.match(r".*(\d+-\d+-\d+-\d+)", s).group(1)
re.match(r".*?(\d+-\d+-\d+-\d+)", s).group(1)
meizi_image = """<img data-original="https://rpic.douyucdn.cn/appCovers/2017/05/19/1740975_20170519162941_big.jpg" src="https://rpic.douyucdn.cn/appCovers/2017/05/19/1740975_20170519162941_big.jpg" width="283" height="163" style="display: block;">"""
re.match(r"https://.*\.jpg", meizi_image)
re.search(r"https://.*\.jpg", meizi_image)
re.search(r"https://.*\.jpg", meizi_image).group()
re.search(r"https://.*?\.jpg", meizi_image).group()
my_path = "c:\a\b\c"
print(my_path)
my_path = "c:\\a\\b\\c"
print(my_path)
re.match("c:", my_path)
re.match("c:", my_path).group()
re.match("c:\\a", my_path).group()
re.match("c:\\\\a", my_path).group()
print(re.match("c:\\\\a", my_path).group())
print(re.match("c:\\\\a\\\\b", my_path).group())
print(re.match("c:\\\\a\\\\b\\\\c", my_path).group())
print(re.match(r"c:\\a\\b\\c", my_path).group())
```

___
> 共同学习，共同进步