#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> await` example


# ===============================================================================
# 标题：python3 asyncio await example
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
# 描述：使用async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，函数让出控制权。
# 协程遇到await，事件循环将会挂起该协程，执行别的协程，直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 阻塞和await，
#   耗时的操作一般是一些IO操作，例如网络请求，文件读取等。
#   我们使用asyncio.sleep函数来模拟IO操作。
#   协程的目的也是让这些IO操作异步化。
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


start_time = now_time()

# 协程对象：由于do_work方法是异步，不会直接运行
coroutine = do_work(3)

loop = asyncio.get_event_loop()

# 创建一个任务：协程对象就是一个原生可以挂起的函数
task = asyncio.ensure_future(coroutine)
# 此时协程对象被任务包装，可以获取任务状态
print("task: ", task)   # pending / running

# 协程对象需要注册到事件循环，由事件循环调用
loop.run_until_complete(task)   # 协程方法运行，协程方法 do_work 输出运行结果
# 协程任务运行完成
print("task: ", task)   # finished / done

# 返回结果发现耗时 3 秒
print("result: ", task.result()) # result:  execute do work finish: 3

print("time: ", now_time() - start_time) # time:  3.001171588897705


# output:
# ---------------------------------------------------------------------------
# task:  <Task pending coro=<do_work() running at D:/work_private/python-examples/28_examples_asyncio/async_await.py:42>>
# waiting:  3
# task:  <Task finished coro=<do_work() done, defined at D:/work_private/python-examples/28_examples_asyncio/async_await.py:42> result='execute do work finish: 3'>
# result:  execute do work finish: 3
# time:  3.001171588897705