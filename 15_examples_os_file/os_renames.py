#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 12:27:00
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os renames` example


import os


'''
概述
    os.renames() 方法用于递归重命名目录或文件。类似rename()。

语法
    renames()方法语法格式如下：
    os.renames(old, new)

参数
    old -- 要重命名的目录
    new --文件或目录的新名字。甚至可以是包含在目录中的文件，或者完整的目录树。

返回值
        该方法没有返回值
'''

os.chdir('/tmp')

os.renames('123', '456/abc')

os.renames('123.txt', '456/abc.txt')