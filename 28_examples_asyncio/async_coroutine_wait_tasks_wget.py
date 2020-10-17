#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-09-25 16:07:27
# @copyright by hoojo@2018
# @changelog python3 `asyncio -> await tasks` example


# ===============================================================================
# 标题：python3 asyncio await tasks example
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
# 描述：并行与并发
#
# 并发指的是同时具有多个活动的系统
# 并行指的是用并发来使一个系统运行的更快。并行可以在操作系统的多个抽象层次进行运用
# 所以并发通常是指有多个任务需要同时进行，并行则是同一个时刻有多个任务执行
#
# 下面这个例子非常形象：
#
# 并发情况下是一个老师在同一时间段辅助不同的人功课。
# 并行则是指多个老师分别同时辅助多个学生功课。
# 简而言之就是一个人同时吃三个馒头（并发） 还是三个人每人同时吃一个的情况 （并行），吃一个馒头算一个任务
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 并行与并发，
#   同时运行一组任务，让多个任务同时执行，简化任务时间
# -------------------------------------------------------------------------------
import time
import asyncio


now_time = (lambda: time.time())


# 定义一个异步方法，返回一个协程对象
async def wget(host):
    print("wget %s host..." % host)

    connect = asyncio.open_connection(host, 80)

    # 等待/阻塞：模拟有耗时操作，如读写文件或网络请求等
    # 模拟了阻塞或者耗时操作，这个时候就会让出控制权
    # 即当遇到阻塞调用的函数的时候，使用await方法将协程的控制权让出，以便loop调用其他协程任务
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host

    writer.write(header.encode('utf-8'))

    await writer.drain()

    while True:
        line = await reader.readline()
        if line == b'\r\n':
            break

        print('%s header > %s ' % (host, line.decode('utf-8').strip()))

    writer.close()


start_time = now_time()

loop = asyncio.get_event_loop()
# 创建一组任务：协程对象就是一个原生可以挂起的函数
tasks = [
    wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']
]

# 协程对象需要注册到事件循环，由事件循环调用
# 并发：asyncio.wait(tasks) 也可以使用 asyncio.gather(*tasks) 前者接受一个task列表，后者接收一堆task
loop.run_until_complete(asyncio.wait(tasks))   # 协程方法运行，协程方法 do_work 输出运行结果

print("time: ", now_time() - start_time)  # time:  0.044002532958984375


# output:
# ---------------------------------------------------------------------------
# wget www.sohu.com host...
# wget www.sina.com.cn host...
# wget www.163.com host...
# ..........
# ........
# time:  0.04000210762023926