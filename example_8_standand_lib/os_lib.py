#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


print('当前位置：%s' % os.getcwd())

# 显示所有属性和方法
print('dir: %s' % dir(os))

# 显示该包的帮助手册
print(help(os))

# 显示某个方法帮助手册
print(help(os.chdir))

print(os.path)
print(os.name)
print(os.curdir)
print(os.pardir)

# 切换目录
os.chdir('c:\\')

# 调用系统命令
os.system('ping www.baidu.com -t')

# 调用系统命令
os.system('mkdir haha')

os.system('del haha')