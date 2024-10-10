# -*- coding: utf-8 -*-
"""
双端的通信
客户发送exit，服务端退出
Server
"""
import socket


def start_server(host='127.0.0.1', port=50000):
    # 创建一个socket对象
    # socket.AF_INET表示使用IPv4地址，socket.SOCK_STREAM表示使用TCP协议
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定地址
    # 127.0.0.1表示本地地址，port端口
    server_socket.bind((host, port))

    # 开始监听
    server_socket.listen(2)
    print(f"服务端启动成功，监听地址为{host}:{port}")

    close = False
    try:

        while True:
            # 接受客户端连接
            client_socket, addr = server_socket.accept()
            print(f"addr: {addr} ; client_socket: {client_socket}")

            while True:
                data = client_socket.recv(1024).decode()  # 接收数据
                print(f"客户端发送了: {data}")
                if data == "exit":
                    close = True
                    break
                response = input("回应客户端: ")  # 处理数据
                client_socket.sendall(response.encode())  # 发送响应

            client_socket.close()

    except Exception as e:
        print(e)
    finally:
        if close:
            server_socket.close()