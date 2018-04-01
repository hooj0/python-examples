#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 18:36:32
# @copyright by hoojo@2018
# @changelog Added python3 `object -> method` example


class Person:
    ''' 定义基本属性 '''
    name = 'lucy'
    age = 22
    
    ''' 定义私有属性，外部无法访问 '''
    __height = 166
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.__height = height
        
    ''' 定义方法，访问私有属性和基本属性 '''    
    def info(self):
        print('I am name is %s, age %s , height %s' % (self.name, self.age, self.__height))    


person = Person('zhangsan', 33, 187)

person.info()

# 私有属性不能访问
# print(person.__height)

        