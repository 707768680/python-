# import socket
# import re
# import gevent
# from gevent import monkey
# import select

# monkey.patch_all()

# def service_client(new_socket, request):
#     """为这个客户端返回数据"""

#     # 1.接收浏览器发送过来的请求, 即 http 请求
#     # GET / HTTP/1.1
#     # 。。。
#     # request = new_socket.recv(1024).decode("utf-8")

#     request_lines = request.splitlines()
#     file_name = ""
#     ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
#     if ret:
#         file_name = ret.group(1)
#         print(file_name)
#         if file_name == "/":
#             file_name = "/index.html"

#     # 2.返回 http 格式的数据给浏览器
#     # header
#     try:
#         f = open("./html" + file_name, "rb")
#     except:
#         response = "HTTP/1.1 404 NOT FOUND\r\n" 
#         response += "\r\n"
#         response += "------file not found------"
#         new_socket.send(response.encode("utf-8"))
#     else:
#         html_content = f.read()
#         f.close()
        
#         response_body = html_content
#         response_header = "HTTP/1.1 200 OK\r\n"
#         response_header += "Content-Length:%d\r\n" % len(response_body)
#         response_header += "\r\n"
        
#         response = response_header.encode("utf-8") + response_body
#         new_socket.send(response)

#     # 关闭套接字--长链接不关闭
#     # new_socket.close()

# def main():
#     """完成整体的控制"""
#     # 1. 创建套接字
#     tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # 设置当服务器先 close 即服务端 4 次挥手之后 资源能立即释放,这样就保证了下次运行可以立即使用
#     tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

#     # 2. 绑定
#     tcp_server_socket.bind(("",7890))

#     # 3. 变为监听套接字
#     tcp_server_socket.listen(128)
#     # 设置为非堵塞
#     tcp_server_socket.setblocking(False)
#     client_socket_list = list()

#     # 创建一个 epoll 对象
#     epl = select.epoll()

#     # 将监听套接字对应的 fd 注册到 epoll 中
#     epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

#     fd_event_dict = dict()
#     # 4. 等待客户端的连接
#     while True:
       
#         fd_event_list = epl.poll()  # 默认会阻塞 知道 os 检测到数据到来,以事件通知的方式告诉程序解堵塞         
#         # [(fd,event)]   (套接字对应的文件描述符,事件例如 recv)
#         for fd, event in fd_event_list:
#             if fd == tcp_server_socket.fileno():
#                 new_socket,client_addr = tcp_server_socket.accept()
#                 epl.register(new_socket,select.EPOLLIN)
#                 fd_event_dict[new_socket.fileno()] = new_socket
#             elif event == select.EPOLLIN:
#                 recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
#                 if recv_data:
#                     service_client(fd_event_dict[fd],recv_data)
#                 else:
#                     fd_event_dict[fd].close()
#                     epl.unregister(fd)
#                     del fd_event_dict[fd]

#     tcp_server_socket.close()


# if __name__ == "__main__":
#     main()