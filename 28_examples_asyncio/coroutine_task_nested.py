#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> task coroutine nested chain` example


# ===============================================================================
# 标题：python3 asyncio task coroutine nested chain example
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
# 描述：嵌套调用，在协程中调用其他协程
# -------------------------------------------------------------------------------
import asyncio
import time


# -------------------------------------------------------------------------------
# 原始协程，被async可被视为一个协程对象
# -------------------------------------------------------------------------------
async def sum(x, y):

    data = await compute(x, y)
    print("{0} + {1} = {2}".format(x, y, data))

    return "now time %s" % time.time()


# 回调函数，参数必须是future
async def compute(x, y):
    print("compute {0} + {1}".format(x, y))
    await asyncio.sleep(1)
    return x + y


loop = asyncio.get_event_loop()
# 传入 协程 对象，构建任务对象
# Task类是Future的子类，它的作用就是把协程包装成一个Future对象
task = loop.create_task(sum(2, 3))

# 传入 任务对象，到事件循环中可直接运行
result = loop.run_until_complete(task)
print("result: ", result)
print("result: ", task.result())


# output:
# ---------------------------------------------------------------------------
# compute 2 + 3
# 2 + 3 = 5
# result:  now time 1602575378.9483352
# result:  now time 1602575378.9483352