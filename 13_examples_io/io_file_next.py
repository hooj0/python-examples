#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-21 22:42:09
# @copyright by hoojo@2018
# @changelog Added python3 `io -> file next` example


try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
# next 读取文件内容      
try:
    print('next 读取内容')
    for index in range(5):
        line = next(file)
        print('读取文件 %s 第 %d 行，内容：%s' % (file.name, index, line))
    
    # 指针移动到0
    file.seek(0)
    
    print('read 读取内容')
    # 读取10 个字节
    print('read(10): %s' % file.read(10))
    
    file.seek(0)
    # 负则读取所有
    print('read(-10): %s' % file.read(-10))
    
except NameError as e:
    print('error:', e)    
else:
    file.close()
    print('file colse:', file)
    

  
