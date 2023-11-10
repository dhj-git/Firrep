#!/usr/bin/env python
#UNIX启动行
from socket import *
from time import ctime

HOST = '' #空白表示可以使用任何可用的地址
PORT = 21567 #随机未被使用和系统保留的端口
BUFSIZ = 1024 #该应用缓冲区大小设置为1kb，根据网络性能和程序改变这个容量
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET,SOCK_STREAM)#分配TCP服务器套接字，什么是套接字就是另一个问题
#AF_INET(IPV4)因特网协议--AF_INET6(IPV6)
tcpSerSock.bind(ADDR) #将套接字绑定到服务器地址和端口
tcpSerSock.listen(5) #监听，参数表示在连接被转接或拒绝之前，传入连接请求的最大数

while True:#无限循环被动等待连接
    print("等待连接......")
    tcpCliSock ,addr = tcpSerSock.accept()
    print("连接来自: ",addr)

    while True:  #连接请求进入对话循环
        data = tcpCliSock.recv(BUFSIZ) #得到数据
        if not data: #空数据，客户端已退出，退出对话循环
            break
        # tcpCliSock.send('[%s] %s'%(byte(ctime(),'utf-8'),data))
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8')) #向客户端发送时间戳数据，必须发送字节数组
        #得到数据，格式化返回相同数据和当前时间戳的前缀
    tcpCliSock.close() #关闭当前客户连接，等待另一个客户连接
tcpSerSocket.close() #不会执行，用于提醒读者退出程序要用close()