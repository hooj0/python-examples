#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 09:58:14
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os remove` example


import os


'''
概述
    os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。
            在Unix, Windows中有效

语法
    remove()方法语法格式如下：
    os.remove(path)

参数
    path -- 要移除的文件路径

返回值
        该方法没有返回值
'''

# 删除文件，不能删除文件夹
os.remove('/tmp/ab')
os.remove('/tmp/ab.txt')

os.remove('/tmp/ab3.txt')
os.remove('/tmp/abe')