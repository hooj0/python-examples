#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
 list 有序集合/有序列表

example：
    names = [ 'jack', 'jason', 'tom' ]

特点：
    1、有序
    2、支持随意添加、删除
    3、速度比dict数据字典、set要慢
    
API：
    1、len(list)     list长度，元素数量
    2、list[+-index]     取值
    3、 list.append(el)    添加新元素
    4、list.insert(index, el)    在list的index插入元素，如果存在就替换；当索引比长度还大时，元素会添加到末尾
    5、list.pop()    删除末尾的元素
    6、list.pop(index)    删除index位置的元素
    7、list + list2    两个list进行拼接
    8、list[start:end]    对list进行分割切片
    9、el in list, el not in    判断el是否在list中出现
    10、list.sort(key=None, reverse=True)     对list进行排序
    11、sorted(list)     对list进行排序
    12、del list[index]     删除指定index位置的元素
    13、list[index] = 'last element'     对已知存在的元素进行赋值，index必须是存在元素的下标
    14、list[start:end] = []    删除某个区间的元素
    15、list[start:end] = [ el, el2, el...]    将某个区间的元素进行覆盖（start:end存在就覆盖）或插入
    16、list.clear()  list[:] = []     清空元素
    
    17、del list_ref    删除指定list对象
    18、list * Number    将list复制指定次数Number
    19、list.copy()    浅复制
    20、list.count(el)    判断el元素出现的次数
    21、max(list)    找到最大的元素
    22、min(list)    找到最小的元素
    23、list.index(el, start, end)    判断el元素首次出现的下标索引，start/end可不传，不包含end位置
    24、list.extend(iter)     继承某个集合，合并一个新的list
    25、list.remove(el)    删除一个存在的元素，每次仅删除一个
    26、list.reverse()    倒序，按照默认插入先后顺序倒序
'''


# 创建一个list
names = [ 'jack', 'jason', 'lily', 'tom', 'coco' ]
print('user names: ', names)

# len() 获取list长度
print('user count: ', len(names))

# 通过索引、下标 访问；索引从0开始
print('first user: ', names[0])
print('three user: ', names[2])

# 当索引越界超出长度就会出现错误
# print('unknow user: ', names[10])

# -1 获取最后一个元素
print('last user: ', names[-1])
print('last 2 user: ', names[-2])

# append 添加新的元素
names.append('charry')
print('names: ', names)

# insert 插入元素到指定索引位置
names.insert(2, 'blom')
print('names:', names)
# 当索引比长度还大时，元素会添加到末尾
names.insert(12, 'blom2')
names.append('charry2')
print('names:', names)

# 对已知存在的元素进行赋值
names[len(names) - 1] = 'last element'
print('names:', names)

# pop 删除末尾的元素
names.pop()
# 删除指定索引位置的元素 pop(index)
names.pop(3)
print('names: ', names)

# 删除指定索引位置的元素
del names[0]
print('del names[0]', names)

# 不同类型的元素的list
objects = [ 1, 'user', [ '5', '6'] ]
print('objects:', objects)
print('objects[0]:', objects[0])
print('objects[-1][1]:', objects[-1][1])

# list 进行叠加，会出现并集结果
list1 = [ 1, 3, 5 ]
list2 = list1 + [ 2, 4, 8 ]
print('list2: ', list2)

# list[index-start, index-end] 对列表进行分片处理，同字符串分片一样，不包含截止下标的元素
list = [ 0, 1, 2, 3, 4, 5 ]
print('list[2:5]:', list[2:5])
print('list[2:-1]:', list[2:-1])
print('list[2:-1]:', list[2:-2])
# 从3开始，到最后
print('list[2:-1]:', list[3:])
# 输出全部元素
print('list[:]:', list[:])

# 删除某个区间的元素
print('remove list before:', list)
list[1:2] = []
print('remove list after:', list)

# 在指定区间插入值，如果区间有元素将被覆盖
list[1:3] = [ 'a', 'b', 'c', 'd' ]
print('list[1:3] = [...]:', list)

# 判断list中是否存在某个元素
print('1 in list ->', 1 in list)
print('3 not in list ->', 3 not in list)

# list 进行排序
list = [5, 3, 6, 2, 1, 9, 0]
list.sort()
print('list sort:', list)

# 倒序
list.sort(key=None, reverse=True)
print('list sort reverse:', list)

list = sorted([5, 3, 6, 2, 1, 9, 0])
print('list sort:', list)

# 清空元素
list.clear()
list[:] = []

print("------------------------------------------")
# 删除对象list
del list

list = [5, 3, 6, 2, 1, 9, 0, 2, 3, 1]
# 复制
print('list * 3:', list * 3)

L = list.copy()
L.append('5')
print('list.copy', L)
print(list)

# 元素出现次数
print('count(el):', list.count(2))
# 元素首次出现的下标
print('index(el):', list.index(2))
print('index(el):', list.index(2, 5))
print('index(el):', list.index(1, 8, 11))

# 最大元素和最小元素
print('max:', max(list))
print('min:', min(list))

# 继承某个list集合，相当于两个集合进行拼接
list.extend(L)
print('list.extend', list)

list.remove(0)
#list.remove('a') # ValueError: list.remove(x): x not in list
print('list remove:', list)

list.reverse()
print('reverse: ', list)

