#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo

'''
### 可迭代对象赋值给多个变量
'''

# 统计平均分，去掉最高低分
def drop_first_last(grades):
    first, *middle, last = grades
    return avg(middle)

def avg(args):
    total = 0
    for val in args:
        total += val
    
    return total / len(args)

print('平均分：', drop_first_last([100, 2, 5, 9, 33, 1]))


# 去掉部分数据
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phones = record
print('name: ', name) # Dave
print('email: ', email) # dave@example.com

# phones 列表类型的，无论phones数据包含几个元素
print('phones: ', phones) # ['773-555-1212', '847-555-1212']

#--------------------------------------------------
record = ('773-555-1212', '847-555-1212', 'Dave', 'dave@example.com')
*phones, name, email = record
print('name: ', name) # Dave
print('email: ', email) # dave@example.com

# phones 列表类型的，无论phones数据包含几个元素
print('phones: ', phones) # ['773-555-1212', '847-555-1212']


#--------------------------------------------------
'''
注意：
*trailing 是一个多数据集
trailing 则是 tuple 元组
'''
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(*trailing) # 10, 8, 7, 1, 9, 5, 10
print(trailing) # [10, 8, 7, 1, 9, 5, 10]
print(current) # 3


# 扩展的迭代解压语法是专门为解压不确定个数或任意个数元素的可迭代对象而设计的
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo:', x, y)

def do_bar(s):
    print('bar:', s)
    
for type, *args in records:
    if type == 'foo':
        do_foo(*args)
    if type == 'bar':
        do_bar(*args)    