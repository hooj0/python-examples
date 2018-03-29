#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-29 22:49:01
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> mkdir` example


import os

'''
概述
    os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
    
语法
    mkdir()方法语法格式如下：
    os.mkdir(path[, mode])
    
参数
    path -- 要创建的目录
    mode -- 要为目录设置的权限数字模式
    
返回值
            该方法没有返回值。
'''

# 创建文件夹，不能递归创建
os.mkdir('/tmp/m', 0x777)

# 递归创建文件夹
os.makedirs('/tmp/mm/nn', 0x755)

print('创建文件夹完成')