#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo

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