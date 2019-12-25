# 线程

* 基本用法

```python
import time
import threading

def sing():
    """ 唱歌5秒 """
    for i in range(5):
        print('---正在唱:菊花台---')
        time.sleep(1)


def dance():
    """ 跳舞5秒 """
    for i in range(5):
        print('---正在跳舞---')
        time.sleep(1)


def main():
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
```

* 循环查看当前运行的线程

```python
import threading
import time


def test1():
    for i in range(5):
        print('-----test1---%d---' % i)
        time.sleep(1)


def test2():
    for i in range(10):
        print('-----test2---%d---' % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)

    t1.start()
    t2.start()

    while len(threading.enumerate()) > 1:
        print(threading.enumerate())
        time.sleep(1)


if __name__ == '__main__':
    main()
```

* 多线程共享全局变量

```python
import threading
import time


def test1(temp):
    temp.append(33)
    print('---in test1 temp=%s---' % str(temp))


def test2(temp):
    print('---in test2 temp=%s---' % str(temp))


g_nums = [11, 22]


def main():
    # target指定将来 这个线程去哪个函数执行代码
    # args指定将来调用函数的时候 传递什么参数过去
    t1 = threading.Thread(target=test1, args=(g_nums,))
    t2 = threading.Thread(target=test2, args=(g_nums,))
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print('---in main Thread g_nums = %s---' % str(g_nums))


if __name__ == '__main__':
    main()
```

* 线程共享全局变量的问题

```python
import threading
import time


# 定义一个全局变量
g_num = 0


def test1(num):
    global g_num
    for i in range(num):
        g_num += 1
    print('---in test1 g_num=%d---' % g_num)


def test2(num):
    global g_num
    for i in range(num):
        g_num += 1
    print('---in test2 g_num=%d---' % g_num)


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待两个线程执行完毕
    time.sleep(5)

    print('---in main Thread g_num = %d---' % g_num)


if __name__ == '__main__':
    main()

"""
---in test1 g_num=1242490---
---in test2 g_num=1511787---
---in main Thread g_num = 1511787---
"""
```

* 互斥锁解决资源竞争问题

```python
import threading
import time


# 定义一个全局变量
g_num = 0


def test1(num):
    global g_num

    # 上锁，如果之前没有上锁，那么此时 上锁成功
    # 如果上锁之前 已经被上锁了，那么此时会堵塞在这里，知道 这个锁被解锁
    # mutex.acquire()  #  原则上锁住代码越少越好

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    # 解锁
    # mutex.release()
    print('---in test1 g_num=%d---' % g_num)


def test2(num):
    global g_num
    # mutex.acquire()

    for i in range(num):
        mutex.acquire()
        g_num += 1
        mutex.release()

    # mutex.release()
    print('---in test2 g_num=%d---' % g_num)


# 创建一个互斥锁，默认是没有上锁
mutex = threading.Lock()


def main():
    t1 = threading.Thread(target=test1, args=(1000000,))
    t2 = threading.Thread(target=test2, args=(1000000,))

    t1.start()
    t2.start()

    # 等待两个线程执行完毕
    time.sleep(2)

    print('---in main Thread g_num = %d---' % g_num)


if __name__ == '__main__':
    main()
```

* 案例多线程udp聊天

```python
import socket
import threading


def recv_msg(udp_socket):
    """ 接收数据并显示 """
    while True:
        recv_data = udp_socket.recvfrom(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    """ 发送数据 """
    while True:
        send_data = input('输入发送的数据：')
        udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))


def main():
    """ 完成udp聊天器的整体控制 """

    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    udp_socket.bind(('', 7890))

    # 获取对方的ip
    # dest_ip = input('请输入对方的ip：')
    dest_ip = '192.168.247.1'
    # dest_port = int(input('请输入对方的port：'))
    dest_port = 8080

    # 创建两个线程执行相应的功能
    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(
        target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()


if __name__ == '__main__':
    main()
```
___
> 共同学习，共同进步