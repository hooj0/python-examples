#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 09:46:45
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os read` example


import os

'''
概述
    os.read() 方法用于从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
            在Unix，Windows中有效

语法
    read()方法语法格式如下：
    os.read(fd,n)

参数
    fd -- 文件描述符。
    n -- 读取的字节。

返回值
        返回包含读取字节的字符串
'''



# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR|os.O_CREAT)

# 读取内容
print('read: %s' % os.read(fd, 100))

os.close(fd)