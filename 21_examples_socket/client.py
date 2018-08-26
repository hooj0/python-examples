#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-10 22:57:34
# @copyright by hoojo@2018
# @changelog Added python3 `socket->client` example


# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 和指定地址、端口的服务器建立链接
s.connect((HOST, PORT))

# 向服务器发送信息
s.send(b'Hello, world')

# 接受服务器消息
data = s.recv(1024)
s.close()

print('Received', repr(data))