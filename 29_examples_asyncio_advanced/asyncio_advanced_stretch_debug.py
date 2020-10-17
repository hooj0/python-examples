#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-16
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> debug` example


# ===============================================================================
# 标题：python3 asyncio advanced debug example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：asyncio调试模式的开启
# -------------------------------------------------------------------------------
import asyncio
import logging
import argparse
import sys
import warnings


# -------------------------------------------------------------------------------
# 调试模式
# -------------------------------------------------------------------------------
async def inner_task():
    log.info("inner task run")
    await asyncio.sleep(1)
    log.info("inner task finished")


async def outer_task():
    log.info("outer task run")
    await asyncio.ensure_future(loop.create_task(inner_task()))
    log.info("outer task finished")


# 配置日志
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(levelname)5s %(name)s: %(message)s")
# 获取日志对象
log = logging.getLogger("main")

# 设置命令参数
parser = argparse.ArgumentParser("debugging asyncio")
parser.add_argument("-v", dest="verbose", action="store_true", default=False)
args = parser.parse_args()

loop = asyncio.get_event_loop()

if args.verbose:
    log.debug("open debug mode")
    loop.set_debug(True)

    # 使“慢”任务的阈值非常小以便于说明；默认值为0.1，即100毫秒。
    loop.slow_callback_duration = 0.001

    # 在警告过滤器列表中插入一个简单的条目（在前面）
    warnings.simplefilter("always", ResourceWarning)

try:
    log.debug("going event loop")
    loop.run_until_complete(outer_task())
finally:
    log.debug("close event loop")
    loop.close()


# output:
# ---------------------------------------------------------------------------
#   python asyncio_advanced_stretch_debug.py -v
# ---------------------------------------------------------------------------
# DEBUG asyncio: Using selector: SelectSelector
# DEBUG main: open debug mode
# DEBUG main: going event loop
#  INFO main: outer task run
# WARNING asyncio: Executing <Task pending coro=<outer_task() running at asyncio_advanced_stretch_debug.py:42> wait_for=<Task pending coro=<inner_task() running at asyncio_advanced_stretch_debug.py:
# 34> cb=[<TaskWakeupMethWrapper object at 0x0000000002B7DEE8>()] created at asyncio_advanced_stretch_debug.py:42> cb=[_run_until_complete_cb() at C:\Users\Administrator\AppData\Local\Programs\Pytho
# n\Python36\lib\asyncio\base_events.py:176] created at C:\Users\Administrator\AppData\Local\Programs\Python\Python36\lib\asyncio\base_events.py:446> took 0.015 seconds
#  INFO main: inner task run
#  INFO main: inner task finished
#  INFO main: outer task finished
# DEBUG main: close event loop
# DEBUG asyncio: Close <_WindowsSelectorEventLoop running=False closed=False debug=True>
