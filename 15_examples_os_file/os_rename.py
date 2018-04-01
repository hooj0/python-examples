#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 11:56:59
# @copyright by hoojo@2018
# @changelog Added python3 `os file -> rename` example


import os


'''
概述
    os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

语法
    rename()方法语法格式如下：
    os.rename(src, dst)

参数
    src -- 要修改的目录名
    dst -- 修改后的目录名

返回值
        该方法没有返回值
'''


# os.chroot("/tmp")
os.chdir("/tmp")

# 列出目录
print ("目录为: %s" % os.listdir(os.getcwd()))

os.rename('open2.txt', '123.txt')
os.rename('ppf', '123')