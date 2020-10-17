#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-16
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> signal` example


# ===============================================================================
# 标题：python3 asyncio advanced signal example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：协程之信号的注册处理
# -------------------------------------------------------------------------------
import asyncio
import functools
import os
import signal


# -------------------------------------------------------------------------------
# 信号的注册处理
# -------------------------------------------------------------------------------
def signal_handler(name):
    print("[signal_handler] processing signal: ", name)


async def trigger_signal():
    print("[trigger_signal] start")

    pid = os.getpid()
    print("[trigger_signal] start trigger signal pid: ", pid)

    for name in ["SIGHUP", "SIGHUP", "SIGUSR1", "SIGINT"]:
        print("[trigger_signal] trigger signal: ", name)
        os.kill(pid, getattr(signal, name))
        print("[trigger_signal] released signal: ", name)
        await asyncio.sleep(0.01)

    print("[trigger_signal] finished")
    return


loop = asyncio.get_event_loop()

# 给信号绑定处理的事件
loop.add_signal_handler(signal.SIGHUP, functools.partial(signal_handler, name="SIGHUP"))
loop.add_signal_handler(signal.SIGUSR1, functools.partial(signal_handler, name="SIGUSR1"))
loop.add_signal_handler(signal.SIGINT, functools.partial(signal_handler, name="SIGINT"))

try:
    print("going event loop")
    loop.run_until_complete(trigger_signal())
finally:
    print("close event loop")
    loop.close()


# output:
# ---------------------------------------------------------------------------
#
