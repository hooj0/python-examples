#!/usr/bin/env python
# -*- coding: utf-8 -*-

#################################################
#                   range 序列                                                 #
#################################################
'''
range 函数 可以生成一个list集合
	
example：
	range(5) -> 生成0 到 4的整数集合	
	range(1, 5) -> 生成 1到4的整数序列集合
	range(1, 10, 2) -> 生成1到9，每个元素+2的序列集合
	
range 函数像是一个for 循环，它可以有循环的起止位置和步长	
'''

# 生成指定截止区间的整数集合
print('range(5): ', end = '')
ranges = range(5)
for x in ranges:
	print(x, end = '; ')
print()
	
# 生成指定区间，带有起始位置的序列集合	
print('range(3, 7): ', end = '')
ranges = range(3, 7)
for x in ranges:
	print(x, end = '; ')
print()

# 生成指定区间，带有起始位置，并且有步长的序列集合	
print('range(3, 11, 2): ', end = '')
ranges = range(3, 11, 2)
for x in ranges:
	print(x, end = '; ')
print()

