#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-27 17:32:25

'''
tuple 元组  不可变列表
    
example:
    objects = ( 1, 2, [ 'a', 'b' ], 'd' )
    tuples = 'e', 'a', 'b', 'c', 'd'
    
API:
    1、tuple[index]    取值
    2、tuple[start:end]    切片取值
    3、(value, )    构建一个值的tuple
    4、tuple1 + tuple2    连接两个元组，并集
    5、del tmp    删除定义的元组对象
    6、len(tuple)    元组长度
    7、tuple * Number    将元组复制Number次
    8、el in tuple / el not in tuple     判断元素是否在元组中
    9、for x in tuple: print(x)        遍历
    
    10、tuple.count(el)    统计元素出现次数
    11、tuple.index(el, start, end)    统计元素首次出现位置，可以设置起止索引
    12、max(tuple)    找到最大的元素
    13、min(tuple)    找到最小的元素
    14、tuple([el, el1, el...])    list转tuple元组
'''

# tuple 和 list 雷同，但是它创建数据后不能随意修改
classes = ( 1, 2, 3)
print('classes: ', classes)

#构建元组
classes2 = 'e', 'a', 'b', 'c', 'd'
print('classes2: ', classes2)

# TypeError: 'tuple' object does not support item assignment
# classes[1] = 4
# AttributeError: 'tuple' object has no attribute 'append'
# classes.append(4)

# 取值方法，用索引下标的方式
print('first element:', classes[1]);
print('last element:', classes[-1]);

# 分片获取数据
print('classes[0:2]:', classes[0:2])
print('classes[0:-2]:', classes[0:-2])
print('classes[1:]:', classes[1:])

# 定义一个元素的tuple, 必须带一个 逗号，不然python不知道是否是运算操作
tmp = (1, )
print(type(tmp))

tmp = (1)
print(type(tmp))

tmp = ()
print(type(tmp))

# 并集
tuple1 = ( 1, 2, 3 )
tuple2 = tuple1 + ( 'a', 'b' )
print(tuple2)

# 删除对象
del tmp
# print('del tmp:', tmp) # NameError: name 'tmp' is not defined

# 元组的长度
print('classes length:', len(classes))

# 复制
print('classes * 3:', classes * 3)

# 判断元素是否存在元组中
print('3 in classes:', 3 in classes)
print('a not in classes:', 'a' not in classes)

# 循环遍历
for x in classes:
    print(x)
    
print('------------------内置函数--------------------')
strs = 'e', 'a', 'b', 'c', 'e', 'a', 'e'
print('统计元素出现次数：', strs.count('e'))
print('查找元素所在索引位置：', strs.index('e'))
print('查找元素所在索引位置：', strs.index('e', 2))
print('查找元素所在索引位置：', strs.index('e', 5, 15))     

print('max:', max(strs))
print('min:', min(strs))

print('list to tuple:', tuple([ 1, 2, 3, 5 ]))