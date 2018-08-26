#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 23:06:40
# @copyright by hoojo@2018
# @changelog Added python3 `os dir->os listdir` example


import os

'''
概述
    os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
    只支持在 Unix, Windows 下使用。

语法
    listdir()方法语法格式如下：
    os.listdir(path)

参数
    path -- 需要列出的目录路径
    
返回值
        返回指定路径下的文件和文件夹列表。
'''

dirs = os.listdir('/var/')

for dir in dirs:
    print('dir: %s' % dir)
    
    
print('-----------------------------')    
dirs = os.listdir('/tmp/')

for dir in dirs:
    print('dir: %s' % dir)