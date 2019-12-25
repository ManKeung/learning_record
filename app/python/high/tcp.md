# 网络通信TCP

TCP协议，传输控制协议（英语：Transmission Control Protocol，缩写为 TCP）是一种面向连接的、可靠的、基于字节流的传输层通信协议，由IETF的RFC 793定义。

TCP通信需要经过创建连接、数据传送、终止连接三个步骤。

## 特点

* 面向连接
通信双方必须先建立连接才能进行数据的传输，双方都必须为该连接分配必要的系统内核资源，以管理连接的状态和连接上的传输。

双方间的数据传输都可以通过这一个连接进行。

完成数据交换后，双方必须断开此连接，以释放系统资源。

这种连接是一对一的，因此TCP不适用于广播的应用程序，基于广播的应用程序请使用UDP协议。

*  可靠传输
1）TCP采用发送应答机制

TCP发送的每个报文段都必须得到接收方的应答才认为这个TCP报文段传输成功

2）超时重传

发送端发出一个报文段之后就启动定时器，如果在定时时间内没有收到应答就重新发送这个报文段。

TCP为了保证不发生丢包，就给每个包一个序号，同时序号也保证了传送到接收端实体的包的按序接收。然后接收端实体对已成功收到的包发回一个相应的确认（ACK）；如果发送端实体在合理的往返时延（RTT）内未收到确认，那么对应的数据包就被假设为已丢失将会被进行重传。

3）错误校验

TCP用一个校验和函数来检验数据是否有错误；在发送和接收时都要计算校验和。

4) 流量控制和阻塞管理

流量控制用来避免主机发送得过快而使接收方来不及完全收下。

* TCP与UDP的不同点

面向连接（确认有创建三方交握，连接已创建才作传输。）
有序数据传输
重发丢失的数据包
舍弃重复的数据包
无差错的数据传输
阻塞/流量控制

* tcp注意点

1. tcp服务器一般情况下都需要绑定，否则客户端找不到这个服务器
2. tcp客户端一般不绑定，因为是主动链接服务器，所以只要确定好服务器的ip、port等信息就好，本地客户端可以随机
3. tcp服务器中通过listen可以将socket创建出来的主动套接字变为被动的，这是做tcp服务器时必须要做的
4. 当客户端需要链接服务器时，就需要使用connect进行链接，udp是不需要链接的而是直接发送，但是tcp必须先链接，只有链接成功才能通信
5. 当一个tcp客户端连接服务器时，服务器端会有1个新的套接字，这个套接字用来标记这个客户端，单独为这个客户端服务
6. listen后的套接字是被动套接字，用来接收新的客户端的链接请求的，而accept返回的新套接字是标记这个新客户端的
6. 关闭listen后的套接字意味着被动套接字关闭了，会导致新的客户端不能够链接服务器，但是之前已经链接成功的客户端正常通信。
7. 关闭accept返回的套接字意味着这个客户端已经服务完毕
8. 当客户端的套接字调用close后，服务器端会recv解堵塞，并且返回的长度为0，因此服务器可以通过返回数据的长度来区别客户端是否已经下线

* tcp的3次握手,tcp的4次挥手

## tcp长连接和短连接

TCP在真正的读写操作之前，server与client之间必须建立一个连接，当读写操作完成后，双方不再需要这个连接时它们可以释放这个连接，连接的建立通过三次握手，释放则需要四次握手，所以说每个连接的建立都是需要资源消耗和时间消耗的。

* TCP短连接

模拟一种TCP短连接的情况:

1. client 向 server 发起连接请求
2. server 接到请求，双方建立连接
3. client 向 server 发送消息
4. server 回应 client
5. 一次读写完成，此时双方任何一个都可以发起 close 操作

在步骤5中，一般都是 client 先发起 close 操作。当然也不排除有特殊的情况。

从上面的描述看，短连接一般只会在 client/server 间传递一次读写操作！

* TCP长连接

再模拟一种长连接的情况:

1. client 向 server 发起连接
2. server 接到请求，双方建立连接
3. client 向 server 发送消息
4. server 回应 client
5. 一次读写完成，连接不关闭
6. 后续读写操作...
7. 长时间操作之后client发起关闭请求

* TCP长/短连接操作过程

> 短连接的操作步骤是：建立连接——数据传输——关闭连接...建立连接——数据传输——关闭连接

> 长连接的操作步骤是：建立连接——数据传输...（保持连接）...数据传输——关闭连接

* TCP长/短连接的优点和缺点

长连接可以省去较多的TCP建立和关闭的操作，减少浪费，节约时间。

对于频繁请求资源的客户来说，较适用长连接。

client与server之间的连接如果一直不关闭的话，会存在一个问题，

随着客户端连接越来越多，server早晚有扛不住的时候，这时候server端需要采取一些策略，

如关闭一些长时间没有读写事件发生的连接，这样可以避免一些恶意连接导致server端服务受损；

如果条件再允许就可以以客户端机器为颗粒度，限制每个客户端的最大长连接数，

这样可以完全避免某个蛋疼的客户端连累后端服务。

短连接对于服务器来说管理较为简单，存在的连接都是有用的连接，不需要额外的控制手段。
但如果客户请求频繁，将在TCP的建立和关闭操作上浪费时间和带宽。

* TCP长/短连接的应用场景

长连接多用于操作频繁，点对点的通讯，而且连接数不能太多情况。每个TCP连接都需要三次握手，这需要时间，如果每个操作都是先连接，再操作的话那么处理速度会降低很多，所以每个操作完后都不断开，再次处理时直接发送数据包就OK了，不用建立TCP连接。例如：数据库的连接用长连接，如果用短连接频繁的通信会造成socket错误，而且频繁的socket 创建也是对资源的浪费。

而像WEB网站的http服务一般都用短链接，因为长连接对于服务端来说会耗费一定的资源，而像WEB网站这么频繁的成千上万甚至上亿客户端的连接用短连接会更省一些资源，如果用长连接，而且同时有成千上万的用户，如果每个用户都占用一个连接的话，那可想而知吧。所以并发量大，但每个用户无需频繁操作情况下需用短连好。

## 代码

* 客服端

```python
import socket

def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接服务器
    server_ip = input('请输入要链接的服务器的ip:')
    server_port = int(input('请输入要连接的服务器的port:'))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    # 发送/接收数据
    send_data = input('请输入发送的数据:')
    tcp_socket.send(send_data.encode('utf-8'))

    # 关闭套接字


if __name__ == '__main__':
    main()
```

* 服务端

```python
import socket


def main():
    # 买个手机（创建套接字）
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 插个手机卡（绑定本地信息）
    tcp_sever_socket.bind(('', 7890))

    # 手机设置正常响铃模式（默认的套接字有主动变被动 listen）
    tcp_sever_socket.listen(128)

    print('------1--------')
    # 等待别人的电话到来（等待客服端连接 accept）
    new_client_socket, client_addr = tcp_sever_socket.accept()
    print('------2--------')
    print(client_addr)

    # 接收客服端发送过来的请求
    recv_data = new_client_socket.recv(1024)
    print(recv_data.decode('utf-8'))

    # 回送一部分数据给客服端
    # new_client_socket.send('haha'.encode('utf-8'))
    new_client_socket.send('你哈啊'.encode('utf-8'))

    # 关闭套接字
    new_client_socket.close()
    tcp_sever_socket.close()


if __name__ == '__main__':
    main()
```

* 文件下载客服端

```python
import socket


def main():
    # 创建套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 获取服务器的ip port
    dest_ip = input('请输入下载服务器的ip：')
    dest_port = int(input('请输入下载服务器的port：'))

    # 连接服务器
    tcp_socket.connect((dest_ip, dest_port))

    # 获取下载的文件名字
    download_file_name = input('请输入要下载的文件名：')

    # 将文件名字发送到服务器
    tcp_socket.send(download_file_name.encode('utf-8'))

    # 接收文件中的数据
    recv_data = tcp_socket.recv(1024)  # 1024 ---> 1k 1024 * 1024 ---> 1mb

    if recv_data:
        # 保存接收到的数据到一个文件中
        with open('[新]' + download_file_name, 'wb') as f:
            f.write(recv_data)

    # 关闭套接字
    tcp_socket.close()


if __name__ == '__main__':
    main()
```

* 文件下载服务端

```python
import socket


def send_file_2_client(new_client_socket, client_addr):
    """ 发送文件给客户端 """
    # 接收客服端发送过来的 要下载的文件名
    file_name = new_client_socket.recv(1024).decode('utf-8')
    print('客服端(%s)需要下载的文件是：%s' % (str(client_addr), file_name))

    file_content = None
    # 打开文件，读取数据
    try:
        f = open(file_name, 'rb')
        file_content = f.read()
        f.close()
    except Exception as ret:
        print('没有要下载的文件（%s）' % file_name)

    # 发送文件数据给客户端
    if file_content:
        # new_client_socket.send('你哈啊'.encode('utf-8'))
        new_client_socket.send(file_content)


def main():
    # 买个手机（创建套接字）
    tcp_sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 插个手机卡（绑定本地信息）
    tcp_sever_socket.bind(('', 7890))

    # 手机设置正常响铃模式（默认的套接字有主动变被动 listen）
    tcp_sever_socket.listen(128)

    while True:
        # 等待别人的电话到来（等待客服端连接 accept）
        new_client_socket, client_addr = tcp_sever_socket.accept()

        # 调用发送文件函数，完成客户端服务
        send_file_2_client(new_client_socket, client_addr)

        # 关闭套接字
        new_client_socket.close()

    tcp_sever_socket.close()


if __name__ == '__main__':
    main()
```

___
> 共同学习，共同进步