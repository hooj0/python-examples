#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 17:52:12
# @copyright by hoojo@2018
# @changelog Added python3 `object -> class` example


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

成员有以下：
    1、字段：   静态字段 普通字段
    2、方法：  静态方法 类方法 普通方法
    3、特性/属性 普通特性

成员修饰符  修饰成员
公有的：没有限制
私有的：以__开头 仅仅内部可以访问，不能被继承，仅自己可访问。私有的成员可通过公有的成员间接访问

何时用类调用，何时用对象调用？
类调用： 无self
对象调用：self

结论：
    1、静态字段和静态方法和类方法通过类来访问，普通字段和方法通过对象来访问
    2、静态方法，使用@staticmethod来装饰
    3、类方法，使用@classmethod来装饰
    4、属性（特性），使用@property来装饰，定义的时候类似普通方法一样，但调用的时候像普通字段一样
    5、属性的getter和setter，通过@property来装饰的方法return来getter，之后通过@方法名.setter装饰的方法来setter

一些特殊的成员：
    __init__ 构造方法，创建对象时调用
    __del__ 析构方法，销毁对象时调用
    __call__ 对象() 调用
    __getitem__ 对象[] 来调用
    __setitem__ 对象[] = xxx 来调用
    __delitem__ del 对象[] 来调用
    __dict__ 列出所有的成员 用途：在表单对象中获取表单所有的字段
    参考字典对象dict
    __str__ 类似java中的toString方法，直接打印对象输出的就是该方法的返回值
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





class Province:
    country = "中国"  # 静态字段，在类中保存，将对象中共有的字段和值可以保存到静态字段
    def __init__(self, name):
        self.name = name  # 普通字段

    @staticmethod
    def xxoo(arg1, arg2): # 静态方法
        print(arg1, arg2)

    @classmethod
    def xo(cls):  # 类方法  会将类传递过来
        print(cls)

    @property
    def xx(self):  # 属性（特性），将方法伪装成字段  getter
        # print("property")
        return self.val

    @xx.setter
    def xx(self, value):  
        self.val = value


hubei = Province("湖北")
print(hubei.__dict__)
print(Province("福建").__dict__)
print(Province.__dict__)
print(Province.country)   # 静态字段通过类来访问
Province.xxoo("hello", "hi")  # 静态方法通过类来访问
Province.xo()  # 类方法通过类来访问
hubei.xx = "property1"  # 属性的setter
print(hubei.xx)  #属性调用 getter