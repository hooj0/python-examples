#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-05 17:07:34
# @copyright by hoojo@2018
# @changelog Added python3 `standand lib -> random lib` example


import random

print(help(random))

# 随机取数组中一个值
print(random.choice(['apple', 'pear', 'banana'])) #banana

# 随机生成一个长度为10的数组
print(random.sample(range(100), 10)) # [84, 6, 62, 12, 79, 82, 86, 55, 27, 41]

# 产生随机float数
print(random.random()) #0.7395803807672576

# 随机生成一个小于6的随机数
print(random.randrange(6)) # 3

# 随机生成一个数组
print(random.choices(['apple', 'pear', 'banana'])) #['banana']

# 随机生成1~10的整数
print(random.randint(1, 10))

print(random.gauss(3, 10))