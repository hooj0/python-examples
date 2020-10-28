#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-27
# @copyright by hoojo@2020
# @changelog python3 `progress bar` example


# ===============================================================================
# 标题：python3 progress bar example
# ===============================================================================
# 使用：利用python在控制台输出进度条
#
#   pip install progressbar
#
# -------------------------------------------------------------------------------
# 描述：在加载或下载、读取的场景中使用进度条
# -------------------------------------------------------------------------------
from progressbar import *
import time


# help(progressbar)
# -------------------------------------------------------------------------------
# progressbar 使用示例 基本用法
# -------------------------------------------------------------------------------
total = 1000


# 基本用法
def example1():
    progress = ProgressBar()
    for i in progress(range(total)):
        time.sleep(0.01)


# example1()
# output:
# ------------------------------------------------------------------------------
# 62% (627 of 1000) |#############        | Elapsed Time: 0:00:06 ETA:   0:00:03


# -------------------------------------------------------------------------------
# progressbar 使用示例 进阶用法
# -------------------------------------------------------------------------------
def example2():
    pbar = ProgressBar().start()
    for i in range(1, 1000):
        pbar.update(int((i / (total - 1)) * 100))
        time.sleep(0.01)
    pbar.finish()


example2()
# output:
# -------------------------------------------------------------------------------
# | | #                                               | 100 Elapsed Time: 0:00:09


# -------------------------------------------------------------------------------
# progressbar 使用示例 高级用法
# -------------------------------------------------------------------------------
# 高级用法
def example3():
    """
    widgets可选参数含义：
        Progress ：设置进度条前显示的文字
        Percentage() ：显示百分比
        Bar('#') ： 设置进度条形状
        ETA() ： 显示预计剩余时间
        Timer() ：显示已用时间
    """
    widgets = ['Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker('>-=')), ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    for i in range(1000000):
        # do something
        pbar.update(10 * i + 1)
        time.sleep(0.0001)
    pbar.finish()


example3()
# output:
# -------------------------------------------------------------------------------
# Progress:   2% |>                                  | ETA:   0:16:18   9.7 KiB/s