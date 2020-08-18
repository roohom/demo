#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 21:07
# @Author  : Roohom
# @Site    : TcpClient客户端
# @File    : TcpClient.py
# @Software: PyCharm


from socket import *

host = "127.0.0.1"
port = 8999
addr = (host, port)

Socket_TCP = socket()
Socket_TCP.connect(addr)

while True:
    data = input("请输入发送给服务端的消息:")
    data = bytes(data, encoding="utf-8")
    Socket_TCP.send(data)

    print(str(Socket_TCP.recv(1024), encoding="utf-8"))
    if data == "exit":
        break

Socket_TCP.close()
