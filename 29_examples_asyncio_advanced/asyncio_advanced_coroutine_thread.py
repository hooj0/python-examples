#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-14
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> thread pool executor` example


# ===============================================================================
# 标题：python3 asyncio advanced thread pool executor example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：协程与线程结合（ThreadPoolExecutor）
# -------------------------------------------------------------------------------
import asyncio
import logging
import sys
import time
import concurrent.futures


# -------------------------------------------------------------------------------
# 协程与线程结合
# -------------------------------------------------------------------------------
def do_block(i):
    logger = logging.getLogger("block[%s]" % i)

    logger.info("run")
    time.sleep(0.1)
    logger.info("done!")

    return i ** 2


async def block_task(executor):
    logger = logging.getLogger("task")

    logger.info("task start")

    logger.info("create block task")
    block_tasks = [loop.run_in_executor(executor, do_block, i) for i in range(6)]

    logger.info("waiting block task")
    done, pending = await asyncio.wait(block_tasks)

    result = [task.result() for task in done]
    logger.info("result: %s", result)

    logger.info("task exit")


# 配置日志
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(threadName)5s_%(name)s: %(message)s")
# 获取日志对象
log = logging.getLogger("main")
# 创建一个线程池执行器，最大开启3个工作线程
pool_executor = concurrent.futures.ThreadPoolExecutor(max_workers=3, thread_name_prefix="Executor")

loop = asyncio.get_event_loop()

try:
    log.debug("wait client run...")
    loop.run_until_complete(block_task(pool_executor))
finally:
    log.debug("close loop event")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# MainThread_asyncio: Using selector: SelectSelector
# MainThread_main: wait client run...
# MainThread_task: task start
# MainThread_task: create block task
#
# 三个线程处理任务，首次处理3个任务
# Executor_0_block[0]: run
# Executor_1_block[1]: run
# Executor_2_block[2]: run
# MainThread_task: waiting block task
#
# 三个任务无序执行完成，执行后续其他任务
# Executor_0_block[0]: done!
# Executor_2_block[2]: done!
# Executor_1_block[1]: done!
# Executor_2_block[3]: run
# Executor_0_block[4]: run
# Executor_1_block[5]: run
#
# 后续任务陆续完成
# Executor_2_block[3]: done!
# Executor_0_block[4]: done!
# Executor_1_block[5]: done!
# MainThread_task: result: [9, 0, 16, 25, 1, 4]
# MainThread_task: task exit
# MainThread_main: close loop event
