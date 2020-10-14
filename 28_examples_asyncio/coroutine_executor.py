#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> task run_in_executor` example


# ===============================================================================
# 标题：python3 asyncio task run_in_executor example
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
# 描述：使用多线程在协程中集成阻塞IO
# -------------------------------------------------------------------------------
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


# -------------------------------------------------------------------------------
# 非协程对象
# -------------------------------------------------------------------------------
def do_work(sleep_times):
    # 休眠的时间会改变任务完成顺序
    time.sleep(sleep_times)
    print("work {} success".format(sleep_times))


loop = asyncio.get_event_loop()
# 线程池的大小会影响任务执行速度
executor = ThreadPoolExecutor(10)

# run_in_executor：将阻塞函数放到executor(线程池)中运行
# loop.run_in_executor 是 async 协程方法，通过它包装构建非协程对象
tasks = [loop.run_in_executor(executor, do_work, i) for i in range(1, 6)]

# 等待task执行完成
loop.run_until_complete(asyncio.wait(tasks))
# loop.run_until_complete(asyncio.gather(*tasks))


# output:
# ---------------------------------------------------------------------------
# 在这个事件循环中，call_soon、call_soon_threadsafe最先执行，
# 接着call_at指定的时间是loop当前时间，call_at执行，随后是call_later根据延时的时间大小执行。
# ---------------------------------------------------------------------------
# work 1 success
# work 2 success
# work 3 success
# work 4 success
# work 5 success
