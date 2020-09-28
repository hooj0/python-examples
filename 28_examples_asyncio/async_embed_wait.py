#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> await & gather & as_completed` example


# ===============================================================================
# 标题：python3 asyncio await & gather & as_completed tasks example
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
# 描述：协程嵌套
#
# 使用async可以定义协程，协程用于耗时的io操作，我们也可以封装更多的io操作过程，
# 这样就实现了嵌套的协程，即一个协程中await了另外一个协程，如此连接起来。
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 协程嵌套，
#   在一个协程中挂起其他的协程，让协程中调用其他协程，进行协程嵌套调用
# -------------------------------------------------------------------------------
import time
import asyncio


now_time = (lambda: time.time())


# 定义一个异步方法，返回一个协程对象
async def do_work(x):
    print("waiting: ", x)

    # 等待/阻塞：模拟有耗时操作，如读写文件或网络请求等
    # 模拟了阻塞或者耗时操作，这个时候就会让出控制权
    # 即当遇到阻塞调用的函数的时候，使用await方法将协程的控制权让出，以便loop调用其他协程任务
    await asyncio.sleep(x)
    return "execute do work finish: %s" % x


# 嵌套调用，main函数嵌套调用协程 do_work
async def main():
    # 协程对象：由于do_work方法是异步，不会直接运行
    coroutine1 = do_work(1)
    coroutine2 = do_work(3)
    coroutine3 = do_work(4)

    # 创建一组任务：协程对象就是一个原生可以挂起的函数
    tasks = [
        asyncio.ensure_future(coroutine1),
        asyncio.ensure_future(coroutine2),
        asyncio.ensure_future(coroutine3),
    ]
    # 此时协程对象被任务包装，可以获取任务状态
    print("task: ", tasks)  # pending / running

    dones, pendings = await asyncio.wait(tasks)

    # 返回结果发现耗时 4 秒，按照同步运行一组任务需要 7 秒
    for task in dones:
        print("result: ", task.result())


start_time = now_time()

loop = asyncio.get_event_loop()

# 协程对象需要注册到事件循环，由事件循环调用
# 嵌套调用，main函数嵌套调用协程 do_work
loop.run_until_complete(main())   # 协程方法运行，协程方法 do_work 输出运行结果

print("time: ", now_time() - start_time) # time:  3.9912283420562744


# output:
# ---------------------------------------------------------------------------
# task:  [<Task pending coro=<do_work() running at D:/work_private/python-examples/28_examples_asyncio/async_wait_gather_completed.py:42>>, <Task pending coro=<do_work() running at D:/work_private/python-examples/28_examples_asyncio/async_wait_gather_completed.py:42>>, <Task pending coro=<do_work() running at D:/work_private/python-examples/28_examples_asyncio/async_wait_gather_completed.py:42>>]
# waiting:  1
# waiting:  3
# waiting:  4
# result:  execute do work finish: 1
# result:  execute do work finish: 4
# result:  execute do work finish: 3
# time:  3.9912283420562744