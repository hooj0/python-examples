#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os

'''
概述
    os.makedev() 方法用于以major和minor设备号组成一个原始设备号。

语法
    makedev()方法语法格式如下：
    os.makedev(major, minor)

参数
    major -- Major 设备号。
    minor -- inor 设备号。

返回值
        返回设备号。
'''



info = os.lstat('/tmp/foo.txt')

print('stat info: %s' % info)

print('major 设备号: %s' % os.major(info.st_dev))
print('minor 设备号: %s' % os.minor(info.st_dev))

print('makedev 设备号: %s' % os.makedev(os.major(info.st_dev), os.minor(info.st_dev)))
