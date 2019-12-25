# 网络编程UDP

* 基本使用

```python
import socket

def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 可以使用套接字收发数据
    # udp_socket.sendto('hahah', 对方的ip和port)
    # udp_socket.sendto(send_data.encode('utf-8'), ('192.168.247.1', 8080))
    udp_socket.sendto(b'hello python', ('192.168.247.1', 8080))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
```

* 绑定端口用来接收数据

```python
import socket

def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    localaddr = ('', 7788)
    udp_socket.bind(localaddr)

    # 接收数据
    recv_data = udp_socket.recvfrom(1024)  # 1024接收多大
    # recv_data这个变量存储的是一个元祖（接收到的数据，（发送的ip，port））
    recv_msg = recv_data[0]  # 存储接收到的数据
    recv_addr = recv_data[1]  # 存储发送方的地址

    # 打印接收到的数据
    # print(recv_data)
    # print('%s:%s' % (str(recv_addr), recv_msg.decode('utf-8')))  # windos默认gbk
    print('%s:%s' % (str(recv_addr), recv_msg.decode('gbk')))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
```

* 接收消息

```python
import socket


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定本地信息
    localaddr = ('', 7788)
    udp_socket.bind(localaddr)

    # 接收数据
    while True:
        recv_data = udp_socket.recvfrom(1024)
        # recv_data这个变量存储的是一个元祖（接收到的数据，（发送的ip，port））
        recv_msg = recv_data[0]  # 存储接收到的数据
        recv_addr = recv_data[1]  # 存储发送方的地址

        # 打印接收到的数据
        # print(recv_data)
        # print('%s:%s' % (str(recv_addr), recv_msg.decode('utf-8')))  # windos默认gbk
        print('%s:%s' % (str(recv_addr), recv_msg.decode('utf-8')))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
```

* 发送消息

```python
import socket


def main():
    # 创建一个udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    while True:
        # 从键盘获取数据
        send_data = input('请输入要发送的数据：')

        # 如果舒服的数据是exit，那么退出程序
        if send_data == 'exit':
            break

        # 可以使用套接字收发数据
        udp_socket.sendto(send_data.encode('utf-8'), ('', 7788))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
```

* 聊天案例

```python
import socket

def send_msg(udp_socket):
    """ 发送消息 """
    dest_ip = input('请输入对方的ip：')
    dest_port = int(input('请输入对方的port：'))
    send_data = input('请输入要发送的消息：')
    udp_socket.sendto(send_data.encode('utf-8'), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """ 接收消息 """
    recv_data = udp_socket.recvfrom(1024)
    print('%s:%s' % (str(recv_data[1]), recv_data[0].decode('utf-8')))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(('', 7788))

    # 循环进行处理事情
    while True:
        print('---------聊天器-------')
        print('1:发送消息')
        print('2:接收消息')
        print('0:退出系统')
        op = input('请输入功能：')

        if op == '1':
            # 发送
            send_msg(udp_socket)
        elif op == '2':
            # 接收并显示
            recv_msg(udp_socket)
        elif op == '0':
            break
        else:
            print('输入有误请重新输入')


if __name__ == '__main__':
    main()
```

___
> 共同学习，共同进步