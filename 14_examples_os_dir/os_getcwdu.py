#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 11:26:42
# @copyright by hoojo@2018
# @changelog Added python3 `os dir->os getcwdu` example


import os

'''
概述
    os.getcwdu() 方法用于返回一个当前工作目录的Unicode对象。
    Unix, Windows 系统下可用。

语法
    getcwdu()方法语法格式如下：
    os.getcwdu()

参数
            无
            
返回值
        返回一个当前工作目录的Unicode对象
'''

# 切换工作目录
os.chdir('/var/tmp/')

print('当前工作目录：', os.getcwdu())

# 打开文件夹
fd = os.open('/home', os.O_RDONLY)

# 切换工作目录
os.fchdir(fd)

print(u'当前工作目录：', os.getcwdu())

os.close(fd)