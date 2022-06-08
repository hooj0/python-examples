#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-15
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> subprocess protocol` example


# ===============================================================================
# 标题：python3 asyncio advanced subprocess protocol example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：利用asyncio.SubprocessProtocol类继承的方式实现子进程的调用
# -------------------------------------------------------------------------------
import asyncio
import functools
import os
#from asyncio import transports


# -------------------------------------------------------------------------------
# 实现子进程的调用
# -------------------------------------------------------------------------------
class DFCommandProtocol(asyncio.SubprocessProtocol):

    FD_NAMES = ["stdin", "stdout", "stderr"]

    def __init__(self, done_future: asyncio.Future):
        super().__init__()

        self.done_future = done_future
        self.buffer = bytearray()

    def connection_made(self, transport: asyncio.transports.SubprocessTransport):
        self.transport = transport

        print("process start up: ", transport.get_pid())

    def pipe_data_received(self, fd: int, data: bytes):
        print("read %s bytes from %s" % (len(data), self.FD_NAMES[fd]))

        if fd == 1:
            self.buffer.extend(data)

    # def connection_lost(self, exc):
    #    loop.stop()  # end loop.run_forever()

    def process_exited(self):
        print("process exited")

        return_code = self.transport.get_returncode()
        print("return code: ", return_code)

        results = []
        if not return_code:
            cmd_output = bytes(self.buffer).decode("gbk")
            results = self.__parser_result(cmd_output)

        self.done_future.set_result((return_code, results))

    @staticmethod
    def __parser_result(output):
        print("parser result...")

        if not output:
            return []

        lines = output.splitlines()
        headers = lines[0].split()
        devices = lines[1:]

        return [dict(zip(headers, line.split())) for line in devices]


async def df_command():
    print("start run cmd df -hl")

    done_future = asyncio.Future(loop=loop)
    # factory = DFCommandProtocol(done_future)
    # factory = functools.partial(DFCommandProtocol, done_future)

    if os.name == 'nt':
        cmd_process = loop.subprocess_exec(lambda: DFCommandProtocol(done_future), "cmd", "/c", "dir", stderr=None, stdin=None)
    else:
        cmd_process = loop.subprocess_exec(lambda: DFCommandProtocol(done_future), "df", "-hl", stderr=None, stdin=None)

    transport = None
    try:
        print("execute process")
        transport, protocol = await cmd_process

        print("wait cmd process finished")
        await done_future
    finally:
        if transport:
            transport.close()

    return done_future.result()


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
