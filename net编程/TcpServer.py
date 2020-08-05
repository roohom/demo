#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 20:59
# @Author  : Roohom
# @Site    : TcpServer服务端
# @File    : TcpServer.py
# @Software: PyCharm
import socket

host = "127.0.0.1"
port = 8998
addr = (host, port)
# 创建套接字
Sock_TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 服务端绑定本地址
Sock_TCP.bind(addr)

Sock_TCP.listen(10)
conn, addr = Sock_TCP.accept()

while True:
    data = conn.recv(1024)
    data = str(data, encoding="utf-8")
    print("收到来自", addr, "发来的消息,内容为:", data)

    conn.send(bytes("服务端收到了你的消息\n", encoding="utf-8"))

    if data == "exit":
        conn.send(bytes("exit",encoding="utf-8"))
        break

conn.close()

