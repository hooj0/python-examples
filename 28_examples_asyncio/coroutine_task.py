#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> task coroutine` example


# ===============================================================================
# 标题：python3 asyncio task coroutine example
# ===============================================================================
# 使用：关于asyncio的一些示例演示，说明asyncio存在的意义
#
# 协程不是进程、也不是线程，它是用户空间调度的按成并发处理的方式
# 进程、线程由操作系统完成调度，而协程是线程内完成调度，它不需要更多的线程，自然也没有多线程切换带来的开销
# 协程是非抢占式调度，只有一个协程主动让出控制权，另一个协程才会被调度
# 协程也不需要使用锁机制，因为是在同一个线程中执行
# 多CPU下，可以使用多进程和协程配合，既能进程并发又能发挥协程在单线程中的优势
# Python中协程是基于生成器的
# asyncio.iscoroutine(obj)判断是不是协程对象
# asyncio.iscoroutinefunction(func)判断是不是协程函数
# Future类似，通过Future对象可以了解人物执行的状态数据。事件循环来监控Future对象是否完成。
# Task类是Future的子类，它的作用就是把协程包装成一个Future对象。
# -------------------------------------------------------------------------------
# 描述：用一些示例演示程序、线程、协程
# -------------------------------------------------------------------------------
import asyncio
import time


# -------------------------------------------------------------------------------
# 原始协程，被async可被视为一个协程对象
# -------------------------------------------------------------------------------
async def get_corouting():
    print("run get corouting...")
    await asyncio.sleep(2)

    return "now time %s" % time.time()


loop = asyncio.get_event_loop()
# 传入 协程 对象到事件循环中可直接运行
task = loop.create_task(get_corouting())
result = loop.run_until_complete(task)
print("result: ", result)


# output:
# ---------------------------------------------------------------------------
# run get corouting...
# result:  now time 1602226852.3201892