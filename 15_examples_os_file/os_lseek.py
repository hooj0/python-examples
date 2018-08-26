#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 23:12:08
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os lseek` example


import os

'''
概述
    os.lseek() 方法用于设置文件描述符 fd 当前位置为 pos, how 方式修改。
            在Unix，Windows中有效。
            
语法
    lseek()方法语法格式如下：
    os.lseek(fd, pos, how)

参数
    fd -- 文件描述符。
    pos -- 这是相对于给定的参数 how 在文件中的位置。。
    how -- 文件内参考位置。SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始。

返回值
    该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

os.write(fd, '写入seek文本')

# 所有 fsync() 方法
os.fsync(fd)

print('读取内容：%s' % os.read(fd, 100))

# 移动到文件行首
os.lseek(fd, 0, 0)
print('读取内容：%s' % os.read(fd, 100))

# 移动到文件末尾
os.lseek(fd, 0, 1)
print('读取内容：%s' % os.read(fd, 100))