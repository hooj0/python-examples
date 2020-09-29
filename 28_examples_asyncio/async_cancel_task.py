#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-28 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> cancel task` example


# ===============================================================================
# 标题：python3 asyncio cancel tasks example
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
# 描述：协程停止，
#
# future对象有几个状态：
#    Pending
#    Running
#    Done
#    Cacelled
#
# 创建future的时候，task为pending，事件循环调用执行的时候当然就是 running，调用完毕自然就是 done，
# 如果需要停止事件循环，就需要先把 task 取消。可以使用 asyncio.Task 获取事件循环的 task
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 协程停止，取消运行中的task
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
print("task: ", tasks)   # pending / running

loop = asyncio.get_event_loop()

try:
    # 协程对象需要注册到事件循环，由事件循环调用
    # 并发：asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) 前者接受一个task列表，后者接收一堆task
    loop.run_until_complete(asyncio.wait(tasks))   # 协程方法运行，协程方法 do_work 输出运行结果
    # 协程任务运行完成
    print("task: ", tasks)   # finished / done

    # 返回结果发现耗时 4 秒，按照同步运行一组任务需要 7 秒
    for task in tasks:
        print("result: ", task.result())

# 在 terminal 终端在启动项目，然后按下 Ctrl + C 结束，触发 run_until_complete的执行异常 KeyboardInterrupt
except KeyboardInterrupt as e:
    # 获取所有协程任务
    print(asyncio.Task.all_tasks())

    # 获取所有协程任务，通过循环asyncio.Task取消future
    for task in asyncio.Task.all_tasks():
        # 取消协程任务
        print("cancel: ", task.cancel()) # True 表示 cancel 成功

    loop.stop()
    # loop.stop之后还需要再次开启事件循环，最后finally中close，不然还会抛出异常
    loop.run_forever()
finally:
    loop.close()

print("time: ", now_time() - start_time) # time:  4.007229328155518


# output:
# ---------------------------------------------------------------------------
# task:  [<Task pending coro=<do_work() running at async_cancel_task.py:47>>, <Task pending coro=<do_work() running at async_cancel_task.py:47>>, <Task pending coro=<do_work() running at async_cance
# l_task.py:47>>]
# waiting:  1
# waiting:  3
# waiting:  4
# {<Task pending coro=<do_work() running at async_cancel_task.py:53> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x0000000002EEF978>()]> cb=[_wait.<locals>._on_completion() at C:\U
# sers\Administrator\AppData\Local\Programs\Python\Python36\lib\asyncio\tasks.py:380]>, <Task finished coro=<do_work() done, defined at async_cancel_task.py:47> result='execute do work finish: 1'>,
# <Task pending coro=<do_work() running at async_cancel_task.py:53> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x0000000002F7CB88>()]> cb=[_wait.<locals>._on_completion() at C:\Us
# ers\Administrator\AppData\Local\Programs\Python\Python36\lib\asyncio\tasks.py:380]>, <Task pending coro=<wait() running at C:\Users\Administrator\AppData\Local\Programs\Python\Python36\lib\asyncio
# \tasks.py:313> wait_for=<Future pending cb=[<TaskWakeupMethWrapper object at 0x0000000002F7CCD8>()]>>}
# True
# False
# True
# True
# time:  3.004171848297119