#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-15
# @copyright by hoojo@2018
# @changelog python3 `asyncio advanced -> protocol server` example


# ===============================================================================
# 标题：python3 asyncio advanced protocol server example
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
# State machine of calls:
#
#       start -> CM [-> DR*] [-> ER?] -> CL -> end
#
#     * CM: connection_made()
#     * DR: data_received()
#     * ER: eof_received()
#     * CL: connection_lost()
# -------------------------------------------------------------------------------
import asyncio
import logging
import sys


# -------------------------------------------------------------------------------
# 实现服务端
# -------------------------------------------------------------------------------
SERVER_ADDRESS = ["localhost", 8080]


class EchoProtocolServer(asyncio.Protocol):

    # 获取链接
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        self.log = logging.getLogger("EchoProtocolServer[{}:{}]".format(*self.address))

        self.log.debug("accept client connect: %s:%s", *self.address)

    # 接收数据
    def data_received(self, data):
        self.log.debug("received data: %s", data)

        # 向客户端发送数据
        text = b"server received [%s], thx!" % data
        self.transport.write(text)
        self.log.debug("send data: %s", text)

    # 接收退出信号
    def eof_received(self):
        self.log.debug("received data EOF")
        # 发送退出信号
        if self.transport.can_write_eof():
            self.transport.write_eof()

    # 关闭链接
    def connection_lost(self, exc):
        if exc:
            self.log.error("connection error: ", exc)
        else:
            self.log.debug("connection closed...")
            # 停止循环事件
            # loop.stop()
            
        super(EchoProtocolServer, self).connection_lost(exc)


# 配置日志
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(name)s: %(message)s")
# 获取日志对象
log = logging.getLogger("main")

loop = asyncio.get_event_loop()
# 创建server
factory = loop.create_server(EchoProtocolServer, *SERVER_ADDRESS)
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
# EchoProtocolServer[127.0.0.1:5496]: accept client connect: 127.0.0.1:5496
# EchoProtocolServer[127.0.0.1:5496]: received data: b'This is the message. '
# EchoProtocolServer[127.0.0.1:5496]: send data: b'server received [This is the message. ], thx!'
# EchoProtocolServer[127.0.0.1:5496]: received data: b'It will be sent in parts.'
# EchoProtocolServer[127.0.0.1:5496]: send data: b'server received [It will be sent in parts.], thx!'
# EchoProtocolServer[127.0.0.1:5496]: received data EOF
# EchoProtocolServer[127.0.0.1:5496]: connection closed...
