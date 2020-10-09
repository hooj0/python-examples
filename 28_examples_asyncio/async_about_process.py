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
import time
import multiprocessing


# -------------------------------------------------------------------------------
# 多进程版本
# -------------------------------------------------------------------------------
def a():
    for x in range(3):
        print(x)


def b():
    for x in "abc":
        print(x)


if __name__=="__main__":
    multiprocessing.Process(target=a, name="p-a").start()
    multiprocessing.Process(target=b, name="p-b").start()
# output:
# ---------------------------------------------------------------------------
# 0
# 1
# 2
# a
# b
# c