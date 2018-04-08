#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-08 23:07:22
# @copyright by hoojo@2018
# @changelog Added python3 `socket -> socket server` example


import socket
from threading import Timer

'''
socket()函数

Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
    socket.socket([family[, type[, proto]]])
    
参数
    family: 套接字家族可以使AF_UNIX或者AF_INET
    type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
    protocol: 一般不填默认为0.

Socket 对象(内建)方法

                函数                                        描述
    服务器端套接字
    s.bind()        绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
    s.listen()      开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
    s.accept()      被动接受TCP客户端连接,(阻塞式)等待连接的到来
    
    客户端套接字
    s.connect()     主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
    s.connect_ex()  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
    
    公共用途的套接字函数
    s.recv()         接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
    s.send()         发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
    s.sendall()      完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
    s.recvform()     接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
    s.sendto()       发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
    s.close()        关闭套接字
    s.getpeername()    返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
    s.getsockname()    返回套接字自己的地址。通常是一个元组(ipaddr,port)
    s.setsockopt(level, optname, value)    设置给定套接字选项的值。
    s.getsockopt(level, optname[.buflen])    返回套接字选项的值。
    
    s.settimeout(timeout)     设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
    s.gettimeout()            返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
    s.fileno()                返回套接字的文件描述符。
    s.setblocking(flag)       如果flag为0，则将套接字设为非阻塞模式，否则将套接字设为阻塞模式（默认值）。非阻塞模式下，如果调用recv()没有发现任何数据，或send()调用无法立即发送数据，那么将引起socket.error异常。
    s.makefile()              创建一个与该套接字相关连的文件
    
---------------------------------------------------------------------------------------------    
Python Internet 模块

            协议           功能用处        端口号        Python模块
    HTTP    网页访问                80    httplib, urllib, xmlrpclib
    NNTP    阅读和张贴新闻文章，俗称为"帖子"    119    nntplib
    FTP     文件传输                20    ftplib, urllib
    SMTP    发送邮件                25    smtplib
    POP3    接收邮件                110    poplib
    IMAP4   获取邮件                143    imaplib
    Telnet  命令行                       23    telnetlib
    Gopher  信息查找                  70    gopherlib, urllib    
'''

help(socket)

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print(serversocket)

host = 'localhost'
port = 8080

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

# 重复建立链接或发送消息  
while True:  
    
    # 建立客户端连接
    clientsocket, addr = serversocket.accept() 
    print('client: %s' % clientsocket)   
    print("客户端连接地址: %s" % str(addr))
    
    for i in range(5):
        # 发送内容    
        msg = '%s 欢迎访问 ，第%s次发送信息' % (addr[1], str(i))
        clientsocket.send(msg.encode('utf-8'))

    clientsocket.close()
    
print(serversocket.getpeername())
print(serversocket.getsockname())