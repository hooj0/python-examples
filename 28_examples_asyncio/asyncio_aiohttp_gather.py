#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> gather` many request result example


# ===============================================================================
# 标题：python3 asyncio use aiohttp lib example
# ===============================================================================
# 使用：异步框架使用 aiohttp 框架一次性多个网页请求示例，并收集每个网页返回的结果
#   组建多个任务
#       task = asyncio.ensure_future(request(url % i))
#       tasks.append(task)
#
#   传入多个任务，同时执行，接受返回值数组
#       result = loop.run_until_complete(asyncio.gather(*tasks))
# -------------------------------------------------------------------------------
# 描述：当我们发出了请求，如果要把响应一一收集到一个列表中，
# 最后保存到本地或者打印出来要怎么实现呢，可通过asyncio.gather(*tasks)将响应全部收集起来
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 异步模式：
#       同时访问多个网址，正常返回结果，并接受返回结果
# -------------------------------------------------------------------------------
import asyncio
import time
from aiohttp import ClientSession

tasks = []
url = "http://www.baidu.com/#%s"


# 异步请求操作
async def request(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            # 等待响应结果返回，读取响应数据
            content = await response.read()

            info = "request url: %s, content length: %s, use time: %s" % (url, len(content), time.time())
            print(info)
            return info, len(content)


# 构建多个任务同时请求
def run():
    for i in range(5):
        task = asyncio.ensure_future(request(url % i))
        tasks.append(task)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    run()

    # 传入多个任务，同时执行，接受返回值数组
    result = loop.run_until_complete(asyncio.gather(*tasks))
    print(result)


# -------------------------------------------------------------------------------
# 结果输出：
#       返回一个数组
# -------------------------------------------------------------------------------
# request url: http://www.baidu.com/#1, content length: 282944, use time: 1601022278.0903664
# request url: http://www.baidu.com/#0, content length: 282911, use time: 1601022278.0973668
# request url: http://www.baidu.com/#2, content length: 282930, use time: 1601022278.1023672
# request url: http://www.baidu.com/#3, content length: 282966, use time: 1601022278.1043673
# request url: http://www.baidu.com/#4, content length: 282895, use time: 1601022278.1073675
#
# [('request url: http://www.baidu.com/#0, content length: 282911, use time: 1601022278.0973668', 282911),
# ('request url: http://www.baidu.com/#1, content length: 282944, use time: 1601022278.0903664', 282944),
# ('request url: http://www.baidu.com/#2, content length: 282930, use time: 1601022278.1023672', 282930),
# ('request url: http://www.baidu.com/#3, content length: 282966, use time: 1601022278.1043673', 282966),
# ('request url: http://www.baidu.com/#4, content length: 282895, use time: 1601022278.1073675', 282895)]