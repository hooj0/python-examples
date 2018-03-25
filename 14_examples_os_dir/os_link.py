#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 22:57:50
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> link` example


import os

'''
概述
   os.link() 方法用于创建硬链接，名为参数 dst，指向参数 src。
        该方法对于创建一个已存在文件的拷贝是非常有用的。
        只支持在 Unix, Windows 下使用。

语法
    link()方法语法格式如下：
    os.link(src, dst)

参数
    src -- 用于创建硬连接的源地址
    dst -- 用于创建硬连接的目标地址

返回值
        该方法没有返回值
'''

# 创建快捷方式链接
#os.link('/tmp/mydir', '/tmp/dir/tmp_my_dir')

os.link('/tmp/foo.txt', '/tmp/dir/foo.txt')