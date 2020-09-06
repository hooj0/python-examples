#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> future` example


# ===============================================================================
# 标题：python3 asyncio advanced future example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：基于Future实现异步返回任务执行结果
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 非协程对象
# -------------------------------------------------------------------------------
def mark_done(future, data):
    print("设置 Future 返回结果：", data)
    future.set_result(data)


loop = asyncio.get_event_loop()

try:
    task = asyncio.Future()
    print("构建任务对象，执行返回结果设置")
    loop.call_soon(mark_done, task, "这里传入数据")

    result = loop.run_until_complete(task)
    print("返回结果：", result)
finally:
    print("关闭循环事件，释放资源")
    loop.close()

print("Future 返回的结果: ", task.result())


# output:
# ---------------------------------------------------------------------------
# 构建任务对象，执行返回结果设置
# 设置 Future 返回结果： 这里传入数据
# 返回结果： 这里传入数据
# 关闭循环事件，释放资源
# Future 返回的结果: 这里传入数据
