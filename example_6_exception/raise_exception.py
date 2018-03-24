#!/usr/bin/env python
# encoding: utf-8
# Created on 2018-03-20
# @author: hoojo

# 抛出异常
#raise NameError('无效名称')

# 捕获抛出的异常
try:
    raise NameError('无效名称')
except NameError as e:
    print('捕获到异常：', e)
    raise