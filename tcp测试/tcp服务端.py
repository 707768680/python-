import socket
 
 
def main():
     # 1.创建套接字  socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     # 2.绑定本地信息  bind
    tcp_server_socket.bind(("",6789))
     # 3.让套接字由主动变被动  listen
    tcp_server_socket.listen(128)
    while True:
         # 4.等待客户端的链接(阻塞模式) 返回一个元祖 1-新的套接字用来服务 accept
        print("等待客户端链接")
        new_client_socket,client_addr = tcp_server_socket.accept()
        print("链接成功")
        print(client_addr)
        
        while True:
            # 接收客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print(recv_data)
            if recv_data:
                # 回送数据给客户端
                new_client_socket.send("hahaha--ok--".encode("utf-8"))
            else:
                break
        # 关闭套接字
        new_client_socket.close()
        print("已经服务完毕")
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
        