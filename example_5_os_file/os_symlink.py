#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.symlink() 方法用于创建一个软链接。
    
语法
    symlink()方法语法格式如下：
    os.symlink(src, dst)
    
参数
    src -- 源地址。
    dst -- 目标地址。
    
返回值
        该方法没有返回值
'''

# 创建软连接
os.symlink('/home/jojo', '/tmp/my_dir')

print('创建软连接完成')