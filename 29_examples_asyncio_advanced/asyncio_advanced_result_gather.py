#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> gather result` example


# ===============================================================================
# 标题：python3 asyncio advanced gather result example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio.gather()多个协程运行，函数返回值接收
# -------------------------------------------------------------------------------
import asyncio


# -------------------------------------------------------------------------------
# 多个协程运行，函数返回值接收返回显示结果
# -------------------------------------------------------------------------------
async def do_work(i):
    print("[do_work] param: ", i)
    await asyncio.sleep(i * 0.1)

    print("[do_work] run finish: ", i)
    return "return data %s" % i


async def call_work():
    print("[call_work] run...")

    print("[call_work] wait work tasks run finish...")
    result = await asyncio.gather(do_work(1), do_work(5))   # 开始执行 do_work 任务
    # result = await asyncio.gather(*[do_work(1), do_work(5)])   # 开始执行 do_work 任务
    # result = await asyncio.gather(asyncio.gather(do_work(1), do_work(2)), asyncio.gather(do_work(3), do_work(4)))

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
# [do_work] param:  5
# [do_work] param:  1
# [do_work] run finish:  1
# [do_work] run finish:  5
# [call_work] task finished result:  ['return data 1', 'return data 5']
# close event loop
