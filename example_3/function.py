#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-11-11
# @author: hoojo

'''
函数
    可以重复调用执行的代码片段
    
语法：
        
        定义函数：
    def function_name(args):
        do something...

        执行函数：
    function_name(values)
'''

# 定义函数
def hello(arg):
    print('hello, ', arg)

# 执行函数
hello('world!')    
    
# 带返回值的函数
def say(content):
    return 'say ' + content

print('exec say:', say('hi~'))    
    
# 函数变量作用域
x = 10
def scope():
    x = 15
    print('scope:', x) # 15

def scope2():
    print('scope2:', x) # 10
    
# 内部的赋值不会影响外部    
scope()
scope2()    


# 形参列表
def get_user(name, age=23, sex='男', address='china'):
    print('name: %s, age=%s, sex=%s, address=%s' %(name, age, sex, address))

# get_user() name为必传参数    
get_user('jack')
get_user(name = 'tom')
get_user(name = 'jason', age=30)
get_user('jason', address='gz')           
get_user('jason', 30)
get_user('jason', 16, 'unknown', 'cz')

# 函数返回值
def get_result(y, z):
    x = y + z
    return x

def get_result2(y, z):
    x = y + z
    return

print('get_result:', get_result(1, 3))
print('get_result2:', get_result2(1, 3))