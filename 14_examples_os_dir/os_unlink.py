#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.unlink() 方法用于删除文件,如果文件是一个目录则返回一个错误。

语法
    unlink()方法语法格式如下：
    os.unlink(path)

参数
    path -- 删除的文件路径

返回值
        该方法没有返回值
'''

# 列举目录
print('dirs: %s' % os.listdir('/tmp'))

# 取消软连接
os.unlink('/tmp/my_dir')

print('dirs: %s' % os.listdir('/tmp'))