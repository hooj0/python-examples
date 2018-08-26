#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-14 22:47:58
# @copyright by hoojo@2018
# @changelog Added python3 `pkg modules->modules->module center` example


import keyword

module_name = 'module_center'

print('module name：', __name__)

def say(content):
    print('you say:', content)
    
def kw():
    print('key word:', keyword.kwlist)   
    
def min_value(*args):
    print('min:', min(args))    