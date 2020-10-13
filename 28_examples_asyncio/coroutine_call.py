#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> task call` example


# ===============================================================================
# 标题：python3 asyncio task call example
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
# 描述：在asyncio事件循环中调用非协程回调函数
#   call_soon：队列中等待到下一个事件循环时会立即执行
#   call_later：根据延时调用的时间确定执行的顺序
#   call_at：在指定的时间运行回调函数  这个时间是loop里面的单调时间(loop.time())
# -------------------------------------------------------------------------------
import asyncio
import time


# -------------------------------------------------------------------------------
# 非协程对象
# -------------------------------------------------------------------------------
def callback(sleep_times, func_name, loop):
    print("{0} time {1} loop_time {2}".format(func_name, sleep_times, loop.time()))


loop = asyncio.get_event_loop()

loop.call_later(3, callback, 3, "call_later", loop)
loop.call_later(2, callback, 2, "call_later", loop)
loop.call_at(loop.time(), callback, 4, "call_at", loop)
loop.call_soon(callback, 5, "call_soon", loop)

loop.call_soon_threadsafe(callback, 2, "call_soon_threadsafe", loop)

loop.run_forever()


# output:
# ---------------------------------------------------------------------------
# 在这个事件循环中，call_soon、call_soon_threadsafe最先执行，
# 接着call_at指定的时间是loop当前时间，call_at执行，随后是call_later根据延时的时间大小执行。
# ---------------------------------------------------------------------------
# call_soon time 5 loop_time 11602572.582
# call_soon_threadsafe time 2 loop_time 11602572.582
# call_at time 4 loop_time 11602572.582
# call_later time 2 loop_time 11602574.579
# call_later time 3 loop_time 11602575.577
