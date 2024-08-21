"""
双端通信，控制台聊天
Client
"""
import socket

def connect_to_server(host='127.0.0.1', port=50000):
    # 创建一个socket对象
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 连接到服务器
    client_socket.connect((host, port))

    try:
        while True:
            # 发送数据
            message = input("发送信息")
            client_socket.sendall(message.encode())
            if message.lower() == 'exit':
                break
            # 接收服务器响应
            response = client_socket.recv(1024).decode()
            print(f"server: {response}")
    except Exception as e:
        print(f"出现错误，连接关闭\nError: {e}")
    finally:
        client_socket.close()
