# http协议

* 基本

```python
import socket

def service_client(new_socket):
    """ 为客服端返回数据 """

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024)
    print(request)

    # 2. 返回http格式的数据，给浏览器
    # 2.1 准备发送给浏览器的数据---header
    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    # 2.2 准备发送给浏览器的数据---boy
    # response += 'hahahhah'
    # new_socket.send(response.encode("utf-8"))

    f = open('./html/index.html', 'rb')
    html_content = f.read()
    f.close()

    # 将response header发送给浏览器
    new_socket.send(response.encode('utf-8'))
    # 将response body发送给浏览器
    new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```

* 根据用户请求返回页面

```python
import socket
import re

def service_client(new_socket):
    """ 为客服端返回数据 """

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()

    print('>'*50)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])

    if ret:
        file_name = ret.group(1)
        print('请求的文件:%s' % file_name)
        if file_name == '/':
            file_name = '/index.html'

    # 2. 返回http格式的数据，给浏览器
    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '------file not found-----'
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        # 2.2 准备发送给浏览器的数据---boy
        # response += "hahahhah"

        # 将response header发送给浏览器
        new_socket.send(response.encode('utf-8'))
        # 将response body发送给浏览器
        new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        service_client(new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```

* 使用多进程

```python
import socket
import re
import multiprocessing

def service_client(new_socket):
    """ 为客服端返回数据 """

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()

    print('>'*50)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])

    if ret:
        file_name = ret.group(1)
        print('请求的文件:%s' % file_name)
        if file_name == '/':
            file_name = '/index.html'

    # 2. 返回http格式的数据，给浏览器
    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '------file not found-----'
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        # 2.2 准备发送给浏览器的数据---boy
        # response += "hahahhah"

        # 将response header发送给浏览器
        new_socket.send(response.encode('utf-8'))
        # 将response body发送给浏览器
        new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        p = multiprocessing.Process(target=service_client, args=(new_socket,))
        p.start()

        new_socket.close()

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```

* 使用多线程

```python
import socket
import re
import threading

def service_client(new_socket):
    """ 为客服端返回数据 """

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()

    print('>'*50)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])

    if ret:
        file_name = ret.group(1)
        print('请求的文件:%s' % file_name)
        if file_name == '/':
            file_name = '/index.html'

    # 2. 返回http格式的数据，给浏览器
    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '------file not found-----'
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        # 2.2 准备发送给浏览器的数据---boy
        # response += "hahahhah"

        # 将response header发送给浏览器
        new_socket.send(response.encode('utf-8'))
        # 将response body发送给浏览器
        new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        t = threading.Thread(target=service_client, args=(new_socket,))
        t.start()

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```

* 使用协程

```python
import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()

def service_client(new_socket):
    """ 为客服端返回数据 """

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    request = new_socket.recv(1024).decode('utf-8')
    # print(request)
    request_lines = request.splitlines()

    print('>'*50)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])

    if ret:
        file_name = ret.group(1)
        print('请求的文件:%s' % file_name)
        if file_name == '/':
            file_name = '/index.html'

    # 2. 返回http格式的数据，给浏览器
    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '------file not found-----'
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1 准备发送给浏览器的数据---header
        response = 'HTTP/1.1 200 OK\r\n'
        response += '\r\n'
        # 2.2 准备发送给浏览器的数据---boy
        # response += "hahahhah"

        # 将response header发送给浏览器
        new_socket.send(response.encode('utf-8'))
        # 将response body发送给浏览器
        new_socket.send(html_content)

    # 关闭套接字
    new_socket.close()


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当服务器先close 即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时 可以立即绑定7890端口
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    while True:
        # 4. 等待新客户端的链接
        new_socket, client_addr = tcp_server_socket.accept()

        # 5. 为这个客户端服务
        gevent.spawn(service_client, new_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```

* 非阻塞

```python
import socket
import time

tcp_server_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_server_tcp.bind(('', 7890))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)  # 设置套接字为非堵塞的方式

client_socket_list = list()

while True:

    # time.sleep(0.5)

    try:
        new_socket, new_addr = tcp_server_tcp.accept()
    except Exception as ret:
        print('---没有新的客户端到来---')
    else:
        print('---只要没有产生异常，那么也就意味着 来了一个新的客户端----')
        new_socket.setblocking(False)  # 设置套接字为非堵塞的方式
        client_socket_list.append(new_socket)

    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024)
        except Exception as ret:
            print(ret)
            print('----这个客户端没有发送过来数据----')
        else:
            print('-----没有异常-----')
            print(recv_data)
            if recv_data:
                # 对方发送过来数据
                print('----客户端发送过来了数据-----')
            else:
                # 对方调用close 导致了 recv返回
                client_socket.close()
                client_socket_list.remove(client_socket)
                print('---客户端已经关闭----')
```

* 非阻塞长链接

```python
import socket
import re


def service_client(new_socket, request):
    """为这个客户端返回数据"""

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    # request = new_socket.recv(1024).decode('utf-8')
    # print('>>>'*50)
    # print(request)

    request_lines = request.splitlines()
    print('')
    print('>'*20)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print('*'*50, file_name)
        if file_name == '/':
            file_name = '/index.html'

    # 2. 返回http格式的数据，给浏览器

    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '------file not found-----'
        new_socket.send(response.encode('utf-8'))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Length:%d\r\n' % len(response_body)
        response_header += '\r\n'

        response = response_header.encode('utf-8') + response_body

        new_socket.send(response)


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    client_socket_list = list()
    while True:
        # 4. 等待新客户端的链接
        try:
            new_socket, client_addr = tcp_server_socket.accept()
        except Exception as ret:
            pass
        else:
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode('utf-8')
            except Exception as ret:
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```

* epoll

```python
import socket
import re
import select  # epoll window下没有


def service_client(new_socket, request):
    """为这个客户端返回数据"""

    # 1. 接收浏览器发送过来的请求 ，即http请求
    # GET / HTTP/1.1
    # .....
    # request = new_socket.recv(1024).decode('utf-8')
    # print('>>>'*50)
    # print(request)

    request_lines = request.splitlines()
    print('')
    print('>'*20)
    print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put del
    file_name = ''
    ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
    if ret:
        file_name = ret.group(1)
        # print('*'*50, file_name)
        if file_name == '/':
            file_name = '/index.html'

    # 2. 返回http格式的数据，给浏览器

    try:
        f = open('./html' + file_name, 'rb')
    except:
        response = 'HTTP/1.1 404 NOT FOUND\r\n'
        response += '\r\n'
        response += '------file not found-----'
        new_socket.send(response.encode('utf-8'))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = 'HTTP/1.1 200 OK\r\n'
        response_header += 'Content-Length:%d\r\n' % len(response_body)
        response_header += '\r\n'

        response = response_header.encode('utf-8') + response_body

        new_socket.send(response)


def main():
    """用来完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2. 绑定
    tcp_server_socket.bind(('', 7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()

    while True:

        fd_event_list = epl.poll()  # 默认会堵塞，直到 os监测到数据到来 通过事件通知方式 告诉这个程序，此时才会解堵塞

        # [(fd, event), (套接字对应的文件描述符, 这个文件描述符到底是什么事件 例如 可以调用recv接收等)]
        for fd, event in fd_event_list:
            # 等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
```
___
> 共同学习，共同进步