#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-10-29
# @author: hoojo

'''
以下类型是指对象类型，也就是数据在内存中的类型；

六个标准的数据类型：
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Sets（集合）
    Dictionaries（字典）
    
    1、Numbers：
        int、float、bool、complex（复数）
    2、String：
        'str'、"str2"
    3、List:
        [ 'element1', 'element2', 'element..' ]
    4、Tuple：
        ( a, b, c, ... )
    5、Sets:
        set([ 1, 2, 3, .... ])
    6、Dict:
        { 1: 'a', 2: 'b', 3: 'c', ....}

数据类型有：整型、浮点型、字符串、布尔类型、空值类型、复数类型

'''

a, b, c, d = 2, 3.12, False, 2.1 + 3j
print(type(a), type(b), type(c), type(d))   

s1, s2 = 'haha', r"wowow\r\n"
print(type(s1), type(s2)) 

list = [ 1, 2, 3, 4 ]
print(type(list))

tuple = ('a', 'b', 'c')
print(type(tuple))

set = set([2, 3, 4])
print(type(set))

dict = { 1: 45, 2: '33', "name": 'jack' }
print(type(dict))