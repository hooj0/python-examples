#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> event` example


# ===============================================================================
# 标题：python3 asyncio advanced event example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio.Event() 事件的查看与设置
# -------------------------------------------------------------------------------
import asyncio
import functools


# -------------------------------------------------------------------------------
# 事件的查看与设置
# -------------------------------------------------------------------------------
def trigger_event(event):
    print("[trigger_event] event setter")
    event.set()


async def listener_event_1(event):
    print("[listener_event_1] start")
    await event.wait()
    print("[listener_event_1] finished")


async def listener_event_2(event):
    print("[listener_event_2] start")
    await event.wait()
    print("[listener_event_2] finished")


async def call_work():
    print("[call_work] run...")

    event = asyncio.Event()
    print("[call_work] get event status: ", event.is_set())

    # 当事件触发后，listener_event_1、listener_event_2 才能挂起等待结束，运行后续业务
    loop.call_later(0.1, trigger_event, event)
    # loop.call_later(0.1, functools.partial(trigger_event, event))

    print("[call_work] wait event trigger run")
    await asyncio.wait([listener_event_1(event), listener_event_2(event)])

    print("[call_work] all event run finished, event status: ", event.is_set())


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
# [call_work] get event status:  False
# [call_work] wait event trigger run
# event 开始等待触发，后续代码未执行
# [listener_event_1] start
# [listener_event_2] start
#
# 触发后事件后，监听业务开始执行
# [trigger_event] event setter
#
# 执行等待触发事件的后续业务
# [listener_event_1] finished
# [listener_event_2] finished
# [call_work] all event run finished, event status:  True
# close event loop
