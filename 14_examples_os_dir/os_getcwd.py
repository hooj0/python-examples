#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 11:05:02
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> getcwd` example


import os

'''
概述
    os.getcwd() 方法用于返回当前工作目录。
    
语法
    getcwd()方法语法格式如下：
    os.getcwd()
参数
        无
        
返回值
        返回当前进程的工作目录。
'''

# 切换目录
os.chdir('/var/tmp')

# 当前工作目录
print('当前工作目录: %s' % os.getcwd())

# 打开文件夹，文件夹不能用 os.O_RDWR
fd = os.open('/tmp', os.O_RDONLY) 

# 切换工作目录，fd 必须为文件夹
os.fchdir(fd)

print('当前工作目录: %s' % os.getcwd())

os.close(fd)