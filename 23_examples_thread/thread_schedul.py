#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-18 22:49:55
# @copyright by hoojo@2018
# @changelog Added python3 `thread -> thread schedul` example


import threading
from threading import Timer

data = threading.local()
data.x = 109

def hello():
    print("hello, world")


# 定时3秒后运行
t = Timer(3.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed