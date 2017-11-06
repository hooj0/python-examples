#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-10-29
# @author: hoojo

'''
set 和dict类似，key集合。set 不能存放value，但key是不可重复的数据

特点：    
    1、key 不可重复，重复的将被过滤
    2、无序
    3、set 可以进行 交集 "&"、差集 "-"、并集"|"、排除交集 "^" 运算

example：
    numbers = set([ 1, 2, 2, 3, 1 ])
    
API:
    1、set.add(el)    添加新元素
    2、set.remove(el)    删除元素
    3、set.clear()    清空元素
    4、set1 & set2    交集
    5、set1 - set2    差集
    6、set1 | set2    并集
    7、set1 ^ set2    排除交集后的元素
'''

# 构造 set，通过set(iterable)方法构造，参数是一个iterable集合
numbers = set([ 1, 2, 2, 3, 1 ])
print('numbers set:', numbers)

numbers = set((2, 2, 4, 5, 1, 4))
print('numbers set:', numbers)

numbers = set({ 2: '', 3: '22', 5: '32' })
print('numbers set:', numbers)


# 添加元素 add，通过add方法添加新元素
numbers.add(6)
print('numbers set:', numbers)

# 删除元素
numbers.remove(6)
print('numbers set:', numbers)

# 清空所有元素
numbers.clear()
print('numbers set:', numbers)

numbers1 = set([ 1, 2, 3, 4 ])
numbers2 = set([ 2, 4, 6, 8 ])

# 求numbers1、numbers2的交集
print('交集:', numbers1 & numbers2) 
print('差集:', numbers1 - numbers2)
print('差集:', numbers2 - numbers1)  
print('并集:', numbers1 | numbers2)
print('排除交集后的元素:', numbers1 ^ numbers2)  

# 字符串直接被构建成set
strs = set('Traceback')
print("set('Traceback')", strs)