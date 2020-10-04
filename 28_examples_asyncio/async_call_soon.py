#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-28 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> call_soon` example


# ===============================================================================
# 标题：python3 asyncio in call_soon example
# ===============================================================================
# 使用：关于asyncio的一些关键字的说明：
#
# event_loop 事件循环：程序开启一个无限循环，把一些函数注册到事件循环上，当满足事件发生的时候，调用相应的协程函数。
# coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象。
#               协程对象需要注册到事件循环，由事件循环调用。
# task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含了任务的各种状态。
# future: 代表将来执行或没有执行的任务的结果。它和task上没有本质上的区别。
# async/await 关键字：python3.5用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。
# -------------------------------------------------------------------------------
# 描述：很多时候我们的事件循环用于注册协程，而有的协程需要动态的添加到事件循环中。
#
# call_soon(callback) 会把callback放到一个先进先出的队列，每个callback会被执行一次。
# call_soon 注册的协程任务之后，立即返回，不阻塞，
# 配合run_forever使用，run_forever会一直循环，直到loop.stop()。
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 不同线程的事件循环，
#   call_soon 注册的协程任务之后，立即返回
#   并且当前线程会被block(阻塞)。
# -------------------------------------------------------------------------------
import time
import asyncio
from threading import Thread


now_time = (lambda: time.time())


# 定义一个模拟阻塞的方法
def do_work(x, loop):
    print("start work: ", x)
    time.sleep(x)
    print("work finished: ", x)

    if x >= 2:
        loop.stop()


start_time = now_time()

# 创建一个新的事件循环
loop = asyncio.get_event_loop()
# 非线程安全，按顺序执行
loop.call_soon(do_work, 1, loop)
loop.call_soon(do_work, 2, loop)

loop.run_forever()
loop.close()

print("time: ", now_time() - start_time)

# output:
# ---------------------------------------------------------------------------
# 启动上述代码之后，当前线程会被block，
# 新线程中会按照顺序执行 call_soon_threadsafe 方法注册的 do_work 方法， 后者因为 time.sleep 操作是同步阻塞的，
# 因此运行完毕more_work需要大致 5 + 3
# ---------------------------------------------------------------------------
# start work:  1
# work finished:  1
# start work:  2
# work finished:  2
# time:  3.000171422958374