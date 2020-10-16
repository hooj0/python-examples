#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-15
# @copyright by hoojo@2020
# @changelog python3 `asyncio advanced -> protocol client` example


# ===============================================================================
# 标题：python3 asyncio advanced protocol client example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：利用 asyncio.Protocol 实现服务端和客户端数据相互传送
# -------------------------------------------------------------------------------
import asyncio
import logging
import sys
import ssl


# -------------------------------------------------------------------------------
# 实现客户端
# -------------------------------------------------------------------------------
SERVER_ADDRESS = ("localhost", 8080)


async def echo_client(address, messages):
    logger = logging.getLogger("client")
    logger.debug("connect server ip: %s port: %s", *address)

    # 与服务端进行链接
    reader, writer = await asyncio.open_connection(*address, ssl=ssl_context)

    # 发送数据
    for data in messages:
        writer.write(data)
        logger.debug("send data: %s", data)

    # ssl EOF 结束标记
    writer.write(b'\x00')

    # 等待所有发送完成
    await writer.drain()

    # 等待服务器响应
    while True:
        data = await reader.read(128)
        if data:
            logger.debug("received data: %s", data)
        else:
            logger.debug("close connect")
            writer.close()
            break


MESSAGES = [
    b'This is the message. ',
    b'It will be sent ',
    b'in parts.',
]

# 设置 SSL 上下文
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = False
ssl_context.load_verify_locations("ssl/test_ssl.crt")

# 配置日志
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(name)s: %(message)s")
# 获取日志对象
log = logging.getLogger("main")
loop = asyncio.get_event_loop()

try:
    log.debug("wait client run...")
    loop.run_until_complete(echo_client(SERVER_ADDRESS, MESSAGES))
finally:
    log.debug("close loop event")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# asyncio: Using selector: SelectSelector
# main: wait client run...
# client: connect server ip: localhost port: 8080
# client: send data: b'This is the message. '
# client: send data: b'It will be sent '
# client: send data: b'in parts.'
# client: received data: b'server received [This is the message. ], thx!'
# client: received data: b'server received [It will be sent in parts.], thx!'
# client: close connect
# main: close loop event
