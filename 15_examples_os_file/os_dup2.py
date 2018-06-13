#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.dup2() 方法用于将一个文件描述符 fd 复制到另一个 fd2。
    Unix, Windows 上可用。

语法
    dup2()方法语法格式如下：
    os.dup2(fd, fd2);
    
参数
    fd -- 要被复制的文件描述符
    fd2 -- 复制的文件描述符

返回值
    没有返回值
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 写入文件
os.write(fd, 'this is new line')

# 复制文件
fd2 = 1000
os.dup2(fd, fd2)

# 移动文件指针
os.lseek(fd2, 0, 0)
print('读取文件内容：%s' % os.read(fd2, 100))

# 关闭文件
os.close(fd)
#os.closerange(fd, fd2)
print('操作完成')