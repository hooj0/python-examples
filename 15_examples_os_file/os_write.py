#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 17:42:04
# @copyright by hoojo@2018
# @changelog Added python3 `os file->os write` example


import os


'''
概述
    os.write() 方法用于写入字符串到文件描述符 fd 中. 返回实际写入的字符串长度。
            在Unix中有效。

语法
    write()方法语法格式如下：
    os.write(fd, str)

参数
    fd -- 文件描述符。
    str -- 写入的字符串。

返回值
        该方法返回写入的实际位数
'''


# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR|os.O_CREAT)

# 写入字符串
str = "new content"
ret = os.write(fd, str)

# 输入返回值
print ("写入的位数为: ")
print (ret)

print ("写入成功")

# 关闭文件
os.close(fd)
print ("关闭文件成功!!")