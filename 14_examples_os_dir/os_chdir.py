#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 12:28:28
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> chdir` example


import os


'''
概述
    os.chdir() 方法用于改变当前工作目录到指定的路径。

语法
    chdir()方法语法格式如下：
    os.chdir(path)

参数
    path -- 要切换到的新路径。

返回值
        如果允许访问返回 True , 否则返回False。
'''

print('当前目录位置：%s' % os.getcwd())

# 切换到目录
os.chdir('/var/tmp')

print('当前目录位置：%s' % os.getcwd())