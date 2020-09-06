#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> future wait` example


# ===============================================================================
# 标题：python3 asyncio advanced future wait example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：基于Future+await类现异步返回任务执行结果
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 非协程对象
# -------------------------------------------------------------------------------
def mark_done(future, data):
    print("设置 Future 返回结果：", data)
    future.set_result(data)


async def main():
    task = asyncio.Future()
    print("构建任务对象，执行返回结果设置")
    loop.call_soon(mark_done, task, "this is data")

    # await作用：等 task 返回结果，再往下运行
    data = await task

    print("Future 返回的结果: ", data)
    print("Future 返回的结果: ", task.result())

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
# 构建任务对象，执行返回结果设置
# 设置 Future 返回结果： this is data
# Future 返回的结果: this is data
# Future 返回的结果: this is data
# 返回结果： this is data
# 关闭循环事件，释放资源
