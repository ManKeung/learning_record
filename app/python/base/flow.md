# 流程控制

## 分支

* if判断

```python
# 输入用户年龄
age = int(input('请输入你的年龄：'))

# 判断是否满18岁 (>=)
if age >= 18:
    # 如果满18岁，允许进入网吧
    print('你已经成年，欢迎进入网吧嗨皮')
# 如果未满18岁，提示回家写作业
else:
    print('你还没成年，请回家写作业吧！')

# 这句代码无论条件是否满足都执行
print('这句代码什么时候执行？')
```

* 逻辑预算符

```python
age = 12
# if age >= 0 and age <= 120
if age >=0 and age <= 120:
    print('年龄正确')
else:
    print('年龄错误')

""" ******* """
python_score = 80
c_score = 75

if python_score > 60 or c_score > 60:
    print('考试通过')
else:
    print('考试失败，继续努力')

""" ******* """
is_employee = True

if not is_employee:
    print('禁止入内')
else:
    print('欢迎进入')

""" ******* """
holiday_name = '平安夜'

if holiday_name == '情人节':
    print('买玫瑰')
elif holiday_name == '平安夜':
    print('买苹果')
elif holiday_name == '生日':
    print('买蛋糕')
else:
    print('每天都是节日')
```

## 循环

* while

```python
i = 1

while i <= 5:
    print('hello python %d' % i)
    i += 1
print('循环结束后，i = %d' % i)
```

* break

```python
i = 0

while i < 10:
    if i == 3:
        break
    print(i)
    i += 1
print('over')
```

* continue

```python
i = 0

while i < 10:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
```

* print

```python
print('❤', end='')
print('*')
```

* 九九乘法表

```python
row = 1

while row <= 9:
    col = 1
    while col <= row:
        # print('%d * %d = %2d' % (col, row, col * row), end='  ')
        print('%d * %d = %d' % (col, row, col * row), end='\t')
        col += 1
    print('')
    row += 1
```

* 转义字符

```python
# \t 在控制台输出 制表符 协助输出文本时 垂直方向 保持对其
print('\t1 \t2 \t3')
print('\t10 \t20 \t30')

# \n 换行符
print('hello\npython')

print('hello \" python')
```

___
> 共同学习，共同进步