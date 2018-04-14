#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os

'''
概述
    os.isatty() 方法用于判断如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

语法
    isatty()方法语法格式如下：
    os.isatty()
    
参数
        无

返回值
        如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
'''


# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 判断文件与设备相连
print('判断文件与设备相连: %s' % os.isatty(fd))

os.close(fd)