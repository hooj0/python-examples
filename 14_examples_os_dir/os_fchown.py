#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 12:51:44
# @copyright by hoojo@2018
# @changelog Added python3 `os dir->os fchown` example


import os

'''
概述
    os.fchown() 方法用于修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
    Unix上可用。

语法
    fchown()方法语法格式如下：
    os.fchown(fd, uid, gid)

参数
    fd -- 文件描述符
    uid -- 文件所有者的用户id
    gid -- 文件所有者的用户组id

返回值
            该方法没有返回值
'''

# 打开文件
fd = os.open('/tmp/dir', os.O_RDONLY)

# 设置文件的用户id = 100
os.fchown(fd, 100, -1)

os.fchown(fd, -1, 50)

# cat /etc/group 查看权限，当前用户为1000
os.fchown(fd, 1000, 1000)

os.close(fd)

print('所有权修改完成')