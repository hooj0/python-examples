#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo

'''
类的专有方法：
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 称方
'''

class Conputer:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # 重载系统方法    
    def __str__(self):
        return 'Conputer(%s, %s)' % (self.a, self.b)
    
    # 重载系统方法    
    def __add__(self, c):
        return Conputer(self.a + c.a, self.b + c.b)
    

c1 = Conputer(1, 3)
print(c1)
c2 = Conputer(-3, 9)
print(c2)

print(c1 + c2)

print(c1 - c2)

    