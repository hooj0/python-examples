#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo


'''
面向对象技术简介

    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    实例变量：定义在方法中的变量，只作用于当前实例的类。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
'''

# 创建一个‘Student’ Class类
class Student:
    ''' student class '''
    name = 'jack'
    age = 22
    
    def getInfo(self):
        return 'student class '
    


# 实例化类
stu = Student()
    
# 访问属性
print('student.name: %s' % stu.name)    
print('student.age: %s' % stu.age)   

# 访问方法
print('student info: %s' % stu.getInfo()) 