#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> ensure_future` example


# ===============================================================================
# 标题：python3 asyncio ensure_future example
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
# 描述：绑定回调，在task执行完成的时候可以获取执行的结果，回调的最后一个参数是future对象，通过该对象可以获取协程返回值
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 绑定回调，
#   在task执行完成的时候可以获取执行的结果，通过future对象可以获取协程返回值
# -------------------------------------------------------------------------------
import time
import asyncio


now_time = (lambda: time.time())


# 定义一个异步方法，返回一个协程对象
async def do_work(x):
    print("waiting: ", x)
    return "execute do work finish: %s" % x


def callback(future):
    # task和回调里的future对象实际上是同一个对象
    # print("future: ", future)
    # 通过回调参数获取返回值
    print("result: ", future.result())


start_time = now_time()

# 协程对象：由于do_work方法是异步，不会直接运行
coroutine = do_work(3)

loop = asyncio.get_event_loop()

# 创建一个任务：协程对象就是一个原生可以挂起的函数
task = asyncio.ensure_future(coroutine)
# 此时协程对象被任务包装，可以获取任务状态
print("task: ", task)   # pending / running

# 添加完成后调用的回调函数
task.add_done_callback(callback)
print("task: ", task)   # pending / running，但已包含回调函数 cb=[callback() ......

# 协程对象需要注册到事件循环，由事件循环调用
loop.run_until_complete(task)   # 协程方法运行，先支持协程方法 dowork 输出运行结果，再运行回调 callback
# 协程任务运行完成
print("task: ", task)   # finished / done

print("time: ", now_time() - start_time)


# output:
# ---------------------------------------------------------------------------
# 从输出结果发现一开始 task 是 pending / running 状态
# 在ensure_future包装回调后，状态依然 pending / running 状态，但已经看得回调绑定 cb=[callback()
# 运行完成后，状态改变为 finished / done
# ---------------------------------------------------------------------------
# task:  <Task pending coro=<do_work() running at D:/work_private/python-examples/28_examples_asyncio/async_ensure_future.py:39>>
# task:  <Task pending coro=<do_work() running at D:/work_private/python-examples/28_examples_asyncio/async_ensure_future.py:39> cb=[callback() at D:/work_private/python-examples/28_examples_asyncio/async_ensure_future.py:44]>
# waiting:  3
# result:  execute do work finish: 3
# task:  <Task finished coro=<do_work() done, defined at D:/work_private/python-examples/28_examples_asyncio/async_ensure_future.py:39> result='execute do work finish: 3'>
# time:  0.0010001659393310547