#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 20:11:17
# @copyright by hoojo@2018
# @changelog Added python3 `os dir->os fstatvfs` example


import os


'''
概述
    os.fstatvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息，类似 statvfs()。
    Unix上可用。

fstatvfs 方法返回的结构:
    f_bsize: 文件系统块大小
    f_frsize: 分栈大小
    f_blocks: 文件系统数据块总数
    f_bfree: 可用块数
    f_bavail:非超级用户可获取的块数
    f_files: 文件结点总数
    f_ffree: 可用文件结点数
    f_favail: 非超级用户的可用文件结点数
    f_fsid: 文件系统标识 ID
    f_flag: 挂载标记
    f_namemax: 最大文件长度

语法
    fstatvfs()方法语法格式如下：
    os.fstatvfs(fd)
    
参数
    fd -- 文件的描述符。
    
返回值
        返回包含文件描述符fd的文件的文件系统的信息。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT)

# 获取文件描述
info = os.fstatvfs(fd)

print('文件信息：%s' % info)

print('文件名最大长度：%s' % info.f_namemax)

print('可用的块数：%s' % info.f_bfree)

os.close(fd)