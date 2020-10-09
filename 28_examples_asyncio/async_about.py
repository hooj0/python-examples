#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> all` example


# ===============================================================================
# 标题：python3 asyncio await example
# ===============================================================================
# 使用：关于asyncio的一些示例演示，说明asyncio存在的意义
# -------------------------------------------------------------------------------
# 描述：用一些示例演示程序、线程、协程
# -------------------------------------------------------------------------------
import threading
import time


# -------------------------------------------------------------------------------
# 这是一个串行的程序，是一个单线程
# -------------------------------------------------------------------------------
def serial_program():

    def a():
        for x in range(3):
            print(x)

    def b():
        for x in "abc":
            print(x)

    a()
    b()


print("----------------------------------serial_program----------------------------------")
serial_program()
# output:
# ---------------------------------------------------------------------------
# 0
# 1
# 2
# a
# b
# c


# -------------------------------------------------------------------------------
# 多线程版本
# -------------------------------------------------------------------------------
def thread_program():

    def a():
        for x in range(3):
            print(x)

    def b():
        for x in "abc":
            print(x)

    threading.Thread(target=a, name="thread-a").start()
    threading.Thread(target=b, name="thread-b").start()


print("---------------------------------thread_program-----------------------------------")
thread_program()
time.sleep(1)
# output:
# ---------------------------------------------------------------------------
# 0
# 1
# a
# 2
# b
# c


# -------------------------------------------------------------------------------
# 生成器
# -------------------------------------------------------------------------------
def generator():
    def a():
        for x in range(3):
            print(x)
            yield

    def b():
        for x in "abc":
            print(x)
            yield

    foo = a()
    bar = b()
    for _ in range(3):
        next(foo)
        next(bar)


print("---------------------------------generator-----------------------------------")
generator()
# output:
# ---------------------------------------------------------------------------
# 0
# a
# 1
# b
# 2
# c