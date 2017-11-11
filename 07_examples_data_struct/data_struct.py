#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-11 23:05:07
# @copyright by hoojo@2018
# @changelog Added python3 `data struct->data struct` example


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

print('stack:', stack) # stack: [1, 2, 3]

print('stack:', stack.pop()) # 3
print('stack:', stack.pop()) # 2

# 将列表当作队列使用
queue = deque([1, 2, 3, 4])
queue.append(5)
queue.append(6)
# 添加到最前面
queue.appendleft(-1)

print('queue:', queue) # queue: deque([-1, 1, 2, 3, 4, 5, 6])
# 弹出最前面的
print('queue.popleft:', queue.popleft()) # queue.popleft: -1
print('queue.popleft:', queue.popleft()) # queue.popleft: 1
# 弹出最后面的
print('queue.popleft:', queue.pop()) # queue.popleft: 6
print('queue:', queue) # queue: deque([2, 3, 4, 5])

# 添加到最前面
queue.extendleft([ 'a', 'b', 'c' ])
print('queue:', queue) # queue: deque(['c', 'b', 'a', 2, 3, 4, 5])
print()

# 列表推导式
list  = [ 1, 3, 5 ]
print('list:', [ x * 3 for x in list ]) # list: [3, 9, 15]

print('list:', [ [x, x + 1, x * 3] for x in list ]) # list: [[1, 2, 3], [3, 4, 9], [5, 6, 15]]

# 调用一些方法
words = [ ' hi ', ' python ', ' good ' ]
print('list:', [ x.strip() for x in words ]) # list: ['hi', 'python', 'good']

# 过滤
print('list:', [ x for x in list if x > 2 ]) # list: [3, 5]

# 循环嵌套
foo = [1, 2, 3]
bar = [4, 5, 6]
print('foo * bar:', [ x * y for x in foo for y in bar ]) # foo * bar: [4, 5, 6, 8, 10, 12, 12, 15, 18]
print('foo + bar:', [ x + y for x in foo for y in bar ]) # foo + bar: [5, 6, 7, 6, 7, 8, 7, 8, 9]

print('round：', [str(round(355/113, i)) for i in range(1, 6)]) # round： ['3.1', '3.14', '3.142', '3.1416', '3.14159']

list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [9, 4, 1]
]

print('4x3:', [ [rows[i] for rows in list] for i in range(3) ]) # 4x3: [[1, 4, 7, 9], [2, 5, 8, 4], [3, 6, 9, 1]]

area = []
for i in range(3):
    area.append([rows[i] for rows in list])
print('area:', area) # area: [[1, 4, 7, 9], [2, 5, 8, 4], [3, 6, 9, 1]]   

# 元组和序列
tmp = 'a', 'b', 'c'
print('tmp:', tmp)       # tmp: ('a', 'b', 'c')
print('tmp[0]:', tmp[0]) # tmp[0]: a

foo = tmp, (1, 2, 3)
print('foo:', foo)  # foo: (('a', 'b', 'c'), (1, 2, 3))

# 集合：可以用大括号({})创建集合。注意：如果要创建一个空集合，你必须用 set() 而不是 {} ；后者创建一个空的字典
foo = { 'a', 'b', 'c', 'a', 'd', 'c' }
print('foo:', foo) # 去掉重复的元素 foo: {'c', 'd', 'b', 'a'}

# 集合也支持推导式
bar = {x for x in 'abracadabra' if x not in 'ab'}
print('bar:', bar) # bar: {'c', 'd', 'r'}

user = { 'name': 'jack', 'age': 25 }
print('dict user:', user) # dict user: {'name': 'jack', 'age': 25}

tmp = { x: x ** 2 for x in (3, 6, 9) }
print('dict-tmp:', tmp) # dict-tmp: {3: 9, 6: 36, 9: 81}

# 遍历技巧

#遍历字典结构，在字典中遍历时，关键字和对应的值可以使用 items() 方法同时解读出来
for k, v in user.items():
    print(k, '->', v) # name -> jack

# 在序列中遍历时，索引位置和对应值可以使用 enumerate() 函数同时得到    
for i, v in enumerate(foo):
    print(i, '->', v) # 0 -> c
    
for i, v in enumerate(foo):
    print(i, '->', v)    
    
# 同时遍历两个或更多的序列，可以使用 zip() 组合：
for a, b in zip([ 1, 2, 3 ], [ 'a', 'b', 'c' ]):
    print('index:{0}, value:{1}'.format(a, b)) # index:1, value:a
        