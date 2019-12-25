# 高级数据类型

## 列表

* 基本使用

```python
name_list = ['zhangsan', 'lisi', 'wangwu']

# 1. 取值和索引
print(name_list[2])
print('*'*50)
print('\n')

# 知道数据内容，想知道数据在列表的位置
index = name_list.index('lisi')
print(index)
print('*'*50)
print('\n')

# 2. 修改
name_list[1] = '李四'
print(name_list[1])
print('*'*50)
print('\n')

# 3. 增加
name_list.append('mankeung')
print(name_list)
print('*'*50)
print('\n')

name_list.insert(0, '王文强')
print(name_list)
print('*'*50)
print('\n')

name_list2 = ['王五', '张三', '王麻子']
name_list.extend(name_list2)
print(name_list)
print('*'*50)
print('\n')

# 4. 删除
name_list2.remove('王五')
print(name_list2)
print('*'*50)
print('\n')

name_list2.pop()
print(name_list2)
print('*'*50)
print('\n')

name_list.clear()
print(name_list)
print('*'*50)
print('\n')
```

* 关键词del

```python
name_list = ['王五', '张三', '王麻子']

# del name_list
# print(name_list)
# NameError: name 'name_list' is not defined

del name_list[1]
print(name_list)
# ['王五', '王麻子']
```

* 列表的数据统计

```python
name_list = ['张三', '李四', '王五', '张三']

list_len = len(name_list)
print('列表中包含%d个元素' % list_len)

count = name_list.count('张三')
print('张三出现了%d次' % count)

# 删除第一次出现
name_list.remove('张三')
print(name_list)
```

* 列表排序

```python
name_list = ['zhangsan', 'lisi', 'wangwu', 'wangxiaoer']
num_list = [6, 8, 4, 1, 10]

# 升序
name_list.sort()
num_list.sort()
print(name_list)
print(num_list)
print('\n')

# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)
print(name_list)
print(num_list)
print('\n')

# 逆序（反转）
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)
print('\n')
```

* 列表遍历

```python
name_list = ['zhangsan', 'lisi', 'wangwu', 'wangxiaoer']

# 使用迭代遍历列表
for name in name_list:
    print('名字是%s' % name)
```

## 元祖

* 基本使用

```python
info_tuple = ('zhangsan', 18, 1.75)

# 1. 取值和取索引
print(info_tuple[0])
print(info_tuple.index('zhangsan'))

# 2. 统计计数
print(info_tuple.count('zhangsan'))
print(len(info_tuple))
```

* 元祖遍历

```python
info_tuple = ('zhangsan', 18, 1.75)

for item in info_tuple:
    print(item)
```

* 格式化字符串

```python
# 格式化字符串后面的`()`本质上就是元祖
# print('%s 年龄是 %d' %('小明', 18))
info_tuple = ('小明', 18)
print('%s 年龄是 %d' % info_tuple)

info_str = '%s 年龄是 %d' % info_tuple
print(info_str)
```

## 字典

* 字典定义

```python
# 字典是一个无序的数据集合
xiaoming = {
    'name': '小明',
    'age': 18,
    'gender': True,
    'height': 1.75,
    'weight': 75.5
}

info = [xiaoming]

print(xiaoming)
print(type(xiaoming))
print(info[0])
print(type(info))
```

* 字典的基本使用

```python
xiaoming_dict = {'name': '小明'}

# 取值
print(xiaoming_dict['name'])

# 增加/修改
xiaoming_dict['age'] = 18
xiaoming_dict['name'] = 'xiaoming'

# 统计键值对数量
print(len(xiaoming_dict))

# 合并字典
temp_dict = {'height': 1.75, 'age': 20}
xiaoming_dict.update(temp_dict)

# 删除
del xiaoming_dict['name']
xiaoming_dict.pop('age')

# 清空
xiaoming_dict.clear()

print(xiaoming_dict)
```

* 字典的遍历

```python
xiaoming_dict = {
    'name': '小明',
    'qq': '123456',
    'phone': '10086'
}

# 遍历字典
for k in xiaoming_dict:
    print("%s - %s" % (k, xiaoming_dict[k]))

print(xiaoming_dict.keys())
print(xiaoming_dict.values())
print(xiaoming_dict.items())
```

* 字典的应用场景

```python
card_list = [
    {
        'name': '张三',
        'qq': '12345',
        'phone': '110'
    },
    {
        'name': '李四',
        'qq': '12346',
        'phone': '119'
    }
]

for card_info in card_list:
    print(card_info)
```

## 字符串

* 字符串定义和遍历

```python
str1 = 'hello python'
str2 = '我的外号是"大西瓜"'

for char in str2:
    print(char)

print(str1[6])
```

* 字符串统计操作

```python
hello_str = 'hello hello'

# 统计字符串长度
print(len(hello_str))

# 统计某个小字符串出现的次数
print(hello_str.count('llo'))

# 某个字符串出现的位置
print(hello_str.index('l'))
```

* 字符串判断方法

```python
# 判断空白字符
space_str = ' \t\n\r'

print(space_str.isspace())

# 判断字符串中是否只包含数字
# 1. 都不能判断小数
# num_str = '1.1'
# 2. unicode 字符串
# num_str = '\u00b2'
# 3. 中文数字
num_str = '一千零一'

print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())
```

* 字符串的查找替换

```python
hello_str = 'hello world'

# 判断是否以指定字符串开始
print(hello_str.startswith('hello'))

# 判断是否以指定字符串结束
print(hello_str.endswith('world'))

# 查找指定字符串
# index同样可以查找指定字符的索引
print(hello_str.find('llo'))
print(hello_str.find('abc'))

# 替换字符串
print(hello_str.replace('world', 'python'))
```

* 字符串文本对齐

```python
poem = [
    '\t\n登黄鹤楼',
    '王焕之',
    '白日依山尽\t\n',
    '黄河入海流',
    '欲穷千里目',
    '更上一层楼',
]

for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10, '　'))
    # print("|%s|" % poem_str.ljust(10, '　'))
```

* 字符串的拼接和拆分

```python
poem_str = '登黄鹤楼\t 王焕之 \t白日依山尽\t\n黄河入海流\t\n欲穷千里目\n更上一层楼'

print(poem_str)

# 拆分字符串
poem_list = poem_str.split()
print(poem_list)

# 合并字符串
result = ' '.join(poem_list)
print(result)
```

* 字符串的切片

```python
num_str = '0123456789'
print('原始数据')
print(num_str)
print('*'*50)
print(num_str[2:6])
print(num_str[2:])
print(num_str[0:6])
print(num_str[:6])
print(num_str[:])
print(num_str[::2])
print(num_str[1::2])
print(num_str[2:-1])
print(num_str[-2:])
print(num_str[-1::-1])
```

## 推导式

### 列表推导式

* 示例1

```python
num_list = [i for i in range(30)]
print(num_list)
```

* 示例2

```python
num_list = [i for i in range(30) if i % 3 is 0]
print(num_list)
```

* 示例3

```python
def squared(x):
    return x*x


num_list = [squared(i) for i in range(30) if i % 3 is 0]
print(num_list)
```

* 示例4

使用()生成generator

```python
num_list = (i for i in range(30) if i % 3 is 0)
print(type(num_list))

for i in num_list:
    print(i)
```

### 字典推导式

* 示例1

```python
mcase = {'a': 10, 'b': 34, 'A': 7, 'Z': 3}
mcase_frequency = {
    k.lower(): mcase.get(k.lower(), 0) + mcase.get(k.upper(), 0)
    for k in mcase.keys()
    if k.lower() in ['a', 'b']
}
print(mcase_frequency)
```

* 示例2

```python
mcase = {'a': 10, 'b': 34}
mcase_frequency = {v: k for k, v in mcase.items()}
print(mcase_frequency)
```

### 集合推导式

* 示例1

```python
squared = {x**2 for x in [1, 1, 2]}
print(squared)
```
___
> 共同学习，共同进步