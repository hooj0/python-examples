#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-15
# @copyright by hoojo@2020
# @changelog python3 `asyncio advanced -> coroutine server ssl` example


# ===============================================================================
# 标题：python3 asyncio advanced protocol server ssl example
# ===============================================================================
# 使用：asyncio模块作用，构建协程并发应用的工具
#
# python并发的三大内置模块，简单认识：
#
# 1、multiprocessing：多进程并发处理
# 2、threading模块：多线程并发处理
# 3、asyncio模块：协程并发处理
# -------------------------------------------------------------------------------
# 描述：基于Coroutine 实现服务端和客户端数据相互传送
#
# 创建ssl证书
# openssl req -newkey rsa:2048 -nodes -keyout test_ssl.key -x509 -days 800 -out test_ssl.crt
# -------------------------------------------------------------------------------
import asyncio
import logging
import sys
import ssl


# -------------------------------------------------------------------------------
# 实现服务端
# -------------------------------------------------------------------------------
SERVER_ADDRESS = ["localhost", 8080]


async def echo_server(reader, writer):
    addr = writer.get_extra_info("peername")
    logger = logging.getLogger("server[{}:{}]".format(*addr))

    logger.debug("accept client connect: %s:%s", *addr)

    while True:
        data = await reader.read(128)

        # ssl不支持EOF结束，需要用'\x00'结束
        terminate = data.endswith(b'\x00')
        # 去掉特殊字符
        data = data.rstrip(b'\x00')

        if data:
            logger.debug("received data: %s", data)

            # 向客户端发送数据
            text = b"server received [%s], thx!" % data
            writer.write(text)
            await writer.drain()
            logger.debug("send data: %s", text)
        elif not data or terminate:
            logger.debug("connection closed...")
            writer.close()
            # loop.stop()
            break


# 设置 SSL 上下文
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.check_hostname = False
ssl_context.load_cert_chain("ssl/test_ssl.crt", "ssl/test_ssl.key")

# 配置日志
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(name)s: %(message)s")
# 获取日志对象
log = logging.getLogger("main")
# 获取事件循环
loop = asyncio.get_event_loop()
# 启动server
factory = asyncio.start_server(echo_server, *SERVER_ADDRESS, ssl=ssl_context)
# 利用事件循环运行server
server = loop.run_until_complete(factory)
log.debug("server start, ip: %s, port: %s", *SERVER_ADDRESS)

try:
    loop.run_forever()
finally:
    log.debug("close server")
    server.close()
    loop.run_until_complete(server.wait_closed())
    log.debug("close loop event")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# asyncio: Using selector: SelectSelector
# main: server start, ip: localhost, port: 8080
# server[127.0.0.1:2581]: accept client connect: 127.0.0.1:2581
# server[127.0.0.1:2581]: received data: b'This is the message. '
# server[127.0.0.1:2581]: send data: b'server received [This is the message. ], thx!'
# server[127.0.0.1:2581]: received data: b'It will be sent in parts.'
# server[127.0.0.1:2581]: send data: b'server received [It will be sent in parts.], thx!'
# server[127.0.0.1:2581]: connection closed...
