#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.tmpnam() 方法用于为创建一个临时文件返回一个唯一的路径。

语法
    tmpnam()方法语法格式如下：
    os.tmpnam

参数
        无

返回值
        返回一个唯一的路径
'''


# 生成临时路径
tmp = os.tmpnam()

print('临时唯一路径：%s' % tmp)