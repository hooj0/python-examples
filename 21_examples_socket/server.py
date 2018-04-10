#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-10 22:54:41
# @copyright by hoojo@2018
# @changelog Added python3 `socket -> server` example


# Echo server program
import socket

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

# 建立socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
s.bind((HOST, PORT))
# 最大建立一个监听
s.listen(1)

# 客户端链接
conn, addr = s.accept()
print('Connected by', addr)

while True:
    #客户端 发送的信息
    data = conn.recv(1024)
    if not data: break
    
    print('客户端消息：', repr(data))
    # 向客户端发送信息
    conn.send(data)
conn.close()