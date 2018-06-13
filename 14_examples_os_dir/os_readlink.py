#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.readlink() 方法用于返回软链接所指向的文件。可能返回绝对火相对路径。
            在Unix中有效

语法
    readlink()方法语法格式如下：
    os.readlink(path)

参数
    path -- 要查找的软链接路径

返回值
        返回软链接所指向的文件
'''

# 创建软连接
os.symlink('/var/tmp', '/tmp/var_tmp')

lk = os.readlink('/tmp/var_tmp')
print('link: %s' % lk)
