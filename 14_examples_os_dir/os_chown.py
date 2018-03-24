#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 09:26:13
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> chown` example


import os

'''
语法
  chown()方法语法格式如下：
        os.chown(path, uid, gid);
        
参数
    path -- 设置权限的文件路径
    uid -- 所属用户 ID
    gid -- 所属用户组 ID
'''

# 假定 /tmp/foo.txt 文件存在.
# 设置所有者 ID 为 1000

#linux 查看用户组
#tail /etc/group 
os.chown("/tmp/open.txt", 1000, -1)