import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()

def service_client(new_socket):
    """为这个客户端返回数据"""

    # 1.接收浏览器发送过来的请求, 即 http 请求
    # GET / HTTP/1.1
    # 。。。
    request = new_socket.recv(1024).decode("utf-8")

    request_lines = request.splitlines()
    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
    print(ret.group(1))
    print(request_lines)
    print(request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    # 2.返回 http 格式的数据给浏览器
    # header
    try:
        print("./html" + file_name)
        f = open("./html" + file_name, "rb")
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

def main():
    """完成整体的控制"""
    # 1. 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置当服务器先 close 即服务端 4 次挥手之后 资源能立即释放,这样就保证了下次运行可以立即使用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    # 2. 绑定
    tcp_server_socket.bind(("",7890))

    # 3. 变为监听套接字
    tcp_server_socket.listen(128)

    # 4. 等待客户端的连接
    while True:
        new_socket, client_addr = tcp_server_socket.accept()
        
        # 为这个客户端服务 - 协程
        gevent.spawn(service_client,new_socket)

        # service_client(new_socket)

    tcp_server_socket.close()


if __name__ == "__main__":
    main()