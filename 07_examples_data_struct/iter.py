#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-11-04
# @author: hoojo
from symbol import except_clause
import sys

'''
迭代器

特点：    
    1、对任意集合进行迭代遍历
    2、只能向前不能后退

example：
    iter = iter({ 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) })
        使用iter()方法进行构造    
API：
    next() 下一个元素
'''


# iter 构造迭代器
it = iter({ 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) })

# next下一个元素
print('next element:', next(it))
print('next element:', next(it))

list = [1, 3, 2, 5]
# 循环遍历
it = iter(list)
for el in it:
    print('iter el:', el, end = ',\t')
print()    

# 循环遍历
it = iter(list)
while True:
    try:
        print(next(it))
    except Exception:
        print('exit')
        sys.exit()    