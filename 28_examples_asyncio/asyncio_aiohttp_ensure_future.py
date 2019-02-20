#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> ensure_future` many URL request example


# ===============================================================================
# 标题：python3 asyncio use aiohttp lib example
# ===============================================================================
# 使用：异步框架使用 aiohttp 框架一次性多个网页请求示例
#   task = asyncio.ensure_future(request(url % i))
#   tasks.append(task)
# 一次性调用多任务：
#   loop.run_until_complete(asyncio.wait(tasks))
# -------------------------------------------------------------------------------
# 描述：利用异步模式进行并发多网页请求，能根据每个请求的地址返回正常的结果
#   如果我们需要请求多个URL该怎么办呢，同步的做法访问多个URL只需要加个for循环就可以了。
#   但异步的实现方式并没那么容易，在之前的基础上需要将 request()包装在asyncio的Future对象中，
#   然后将Future对象列表作为任务传递给事件循环。
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 异步模式：
#       同时访问多个网址，正常返回结果
# -------------------------------------------------------------------------------
import asyncio
import time
from aiohttp import ClientSession

tasks = []
url = "http://www.baidu.com/%s"


# 异步请求操作
async def request(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            # 等待响应结果返回，读取响应数据
            content = await response.read()

            print("request url: %s, content length: %s, use time: %s" % (url, len(content), time.time()))


# 构建多个任务同时请求
def run():
    for i in range(5):
        task = asyncio.ensure_future(request(url % i))
        tasks.append(task)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    run()
    # 传入多个任务，同时执行
    loop.run_until_complete(asyncio.wait(tasks))


# -------------------------------------------------------------------------------
# 结果输出：
#       程序瞬间同时输出，没有任何等待，无间隔
# -------------------------------------------------------------------------------
# request url: http://www.baidu.com/1, content length: 199, use time: 1601021616.7965426
# request url: http://www.baidu.com/2, content length: 199, use time: 1601021616.7975426
# request url: http://www.baidu.com/0, content length: 199, use time: 1601021616.7975426
# request url: http://www.baidu.com/3, content length: 199, use time: 1601021616.7985427
# request url: http://www.baidu.com/4, content length: 199, use time: 1601021616.7985427