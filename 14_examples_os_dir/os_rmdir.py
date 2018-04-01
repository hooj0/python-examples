#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 12:37:44
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> rmdir` example


import os


'''
概述
    os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。

语法
    rmdir()方法语法格式如下：
    os.rmdir(path)

参数
    path -- 要删除的目录路径

返回值
        该方法没有返回值
'''

# 切换工作目录
os.chdir('/tmp')

# 文件列表
print('file list: %s' % os.listdir(os.getcwd()))
      
# 该目录不能包含文件或文件夹      
os.rmdir('ppf2')      

print('file list: %s' % os.listdir(os.getcwd()))