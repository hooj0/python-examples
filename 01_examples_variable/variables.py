#!/usr/bin/env python
# -*- coding: utf-8 -*-

# varables.py

'''
#  变量 用大小写字母、_、数字进行表示，且不能用 数字开头
#  常量，由全大写字符串和下划线、数字组成

API：
    del var    删除变量
    del var, var2, varN...    删除多个变量
    a = b = c = 1    多个变量赋值
    a, b, c = 1, 'a', False
'''

# 纯小写字符变量
a = '123'
print('var a =', a)

# 不能以数字开头
# 23b = 'no think'
# print('', 23b)

# 大小写混合变量
Name = 'python'
print('var Name =', Name)

# 带_组合变量
user_age = 22
print('var user_age =', user_age)

# 带_和数字、字母组合变量
t_0 = -1
print('var t_0 =', t_0)

# _ 下划线开头变量
_super = 2
print('var _super =', _super)

__self = 2
print('var _super =', __self)

print()

# 常量，由全大写字符串和下划线、数字组成 
MAX_COUNT = 20
print('MAX_COUNT =', MAX_COUNT)
print()

# 删除变量
del MAX_COUNT
del user_age, Name

# 多个变量赋值
a = b = c = 5
print(a, b, c)

a, b, c = 1, 'a', False
print(a, b, c)
