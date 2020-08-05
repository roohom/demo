import socket


def tcp_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    addr = ("127.0.0.1", 8998)
    sock.bind(addr)

    sock.listen()

    skt, addr = sock.accept()
    msg = skt.recv(500)

    msg.decode()

    rst = "receive message: {} from {}".format(msg, addr)
    #print(rst)

    skt.send(rst.encode("utf-8"))
    skt.close()


if __name__ == '__main__':
    print("Starting tcp sever......")
    tcp_server()
    print("Ending tcp sever........")
