#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 22:54:04
# @copyright by hoojo@2018
# @changelog Added python3 `os file -> ftruncate` example


import os

'''
概述
    os.ftruncate() 裁剪文件描述符fd对应的文件, 它最大不能超过文件大小。
    Unix上可用。

语法
    ftruncate()方法语法格式如下：
    os.ftruncate(fd, length)¶

参数
    fd -- 文件的描述符。
    length -- 要裁剪文件大小。

返回值
        该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR)

# 写入内容
os.write(fd, '新生代文本内容')

# 截取文件内容
os.ftruncate(fd, 20)

# 移动文件指针
os.lseek(fd, 0, 0)
print('读取文件内容：%s' % os.read(fd, 100))

os.close(fd)