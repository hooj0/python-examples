#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> future callback` example


# ===============================================================================
# 标题：python3 asyncio advanced future callback example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：基于Future的回调
# -------------------------------------------------------------------------------
import asyncio
import functools


# -------------------------------------------------------------------------------
# 回调
# -------------------------------------------------------------------------------
def callback(future, n):
    print("Future-%s 完成：%s" % (n, future.result()))


async def add_callback(future):
    # partial 会为 callback的参数 n 设置值，并返回
    future.add_done_callback(functools.partial(callback, n=1))
    future.add_done_callback(functools.partial(callback, n=2))


async def main(future):

    # 设置future的回调函数
    print("将回调函数注册到Future中")
    await add_callback(future)

    # 设置返回结果
    print("设置返回结果")
    future.set_result("haha")


loop = asyncio.get_event_loop()
try:
    # 创建一个 future 对象
    task = asyncio.Future()

    loop.run_until_complete(main(task))
finally:
    print("关闭循环事件，释放资源")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# 将回调函数注册到Future中
# 设置返回结果
# Future-1 完成：haha
# Future-2 完成：haha
# 关闭循环事件，释放资源
