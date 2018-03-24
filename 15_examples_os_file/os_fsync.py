#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 21:59:20
# @copyright by hoojo@2018
# @changelog Added python3 `os file -> fsync` example


import os

'''
概述
    os.fsync() 方法强制将文件描述符为fd的文件写入硬盘。在Unix, 将调用fsync()函数;在Windows, 调用 _commit()函数。
    如果你准备操作一个Python文件对象f, 首先f.flush(),然后os.fsync(f.fileno()), 确保与f相关的所有内存都写入了硬盘.在unix，Windows中有效。
    Unix、Windows上可用。
    
语法
    fsync()方法语法格式如下：
    os.fsync(fd)

参数
    fd -- 文件的描述符。
    
返回值
            该方法没有返回值。
'''

# 打开读取文件
fd = os.open('/tmp/foo.txt', os.O_RDWR)

# 写入内容
os.write(fd, '写入内容试试看')

# 同步文件内容到物理硬盘
os.fsync(fd)

# 移动文件指针到最前面
os.lseek(fd, 0, 0)
print('读取文件内容：%s' % os.read(fd, 100))

os.close(fd)