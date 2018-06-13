#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import glob
import os

# 显示方法帮助文档手册
print(help(glob))

print(glob.escape('c://a**?//*b*/c?/d')) # c://a[*][*][?]//[*]b[*]/c[?]/d


# 搜索当前目录下的*.py后缀的文件
print(glob.glob('*.py', recursive=True)) # ['glob_lib.py', 'os_lib.py', 'shutil_lib.py', 'sys_lib.py']

# 搜索路径包含lib字符的文件
os.chdir('F:\Example Exercise\Python')
print(glob.glob('*lib*', recursive=False)) # ['example_8_standand_lib']

print(glob.iglob('*.py', recursive=True)) # <generator object _iglob at 0x00000000029A3B48>