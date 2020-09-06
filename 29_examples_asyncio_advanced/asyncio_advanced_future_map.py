#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> future process map` example


# ===============================================================================
# 标题：python3 asyncio advanced future process map example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio.ensure_future() 函数，直到await才运行
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 运行线路图
# -------------------------------------------------------------------------------
async def result():
    print("[result] get result...")
    return "hello"


async def inner_call(task):
    print("[inner_call] run...")
    print("[inner_call] task: ", task)  # pending
    # 获取task返回值，此时 task 协程需要挂起，待运行完成，并直到返回结果
    data = await task   # result 运行
    print("[inner_call] task: ", task)  # finished

    print("[inner_call] task result: ", data)


async def outer_call():
    print("[outer_call] create [result] task")
    task = asyncio.ensure_future(result())  # result 未运行
    print("[outer_call] task: ", task)  # pending

    print("[outer_call] wait inner call run...")
    # 挂起 inner call，会运行 inner call方法
    await inner_call(task)
    print("[outer_call] inner call return data")


loop = asyncio.get_event_loop()

try:
    print("going event loop")
    loop.run_until_complete(outer_call())
finally:
    print("close event loop")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# going event loop
# [outer_call] create [result] task
# [outer_call] task:  <Task pending coro=<result() running at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_future_map.py:30>>
# [outer_call] wait inner call run...
# [inner_call] run...
# [inner_call] task:  <Task pending coro=<result() running at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_future_map.py:30>>
# [result] get result...
# [inner_call] task:  <Task finished coro=<result() done, defined at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_future_map.py:30> result='hello'>
# [inner_call] task result:  hello
# [outer_call] inner call return data
# close event loop
