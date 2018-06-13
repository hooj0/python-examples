#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.pathconf() 方法用于返回一个打开的文件的系统配置信息。
    Unix 平台下可用。
    
语法
    fpathconf()方法语法格式如下：
    os.fpathconf(fd, name)
    
参数
    name -- 文件描述符
    name -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，传递一个数字作为名字，也是可以接受的。

返回值
        返回文件的系统信息。
'''
import os

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR|os.O_CREAT)

print('pathconf_names: %s' % os.pathconf_names)

# 最大连接数
print('最大连接数：%s' % os.fpathconf(fd, 'PC_LINK_MAX'))

os.close(fd)