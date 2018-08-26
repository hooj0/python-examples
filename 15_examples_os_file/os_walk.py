#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 17:21:55
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os walk` example


import os


'''
概述
    os.walk() 方法用于通过在目录树种游走输出在目录中的文件名，向上或者向下。
            在Unix，Windows中有效。
    
语法
    walk()方法语法格式如下：
    os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
    
参数
    top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
    topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
    onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
    followlinks -- 设置为 true，则通过软链接访问目录。
    
返回值
        该方法没有返回值
'''


for root, dirs, files in os.walk("/tmp", topdown=False):
    for name in files:
        print('files: %s' % os.path.join(root, name))
    for name in dirs:
        print('dirs: %s' % os.path.join(root, name))