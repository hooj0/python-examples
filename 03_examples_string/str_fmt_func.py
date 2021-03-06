#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-18 20:41:23
# @copyright by hoojo@2018
# @changelog Added python3 `string->str fmt func` example


import sys

'''
    文件输入输出：
            磁盘文件输出输入
            
            
  输出格式美化
    Python两种输出值的方式: 表达式语句和 print() 函数。(第三种方式是使用文件对象的 write() 方法; 标准输出文件可以用 sys.stdout 引用。)
          如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
          如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    str() 函数返回一个用户易读的表达形式，转换为字符串 可以进行字符串拼接。
    repr() 产生一个解释器易读的表达形式，以转义字符串中的特殊字符。          
'''

# 字符串输出
a = "I'am is python!"
print("str(a):", str(a)) # str(a): I'am is python!

b = dict([ ('a', 10), ('b', 20), ('c', 30) ])
print("str(b):", str(b)) # str(b): {'a': 10, 'b': 20, 'c': 30}

print('path: ' + str(sys.path)) # path: ['F:\\Example Exercise\\Python\\03_examples_string', 'E:\\Python\\Python36\\DLLs', 'E:\\Python\\Python36\\lib', 'E:\\Python\\Python36', 'E:\\Python\\Python36\\lib\\site-packages', 'E:\\Python\\Python36\\lib\\site-packages\\win32', 'E:\\Python\\Python36\\lib\\site-packages\\win32\\lib', 'E:\\Python\\Python36\\lib\\site-packages\\Pythonwin', 'E:\\Python\\Python36\\lib\\site-packages\\setuptools-39.1.0-py3.6.egg', 'E:\\Python\\Python36\\lib\\site-packages\\pip-10.0.1-py3.6.egg', 'E:\\Python\\Python36\\python36.zip']

print('1/7:', 1/7)      # 1/7: 0.14285714285714285
print('1/7:', str(1/7)) # 1/7: 0.14285714285714285

# 表达式输出
print('repr():', repr(a)) # repr(): "I'am is python!"
print('repr():', repr(b)) # repr(): {'a': 10, 'b': 20, 'c': 30}
print('repr():', repr(sys.path))
print('repr 1/7:', type(repr(1/7))) # repr 1/7: <class 'str'>

x = 3 ** 4.2
y = 13 // 3
result = 'x = ' + repr(x) + ', y = ' + repr(y)
print('result:', result)    # result: x = 100.90420610885693, y = 4

result = 'x = ' + str(x) + ', y = ' + str(y)
print('result:', result)    # result: x = 100.90420610885693, y = 4

result = 'hi, python\n\r'
print('str(result):', str(result))  # str(result): hi, python
print('repr(result):', repr(result)) # repr(result): 'hi, python\n\r'

# 格式化输出
for x in range(1, 9):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end = ' ') #  3   9   27
    print(repr(x * x * x).rjust(4))
    
print('--------------------------------------------')    
for x in range(1, 9):
    print('{0:2d}{1:4d}{2:6d}\n'.format(x, x * x, x * x * x)) #  1   1     1
    
