# 协程

* 自己实现一个可以迭代的对象

```python
from collections.abc import Iterable
from collections.abc import Iterator
import time


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """ 如果想要一个对象成为一个 可以迭代的对象，既可以使用for，那么必须实现__iter__方法 """
        return ClassIterator()


class ClassIterator(object):
    def __iter__(self):
        pass

    def __next__(self):
        return 11


classmate = Classmate()

classmate.add('老王')
classmate.add('老二')
classmate.add('张三')

# print('判断classmate是不是可以迭代的对象:', isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print('判断classmate_iterator是否是迭代器：', isinstance(classmate_iterator, Iterator))

# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)

""" 2 """
import time
from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个　可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        return self.obj.names[0]


classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)

""" 3 """
import time
from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个　可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        ret = self.obj.names[self.current_num]
        self.current_num += 1
        return ret


classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)

""" 4 """
import time
from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个　可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return ClassIterator(self)


class ClassIterator(object):

    def __init__(self, obj):
        self.obj = obj
        self.current_num = 0

    def __iter__(self):
        pass

    def __next__(self):
        if self.current_num < len(self.obj.names):
            ret = self.obj.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)

""" 5 """
import time
from collections.abc import Iterable
from collections.abc import Iterator


class Classmate(object):
    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """如果想要一个对象称为一个　可以迭代的对象，即可以使用for，那么必须实现__iter__方法"""
        return self  # 调用iter(xxobj)的时候 只要__iter__方法返回一个 迭代器即可，至于是自己 还是 别的对象都可以的, 但是要保证是一个迭代器(即实现了 __iter__  __next__方法)

    def __next__(self):
        if self.current_num < len(self.names):
            ret = self.names[self.current_num]
            self.current_num += 1
            return ret
        else:
            raise StopIteration


classmate = Classmate()
classmate.add("老王")
classmate.add("王二")
classmate.add("张三")

# print("判断classmate是否是可以迭代的对象:", isinstance(classmate, Iterable))
# classmate_iterator = iter(classmate)
# print("判断classmate_iterator是否是迭代器:", isinstance(classmate_iterator, Iterator))
# print(next(classmate_iterator))

for name in classmate:
    print(name)
    time.sleep(1)
```

* fibonacci

```python
nums = list()

a = 0
b = 1
i = 0

while i < 10:
    nums.append(a)
    a, b = b, a+b
    i += 1

print(nums)

""" 迭代器实现 """
import time
from collections.abc import Iterable
from collections.abc import Iterator


class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            ret = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return ret
        else:
            raise StopIteration


fibo = Fibonacci(10)

for num in fibo:
    print(num)

""" 使用生成器 """
def create_num(all_num):
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么不再是函数，而是一个生成器模板
        a, b = b, a+b
        current_num += 1


# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建爱你一个生成器对象
obj = create_num(10)

for num in obj:
    print(num)
```

* 生成器的研究

```python
def create_num(all_num):
    print('---1---')
    a, b = 0, 1
    current_num = 0

    while current_num < all_num:
        print('---2---')
        yield a  # 如果一个函数中有yield语句，那么这个就不在是函数，而是一个生成器的模板
        print('---3---')
        a, b = b, a+b
        current_num += 1
        print('---4---')


# 如果在调用create_num的时候，发现这个函数中有yield那么此时，不是调用函数，而是创建一个生成器对象
obj = create_num(10)
obj2 = create_num(2)

ret = next(obj)
print('obj:%d' % ret)

ret = next(obj)
print('obj:%d' % ret)

ret = next(obj2)
print('obj2:%d' % ret)

ret = next(obj)
print('obj:%d' % ret)

ret = next(obj)
print('obj:%d' % ret)

ret = next(obj)
print('obj:%d' % ret)

ret = next(obj2)
print('obj2:%d' % ret)

ret = next(obj2)
print('obj2:%d' % ret)
```

* 通过异常判断生成器已经结束

```python
def create_num(all_num):
    # a = 0
    # b = 1
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        # print(a)
        yield a  # 如果一个函数中有yield语句，那么这个就不在是函数，而是一个生成器的模板
        a, b = b, a+b
        current_num += 1
    return 'ok....'


obj2 = create_num(50)

while True:
    try:
        ret = next(obj2)
        print(ret)
    except Exception as ret:
        print(ret.value)
        break
```

* 通过send传值并启动生成器

```python
def create_num(all_num):
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        ret = yield a
        print('>>>ret>>>', ret)
        a, b = b, a+b
        current_num += 1


obj = create_num(10)

ret = next(obj)
print(ret)

# ret = obj.send(None)  #  传值
ret = obj.send('哈哈')
print(ret)
```

* 协程yield实现

```python
import time


def task_1():
    while True:
        print('---1---')
        time.sleep(0.1)
        yield


def task_2():
    while True:
        print('---2---')
        time.sleep(0.1)
        yield


def main():
    t1 = task_1()
    t2 = task_2()

    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
```

* greenlet

```bash
pip3 install greenlet
```

```python
from greenlet import greenlet  # pip3 install greenlet
import time


def test1():
    while True:
        print("---A--")
        gr2.switch()
        time.sleep(0.5)


def test2():
    while True:
        print("---B--")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到gr1中运行
gr1.switch()
```

* gevent

```bash
pip3 install gevent
```

```python
import gevent
import time


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


print("----1---")
g1 = gevent.spawn(f1, 5)
print("----2---")
g2 = gevent.spawn(f2, 5)
print("----3---")
g3 = gevent.spawn(f3, 5)
print("----4---")
g1.join()
g2.join()
g3.join()

""" 打补丁 """
import gevent
import time
from gevent import monkey

monkey.patch_all()


def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)


print("----1---")
g1 = gevent.spawn(f1, 5)
print("----2---")
g2 = gevent.spawn(f2, 5)
print("----3---")
g3 = gevent.spawn(f3, 5)
print("----4---")
g1.join()
g2.join()
g3.join()
```

* 示例

```python
import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
	req = urllib.request.urlopen(img_url)

	img_content = req.read()

	with open(img_name, 'wb') as f:
		f.write(img_content)


def main():
	gevent.joinall([
		gevent.spawn(downloader, '3.jpg', 'https://rpic.douyucdn.cn/appCovers/2017/09/22/1760931_20170922133718_big.jpg'),
		gevent.spawn(downloader, '4.jpg', 'https://rpic.douyucdn.cn/appCovers/2017/09/17/2308890_20170917232900_big.jpg')
	])


if __name__ == '__main__':
	main()
```

___
> 共同学习，共同进步