#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-29 23:00:44
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os mknod` example


import os
import stat

'''
概述
    os.mknod() 方法用于创建一个指定文件名的文件系统节点（文件，设备特别文件或者命名pipe）。

语法
    mknod()方法语法格式如下：
    os.mknod(filename[, mode=0600[, device=0]])

参数
    filename -- 创建的文件系统节点
    mode -- mode指定创建或使用节点的权限, 组合 (或者bitwise) stat.S_IFREG, stat.S_IFCHR, stat.S_IFBLK, 和stat.S_IFIFO (这些常数在stat模块). 对于 stat.S_IFCHR和stat.S_IFBLK, 设备定义了 最新创建的设备特殊文件 (可能使用 os.makedev()),其它都将忽略。
    device -- 可选，指定创建文件的设备

返回值
        该方法没有返回值
'''

# 创建文件，无后缀
os.mknod('/tmp/dir/abcd', 0x600|stat.S_IFCHR)

# 创建文件
os.mknod('/tmp/dir/zz.txt', 0x600|stat.S_IFCHR)

