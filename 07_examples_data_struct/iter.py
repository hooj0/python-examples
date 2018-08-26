#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-04 18:34:40
# @copyright by hoojo@2018
# @changelog Added python3 `data struct->iter` example


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