#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-03 21:05:08
# @copyright by hoojo@2018
# @changelog Added python3 `object -> private` example


class Private:
    
    __name = '私有属性'
    
    def __print(self):
        print('私有方法')
        
    def println(self):
        print(self.__name)
        
pri = Private()

# 私有属性无法访问
# print(pri.__name)

# 私有方法无法访问
# pri.__print()

# 公有方法访问私有属性
pri.println()



#测试私有属性、私有方法
class Employee:
    __company = 'xxx公司'      #私有类属性，通过dir可以查到_Employee__company
    
    def __init__(self,name,age):
        self.name = name
        self.__age = age      #私有实例属性

    def __work(self):     #私有实例方法，通过dir可以查到_Employee__work
        print('好好工作，努力赚钱')

    def say_company(self):
        print('我的公司是：',Employee.__company)    #类内部可以直接访问私有属性，通过类名.属性名
        print(self.name,'年龄是：',self.__age)
        self.__work()

p = Employee('jack',18)
print(p.name)
print(dir(p))
p.say_company()
print(p._Employee__age)     #通过这种方式可以直接访问到私有属性
p._Employee__work()         #通过这种方式可以直接访问到私有方法

#print(p.__age)         #直接访问私有属性报错
#p.__work()             #直接访问私有方法报错        