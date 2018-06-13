#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-11-19
# @author: hoojo
import pickle
import pprint

'''
基本的数据序列和反序列化。
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
'''

data = { 'list': [ 1, 2, 'a', 2.3, 4.3+4j ], 'dict': { 'a': 1, 'b': '222' }, 'tuple': ('a', 233, 666) }
list = [ 'a', '2', 3, 2.2+2j ]
list.append(list)

#序列化----------------------------------------
output = open('f:/serial.txt', 'wb')

pickle.dump(data, output)
pickle.dump(list, output, -1)

output.close()

#反序列化--------------------------------------
output = open('f:/serial.txt', 'rb')

# 加载序列化的数据
data = pickle.load(output)
print('data:', data)

# 格式化输出反序列数据
pprint.pprint(data)
print()

# 加载数据
data2 = pickle.load(output)
print('data2:', data2)

# 格式化输出反序列数据
pprint.pprint(data2)

output.close()
