#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-19 22:20:05
# @copyright by hoojo@2018
# @changelog Added python3 `varables -> var assignment process` example


from _collections_abc import ItemsView

#===============================================================================
# 示例：可迭代对象赋值给多个变量
#===============================================================================


#-------------------------------------------------------------------------------
# 统计平均分，去掉最高低分
#-------------------------------------------------------------------------------
def drop_first_last(grades):
    first, *middle, last = grades
    # 只计算middle，去掉first和last
    return avg(middle)

def avg(args):
    total = 0
    for val in args:
        total += val
    
    return total / len(args)

print('平均分：', drop_first_last([100, 2, 5, 9, 33, 1]))


#-------------------------------------------------------------------------------
# 去掉部分数据
#-------------------------------------------------------------------------------
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# 获取 name、email
name, email, *phones = record
print('name: ', name) # Dave
print('email: ', email) # dave@example.com

# phones 列表类型的，无论phones数据包含几个元素
print('phones: ', phones) # ['773-555-1212', '847-555-1212']



#-------------------------------------------------------------------------------
# 只取最后两个数据
#-------------------------------------------------------------------------------
record = ('773-555-1212', '847-555-1212', 'Dave', 'dave@example.com')
*phones, name, email = record
print('name: ', name) # Dave
print('email: ', email) # dave@example.com

# phones 列表类型的，无论phones数据包含几个元素
print('phones: ', phones) # ['773-555-1212', '847-555-1212']


#-------------------------------------------------------------------------------
# 注意：
#     *trailing 是一个多数据集
#     trailing 则是 tuple 元组
#-------------------------------------------------------------------------------
*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(*trailing) # 10, 8, 7, 1, 9, 5, 10
print(trailing) # [10, 8, 7, 1, 9, 5, 10]
print(current) # 3，最后一个元素


#===============================================================================
# 扩展的迭代解压语法
#        是专门为解压不确定个数或任意个数元素的可迭代对象而设计的
#===============================================================================
records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo:', x, y)

def do_bar(s):
    print('bar:', s)

# 取到第一个元素，作为类型，进行分别处理    
for type, *args in records:
    if type == 'foo':
        do_foo(*args)
    if type == 'bar':
        do_bar(*args)    
print()
        
        
#=======================================================================
# 星号解压语法
#        在字符串操作的时候也会很有用，比如字符串的分割。
#=======================================================================
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
usr, *others, dir, sh = line.split(':')

print('usr: ', usr)
print('dir: ', dir)
print('sh: ', sh)
print()


#-------------------------------------------------------------------------------
### 占位符赋值；解压一部分，丢弃其他(一个或多个)的值
#-------------------------------------------------------------------------------
data = [ 'ACME', 50, 91.1, (2012, 12, 21), 'last' ]
_, a, b, *_ = data
print('a: ', a) # 50
print('b: ', b) # 91.1


#-------------------------------------------------------------------------------
# 简单递归
#-------------------------------------------------------------------------------
def sum(items):
    first, *args = items
    # a if x > y else b 三元运算，返回 a or b ，条件取决于 x > y 的比较
    return first + sum(args) if args else first

print('sum: ', sum([1, 3, 5, 7, 9]))
