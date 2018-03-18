#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-18 16:38:08
# @copyright by hoojo@2018
# @changelog Added python3 `exception -> exception` example


try:
    x = int(input('请输入一个数字：'))
except: # 捕获任意异常
    print('你输入的是一个非数字字符')
        

try:
    int('a')
except ValueError: # 捕获指导异常
    print('类型错误')


try:
    int('a')
except ValueError as e: # 转换异常数据
    print('类型错误: ', e)
    
try:
    #int('a')
    int(a)
except (RuntimeError, TypeError, NameError, ValueError) as e: # 捕获多个异常
    print('发生多个异常: ', e)  
    
    
import sys

# 多次捕获异常
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise # 未知异常，再次抛出         


# try except 语句还有一个可选的else子句，如果使用这个子句，那么必须放在所有的except子句之后。
# 这个子句将在try子句没有发生任何异常的时候执行
try:
    arg = '/a.py'
    f = open(arg, 'r') # 发生异常，else不被执行
except IOError:
    print('cannot open', arg)
else:
    print(arg, 'has', len(f.readlines()), 'lines')
    f.close()
    
try:
    f = int('1') # 没有异常，else被执行
except:
    print('cannot open', f)
else:
    print('input number ', f)
    
    