# 闭包与装饰器

* 闭包初识

```python
class Line(object):
    def __init__(self, k, b):
        self.k = k
        self.b = b

    def __call__(self, x):
        print(self.k * x + self.b)


line = Line(1, 2)
line(0)
line(1)
# 缺点：为了计算多条线上的y值，所以需要保存多个k, b的值，因此用了很多个实例对象， 浪费资源


def lineFn(k, b):
    def create_y(x):
        print(k*x + b)

    return create_y


fn = lineFn(1, 2)

fn(0)
fn(1)
```

* 修改闭包中的数据

```python
x = 300


def test1():
	x = 200

	def test2():
		nonlocal x
		print("----1----x=%d" % x)
		x = 100
		print("----2----x=%d" % x)

	return test2


t1 = test1()
t1()
```

* 装饰器演示

```python
import time


def set_func(func):
	def call_func():
		start_time = time.time()
		func()
		stop_time = time.time()
		print('alltimes is %f' % (stop_time-start_time))
	return call_func


@set_func  # 等价于test1 = set_func(test1)
def test1():
	print("-----test1----")
	for i in range(10000):
		pass


test1()
```

* 带不定参数

```python
def set_func(func):
	print("---开始进行装饰")

	def call_func(*args, **kwargs):
		print("---这是权限验证1----")
		print("---这是权限验证2----")
		# func(args, kwargs)  # 不行，相当于传递了2个参数 ：1个元组，1个字典
		func(*args, **kwargs)  # 拆包
	return call_func


@set_func  # 相当于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
	print("-----test1----%d" % num)
	print("-----test1----", args)
	print("-----test1----", kwargs)


test1(100)
test1(100, 200)
test1(100, 200, 300, mm=100)
```

* 带返回值

```python
def set_func(func):
	print("---开始进行装饰")

	def call_func(*args, **kwargs):
		print("---这是权限验证1----")
		print("---这是权限验证2----")
		# func(args, kwargs)  # 不行，相当于传递了2个参数 ：1个元组，1个字典
		return func(*args, **kwargs)  # 拆包
	return call_func


@set_func  # 相当于 test1 = set_func(test1)
def test1(num, *args, **kwargs):
	print("-----test1----%d" % num)
	print("-----test1----", args)
	print("-----test1----", kwargs)
	return 'ok'


ret = test1(100)
print(ret)
```

* 使用类做装饰器

```python
class Test(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, a):
        # print('这里是装饰器添加的功能... %s' % self.func())
        print('这里是装饰器添加的功能...')
        print(a)
        return '这里是装饰器添加的功能... %s' % self.func(a)


@Test  # 相当于get_str = Test(get_str)
def get_str(a):
    print(a)
    return 'haah'


print(get_str(1))
```

* 带参数装饰器

```python
def set_level(level_num):
    def set_func(func):
        def call_func(*args, **kwargs):
            if level_num == 1:
                print('---权限验证级别1，验证---')
            elif level_num == 2:
                print('---权限验证级别2，验证---')
            return func()
        return call_func
    return set_func


@set_level(1)
def test():
    print('----test---')
    return 'ok'


@set_level(2)
def test2():
    print('----test2---')
    return 'ok'


test()
test2()
```

___
> 共同学习，共同进步