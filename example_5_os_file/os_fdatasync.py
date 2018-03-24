#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.fdatasync() 方法用于强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。如果你需要刷新缓冲区可以使用该方法。
    Unix上可用。

语法
    fdatasync()方法语法格式如下：
    os.fdatasync(fd);

参数
    fd -- 文件描述符

返回值
        该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 写入文件内容
os.write(fd, '新的内容写入')

# 同步文件到硬盘，防止文件内容丢失
os.fdatasync(fd)

# 移动文件指针
os.lseek(fd, 0, 0)

# 读取文件内容
str = os.read(fd, 100)
print('读到内容：%s' % str)

os.close(fd)
