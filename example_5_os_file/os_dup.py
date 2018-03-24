#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os

'''
概述
    os.dup() 方法用于复制文件内容 fd。
    
语法
    dup()方法语法格式如下：
    os.dup(fd);
    
参数
    fd -- 文件内容
    
返回值
        返回复制的文件内容。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 复制文件内容
dup_fd = os.dup(fd)

# 写入新文本
os.write(dup_fd, 'write new text')

# 关闭文件fd、dup_fd
os.closerange(fd, dup_fd)

print('操作完成')