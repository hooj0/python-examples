#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> as_completed result` example


# ===============================================================================
# 标题：python3 asyncio advanced as_completed result example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio.as_completed()多个协程运行，函数返回值不是有序的接收
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 多个协程运行，函数返回值不是有序的接收
# -------------------------------------------------------------------------------
async def do_work(i):
    print("[do_work] param: ", i)
    await asyncio.sleep(i * 0.1)

    print("[do_work] run finish: ", i)
    return "return data %s" % i


async def call_work():
    print("[call_work] run...")

    tasks = [do_work(i) for i in range(3)]
    print("[call_work] wait work tasks run finish...")

    result = []
    for task in asyncio.as_completed(tasks):
        data = await task
        result.append(data)

    # 获取返回值集合
    print("[call_work] task finished result: ", result)


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
# [do_work] param:  2
# [do_work] param:  1
# [do_work] param:  0
# [do_work] run finish:  0
# [do_work] run finish:  1
# [do_work] run finish:  2
# [call_work] task finished result:  ['return data 0', 'return data 1', 'return data 2']
# close event loop
