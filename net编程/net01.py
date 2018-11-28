import socket

# 模拟服务器函数


def severFunc():
    # 建立socket

    # socket.AF_INET:使用ipv4协议族
    # socket.SOCK_DGRAM:使用UDP通信
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    addr = ("127.0.0.1", 7852)
    # 绑定ip和port
    sock.bind(addr)

    data, addr = sock.recvfrom(500)
    print(data)
    print(type(data))

    text = data.decode()
    print(text)
    print(type(text))

    # 给对方发送消息

    rsp = "Respond to you!"

    data = rsp.encode()
    sock.sendto(data, addr)


if __name__ == '__main__':
    print("Sever starting now.......")
    severFunc()
    print("Sever ending here........")
