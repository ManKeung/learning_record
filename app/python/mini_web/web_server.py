import socket
import re
import multiprocessing
# import dynamic.mini_frame
import sys


class WSGIServer(object):
    def __init__(self, port, app, static_path):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.tcp_server_socket.bind(('', 7890))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

        self.application = app
        self.static_path = static_path

    def service_client(self, new_socket):
        """ 微客户端返回数据 """

        # 1. 接收浏览器发送过来的请求 ，即http请求
        # GET / HTTP/1.1
        # .....
        request = new_socket.recv(1024).decode('utf-8')

        request_lines = request.splitlines()

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
        # 2.1 如果请求的资源不是.py结尾，那么就认为是静态资源
        if not file_name.endswith('.html'):
            try:
                f = open(self.static_path + file_name, 'rb')
            except:
                response = 'HTTP/1.1 404 NOT FOUND\r\n'
                response += '\r\n'
                response += '------file not found-----'
                new_socket.send(response.encode('utf-8'))
            else:
                html_content = f.read()
                f.close()
                # 2.1 准备发送给浏览器的数据---header
                response = 'HTTP/1.1 200 OK\r\n'
                response += '\r\n'
                # 2.2 准备发送给浏览器的数据---boy
                # response += 'hahahhah'

                # 将response header发送给浏览器
                new_socket.send(response.encode('utf-8'))
                # 将response body发送给浏览器
                new_socket.send(html_content)
        else:
            # 2.2 如果是以.py结尾，那么就认为是动态资源请求
            env = dict()
            env['PATH_INFO'] = file_name
            # body = dynamic.mini_frame.application(env, self.set_response_header)
            body = self.application(env, self.set_response_header)

            header = 'HTTP/1.1 %s \r\n' % self.status
            for temp in self.headers:
                header += '%s:%s\r\n' % (temp[0], temp[1])

            header += '\r\n'

            response = header + body
            # 发送response给浏览器
            new_socket.send(response.encode('utf-8'))

        # 关闭套接
        new_socket.close()

    def set_response_header(self, status, headers):
        self.status = status
        self.headers = [('server', 'min_web v8.8')]
        self.headers += headers

    def run_forever(self):
        """用来完成整体的控制"""
        while True:
            # 4. 等待新客户端的链接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()

        # 关闭监听套接字
        self.tcp_server_socket.close()


def main():
    """ 控制整体，创建一个web 服务器对象，然后调用对象的run_forever方法运行 """
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = (sys.argv[2])
        except Exception as ret:
            print('端口输入错误...')
            return
    else:
        print('请按照以下方式运行：')
        print('python xxx.py 7890 mini_frame:application')
        return

    ret = re.match(r'([^:]+):(.*)', frame_app_name)

    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
    else:
        print('请按照以下方式运行：')
        print('python web_server.py 7890 mini_frame:application')
        return

    with open('./web_server.conf') as f:
        conf_info = eval(f.read())

    sys.path.append(conf_info['dynamic_path'])

    frame = __import__(frame_name)  # 返回值标记着 导入的模块
    # 此时app就指向了 dynamic/mini_frame模块中的application函数
    app = getattr(frame, app_name)

    wsgi_server = WSGIServer(port, app, conf_info['static_path'])
    wsgi_server.run_forever()


if __name__ == '__main__':
    main()
