#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.tempnam() 方法用于返回唯一的路径名用于创建临时文件。

语法
    tempnam()方法语法格式如下：
    os.tempnam(dir, prefix)

参数
    dir -- 要创建的临时文件路径。
    prefix -- 临时文件前缀

返回值
        该方法返回唯一路径。
'''

# 生成某个文件夹下的带指定前缀的唯一路径
tmp = os.tempnam('/tmp/aiay', 'data')
print('tmp: %s' % tmp)

