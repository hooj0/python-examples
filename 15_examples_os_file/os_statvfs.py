#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.statvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息。
    
语法
    statvfs()方法语法格式如下：
    os.statvfs([path])
    
参数
    path -- 文件路径。
    
返回值

    返回的结构:
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
'''

# 文件系统的信息
st = os.statvfs('/tmp/foo.txt')

print('st info: %s' % st)

print('f_namemax: %s' % st.f_namemax)
print('f_ffree: %s' % st.f_ffree)