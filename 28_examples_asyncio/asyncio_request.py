#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> run_until_complete` request example


# ===============================================================================
# 标题：python3 asyncio use aiohttp lib example
# ===============================================================================
# 使用：异步框架使用aiohttp 框架请求网页示例
# -------------------------------------------------------------------------------
# 描述：利用异步模式进行网页并发请求，能根据每个请求的地址返回正常的结果
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 异步模式：
#       访问网址，正常返回结果
# -------------------------------------------------------------------------------
import asyncio
from aiohttp import ClientSession


# 异步请求操作
async def request(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            # 等待响应结果返回，读取响应数据
            content = await response.read()

            print("rquest url: ", url)
            print("content: ", len(content))


if __name__ == '__main__':
    url = "http://www.baidu.com/"

    loop = asyncio.get_event_loop()
    loop.run_until_complete(request(url))

    url = "http://www.163.com/"
    loop.run_until_complete(request(url))