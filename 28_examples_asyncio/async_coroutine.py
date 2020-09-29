#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> coroutine` example


# ===============================================================================
# 标题：python3 asyncio coroutine example
# asyncio的编程模型就是一个消息循环，我们从asyncio模块中直接获取一个EventLoop的引用，
# 然后把需要执行的协程扔到EventLoop中执行，就实现了异步IO
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
# 描述：协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象.
# task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 定义一个协程对象，
#   指一个使用async关键字定义的函数，它的调用不会立即执行函数，而是会返回一个协程对象
#
#  async 把一个 generator 标记为 coroutine 类型，
#  然后我们就把这个 coroutine 扔到 EventLoop 中执行
# -------------------------------------------------------------------------------
import time
import asyncio


now_time = (lambda: time.time())


# 定义一个异步方法，返回一个协程对象
async def do_work(x):
    print("waiting: ", x)


start_time = now_time()

# 协程对象：由于do_work方法是异步，不会直接运行
coroutine = do_work(2)  # async 把一个 generator 标记为 coroutine 类型

loop = asyncio.get_event_loop()
# 创建一个任务：一个协程对象就是一个原生可以挂起的函数
task = loop.create_task(coroutine)
#
# task = asyncio.ensure_future(coroutine)
# 此时协程对象被任务包装，可以获取任务状态
print("task: ", task)   # pending

# 协程对象需要注册到事件循环，由事件循环调用
# 把这个 coroutine 扔到 EventLoop 中执行
loop.run_until_complete(task)   # 协程方法运行，输出运行结果
# 协程任务运行完成
print("task: ", task)   # finished

print("time: ", now_time() - start_time)

# output:
# ---------------------------------------------------------------------------
# 从输出结果发现一开始 task 是 pending 状态
# 运行完成后，状态改变为 finished
# ---------------------------------------------------------------------------
# task:  <Task pending coro=<do_work() running at D:/work_private/python-examples/28_examples_asyncio/async_coroutine.py:40>>
# waiting:  2
# task:  <Task finished coro=<do_work() done, defined at D:/work_private/python-examples/28_examples_asyncio/async_coroutine.py:40> result=None>
# time:  0.0010001659393310547