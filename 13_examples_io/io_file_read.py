#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-21 22:55:55
# @copyright by hoojo@2018
# @changelog Added python3 `io -> file read` example


try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
# read 读取内容      
try:
    # 读取10 个字节
    print('read(10): %s' % file.read(10))
    
    # 指针移动到0
    file.seek(0)
    # 负则读取所有
    print('read(-10): %s' % file.read(-10))
    
    file.seek(0)
    #  读取整行
    line = file.readline()
    print('read line: %s' % (line))
    
    file.seek(0)
    #  读取3个字节
    line = file.readline(3)
    print('read 3 line: %s' % (line))
    
    file.seek(0)
    # 读取所有行
    lines = file.readlines()
    for line in lines:
        print('read lines: %s' % (line))
        
    print('当前位置：%d' % file.tell())    
    
    file.seek(0)
    print('当前位置：%d' % file.tell())
        
    # 读取3个字节的行
    lines = file.readlines(3)
    for line in lines:
        print('read 3 lines: %s' % (line))
except NameError as e:
    print('error:', e)    
else:
    file.close()
    print('file colse:', file)
    

  
