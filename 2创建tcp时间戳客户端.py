#!/usr/bin/env python

from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)

tcpclisock = socket(AF_INET,SOCK_STREAM)
tcpclisock.connect(ADDR)#主动连接服务器

while True:#循环，有条件退出
    data = input('>> ')
    if not data:
        print('发送为空，退出服务器连接')
        break
    tcpclisock.send(bytes(data, 'utf-8'))
    data = tcpclisock.recv(BUFSIZ)
    if not data:
        print('接收为空，退出服务器连接')
        break
    print(data.decode('utf-8'))
tcpclisock.close()
