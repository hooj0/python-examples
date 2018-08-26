#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-29 22:54:37
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os mkfifo` example


import os

'''
概述
    os.mkfifo() 方法用于创建指令路径的管道，并设置权限模式。默认的模式为 0666 (八进制)。

语法
    mkfifo()方法语法格式如下：
    os.mkfifo(path[, mode])

参数
    path -- 要创建的目录
    mode -- 要为目录设置的权限数字模式

返回值
        该方法没有返回值。
'''

# 创建文件
os.mkfifo('/tmp/ab3.txt', 0x777)

os.mkfifo('/tmp/abe', 0x777)

print('创建完成')