#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 22:44:01
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> lchown` example


import os

'''
概述
    os.lchown() 方法用于更改文件所有者，类似 chown，但是不追踪链接。
        只支持在 Unix 下使用。

语法
    lchown()方法语法格式如下：
    os.lchown(path, uid, gid)
    
参数
    path -- 设置权限的文件路径
    uid -- 所属用户 ID
    gid -- 所属用户组 ID
    
返回值
        该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)
print('状态：%s' % os.fstat(fd))

os.lchown('/tmp/foo.txt', 100, -1)
print('状态：%s' % os.fstat(fd))

os.lchown('/tmp/foo.txt', 1000, 1000)
print('状态：%s' % os.fstat(fd))

os.close(fd)