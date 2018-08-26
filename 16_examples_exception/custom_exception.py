#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-20 21:38:27
# @copyright by hoojo@2018
# @changelog Added python3 `exception->custom exception` example


class MyError(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)  
    
    
try:
    raise MyError('boom!')
except MyError as e: # 捕获自定义异常
    print('炸裂', e.value)    