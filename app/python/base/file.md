# 文件

* 读取文件

```python
# 打开文件
file = open('./txt.txt')

# 读取文件
text = file.read()
print(text)

# 关闭
file.close()
```

* 读取文件后文件指针会改变

```python
# 打开文件
file = open('./txt.txt')

# 读取文件
text = file.read()
print(text)
print(len(text))

print('-' * 50)

text2 = file.read()
print(text2)
print(len(text2))

# 关闭
file.close()
```

* 写入文件

```python
# 打开
# file = open('./text.txt', 'w')
file = open('./text.txt', 'a')

# 写入文件
file.write('hello world!')

# 关闭文件
file.close()
```

* 分行读取文件

```python
file = open('./txt.txt')

while True:
    text = file.readline()

    # 判断是否读取到内容
    if not text:
        break

    print(text)

file.close()
```

* 复制文件

```python
# 打开
file_read = open('./txt.txt')
file_write = open('./txt[附件].txt', 'w')


# 读、写
text = file_read.read()
file_write.write(text)


# 关闭
file_read.close()
file_write.close()

""" 复制大文件 """
# 打开
file_read = open('./txt.txt')
file_write = open('./txt[附件].txt', 'w')


# 读、写
while True:
    text = file_read.readline()

    if not text:
        break

    file_write.write(text)


# 关闭
file_read.close()
file_write.close()
```

* eval

```python
input_str = input('输入算术题：')

print(eval(input_str))
```

* os

```python
import os
print(os.getcwd())  # 获取当前工作目录路径
print(os.path.abspath('.'))  # 获取当前工作目录路径
print(os.path.abspath('txt.txt'))  # 获取当前目录文件下的工作目录路径
print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
print(os.path.abspath(os.curdir))  # 获取当前工作目录路径
print(os.listdir())
```

* with

```python
# 自己实现
from contextlib import contextmanager

@contextmanager
def my_open(path, mode):
    f = open(path, mode)
    yield f
    f.close()

with my_open('out.txt', 'w') as f:
    f.write('hello , the simplest context manager')

# with open打开文件
with open('out.txt', 'w') as f:
    f.write('hello , the simplest context manager')
```

___
> 共同学习，共同进步