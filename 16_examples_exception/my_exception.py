#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-20 22:03:33
# @copyright by hoojo@2018
# @changelog Added python3 `exception -> my exception` example


class Error(Exception):
    '''base excption module'''
    pass

class InputError(Error):
    '''
    input error extends Error exception module

    Attribute:
        exception 异常信息
        message 自定义信息
    '''
    
    def __init__(self, exception, message):
        self.exception = exception
        self.message = message
        
        
class OutputError(Error):
    '''
    output exception extends Error exception module
    
    Attribute:
        prev 前一个输出内容 
        next 下一个输出内容
        message 消息内容
    '''        
    
    def __init__(self, prev, next, message):
        self.prev = prev
        self.next = next
        self.message = message
        

try:
    raise InputError('input error code', 'raise input exception!')
except InputError as e:
    print('捕获到异常：', e.exception, '，消息：', e.message)   
    

try:
    raise OutputError('first message', 'current message', 'output exception!')
except OutputError as e:
    print('prve：', e.prev, ', next: ', e.next, ', exception: ', e.message)         
        