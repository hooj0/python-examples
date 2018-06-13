#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo


import threading
from threading import Timer

data = threading.local()
data.x = 109

def hello():
    print("hello, world")


# 定时3秒后运行
t = Timer(3.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed