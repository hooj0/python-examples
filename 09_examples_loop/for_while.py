#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-28 21:28:42
# @copyright by hoojo@2018
# @changelog Added python3 `loop -> for while` example


'''
遍历循环

for i in list:
    print(i)
    
for i in list:
    print(i)
else:
    print('xxx')
    
while i > 0:
    i += 1
    print(i)
    
'''

names = [ 'jack', 'tom', 'alex', 'charry' ]

# for 循环
for name in names:
    print('element: ', name)
print()

# 通过下标进行迭代循环
for i in range(len(names)):
    print('index: %s, val: %s' % (i, names[i]))
print()    
    
# range 序列函数，range可以生成一个指定区间的list集合    
ints = range(5)    
for i in ints:
    print('i: ', i)         
print()

# for...else...
for w in 'abcdef':
    print(w)
else:
    print('循环结束时执行')    
print()    

# 正常结束会被执行，break中断的不被执行
for x in range(20):
    if x % 3 == 0:
        print('能被3整除', x)
    else:
        break
else:
    print('正常结束会被执行，break不被执行')    
print()
        
users = [ 'json', 'kili', 'M', 'jack' ]
for user in users:
    for name in names:
        if user == name:
            print('找到了', user)
            break
    else:
        print('没有找到')    
print()
    
# while 循环
x = 10
while x > 0:
    print('x: ', x)
    x = x - 1
print(x)  
print()

# while...else
x = 100
sum = 0
while x > 0:
    sum = sum + x
    x = x - 1
else:    
    print(sum)       
print()

# continue continue后的语句不被执行，正常结束else被执行
for i in range(1, 20):
    if i % 17 == 0:
        print('%s %% 7 == 0' % i)
        continue
    print('i ->', i)
else:
    print('else被执行') 
print()

# 站位，不做任何事情
i = 5    
while i > 0:
    i -= 1
    if i == 2:
        pass
        print('pass code line')
    print('i', i)