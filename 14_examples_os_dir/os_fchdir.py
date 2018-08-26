#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 10:39:27
# @copyright by hoojo@2018
# @changelog Added python3 `os dir->os fchdir` example


import os

'''
概述
    os.fchdir() 方法通过文件描述符改变当前工作目录。
    Unix, Windows 上可用。
    
语法
    fchdir()方法语法格式如下：
    os.fchdir(fd);

参数
    fd -- 文件描述符

返回值
        该方法没有返回值。
'''

# 切换到目录
os.chdir('/var/tmp')

print('当前目录位置：%s' % os.getcwd())

# 打开文件目录
fd = os.open('/tmp', os.O_RDONLY)

# fchdir 修改目录，必须是文件夹fd
os.fchdir(fd)

print('当前目录位置：%s' % os.getcwd())

os.close(fd)


