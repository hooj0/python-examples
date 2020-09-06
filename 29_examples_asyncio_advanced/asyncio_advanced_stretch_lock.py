#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> lock` example


# ===============================================================================
# 标题：python3 asyncio advanced lock example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio.Lock() 协程锁的打开与关闭
# -------------------------------------------------------------------------------
import asyncio
import functools


# -------------------------------------------------------------------------------
# 协程锁的打开与关闭
# -------------------------------------------------------------------------------
def unlock(lock):
    print("[unlock] lock release")
    lock.release()


async def do_work_with(lock):
    print("[do_work_with] with mode")

    async with lock:
        print("[do_work_with] open locked...")

    print("[do_work_with] lock release")


async def do_work_common(lock):
    print("[do_work_common] common mode")

    await lock.acquire()
    try:
        print("[do_work_common] open locked...")
    finally:
        print("[do_work_common] lock release")
        lock.release()


async def call_work():
    print("[call_work] run...")

    lock = asyncio.Lock()
    print("[call_work] get lock resource")

    # 获取锁
    await lock.acquire()
    print("[call_work] lock acquire: ", lock.locked())

    # 当锁释放后，do_work_with、do_work_common 才能获取锁资源，运行被锁定的代码逻辑
    # loop.call_later(0.1, unlock, lock)
    loop.call_later(0.1, functools.partial(unlock, lock))

    print("[call_work] wait task running")
    await asyncio.wait([do_work_with(lock), do_work_common(lock)])

    print("[call_work] all task run finished")


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
# [call_work] get lock resource
# 这里开始被锁定
# [call_work] lock acquire:  True
# [call_work] wait task running
#
# 由于被锁定，以下方法只执行了未被锁定的业务
# [do_work_common] common mode
# [do_work_with] with mode
#
# [unlock] lock release
# 这里释放锁，后续锁定的代码业务运行完成
# [do_work_common] open locked...
# [do_work_common] lock release
# [do_work_with] open locked...
# [do_work_with] lock release
# [call_work] all task run finished
# close event loop
