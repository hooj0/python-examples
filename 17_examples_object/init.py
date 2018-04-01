#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 18:09:37
# @copyright by hoojo@2018
# @changelog Added python3 `object -> init` example


class Student:
    name = 'jack'
    age = 22
    
    ''' 初始化方法，构造方法 ，在实例化创建'''
    def __init__(self):
        self.name = 'jason'
        self.age = 33
        

# 创建实例化，init方法被执行        
stu = Student()
        
print('name: %s, age: %s' % (stu.name, stu.age))    




class Class:
    name = 'calss 1'
    
    # 有参构造函数
    def __init__(self, no, author):
        self.Num = no
        self.Author = author

cla = Class('453122645', 'tom')

print('name: %s' % cla.name)
print('Num: %s, Author: %s' % (cla.Num, cla.Author))    