#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-11-04
# @author: hoojo

'''
类型转换

函数                                                                描述
int(x [,base])            将x转换为一个整数
float(x)                  将x转换到一个浮点数
complex(real [,imag])     创建一个复数
str(x)                    将对象 x 转换为字符串
repr(x)                   将对象 x 转换为表达式字符串
eval(str)                 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                  将序列 s 转换为一个元组
list(s)                   将序列 s 转换为一个列表
set(s)                    转换为可变集合
dict(d)                   创建一个字典。d 必须是一个序列 (key,value)元组。
chr(x)                    将一个整数转换为一个字符
ord(x)                    将一个字符转换为它的整数值
hex(x)                    一个整数转换为一个十六进制字符串
oct(x)                    将一个整数转换为一个八进制字符串            
'''

# int类型转换
print('int(n)', int('123') + 1)
print('int(n)', int('123', base = 10) + 1)
print('int(n)', int('10', base = 36) + 1)

# float类型转换
print('float(n)', float('123') + 1)
print('float(n)', float(30) + 1)

# complex 复数转换
print('complex:', complex(34.6))

# 字符串转换
print('str:', str(12.34))
print('str:', str(tuple('abcdefg')) + 'oh')

# 表达式转换
print('repr:', repr('0 == 1'))

# 元组转换
print('tuple:', tuple('ab1cd2of3'))
print('tuple:', tuple([1, 2, 3]))

# list 列表转换
print('list:', list('abcd'))
print('list:', list(tuple('ab1cd2of3')))

# set 集合转换
print('set:', set('abcabefg'))
print('set:', set([1, 2, 3]))

# dict字典转换
print('dict:', dict([ tuple('ab'), tuple('cd') ]))

# 整数转字符
print('chr:', chr(66))

# 字符转整数
print('ord:', ord('A'))

# 整数转16进制字符串
print('hex:', hex(66))
print('hex:', hex(136))

# 整数转8进制
print('oct:', oct(66))
print('oct:', oct(96))

# 类型转换
print(bool(1))
print(bool(0))
print(bool(''))