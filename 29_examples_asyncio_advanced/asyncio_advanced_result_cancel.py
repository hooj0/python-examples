#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> await result cancel pending` example


# ===============================================================================
# 标题：python3 asyncio advanced await result cancel pending example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio.wait()批量等待多个协程设置超时时间并且取消未完成的任务，包装多个返回显示结果
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 等待多个协程设置超时时间并且取消未完成的任务，包装多个返回显示结果
# -------------------------------------------------------------------------------
async def do_work(i):
    print("[do_work] param: ", i)

    try:
        await asyncio.sleep(i * 0.1)
    except asyncio.CancelledError:
        print("[do_work] cancel: ", i)
    else:
        print("[do_work] run finish: ", i)
        return "return data %s" % i


async def call_work():
    print("[call_work] run...")
    tasks = [do_work(i) for i in range(3)]

    print("[call_work] wait work tasks run finish...")
    finished, pending = await asyncio.wait(tasks, timeout=0.1)   # 开始执行 do_work 任务
    print("[call_work] task finished: %s, pending: %s" % (len(finished), len(pending)))

    # 获取返回值，包装成集合
    result = [task.result() for task in finished]
    print("[call_work] task finished result: ", str(result))

    if pending:
        print("[call_work] task cancel pending: ", pending)
        for task in pending:
            task.cancel()


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
# [call_work] wait work tasks run finish...
# [do_work] param:  0
# [do_work] param:  1
# [do_work] param:  2
# [do_work] run finish:  0
# [call_work] task finished: 1, pending: 2
# [call_work] task finished result:  ['return data 0']
# [call_work] task cancel pending:  {<Task pending coro=<do_work() running at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_await_cancel.py:34> wait_for=<Future finished result=None>>, <Task pending coro=<do_work() running at D:/work_private/python-examples/29_examples_asyncio_advanced/asyncio_advanced_await_cancel.py:34> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x0000000002B7FBB8>()]>>}
# [do_work] cancel:  1
# [do_work] cancel:  2
# close event loop
