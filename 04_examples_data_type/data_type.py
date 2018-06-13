#!/usr/bin/env python
# -*- coding: utf-8 -*-

# data_type.py

'''
数据类型

    数据类型有：整型、浮点型、字符串、布尔类型、空值类型、复数类型
    
    特点：
    1、都不是不可变数据，不能进行改变内容，但可以改变内存地址指向
    2、都是基本数据类型    
    

int                   float        complex
10                     0.0          3.14j
100                   15.20         45.j
-786                  -21.9         9.322e-36j
080                   32.3+e18    .876j
-0490                  -90.        -.6545+0J
-0x260                 -32.54e100    3e+26J
0x69                   70.2-E12      4.53e-7j    
'''

############## 整数类型 ##############
print('整数：', 0)
print('整数：', 100)
print('整数：', -100)

# 十六进制 ox前缀开头, 0-9/a-f 表示
print('整数：', 0xa100)
print('整数：', 0xa1b0c0f)
print()

'''
输出：
        整数： 0
        整数： 100
        整数： -100
        整数： 41216
        整数： 169544719
'''

############## 长整数 是比较大的整数
print('long:', 0x19323) #long: 103203

############## 浮点型 ##################
print('浮点型：', 31.415 * 10) #浮点型： 314.15
print('浮点型：', 3.1415 * 10) #浮点型： 31.415000000000003
print('浮点型：', -3.1415) #浮点型： -3.1415
# E1小数点向后移动 1 位
print('浮点型：3.1415 x 10^1 =', 3.1415E1) #浮点型：3.1415 x 10^1 = 31.415
# E2小数点向后移动 2 位
print('浮点型：3.1415 x 10^2 =', 3.1415E2) #浮点型：3.1415 x 10^2 = 314.15
# E3小数点向后移动 3 位
print('浮点型：3.1415 x 10^3 =', 3.1415E3) #浮点型：3.1415 x 10^9 = 3141500000.0
print('浮点型：3.1415 x 10^9 =', 3.1415E9) #浮点型：31.415 x 10^8 = 3141500000.0
print('浮点型：31.415 x 10^8 =', 31.415E8) #浮点型：0.1E8 = 10000000.0
print('浮点型：0.1E8 =', 0.1E8) #浮点型：0.1E8 = 10000000.0

# 浮点型 4 + 2 位小数
print('浮点型：0.000123 =', 1.23E-4) #浮点型：0.000123 = 0.000123
# 浮点型 6位小数
print('浮点型：0.000123 =', 123E-6) #浮点型：0.000123 = 0.000123
# 2 位小数
print('浮点型：1.23 =', 123E-2) #浮点型：1.23 = 1.23
print()

################ 字符串 #################
print('字符串：', 'abc') #字符串： abc
print('字符串：', "xyz") #字符串： xyz
print('字符串：', "xy\"z") #字符串： xy"z
print('字符串：', "xy\'z") #字符串： xy'z
print('abcd'[1]) #b

print()

################ 布尔值 ################
print('真：', True) #真： True
print('假：', False) #假： False
# boolean 与 and 或 or 非 not
# and
print('True and False：', True and False) #True and False： False
print('True and True: ', True and True) #True and True:  True

# or
print('True or True: ', True or True) #True or True:  True
print('True or False: ', True or False) #True or False:  True

# not
print('not True: ', not True) #not True:  False
print('not False: ', not False) #not False:  True

print()

################ 空值 ################ 
# 空值 None 表示，不等于 0，没有null

print('空值：', None)
print('空值 == 0：', None == 0)

############## 复数 ##################
print('复数：', 2 + 3j)
print('复数：', 1.1 + 2.2j)

input('按任意键退出')
