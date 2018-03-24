#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 13:13:08
# @copyright by hoojo@2018
# @changelog Added python3 `os file -> fdopen` example


import os


'''
概述
    os.fdopen() 方法用于通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。
    Unix, Windows上可用。
    
语法
    fdopen()方法语法格式如下：
    os.fdopen(fd, [, mode[, bufsize]]);
    
参数
    fd -- 打开的文件的描述符，在Unix下，描述符是一个小整数。
    mode -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
    bufsize -- 可选，指定返回的文件对象是否带缓冲：buffersize=0，表示没有带缓冲；bufsize=1，表示该文件对象是行缓冲的；bufsize=正数，表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，对于tty字元设备一般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。
    
返回值
        通过文件描述符返回的文件对象
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR)

# 打开文件fd，获取文件对象; 并且开启写入权限
file = os.fdopen(fd, 'w+')

print('当前位置: %d' % file.tell())

# 写入新内容
file.write('fdopen file write line\n')

# 移动指针
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print('读到文本：%s' % str)

# 当前位置
print('当前位置: %d' % file.tell())

#os.close(fd)


