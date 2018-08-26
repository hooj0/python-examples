#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-26 22:22:27
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os major` example


import os

'''
概述
    os.major() 方法用于从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。

语法
    major()方法语法格式如下：
    os.major(device)

参数
    device -- 原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
    
返回值
        返回设备major号码
'''


info = os.lstat('/tmp/foo.txt')

print('stat info: %s' % info)

print('major 设备号: %s' % os.major(info.st_dev))
print('minor 设备号: %s' % os.minor(info.st_dev))