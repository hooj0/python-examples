#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo


'''
概述
    os.close() 方法用于关闭指定的文件描述符 fd。
语法
    close()方法语法格式如下：
    os.close(fd);
    
参数
    fd -- 文件描述符。
    
返回值
        该方法没有返回值。
'''

import os, sys

# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR|os.O_CREAT)

#  写入字符串
os.write(fd, "This is test")

# 关闭文件
os.close(fd)

print ("关闭文件成功!!")