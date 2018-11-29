import socket

def tcp_func():
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    addr = ("127.0.0.1",8998)
    sock.bind(addr)

    sock.listen()

    skt,addr = sock.accept()
    msg = skt.recv(500)

    msg.decode()

    rst = "receive message: {} from {}".format(msg,addr)
    print(rst)

    skt.send(rst.encode())

    skt.close()


if __name__ == '__main__':
    print("Starting tcp sever......")
    tcp_func()
    print("Ending tcp sever........")
