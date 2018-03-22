#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-22 22:49:15
# @copyright by hoojo@2018
# @changelog Added python3 `io -> file write` example


try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
try:
    
    file.truncate() # 清空文件内容

    # 指针移动到最开始位置
    file.seek(0, 0)
    
    print('1-tell: ', file.tell())
    
    file.write('This is a new line\n')
    file.write('This is a new line2\n')
    file.write('This is a new line3\n')
    file.write('This is a new line4\n')
    file.write('This is a new line5\n')
          
    # 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。       
    file.seek(0, 0)       
    print('readline: %s' % file.readline())
    print('2-tell: ', file.tell())
    
    # 代表从文件末尾算起
    file.seek(0, 2)    
    file.write('This is a new line666\n')
    
    # 读取所有
    file.seek(0, 0)   
    print('readline: %s' % file.read(-1))
    
except NameError as e:
    print('error:', e)    
else:
    file.close()
    print('file colse:', file)    
    

  
