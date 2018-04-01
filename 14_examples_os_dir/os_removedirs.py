#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 10:52:17
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> removedirs` example


import os

'''
概述
    os.removedirs() 方法用于递归删除目录。像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。

语法
    removedirs()方法语法格式如下：
    os.removedirs(path)

参数
    path -- 要移除的目录路径

返回值
        该方法没有返回值
'''

# 列出目录
print ("目录为: %s" % os.listdir('/tmp'))

# 递归删除目录
os.removedirs('/tmp/da/db')
os.removedirs('/tmp/m')

print ("目录为: %s" % os.listdir('/tmp'))