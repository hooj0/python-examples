#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-05 10:41:26
# @copyright by hoojo@2018
# @changelog Added python3 `standand lib -> re lib` example


import re

# 找到所有匹配的字符
print(re.findall(r'f[a-z]*', 'which foot or hand fell fastest')) # ['foot', 'fell', 'fastest']

# 转换表达式
print(re.escape(r'f[a-z]*')) # f\[a\-z\]\*

# 找到不重复的字符串
print(re.sub(r'([a-z]+) \1', r'\1', 'cat in the the hat')) #cat in the hat

# iter
iter = re.finditer(r'f[a-z]*', 'which foot or hand fell fastest')
for item in iter:
    print((item))
print()    

# 查找首个匹配的字符串
print(re.search(r'f[a-z]*', 'which foot or hand fell fastest'))

# match
print(re.match(r'f[a-z]*', 'which foot or hand fell fastest'))

# 拆分字符串
print(re.split(r'f[a-z]*', 'which foot or hand fell fastest'))

print(re.split(r' ', 'which foot or hand fell fastest'))
# 最大分割2个字符串
print(re.split(r' ', 'which foot or hand fell fastest', 2))

compile = re.compile(r'f[a-z]*', 0)
