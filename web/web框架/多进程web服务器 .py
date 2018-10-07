import socket
import re
import multiprocessing


class WSGIServer(object):
    def __init__(self):
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 2. 绑定
        self.tcp_server_socket.bind(("", 7890))

        # 3. 变为监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self, new_socket):
        """为这个客户端返回数据"""

        # 1.接收浏览器发送过来的请求, 即 http 请求
        # GET / HTTP/1.1
        # 。。。
        request = new_socket.recv(1024).decode("utf-8")

        request_lines = request.splitlines()

        ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == "/":
                file_name = "/index.html"

        # 2.返回 http 格式的数据给浏览器
        # header
        try:
            f = open("../html" + file_name, "rb")
        except:
            response = "HTTP/1.1 404 NOT FOUND\r\n" 
            response += "\r\n"
            response += "------file not found------"
            new_socket.send(response.encode("utf-8"))
        else:
            html_content = f.read()
            f.close()
            # header
            response = "HTTP/1.1 200 OK\r\n"
            response += "\r\n"
            # 分两次发送
            new_socket.send(response.encode("utf-8"))
            new_socket.send(html_content)

        # 关闭套接字
        new_socket.close()


    def run_forever(self):
        """用来完成整体的控制"""

        while True:
            # 4. 等待新客户端的连接
            new_socket, client_addr = self.tcp_server_socket.accept()

            # 5. 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()

            new_socket.close()
        
        # 关闭监听套接字
        self.tcp_server_socket.close()

def main():
    """控制整体,创建一个 web 服务器对象, 然后调用 run_forever"""
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()


if __name__ == "__main__":
    main()












