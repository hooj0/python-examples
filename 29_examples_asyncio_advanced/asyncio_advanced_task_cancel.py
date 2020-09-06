#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> task cancel` example


# ===============================================================================
# 标题：python3 asyncio advanced task cancel example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio取消任务运行
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 协程对象
# -------------------------------------------------------------------------------
async def do_work():
    print("start do work")
    return "say start work"


async def main():
    print("构建任务")
    task = loop.create_task(do_work())

    print("取消任务")
    task.cancel()
    print("取消任务的task：", task)  # cancelling 状态

    try:
        # await 等 task 返回结果，再往下运行
        data = await task   # 遇到await，发现需要返回值结果，立即运行上面的task
    except asyncio.CancelledError:
        print("取消任务获取返回值发生异常")
    else:
        print("返回的结果data: ", data)
        print("返回的结果result: ", task.result())

        return data


loop = asyncio.get_event_loop()

try:
    result = loop.run_until_complete(main())
    print("返回结果：", result)
finally:
    print("关闭循环事件，释放资源")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# 构建任务
# 取消任务
# 取消任务的task： <Task cancelling coro=<do_work() running at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_task_cancel.py:30>>
# 取消任务获取返回值发生异常
# 返回结果： None
# 关闭循环事件，释放资源
