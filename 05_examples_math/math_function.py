#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-05 13:37:21
# @copyright by hoojo@2018
# @changelog Added python3 `math->math function` example


import math
from random import choice, randrange, random, seed, shuffle, uniform
from math import sin, acos, asin



'''
---------------------------------数学函数------------------------------------
函数                                                                                                                  返回值 ( 描述 )
abs(x)                                    返回数字的绝对值，如abs(-10) 返回 10
ceil(x)                                   返回数字的上入整数，如math.ceil(4.1) 返回 5
exp(x)                                    返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)                                   返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)                                  返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)                                    如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)                                  返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)                           返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)                           返回给定参数的最小值，参数可以为序列。
modf(x)                                   返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)                                 x**y 运算后的值。
round(x [,n])                             返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)                                   返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j

---------------------------------随机数函数------------------------------------
函数                                                                                                                        描述
choice(seq)                                从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])          从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()                                   随机生成下一个实数，它在[0,1)范围内。
seed([x])                                  改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)                               将序列的所有元素随机排序
uniform(x, y)                              随机生成下一个实数，它在[x,y]范围内。

---------------------------------三角函数------------------------------------
函数                                                                                                                        描述
acos(x)                                   返回x的反余弦弧度值。
asin(x)                                   返回x的反正弦弧度值。     
atan(x)                                   返回x的反正切弧度值。
atan2(y, x)                               返回给定的 X 及 Y 坐标值的反正切值。
cos(x)                                    返回x的弧度的余弦值。
hypot(x, y)                               返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)                                    返回的x弧度的正弦值。
tan(x)                                    返回x弧度的正切值。
degrees(x)                                将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)                                将角度转换为弧度

'''

print('PI:', math.pi) # 3.141592653589793
print('E:', math.e)   # 2.718281828459045  

print('---------------------数学函数------------------------')
# 绝对值 abs
print('abs:', abs(-10)) # 10
print('abs:', abs(10))  # 10
print('abs:', abs(-10.2))   # 10.2

# 上入整数
print('math.ceil:', math.ceil(4.1)) # 5
print('math.ceil:', math.ceil(4.9)) # 5

# 下舍整数
print('math.floor:', math.floor(4.9)) # 4
print('math.floor:', math.floor(4.5)) # 4
print('math.floor:', math.floor(4.1)) # 4

# 返回e的x次幂(ex)
print('math.exp:', math.exp(2)) # 7.38905609893065

# 返回数字的绝对值
print('math.fabs:', math.fabs(-10.4))   # 10.4
print('math.fabs:', math.fabs(10.4))    # 10.4

# log
print('math.log:', math.log(math.e))    # 1.0
print('math.log:', math.log(math.pi))   # 1.1447298858494002
print('math.log:', math.log(100, 10))   # 2.0
print('math.log:', math.log(1000, 10))  # 2.9999999999999996

# max
print('max:', max(1, 3))    # 3
print('max:', max(1, 3, 2, 9, 5)) # 9

# min
print('min:', min(1, 3)) # 1
print('min:', min(1, 3, 2, 9, 5)) # 1

# 将一个浮点数的整数和小数进行拆分
print('modf:', math.modf(1.2))  # (0.19999999999999996, 1.0)
print('modf:', math.modf(35.27)) # (0.2700000000000031, 35.0)

# 乘方
print('math.pow:', math.pow(2, 2)) # 4.0
print('math.pow:', math.pow(2, 4)) # 16.0

# round 四舍五入
print('round:', round(4.234)) # 4
print('round:', round(4.634)) # 5
print('round:', round(4.534)) # 5

# 保留2位小数
print('round:', round(4.23512, 2))  # 4.23
# 保留3位小数
print('round:', round(4.6344511, 3)) #4.634
# 3位小数
print('round:', round(math.pi, 3))  # 3.142

# sqrt 求平方根
print('math.sqrt:', math.sqrt(4))   # 2.0
print('math.sqrt:', math.sqrt(10))  # 3.1622776601683795

print('---------------------随机数函数------------------------')
# 从序列的元素中随机挑选一个元素
print('choice:', choice(range(10))) # 5
print('choice:', choice([ 'a', 3, 'b', 'd', 5 ])) # choice: 5   
print('choice:', choice(('a', 3, 'b', 'd', 5))) # choice: 3

# 从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
print('randrange:', randrange(1))       # randrange: 0
print('randrange:', randrange(1, 10))   # randrange: 8
print('randrange:', randrange(1, 10, 3))
print('randrange:', randrange(1, 10, 3))
print('randrange:', randrange(1, 10, 3))

# 随机生成下一个实数，它在[0,1)范围内。
print('random:', random())  # random: 0.7803577704521725
print('random:', random())  # random: 0.9502681500134833
print('random:', math.floor(random() * 100)) # random: 70

# 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
print('seed:', seed())  # seed: None

# 将序列的所有元素随机排序
numbers = [1, 2, 3, 4, 5, 6]
shuffle(numbers)
print('shuffle:', numbers)  # shuffle: [4, 2, 1, 3, 6, 5]
shuffle(numbers)
print('shuffle:', numbers)  # shuffle: [1, 4, 2, 3, 6, 5]
strs = list('abcdefg') 
shuffle(strs)
print('shuffle:', strs)     # shuffle: ['d', 'f', 'g', 'e', 'c', 'b', 'a']

# 随机生成下一个实数，它在[x,y]范围内。
print('uniform:', uniform(2, 9))    # uniform: 7.317168189627886
print('uniform:', uniform(2, 9))    # uniform: 2.09607801330631

print('---------------------三角函数------------------------')
# 返回的x弧度的正弦值。
print('sin:', sin(90))
print('sin:', sin(180))
print('sin:', sin(360))

# 返回x的反余弦弧度值。
print('acos:', acos(0.893996663))
# 返回x的反正弦弧度值。   
print('asin:', asin(0.9589157234143065))  
# 返回x弧度的正切值。
print('tan:', math.tan(45))
# 返回x的弧度的余弦值。
print('cos:', math.cos(45))
# 返回x的反正切弧度值。
print('atan:', math.atan(1.6197751905438615))
# 返回给定的 X 及 Y 坐标值的反正切值。
print('atan2:', math.atan2(16, 15))
# 返回欧几里德范数 sqrt(x*x + y*y)。
print('hypot:', math.hypot(3*3, 5*5))
# 将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
print('degrees:', math.degrees(math.pi/2))
# 将角度转换为弧度
print('radians:', math.radians(90))