#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.tmpfile() 方法用于返回一个打开的模式为(w+b)的临时文件对象，这文件对象没有文件夹入口，没有文件描述符，将会自动删除。

语法
    tmpfile()方法语法格式如下：
    os.tmpfile

参数
    无

返回值
        返回一个临时文件对象
'''


# 创建临时文件
tmp = os.tmpfile()

tmp.write('写入临时数据')

tmp.seek(0)
print('read: %s' % tmp.read())

tmp.close()