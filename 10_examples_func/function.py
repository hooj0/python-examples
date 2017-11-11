#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-11 17:29:46
# @copyright by hoojo@2018
# @changelog Added python3 `func -> function` example


import string

'''
函数
    可以重复调用执行的代码片段
    
语法：
        
        定义函数：
    def function_name(args):
        do something...

        执行函数：
    function_name(values)
    
参数

以下是调用函数时可使用的正式参数类型：

    必备参数：必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。    
    命名参数：命名参数和函数调用关系紧密，调用方用参数的命名确定传入的参数值。你可以跳过不传的参数或者乱序传参，因为Python解释器能够用参数名匹配参数值
    缺省参数：调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
    不定长参数：你可能需要一个函数能处理比当初声明时更多的参数

'''

# 定义函数（必备参数）
def hello(arg):
    print('hello, ', arg)

# 执行函数
hello('world!')    # hello,  world!
    
# 带返回值的函数
def say(content):
    return 'say ' + content

print('exec say:', say('hi~'))    # exec say: say hi~
    
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


# 缺省参数（age/sex/address 为缺省参数）
def get_user(name, age=23, sex='男', address='china'):
    print('name: %s, age=%s, sex=%s, address=%s' %(name, age, sex, address))

# get_user() name为必传参数    
get_user('jack') # name: jack, age=23, sex=男, address=china
get_user(name = 'tom') # name: tom, age=23, sex=男, address=china
get_user(name = 'jason', age=30) # name: jason, age=30, sex=男, address=china
get_user('jason', address='gz')  # name: jason, age=23, sex=男, address=gz
get_user('jason', 30) # name: jason, age=30, sex=男, address=china
get_user('jason', 16, 'unknown', 'cz') # name: jason, age=16, sex=unknown, address=cz

# 函数返回值（命名参数）
def get_result(y, z):
    x = y + z
    return x

def get_result2(y, z):
    x = y + z
    return

def get_result3(y, z):
    x = y + z
    y = x + z
    return x, y

print('get_result:', get_result(1, 3))
print('get_result2:', get_result2(1, 3))
print('get_result3:', get_result3(1, 3))
print('get_result3:', type(get_result3(1, 3))) #<class 'tuple'>


# 可变参数（不定长参数）
def get_sum(*args):
    sum = 0
    for x in args:
        sum += x
    return sum

print('get_sum:', get_sum())
print('get_sum:', get_sum(2, 5))
print('get_sum:', get_sum(2, 5, 3.3, 6.3)) 

# 可变参数（不定长参数） kw key-value 参数   
'''
*args是可变参数，args接收的是一个tuple；
**kw 是关键字参数，kw接收的是一个dict。
'''
def get_user(name, age, **kw):
    print('name: %s, age=%s, kw=%s' %(name, age, kw))   
     
get_user('tom', 22) #name: tom, age=22, kw={}
get_user('tom', 22, a=2, b=3)   #name: tom, age=22, kw={'a': 2, 'b': 3}    

# 按引用传递参数，传入list值，发现方法里面对list进行操作会影响外部定义的变量
def get_reference(list):
    list.reverse()
    print('list reverse:', list)
    return

list = [ 2, 1, 5, 4 ]
get_reference(list)
print('list:', list)

'''
# lambda 来创建匿名函数
lambda函数的语法只包含一个语句，如下：
lambda [arg1 [,arg2,.....argn]]:expression
'''

sum = lambda x, y: x + y
print('lambda.sum:', sum(3, 4))
print('lambda.sum:', sum(32, 44))

'''
isinstance 判断类型
'''
x = 3
if isinstance(x, (int, float, list)):
    print('x is int/float')
    
    

