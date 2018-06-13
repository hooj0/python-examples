#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


'''
概述
    os.stat_float_times() 方法用于决定stat_result是否以float对象显示时间戳。

语法
    stat_float_times()方法语法格式如下：
    os.stat_float_times([newvalue])

参数
    newvalue -- 如果为 True, 调用 stat() 返回 floats,如果 False, 调用 stat 返回 ints。如果没有该参数返回当前设置。

返回值
        返回 True 或 False。
'''

st = os.stat('/tmp/foo.txt')
print('stat: %s' % st)

st = os.stat_float_times()
print('stat_float_times: %s' % st)

print('stat: %s' % os.stat('/tmp/foo.txt'))

###########################################################
st = os.stat_float_times()
print('stat_float_times: %s' % st)

print('stat: %s' % os.stat('/tmp/foo.txt'))