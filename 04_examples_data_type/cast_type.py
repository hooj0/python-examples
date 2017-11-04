#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-04 20:46:17
# @copyright by hoojo@2018
# @changelog Added python3 `data type->cast type` example


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
print('int(n)', int('123') + 1) # int(n) 124
print('int(n)', int('123', base = 10) + 1) # int(n) 124
print('int(n)', int('10', base = 36) + 1)  # int(n) 37

# float类型转换
print('float(n)', float('123') + 1) # float(n) 124.0
print('float(n)', float(30) + 1) # float(n) 31.0

# complex 复数转换
print('complex:', complex(34.6)) # complex: (34.6+0j)

# 字符串转换
print('str:', str(12.34)) # str: 12.34
print('str:', str(tuple('abcdefg')) + 'oh') # str: ('a', 'b', 'c', 'd', 'e', 'f', 'g')oh

# 表达式转换
print('repr:', repr('0 == 1')) # repr: '0 == 1'

# 元组转换
print('tuple:', tuple('ab1cd2of3')) # tuple: ('a', 'b', '1', 'c', 'd', '2', 'o', 'f', '3')
print('tuple:', tuple([1, 2, 3])) # tuple: (1, 2, 3)

# list 列表转换
print('list:', list('abcd')) # list: ['a', 'b', 'c', 'd']
print('list:', list(tuple('ab1cd2of3'))) # list: ['a', 'b', '1', 'c', 'd', '2', 'o', 'f', '3']

# set 集合转换
print('set:', set('abcabefg')) # set: {'b', 'g', 'c', 'f', 'a', 'e'}
print('set:', set([1, 2, 3])) # set: {1, 2, 3}

# dict字典转换
print('dict:', dict([ tuple('ab'), tuple('cd') ])) # dict: {'a': 'b', 'c': 'd'}

# 整数转字符
print('chr:', chr(66)) # chr: B

# 字符转整数
print('ord:', ord('A')) # ord: 65

# 整数转16进制字符串
print('hex:', hex(66)) #hex: 0x42
print('hex:', hex(136)) #hex: 0x88

# 整数转8进制
print('oct:', oct(66)) # oct: 0o102
print('oct:', oct(96)) # oct: 0o140

# 类型转换
print(bool(1)) # True
print(bool(0)) # False
print(bool('')) # False