#!/usr/bin/python3
# encoding: utf-8

import os, sys

print ("The child will write text to a pipe and ")
print ("the parent will read the text written by child...")

# 文件描述符 r, w 用于读、写
r, w = os.pipe() 

processid = os.fork()
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