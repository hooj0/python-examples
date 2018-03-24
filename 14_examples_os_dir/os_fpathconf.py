#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-24 16:35:06
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> fpathconf` example


import os

'''
概述
    os.fpathconf() 方法用于返回一个打开的文件的系统配置信息。
    Unix上可用。

语法
    fpathconf()方法语法格式如下：
    os.fpathconf(fd, name)
    
参数
    fd -- 打开的文件的描述符。
    name -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
    bufsize -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，传递一个数字作为名字，也是可以接受的。

返回值
        返回一个打开的文件的系统配置信息
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 配置名称列表
print('配置名称列表: %s' % os.pathconf_names)

print('文件最大连接数：%d' % os.fpathconf(fd, 'PC_LINK_MAX'))

print('文件名最大长度：%d' % os.fpathconf(fd, 'PC_NAME_MAX'))

os.close(fd)