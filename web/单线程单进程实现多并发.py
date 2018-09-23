import socket
import time

tcp_server_tcp = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
tcp_server_tcp.bind(("",7890))
tcp_server_tcp.listen(128)
tcp_server_tcp.setblocking(False)  # 设置套接字为非堵塞方式

client_socket_list = list()

while True: 
 
    try:
        new_socket, new_addr = tcp_server_tcp.accept()
    except Exception as ret:
        print("没有新的客户端到来")
    else:
        print("来了一个客户端")
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

    # 遍历 socket 列表处理
    for client_socket in client_socket_list:
        try:
            recv_data = client_socket.recv(1024) 
        except Exception as ret:
            print("客户端没发送数据")
        else:
            print("无异常")
            print(recv_data)
            if recv_data:
                # 对方发送了数据
                print("----客户端发送来了数据")
            else:
                # 对方调用了 close 导致了 recv 返回
                client_socket.close()
                client_socket_list.remove(client_socket)
                print("---客户端已关闭")
    