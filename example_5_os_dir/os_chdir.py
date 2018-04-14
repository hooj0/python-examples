#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
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