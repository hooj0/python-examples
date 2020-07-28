#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-23 21:03:13
# @copyright by hoojo@2018
# @changelog Added python3 `variable -> variables` example


# ===============================================================================
#     variable 变量
# ===============================================================================
# 描述：变量是存储任何类型数据的一种媒介
# -------------------------------------------------------------------------------
# API：
#    del var    删除变量
#    del var, var2, varN...    删除多个变量
#    a = b = c = 1    多个变量赋值
#    a, b, c = 1, 'a', False
# -------------------------------------------------------------------------------
#  变量 用大小写字母、_、数字进行表示，且不能用 数字开头
#  常量，由全大写字符串和下划线、数字组成
# -------------------------------------------------------------------------------


# 纯小写字符变量
a = '123'
print('var a =', a)     # var a = 123

# 不能以数字开头
# 23b = 'no think'
# print('', 23b)

# 大小写混合变量
Name = 'python'
print('var Name =', Name)   # var Name = python

# 带_组合变量
user_age = 22
print('var user_age =', user_age)   # var user_age = 22

# 带_和数字、字母组合变量
t_0 = -1
print('var t_0 =', t_0)     # var t_0 = -1

# _ 下划线开头变量
_super = 2
print('var _super =', _super)   # var _super = 2

__self = 2
print('var _super =', __self)   # var _super = 2

print()

# 常量，由全大写字符串和下划线、数字组成 
MAX_COUNT = 20
print('MAX_COUNT =', MAX_COUNT) # MAX_COUNT = 20
print()

# 删除变量
del MAX_COUNT
del user_age, Name

# 多个变量赋值
a = b = c = 5
print(a, b, c)  # 5 5 5

a, b, c = 1, 'a', False
print(a, b, c)  # 1 a False