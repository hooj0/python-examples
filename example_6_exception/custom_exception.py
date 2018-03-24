#!/usr/bin/env python
# encoding: utf-8
# Created on 2018-03-20
# @author: hoojo

class MyError(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)  
    
    
try:
    raise MyError('boom!')
except MyError as e: # 捕获自定义异常
    print('炸裂', e.value)    