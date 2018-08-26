#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 17:18:57
# @copyright by hoojo@2018
# @changelog Added python3 `os dir-> os lchmod` example


import os

'''
概述
    os.lchmod() 方法用于修改连接文件权限。
        只支持在 Unix 下使用。
    
语法
    lchmod()方法语法格式如下：
    os.lchmod(path, mode)

参数
    path -- 设置标记的文件路径
    mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：
    stat.S_ISUID:设置 UID 位
    stat.S_ISGID: 设置组 ID 位
    stat.S_ENFMT: 系统文件锁定的执法行动
    stat.S_ISVTX: 在执行之后保存文字和图片
    
    stat.S_IREAD: 对于拥有者读的权限
    stat.S_IWRITE: 对于拥有者写的权限
    stat.S_IEXEC: 对于拥有者执行的权限
    
    stat.S_IRWXU:对于拥有者读、写、执行的权限
    stat.S_IRUSR: 对于拥有者读的权限
    stat.S_IWUSR: 对于拥有者写的权限
    stat.S_IXUSR: 对于拥有者执行的权限
    
    stat.S_IRWXG: 对于同组的人读写执行的权限
    stat.S_IRGRP: 对于同组读的权限
    stat.S_IWGRP:对于同组写的权限
    stat.S_IXGRP: 对于同组执行的权限
    
    stat.S_IRWXO: 对于其他组读写执行的权限
    stat.S_IROTH: 对于其他组读的权限
    stat.S_IWOTH: 对于其他组写的权限
    stat.S_IXOTH:对于其他组执行的权限

返回值
        该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

os.close(fd)

os.lchmod(fd, stat.S_IEXEC)

print('权限修改完成！')