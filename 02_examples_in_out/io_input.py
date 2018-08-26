#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-21 18:47:45
# @copyright by hoojo@2018
# @changelog Added python3 `in out->io input` example


# input.py

'''
input输入流

        接受控制台输入参数，参数以字符串形式接受。
 
'''

# input 接收输入参数，可以输入文本
print("plase input your name")
print("your name:", input())

# 变量接收输入参数
name = input("请输入名称：")
print("name:", name)

# 输入之前可以打印输入提示文本
age = input("plase enter your age:")
print("your age:", age)
