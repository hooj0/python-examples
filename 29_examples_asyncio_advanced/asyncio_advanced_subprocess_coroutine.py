#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-15
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> subprocess coroutine` example


# ===============================================================================
# 标题：python3 asyncio advanced subprocess coroutine example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：利用协程的方式实现子进程的调用
# -------------------------------------------------------------------------------
import asyncio
import os


# -------------------------------------------------------------------------------
# 实现子进程的调用
# -------------------------------------------------------------------------------
def parser_result(output):
    print("parser result...")
    if not output:
        return []

    lines = output.splitlines()
    headers = lines[0].split()
    devices = lines[1:]

    return [dict(zip(headers, line.split())) for line in devices]


async def df_command():
    print("start run cmd df -hl")

    buffer = bytearray()

    if os.name == 'nt':
        cmd_process = asyncio.create_subprocess_exec("cmd", "/c", "dir", "c:\\Users", stdout=asyncio.subprocess.PIPE)
        # cmd_process = asyncio.create_subprocess_exec("cmd", "/c", "dir", stdout=asyncio.subprocess.PIPE)
        # cmd_process = asyncio.create_subprocess_exec("diskpart", "list disk", stdout=asyncio.subprocess.PIPE)
    else:
        cmd_process = asyncio.create_subprocess_exec("df", "-h", stdout=asyncio.subprocess.PIPE)
    print("execute process")

    proc = await cmd_process
    print("process startup: ", proc.pid)

    while True:
        line = await proc.stdout.readline()
        print("read line: ", line)

        if not line:
            print("read stdout finished")
            break

        buffer.extend(line)

    print("wait cmd process finished")
    await proc.wait()

    return_code = proc.returncode
    print("return code: ", return_code)

    results = []
    if not return_code:
        cmd_output = bytes(buffer).decode("gbk")
        results = parser_result(cmd_output)

    return (return_code, results)


if os.name == 'nt':
    # On Windows, the ProactorEventLoop is necessary to listen on pipes
    loop = asyncio.ProactorEventLoop() # for subprocess' pipes on Windows
    asyncio.set_event_loop(loop)
else:
    loop = asyncio.get_event_loop()

try:
    print("going event loop")

    code, result = loop.run_until_complete(df_command())
    print("result：", result)

    if code:
        print("error exit: ", code)
    else:
        print("\n\nFree space:")
        for item in result:
            print(item)

    loop.run_forever()
finally:
    print("close event")
    loop.close()


# output:
# ---------------------------------------------------------------------------
#
