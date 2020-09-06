#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> task call cancel` example


# ===============================================================================
# 标题：python3 asyncio advanced task call cancel example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：利用回调取消任务执行
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 协程对象
# -------------------------------------------------------------------------------
async def do_work():
    print("start do work")

    try:
        await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("do_work 任务取消")
        raise

    return "say start work"


def do_cancel(task):
    print("do cancel task...")
    task.cancel()
    print("do cancel task success")


async def main():
    print("构建任务")
    task = loop.create_task(do_work())

    print("回调取消任务")
    loop.call_soon(do_cancel, task)
    print("取消任务的task：", task)  # pending 状态

    try:
        # await 等 task 返回结果，再往下运行
        data = await task   # 遇到await，发现需要返回值结果，立即运行上面的task
    except asyncio.CancelledError:
        print("取消任务获取返回值发生异常")
        print("取消任务的task：", task)  # cancelled 状态
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
# 回调取消任务
# 取消任务的task： <Task pending coro=<do_work() running at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_task_cancel_call.py:30>>
# start do work
# do cancel task...
# do cancel task success
# do_work 任务取消
# 取消任务获取返回值发生异常
# 取消任务的task： <Task cancelled coro=<do_work() done, defined at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_task_cancel_call.py:30>>
# 返回结果： None
# 关闭循环事件，释放资源
