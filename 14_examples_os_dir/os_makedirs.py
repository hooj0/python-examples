#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.makedirs() 方法用于递归创建目录。像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。

语法
    makedirs()方法语法格式如下：
    os.makedirs(path, mode=0o777)

参数
    path -- 需要递归创建的目录。
    mode -- 权限模式。

返回值
        该方法没有返回值。
'''

# 递归创建文件夹
os.makedirs('/tmp/da/db', 0x755)

print('创建文件夹')