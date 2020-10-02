#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> async` example


# ===============================================================================
# 标题：python3 `asyncio -> async` example
# ===============================================================================
# 使用：asyncio 库中的 async 异步示例
#
# 需要使用 async 关键字定义函数，表明异步函数：
#   async def func():
#       async_r = asyncio.async(func())
#       pass
#
# 在调用函数时，需要使用 以下方式运行函数：
#   asyncio.get_event_loop().run_until_complete(func())
# -------------------------------------------------------------------------------
# 描述：使用asyncio.async包装的协程，不阻塞，立即返回一个Task对象
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 异步模式：
#       使用asyncio.async包装的协程，不阻塞，立即返回一个Task对象
# -------------------------------------------------------------------------------
import time
import asyncio
import itertools
import sys


# 控制台动画效果
async def console():
    for i in itertools.cycle('|/-\\'):
        write, flush = sys.stdout.write, sys.stdout.flush
        write(i)
        flush()
        write('\x08' * len(i))

        try:
            await asyncio.sleep(1)
        except asyncio.CancelledError:
            break


async def hello():
    await asyncio.sleep(5)
    return "say hello"


# 使用异步关键字，异步函数
async def run():
    # task = asyncio.async(console()) 被移除
    # task = asyncio.ensure_future(console())
    task = loop.create_task(console())
    print("task: ", task)
    # 接受返回值
    result = await hello()
    # 取消动画
    task.cancel()

    return result


def main():
    # 接受循环异步程序运行，接收 run 方法返回值
    result = loop.run_until_complete(run())
    loop.close()

    print("result: ", result)


# 构建创建事件循环
loop = asyncio.get_event_loop()
if __name__ == '__main__':
    main()


# -------------------------------------------------------------------------------
# 结果输出：
#       程序在等待输出 result 时候，会显示 动画指针效果
# -------------------------------------------------------------------------------
# task:  <Task pending coro=<console() running at D:/work_private/python-examples/28_examples_asyncio/asyncio_task_async.py:38>>
# result:  say hello
