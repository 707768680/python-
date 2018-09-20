import socket

def main():
    # 创建一个 udp 套接字
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    # 获取对方的 ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))

    # 从键盘获取数据
    send_data = input("请输入要发送的数据:")

    #可以使用套接字收发数据
    udp_socket.sendto(send_data.encode("utf-8"),(dest_ip,dest_port))

    # 接收送回来的数据
    recv_data = udp_socket.recvfrom(1024)
    #套接字可以同时收发数据

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
