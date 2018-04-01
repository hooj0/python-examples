#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 15:18:25
# @copyright by hoojo@2018
# @changelog Added python3 `os file -> tcgetpgrp` example


import os


'''
概述
    os.tcgetpgrp() 方法用于回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组。

语法
    tcgetpgrp()方法语法格式如下：
    os.tcgetpgrp(fd)

参数
    fd -- 文件描述符。

返回值
        该方法返回进程组
'''


fd = os.open("/dev/tty", os.O_RDONLY)

f = os.tcgetpgrp(fd)

print('tcgetpgrp: %s' % f)