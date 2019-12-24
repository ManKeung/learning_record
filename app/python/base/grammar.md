# 语法进阶

* 引用

```python
def test (num):
    print('在函数内部%d对应的内存地址是%d' % (num, id(num)))

    # 定义一个字符串变量
    result = 'hello'

    print('函数要返回数据的内存地址是%d' % id(result))

    # 将字符串变量返回
    return result


# 定义一个数字的变量
a = 10

# 数据的地址本质上就是一个数字
print('a变量保存数据的内存地址%d' % id(a))

# 调用 test 函数 本质上传递的是实参保存数据的引用 而不是实参保存的数字
# 注意：函数有返回值没有定义变量接收
# 程序不会报错，但是无法获取返回结果
r = test(a)

print('%s的内存地址是%d' % (r, id(r)))

"""
a变量保存数据的内存地址9282016
在函数内部10对应的内存地址是9282016
函数要返回数据的内存地址是139915218494640
hello的内存地址是139915218494640
"""
```

* 局部变量

```python
def demo1 ():
    # 定义一个局部变量
    num = 10

    print('在demo1函数内部的变量是%d' % num)


def demo2 ():
    # print('%d' % num)  # error
    pass

demo1()
demo2()
```

* 全局变量

```python
# 全局变量
num = 10


def demo1():

    print('demo1 ==> %d' % num)


def demo2():

    print('demo2 ==> %d' % num)


demo1()
demo2()

# 修改全局变量
# 全局变量
num = 10


def demo1():

    # 修改全局变量
    global num
    num = 99
    print('demo1 ==> %d' % num)


def demo2():

    print('demo2 ==> %d' % num)


demo1()
demo2()
```

* 返回多个参数

```python
def measure():
    ''' 测量温度和湿度 '''

    print('测量开始...')
    temp = 39
    wetness = 50
    print('测量结束...')

    # 元祖 可以返回多个数据，因此可以使用元祖
    # 如果函数返回的类型是元祖，小括号可以省略
    # return  (temp, wetness)
    return temp, wetness


result = measure()
print(result)

# 单独处理温度或者湿度 - 不方便
print(result[0])
print(result[1])

# 若果返回类型是元祖，同时希望单独的处理元祖中的元素
# 可以使用多个变量，一次接收函数的返回结果
gl_temp, gl_wetness = measure()

print(gl_temp)
print(gl_wetness)
```

* 交换数字

```python
a = 6
b = 100

# 解法1 - 使用其他变量
c = a
a = b
b = c

print(a, b)

# 解法2 - 不使用其他变量
a = a + b
b = a - b
a = a - b

print(a, b)

# 解法3 - 利用元祖
a, b = b, a

print(a, b)
```

* 多值参数

```python
def demo(num, *nums, **person):

    print(num)
    print(nums)
    print(person)


demo(1, 2, 3, 4, 5, name="小美", age=10)

"""
1
(2, 3, 4, 5)
{'name': '小美', 'age': 10}
"""
```

* 元祖字典的拆包

```python
def demo(*args, **kwargs):

    print(args)
    print(kwargs)


# 元祖变量/字典变量
gl_num = (1, 2, 3)
gl_dict = {'name': '小明', 'age': 18}

demo(*gl_num, **gl_dict)

"""
(1, 2, 3)
{'name': '小明', 'age': 18}
"""
```

* 递归函数

```python
def sum_number(num):

    print(num)

    # 递归的出口，当参数满足某个条件时，不在执行函数
    if num == 1:
        return

    # 自己调用自己
    sum_number(num - 1)


sum_number(3)

# 递归求和
def sum_numbers(num):

    # 出口
    if num == 1:
        return 1

    # 数字累加
    # 假设sum_numbers 能够正确处理1 ... num累加
    temp = sum_numbers(num - 1)

    # 两个数字相加
    return num + temp


result = sum_numbers(100)

print(result)
```

___
> 共同学习，共同进步