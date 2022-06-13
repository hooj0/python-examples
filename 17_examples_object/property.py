#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-03 21:05:08
# @copyright by hoojo@2018
# @changelog Added python3 `object -> @property` example

'''
	@property装饰器-get和set方法
	@property 可以将一个方法的调用方式变成“属性调用”
	@property 主要用于帮助我们处理属性的读操作、写操作。
		对于某一个属性，我们可以直 接通过： emp.salary = 30000
'''

#简单测试@property
class Employee:
    @property
    def salary(self):
        return 20000

emp = Employee()
print(emp.salary)    #方法salary()转为了属性调用
print(type(emp.salary))    #<class 'int'>

#emp.salary()        #报错：TypeError: 'int' object is not callable
#emp.salary = 2000    #@property修饰的属性如果没有加setter方法，则为只读属性。报错：AttributeError: can't set attribute


#测试@property
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary   #私有属性

    @property         #相当于salary属性的getter方法
    def salary(self):
        print('月薪为：{}，年薪为：{}'.format(self.__salary,12*self.__salary))
        return self.__salary

    @salary.setter    #相当于salary属性的setter方法
    def salary(self,salary):
        if(0<salary<100000):
            self.__salary = salary
        else:
            print('薪水录入错误，只能在0-100000之间')

emp = Employee('jack',10000)
print(emp.salary)
emp.salary = 0