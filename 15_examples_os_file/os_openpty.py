#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-31 15:47:44
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os openpty` example


import os


'''
概述
    os.openpty() 方法用于打开一个新的伪终端对。返回 pty 和 tty的文件描述符。

语法
    openpty()方法语法格式如下：
    os.openpty()

参数
        无

返回值
        返回文件描述符对，主从。
'''

# 打开终端
pty, tty = os.openpty()

print('pty: %s' % pty)
print('tty: %s' % tty)

print('ttyname: %s' % os.ttyname(pty))