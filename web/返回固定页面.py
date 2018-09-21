import socket


def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1.接收浏览器发送过来的请求, 即 http 请求
    # GET / HTTP/1.1
    # 。。。
    request = new_socket.recv(1024)
    print(request)

    # 2.返回 http 格式的数据给浏览器
    # header
    response = "HTTP/1.1 200 OK\r\n" 
    response += "\r\n"
    # body
    response += "hahahhahaha"

    new_socket.send(response.encode("utf-8"))

    # 关闭套接字
    new_socket.close()

def main():
    """完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置当服务器先 close 即服务端 4 次挥手之后 资源能立即释放,这样就保证了下次运行可以立即使用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)

    # 2. 绑定
    tcp_server_socket.bind(("",7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    # 4. 等待客户端的连接
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        service_client(new_socket)

    tcp_server_socket.close()


if __name__ == "__main__":
    main()