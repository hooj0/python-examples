#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.utime() 方法用于设置指定路径文件最后的修改和访问时间。
            在Unix，Windows中有效。

语法
    utime()方法语法格式如下：
    os.utime(path, times)

参数
    path -- 文件路径
    times -- 如果时间是 None, 则文件的访问和修改设为当前时间 。 否则, 时间是一个 2-tuple数字, (atime, mtime) 用来分别作为访问和修改的时间。

返回值
        该方法没有返回值
'''

info = os.stat('/tmp/foo.txt')

print('info: %s' % info)

print('st_ctime: %s' % info.st_ctime)
print('st_mtime: %s' % info.st_mtime)

os.utime('/tmp/foo.txt', (1522073000, 1522073000))

info = os.stat('/tmp/foo.txt')
print('st_ctime: %s' % info.st_ctime)
print('st_mtime: %s' % info.st_mtime)