#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-21 18:38:51
# @copyright by hoojo@2018
# @changelog Added python3 `in out->io print` example


# print.py

'''
print 输出流 

    将文本内容输出到控制台，在默认情况下。
    如果设置了file会把内容输出到指定的地方，如：文件中。
'''

import sys

# 直接输入内容
print("i like python") #i like python
# 中间的 “,” 会用空格进行输出，相当于是拼接字符串
print("i like python,", 'you ?') #i like python, you ?
# "\n" 就是换行
print("i like python,\nyou ?") 
#i like python,
#you ?

# 多个字符串拼接输出
print("I", "like", 'python', "\n", "you?")
#I like python 
# you?
 
# 传递数字或变量
print("10 + 1 =", 10 + 1) #10 + 1 = 11

# 设置分隔符，默认的是‘ ’空格；设置结束符号，默认是 '\n'
print('a', 'b', 'c', sep = ', ', end = '! \n') #a, b, c! 
print('a', 'b', 'c', sep = ', ', end = '! \n', file = sys.stdout, flush = True) #a, b, c! 

# 设置打印内容输出流，默认是 sys.stdout，输出到屏幕控制台；
# open(path, mode) 可以指定输出到文件中，path 指定路径，mode = w 表示写入且每次覆盖，a 表示追加写入，+ 表示指针移到末尾行
print('a', 'b', 'c', sep = ', ', end = '! \n', file = open(r'c:\a.txt', 'w'), flush = True)
print('a2', 'b2', 'c2', sep = ', ', end = '! \n', file = open(r'c:\a.txt', 'a+'), flush = True)
print('a3', 'b3', 'c3', sep = ', ', end = '! \n', file = open(r'c:\a.txt', 'a+'), flush = False)

input("按任意键退出")
