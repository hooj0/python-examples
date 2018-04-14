#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.ttyname() 方法用于返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

语法
    ttyname()方法语法格式如下：
    os.ttyname(fd)

参数
    fd -- 文件描述符

返回值
        返回一个字符串，它表示与文件描述符fd 关联的终端设备
'''


fd = os.open('/dev/tty', os.O_RDONLY)

print('ttyname: %s' % os.ttyname(fd))

os.close(fd)