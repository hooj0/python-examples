#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-10 22:12:10
# @copyright by hoojo@2018
# @changelog Added python3 `socket->socket client` example


import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080

client.connect((host, port))

print('开始接受消息')

while True:
    
    message = client.recv(1024)
    if message:
        print(message.decode('utf-8'))

client.close()

print('关闭链接')