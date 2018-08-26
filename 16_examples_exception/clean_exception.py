#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-20 22:29:37
# @copyright by hoojo@2018
# @changelog Added python3 `exception->clean exception` example


try:
    raise KeyboardInterrupt
except:
    print('exception!')
finally:
    print('clean！')    
    
    
    
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print('zero error:', e)
    else:
        print('result:', result)
    finally:
        print('divide execute finish!')             
    
    
divide(10, 1)
'''
result: 10.0
divide execute finish!
'''

divide(10, 0)
'''
zero error: division by zero
divide execute finish!
'''

divide('10', '2')
'''
error
'''  


for line in open("myfile.txt"):
    print(line, end="")
# 以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。


# 关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法:
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
# 以上这段代码执行完毕后，就算在处理过程中出问题了，文件 f 总是会关闭      