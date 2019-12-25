# 进程

* 使用进程

```python
import time
import multiprocessing


def test1():
    while True:
        print("1--------")
        time.sleep(1)


def test2():
    while True:
        print("2--------")
        time.sleep(1)


def main():
    p1 = multiprocessing.Process(target=test1)
    p2 = multiprocessing.Process(target=test2)
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
```

* 获取进程的pid

```python
import multiprocessing
import os
import time


def test():
    while True:
        print("----in 子进程 pid=%d ,父进程的pid=%d---" % (os.getpid(), os.getppid()))
        time.sleep(1)


def main():
    print("----in 主进程 pid=%d---父进程pid=%d----" % (os.getpid(), os.getppid()))
    p = multiprocessing.Process(target=test)
    p.start()


if __name__ == "__main__":
    main()
```

* 进程的运行顺序

```python
import multiprocessing
import os
import time


def test():
    while True:
        print("----in 子进程 pid=%d ,父进程的pid=%d---" % (os.getpid(), os.getppid()))
        time.sleep(1)


def test2():
    while True:
        print("----in 子进程2 pid=%d ,父进程的pid=%d---" %
            (os.getpid(), os.getppid()))
        time.sleep(1)


def main():
    print("----in 主进程 pid=%d---父进程pid=%d----" % (os.getpid(), os.getppid()))
    p = multiprocessing.Process(target=test)
    p.start()

    p2 = multiprocessing.Process(target=test2)
    p2.start()


if __name__ == "__main__":
    main()
```

* 给Process传递参数

```python
import multiprocessing
import os
import time


def test(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)


def main():
    print("----in 主进程 pid=%d---父进程pid=%d----" % (os.getpid(), os.getppid()))
    p = multiprocessing.Process(target=test, args=(
        11, 22, 33, 44, 55, 66, 77, 88), kwargs={"mm": 11})
    p.start()


if __name__ == "__main__":
    main()
```

* 多进程通过Queue来实现数据共享

```python
# 不共享全局变量
import multiprocessing

"""
一个进程向Queue中写入数据，另外一个进程从Queue中获取数据，
通过Queue完成了 多个需要配合的进程间的数据共享，从而能够 起到 解耦的作用
"""


def download_from_web(q):
    """下载数据"""
    # 模拟从网上下载的数据
    data = [11, 22, 33, 44]

    # 向队列中写入数据
    for temp in data:
        q.put(temp)

    print("---下载器已经下载完了数据并且存入到队列中----")


def analysis_data(q):
    """数据处理"""
    waitting_analysis_data = list()
    # 从队列中获取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)

        if q.empty():
            break

    # 模拟数据处理
    print(waitting_analysis_data)


def main():
    # 1. 创建一个队列
    q = multiprocessing.Queue()

    # 2. 创建多个进程，将队列的引用当做实参进行传递到里面
    p1 = multiprocessing.Process(target=download_from_web, args=(q,))
    p2 = multiprocessing.Process(target=analysis_data, args=(q,))
    p1.start()
    p2.start()


if __name__ == "__main__":
    main()
```

* 进程池

```python
from multiprocessing import Pool
import os
import time
import random


def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


po = Pool(3)  # 定义一个进程池，最大进程数3
for i in range(0, 10):
    # Pool().apply_async(要调用的目标,(传递给目标的参数元祖,))
    # 每次循环将会用空闲出来的子进程去调用目标
    po.apply_async(worker, (i,))

print("----start----")
po.close()  # 关闭进程池，关闭后po不再接收新的请求
po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
print("-----end-----")
```

* 多任务文件拷贝

```python
import os
import multiprocessing


def copy_file(q, file_name, old_folder_name, new_folder_name):
    """完成文件的复制"""
    # print("======>模拟copy文件：从%s--->到%s 文件名是:%s" % (old_folder_name, new_folder_name, file_name))
    old_f = open(old_folder_name + "/" + file_name, "rb")
    content = old_f.read()
    old_f.close()

    new_f = open(new_folder_name + "/" + file_name, "wb")
    new_f.write(content)
    new_f.close()

    # 如果拷贝完了文件，那么就向队列中写入一个消息，表示已经完成
    q.put(file_name)


def main():
    # 1. 获取用户要copy的文件夹的名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2. 创建一个新的文件夹
    try:
        new_folder_name = old_folder_name + "[复件]"
        os.mkdir(new_folder_name)
    except:
        pass

    # 3. 获取文件夹的所有的待copy的文件名字  listdir()
    file_names = os.listdir(old_folder_name)
    # print(file_names)

    # 4. 创建进程池
    po = multiprocessing.Pool(5)

    # 5. 创建一个队列
    q = multiprocessing.Manager().Queue()

    # 6. 向进程池中添加 copy文件的任务
    for file_name in file_names:
        po.apply_async(copy_file, args=(
            q, file_name, old_folder_name, new_folder_name))

    po.close()
    # po.join()
    all_file_num = len(file_names)  # 测一下所有的文件个数
    copy_ok_num = 0
    while True:
        file_name = q.get()
        # print("已经完成copy：%s" % file_name)
        copy_ok_num += 1
        print("\r拷贝的进度为：%.2f %%" % (copy_ok_num*100/all_file_num), end="")
        if copy_ok_num >= all_file_num:
            break

    print()


if __name__ == "__main__":
    main()
```
___
> 共同学习，共同进步