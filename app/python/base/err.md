# 异常

* 简单的异常捕获

```python
try:
    # 不能确定执行的代码
    num = int(input('请输入一个整数：'))
except:
    # 错误的处理代码
    print('请输入正确的整数')

print('-' * 50)
```

* 捕获异常类型

```python
try:
    num = int(input('输入一个整数：'))

    result = 8 / num

    print(result)
except ZeroDivisionError:
    print('除0错误')
except ValueError:
    print('请输入正确的整数')

# 错误类型 异常抛出最后一行 第一个单词
```

* 捕获未知异常

```python
try:
    num = int(input('输入一个整数：'))

    result = 8 / num

    print(result)
except ValueError:
    print('请输入正确的整数')
except Exception as error:
    print('未知错误 %s' % error)
```

* 完整的异常语法

```python
try:
    num = int(input('输入一个整数：'))

    result = 8 / num

    print(result)
except ValueError:
    print('请输入正确的整数')
except Exception as error:
    print('未知错误 %s' % error)
else:
    print('尝试成功')
finally:
    print('无论是否出现错误都会执行的代码')

print('-' * 50)
```

* 异常的传递

```python
def demo1():
    return int(input('输入整数：'))


def demo2():
    return demo1()


# 利用异常的传递性，在主程序捕获异常
try:
    print(demo2())
except Exception as error:
    print('未知错误 %s' % error)
```

* 抛出异常

```python
def input_password():

    # 提示用户输入密码
    pwd = input('请输入密码：')

    # 判断密码长度 >= 8 返回输入的密码
    if len(pwd) >= 8:
        return pwd

    # 如果 < 8 主动抛出异常
    print('主动抛出异常')
    # 创建异常对象
    ex = Exception('密码长度不够')

    # 主动抛出异常
    raise ex


# 提示用户输入密码
try:
    print(input_password())
except Exception as error:
    print('捕获异常：%s' % error)
```

___
> 共同学习，共同进步