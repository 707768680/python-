import socket
 
def send_file_to_client(new_client_socket,client_addr):
    # 1. 接收需要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)要下载的文件是: %s " %  (str(client_addr),file_name))
    # 2. 打开文件 读取数据  with 语法适用于写文件的操作(文件一定能打开),读文件用 with 可能出错
    file_content = None
    try:
        f = open(file_name,"rb")
        file_content =f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件(%s)" % file_name)
    # 3. 发送文件的数据给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
     # 1.创建套接字  socket
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
     # 2.绑定本地信息  bind
    tcp_server_socket.bind(("",6789))
     # 3.让套接字由主动变被动  listen
    tcp_server_socket.listen(128)
    while True:
        # 4.等待客户端的链接(阻塞模式) 返回一个元祖 1-新的套接字用来服务 accept

        new_client_socket,client_addr = tcp_server_socket.accept()

        # 调用发送文件函数
        send_file_to_client(new_client_socket,client_addr)

        # 关闭套接字
        new_client_socket.close()
    tcp_server_socket.close()

if __name__ == "__main__":
    main()
        