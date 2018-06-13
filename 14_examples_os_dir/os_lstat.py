#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os

'''
概述
    os.lstat() 方法用于类似 stat() 返回文件的信息,但是没有符号链接。在某些平台上，这是fstat的别名，例如 Windows。

语法
    lstat()方法语法格式如下：
    os.lstat(path)

参数
    path -- 要返回信息的文件。

返回值
        返回文件信息。
'''

print('stat：%s' % os.lstat('/tmp/foo.txt'))

print('stat：%s' % os.lstat('/tmp/'))