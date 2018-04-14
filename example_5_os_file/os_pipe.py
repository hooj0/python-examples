#!/usr/bin/python3
# encoding: utf-8


'''
概述
    os.pipe() 方法用于创建一个管道, 返回一对文件描述符(r, w) 分别为读和写。

语法
    pipe()方法语法格式如下：
    os.pipe()

参数
    无

返回值
    返回文件描述符对。
'''

import os, sys

print ("The child will write text to a pipe and ")
print ("the parent will read the text written by child...")

# 文件描述符 r, w 用于读、写
r, w = os.pipe() 

# 获取线程id
processid = os.fork()
print('进程类型：%s' % processid)

if processid:
    # 父进程
    # 关闭文件描述符 w
    os.close(w)
    r = os.fdopen(r)
    print ("Parent reading")
    str = r.read()
    print ("text =", str)
    sys.exit(0)
else:
    # 子进程
    os.close(r)
    w = os.fdopen(w, 'w')
    print ("Child writing")
    w.write("Text written by child...")
    w.close()
    print ("Child closing")
    sys.exit(0)