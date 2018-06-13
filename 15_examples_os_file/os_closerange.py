#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo


'''
概述
    os.closerange() 方法用于关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。

语法
    closerange()方法语法格式如下：
    os.closerange(fd_low, fd_high);

参数
    fd_low -- 最小文件描述符
    fd_high -- 最大文件描述符

该方法类似于：
    for fd in xrange(fd_low, fd_high):
        try:
            os.close(fd)
        except OSError:
            pass
            
返回值
        该方法没有返回值
'''

import os

# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR|os.O_CREAT)

# 写入字符串
os.write(fd, "This is test2")

# 关闭文件
os.closerange(fd, fd)

print("关闭文件成功!!")