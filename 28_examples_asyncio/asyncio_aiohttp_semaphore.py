#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> semaphore` request example


# ===============================================================================
# 标题：python3 asyncio use aiohttp lib example
# ===============================================================================
# 使用：异步框架使用 aiohttp 框架一次性多个网页，限制并发请求数量示例
#       semaphore = asyncio.Semaphore(300) 限制并发数量 300
#
#       # 开启并发信号限制
#       async with semaphore:
#           pass
# -------------------------------------------------------------------------------
# 描述：利用异步模式进行并发多网页请求，能根据每个请求的地址返回正常的结果
#       当并发数量过大系统无法承载，可以限制并发数量
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 异步模式：
#       同时访问多个网址，限制并发数量，正常返回结果
# -------------------------------------------------------------------------------
import asyncio
import time
from aiohttp import ClientSession

url = "http://www.baidu.com/#%s"


# 异步请求操作
async def request(url, semaphore):

    # 开启并发信号限制
    async with semaphore:

        async with ClientSession() as session:
            async with session.get(url) as response:
                # 等待响应结果返回，读取响应数据
                content = await response.read()

                print("request url: %s, content length: %s, use time: %s" % (url, len(content), time.time()))


# 构建多个任务同时请求
async def run():
    # 限制并发数量 300
    semaphore = asyncio.Semaphore(300)
    tasks = [request(url % i, semaphore) for i in range(900)]
    await asyncio.wait(tasks)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    # 传入多个任务，同时执行
    loop.run_until_complete(run())
    loop.close()
