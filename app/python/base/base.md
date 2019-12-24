# 初认识

* hello.py

```python
print('hello python')
print(1.01**365)
# 这是一个注释
""" 多行注释 """
```

* 个人信息

```python
"""
姓名：小明
年龄：18岁
性别：是男生
身高：1.75米
体重：75.0公斤
"""

# 在 python中，定义变量时是不需要指定变量的类型
# 在运行的时候，python解释器，会根据赋值语句等号右侧
# 自动推出变量中保存数据的准确类型

# str 表示是一个字符串类型
name = "小明"
# int 表示是一个整数类型
age = 18
# bool 表示是一个布尔类型，真 True 或者是 False
gender = True
# float 表示是一个小数类型，浮点型
height = 1.75
weight = 75.0

print(name, age)
```

* 超市买苹果

```python
# 1. 苹果单价输入
# price_str = input("苹果的单价：")
price = float(input("苹果的单价："))

# 2. 输入苹果的重量
# weight_str = input("苹果的重量：")
weight = float(input("苹果的重量："))

# 3. 计算支付的总额
# 注意：两个字符串变量之前是不能直接用乘法
# money = price_str * weight_str
# 转换成小数
# price = float(price_str)
# weight = float(weight_str)
money = price * weight

print(money)
```

* 格式化输出

```python
name = "小明"
print("我的名字叫%s，请多多关照！" % name)

student_no = 1
print("我的学号是%06d" % student_no)

price = 12.4
weight = 3.2
money = price * weight
print("苹果单价%.02f元/斤，购买了%.02f斤，需要支付%.02f元。" %(price, weight, money))

scale = 0.2
print("数据比例是%.02f%%" % (scale * 100))

import keyword
print(keyword.kwlist)
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
"""
```

___
> 共同学习，共同进步