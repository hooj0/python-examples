#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-15
# @copyright by hoojo@2018
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
import functools


# -------------------------------------------------------------------------------
# 实现客户端
# -------------------------------------------------------------------------------
SERVER_ADDRESS = ["localhost", 8080]


class EchoProtocolClient(asyncio.Protocol):

    def __init__(self, messages, future):
        super().__init__()
        self.messages = messages
        self.future = future
        self.log = logging.getLogger("EchoProtocolClient")

    # 创建链接
    def connection_made(self, transport):
        self.transport = transport
        self.address = transport.get_extra_info("peername")
        self.log.debug("connect server ip: %s port: %s", *self.address)

        # 发送数据
        # transport.writelines(self.messages)
        for data in self.messages:
            transport.write(data)
            self.log.debug("send data: %s", data)

        # 发送退出信号
        if transport.can_write_eof():
            transport.write_eof()

    # 接收数据
    def data_received(self, data):
        self.log.debug("received data: %s", data)

    # 接收退出信号
    def eof_received(self):
        self.log.debug("received data EOF")
        # 关闭传送
        self.transport.close()
        # 判断任务是否完成
        if not self.future.done():
            self.future.set_result(True)

    # 链接关闭
    def connection_lost(self, exc):
        self.log.debug("close connect")
        # 关闭传送
        self.transport.close()
        # 判断任务是否完成
        if not self.future.done():
            self.future.set_result(True)
            
        super(EchoProtocolClient, self).connection_lost(exc)


MESSAGES = [
    b'This is the message. ',
    b'It will be sent ',
    b'in parts.',
]
# 配置日志
logging.basicConfig(level=logging.DEBUG, stream=sys.stderr, format="%(name)s: %(message)s")
# 获取日志对象
log = logging.getLogger("main")

loop = asyncio.get_event_loop()
# 创建 client
client_future = asyncio.Future()
# 利用偏函数自动传参给EchoProtocolClient实例化类
client_protocol_factory = functools.partial(
    EchoProtocolClient,
    messages=MESSAGES,
    future=client_future,
)
# 创建链接
client_connect = loop.create_connection(client_protocol_factory, *SERVER_ADDRESS)
# 利用事件循环运行server
log.debug("wait client run...")

try:
    loop.run_until_complete(client_connect)
    loop.run_until_complete(client_future)
finally:
    log.debug("close loop event")
    loop.close()


# output:
# ---------------------------------------------------------------------------
# asyncio: Using selector: SelectSelector
# main: wait client run...
# EchoProtocolClient: connect server ip: 127.0.0.1 port: 8080
# EchoProtocolClient: send data: b'This is the message. '
# EchoProtocolClient: send data: b'It will be sent '
# EchoProtocolClient: send data: b'in parts.'
# EchoProtocolClient: received data: b'server received [This is the message. ], thx!'
# EchoProtocolClient: received data: b'server received [It will be sent in parts.], thx!'
# EchoProtocolClient: received data EOF
# EchoProtocolClient: close connect
# main: close loop event
