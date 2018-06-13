#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-11-11
# @author: hoojo
from _collections import deque

'''
列表：有序
堆栈：先进后出
队列：先进先出

元组和序列：
集合：集合是一个无序不重复元素的集
字典：

'''

# 将列表当做堆栈使用，结合append、pop方法，达到先进后出的目的
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print('stack:', stack)

print('stack:', stack.pop()) # 3
print('stack:', stack.pop()) # 2

# 将列表当作队列使用
queue = deque([1, 2, 3, 4])
queue.append(5)
queue.append(6)
# 添加到最前面
queue.appendleft(-1)

print('queue:', queue)
# 弹出最前面的
print('queue.popleft:', queue.popleft())
print('queue.popleft:', queue.popleft())
# 弹出最后面的
print('queue.popleft:', queue.pop())
print('queue:', queue)

# 添加到最前面
queue.extendleft([ 'a', 'b', 'c' ])
print('queue:', queue)
print()

# 列表推导式
list  = [ 1, 3, 5 ]
print('list:', [ x * 3 for x in list ])

print('list:', [ [x, x + 1, x * 3] for x in list ])

# 调用一些方法
words = [ ' hi ', ' python ', ' good ' ]
print('list:', [ x.strip() for x in words ])

# 过滤
print('list:', [ x for x in list if x > 2 ])

# 循环嵌套
foo = [1, 2, 3]
bar = [4, 5, 6]
print('foo * bar:', [ x * y for x in foo for y in bar ])
print('foo + bar:', [ x + y for x in foo for y in bar ])

print('round：', [str(round(355/113, i)) for i in range(1, 6)])

list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [9, 4, 1]
]

print('4x3:', [ [rows[i] for rows in list] for i in range(3) ])

area = []
for i in range(3):
    area.append([rows[i] for rows in list])
print('area:', area)    

# 元组和序列
tmp = 'a', 'b', 'c'
print('tmp:', tmp)
print('tmp[0]:', tmp[0])

foo = tmp, (1, 2, 3)
print('foo:', foo)

# 集合：可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
foo = { 'a', 'b', 'c', 'a', 'd', 'c' }
print('foo:', foo) # 去掉重复的元素

# 集合也支持推导式
bar = {x for x in 'abracadabra' if x not in 'ab'}
print('bar:', bar)

user = { 'name': 'jack', 'age': 25 }
print('dict user:', user)

tmp = { x: x ** 2 for x in (3, 6, 9) }
print('dict-tmp:', tmp)

# 遍历技巧

#遍历字典结构，在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
for k, v in user.items():
    print(k, '->', v)

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到    
for i, v in enumerate(foo):
    print(i, '->', v)
    
for i, v in enumerate(foo):
    print(i, '->', v)    
    
# 同时遍历两个或更多的序列，可以使用 zip() 组合：
for a, b in zip([ 1, 2, 3 ], [ 'a', 'b', 'c' ]):
    print('index:{0}, value:{1}'.format(a, b))
        