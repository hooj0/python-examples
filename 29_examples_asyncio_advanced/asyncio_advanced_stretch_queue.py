#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> queue` example


# ===============================================================================
# 标题：python3 asyncio advanced queue example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：协程队列Queue,生产者与消费者的示例
# -------------------------------------------------------------------------------
import asyncio
import functools


# -------------------------------------------------------------------------------
# 协程队列Queue
# -------------------------------------------------------------------------------
async def consumer(i, queue):
    print("[consumer-%s] start " % i)

    while True:
        print("[consumer-%s] waiting " % i)

        item = await queue.get()
        print("[consumer-%s] get queue: %s" % (i, item))

        queue.task_done()
        if item is None:
            # queue.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            # queue.task_done()
            print("[consumer-%s] sleep" % i)

    print("[consumer-%s] finished " % i)


async def producer(size, queue):
    print("[producer] start")

    for i in range(3 * size):
        await queue.put(i)
        print("[producer] queue put: ", i)

    print("[producer] queue put None stopped")
    for _ in range(size):
        await queue.put(None)

    print("[producer] queue join clear")
    await queue.join()
    print("[producer] finished")


async def call_work(size):
    print("[call_work] run...")

    # 创建一个队列，最大的长度是 size
    queue = asyncio.Queue(maxsize=size)
    # 创建消费者
    consumers = [loop.create_task(consumer(i, queue)) for i in range(size)]
    # 创建一个生产者的任务
    producers = loop.create_task(producer(size, queue))

    print("[call_work] wait consumers/producers run")
    # 等待consumers, producers 所有的函数执行完成
    await asyncio.wait(consumers + [producers])

    print("[call_work] run finished")


loop = asyncio.get_event_loop()

try:
    print("going event loop")
    loop.run_until_complete(call_work(2))
finally:
    print("close event loop")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# going event loop
# [call_work] run...
# [call_work] wait consumers/producers run
# [consumer] start  0
# [consumer] waiting  0
# [consumer] start  1
# [consumer] waiting  1
# [producer] start
# [producer] queue put:  0
# [producer] queue put:  1
# [consumer] 0 get queue: 0
# [consumer] 1 get queue: 1
# [producer] queue put:  2
# [producer] queue put:  3
# [consumer] waiting  0
# [consumer] 0 get queue: 2
# [producer] queue put:  4
# [consumer] waiting  1
# [consumer] 1 get queue: 3
# [producer] queue put:  5
# [producer] queue put None stopped
# [consumer] waiting  0
# [consumer] 0 get queue: 4
# [consumer] waiting  1
# [consumer] 1 get queue: 5
# [producer] queue join clear
# [consumer] waiting  0
# [consumer] 0 get queue: None
# [consumer] finished  0
# [consumer] waiting  1
# [consumer] 1 get queue: None
# [consumer] finished  1
# [producer] finished
# [call_work] run finished
# close event loop
