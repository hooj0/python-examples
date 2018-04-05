#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-05 22:13:33
# @copyright by hoojo@2018
# @changelog Added python3 `standand lib -> timeit lib` example


import timeit


print(help(timeit))

# 计算耗时
print(timeit.Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(timeit.Timer('a,b = b,a', 'a=1; b=2').timeit())

print(timeit.Timer('lambda x, y: x + y', 'x=10; y=5').timeit())

print(timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit())

print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

print(timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))

print(timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"'))


t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
print(t.timeit())
print(t.repeat(repeat = 3)) # 重复定时器的次数，每次结果以数组形式返回

s = '''\
for i in range(10):
    print(i)
print('done!')    
'''
# 执行一段代码 number=2 次
print(timeit.timeit(stmt=s, number=2))