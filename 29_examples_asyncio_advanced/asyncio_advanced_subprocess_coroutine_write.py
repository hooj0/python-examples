#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-16
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> subprocess coroutine communicate` example


# ===============================================================================
# 标题：python3 asyncio advanced subprocess coroutine communicate example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：利用协程管道传数据给子进程的调用处理
# -------------------------------------------------------------------------------
import asyncio
import os
import sys


# -------------------------------------------------------------------------------
# 实现子进程的调用
# -------------------------------------------------------------------------------
async def tr_command(input):
    print("start run tr command")

    cmd_process = asyncio.create_subprocess_exec("tr", "[:lower:]", "[:upper:]", stdout=asyncio.subprocess.PIPE, stdin=asyncio.subprocess.PIPE)

    print("wait subprocess execute finished")
    sub_process = await cmd_process
    print("subprocess process startup:", sub_process.pid)

    # 查看子进程运行的标准输出和错误
    print("subprocess output & error")
    stdout, stderr = sub_process.communicate(input.encode())

    print("wait subprocess finished")
    await sub_process.wait()

    return_code = sub_process.returncode
    print("return code: ", return_code)

    data = ""
    if not return_code:
        data = bytes(stdout).decode("gbk")

    return (return_code, data)


MESSAGE = """
This message will be converted
to all caps.
"""

loop = asyncio.get_event_loop()

try:
    print("going event loop")
    print("os.name: ", os.name)
    print("sys.platform: ", sys.platform)

    code, result = loop.run_until_complete(tr_command(MESSAGE))
    print("result：", result)

    if code:
        print("error exit: ", code)
    else:
        print("result:", result)

    loop.run_forever()
finally:
    print("close event")
    loop.close()


# output:
# ---------------------------------------------------------------------------
#
