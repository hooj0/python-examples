#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-20 21:18:56
# @copyright by hoojo@2018
# @changelog Added python3 `exception -> raise exception` example


# 抛出异常
#raise NameError('无效名称')

# 捕获抛出的异常
try:
    raise NameError('无效名称')
except NameError as e:
    print('捕获到异常：', e)
    raise