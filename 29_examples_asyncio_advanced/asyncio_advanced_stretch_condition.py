#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> condition` example


# ===============================================================================
# 标题：python3 asyncio advanced condition example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio.Condition() 对事件状态单独通知执行
# -------------------------------------------------------------------------------
import asyncio
import functools


# -------------------------------------------------------------------------------
# 对事件状态单独通知执行
# -------------------------------------------------------------------------------
async def consumer(condition, i):
    print("[consumer] start")

    async with condition:
        print("[consumer] waiting ", i)
        await condition.wait()
        print("[consumer] trigger ", i)

    print("[consumer] finished")


async def publisher_notify(condition):
    print("[publisher_notify] start")

    await asyncio.sleep(0.1)
    for i in range(3):
        async with condition:
            print("[publisher_notify] notify consumer ", i)
            condition.notify(i)

    async with condition:
        print("[publisher_notify] notify other consumer")
        condition.notify_all()

    print("[publisher_notify] finished")


async def call_work():
    print("[call_work] run...")

    # 创建一个操作状态的对象
    condition = asyncio.Condition()
    # 5个消费者函数
    consumers = [consumer(condition, i) for i in range(5)]
    # 创建一个发布通知的任务
    loop.create_task(publisher_notify(condition))

    print("[call_work] wait consumers run")
    # 等待consumers所有的函数执行完成
    await asyncio.wait(consumers)

    print("[call_work] run finished")


loop = asyncio.get_event_loop()

try:
    print("going event loop")
    loop.run_until_complete(call_work())
finally:
    print("close event loop")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# going event loop
# [call_work] run...
# [call_work] wait consumers run
#
# 运行发布者，发送通知
# [publisher_notify] start
#
# 消费者开始运行，等待接收通知
# [consumer] start
# [consumer] waiting  2
# [consumer] start
# [consumer] waiting  3
# [consumer] start
# [consumer] waiting  4
# [consumer] start
# [consumer] waiting  1
# [consumer] start
# [consumer] waiting  0
#
# 发布者 通知消各个费者
# [publisher_notify] notify consumer  0
# [publisher_notify] notify consumer  1
# [publisher_notify] notify consumer  2
# [publisher_notify] notify other consumer
# [publisher_notify] finished
#
# 接收到通知，消费者运行 等待的后续业务
# [consumer] trigger  2
# [consumer] finished
# [consumer] trigger  3
# [consumer] finished
# [consumer] trigger  4
# [consumer] finished
# [consumer] trigger  1
# [consumer] finished
# [consumer] trigger  0
# [consumer] finished
# [call_work] run finished
# close event loop
