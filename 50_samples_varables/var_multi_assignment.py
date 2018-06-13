#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo


# 多变量赋值
# 唯一的前提就是变量的数量必须跟序列元素的数量是一样的

### tuple
data = ('a', 2, ('b', 10.2))

a, b, c = data
print('a: ', a)
print('b: ', b)
print('c: ', c)
print()

###list

data = [ 'a', 2, ('c', 2.2) ]

a, b, c = data
print('a: ', a)
print('b: ', b)
print('c: ', c)
print()


###进一步赋值
a, b, (c, d) = data
print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print()

### 字符串赋值
data = '1234'

a, b, c, d = data
print('a: ', a)
print('b: ', b)
print('c: ', c)
print('d: ', d)
print()

### 占位符赋值；解压一部分，丢弃其他的值
data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]
_, a, b, _ = data
print('a: ', a)
print('b: ', b)