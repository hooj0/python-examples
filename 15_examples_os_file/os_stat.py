#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 12:50:28
# @copyright by hoojo@2018
# @changelog Added python3 `os file -> stat` example


import os


'''
概述
    os.stat() 方法用于在给定的路径上执行一个系统 stat 的调用。

语法
    stat()方法语法格式如下：
    os.stat(path)

参数
    path -- 指定路径

返回值
    stat 结构:
    st_mode: inode 保护模式
    st_ino: inode 节点号。
    st_dev: inode 驻留的设备。
    st_nlink: inode 的链接数。
    st_uid: 所有者的用户ID。
    st_gid: 所有者的组ID。
    st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
    st_atime: 上次访问的时间。
    st_mtime: 最后一次修改的时间。
    st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
'''

st = os.stat('/tmp/foo.txt')

print('stat: %s' % st)

print('st_size: %s' % st.st_size)
print('st_mode: %s' % st.st_mode)
print('st_ctime: %s' % st.st_ctime)