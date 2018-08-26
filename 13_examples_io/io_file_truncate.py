#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-21 23:10:07
# @copyright by hoojo@2018
# @changelog Added python3 `io->io file truncate` example


try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
file.write('This is a new line\n')
file.write('This is a new line2\n')
file.write('This is a new line3\n')
file.write('This is a new line4\n')
file.write('This is a new line5\n')
            
# read 读取内容      
try:
    file.seek(0);
    print('1-tell: ', file.tell())
    # 读取第一行
    print('readline: %s' % file.readline())
    print('2-tell: ', file.tell())
    
    file.truncate() # 上面的readline后指针移动到第二行，截取的数据将第一行之后的都删除
    print('3-tell: ', file.tell())
    
    file.seek(0);
    print('4-tell: ', file.tell())
    print('file line: %s' % file.readlines()) # 读到的内容和上面的是一样的
    print('5-tell: ', file.tell())
    
except NameError as e:
    print('error:', e)    
    

file.seek(0, 0)
file.write('ABC def ghi jkl mno')
    
# read 读取内容      
try:
    print('1-tell: ', file.tell())
    
    # 读取10个字节，表示0~10个字节保留，其他数据删除
    # 从10 + 1 个位置开始截取后面的所有数据并删除
    file.truncate(10) # 从0开始截取10个字节，如果不传将从当前指针位置截取后面所有数据
    print('2-tell: ', file.tell())

    file.seek(0, 0)
    print('truncate file line: %s' % file.read()) 
    print('3-tell: ', file.tell())
    
except NameError as e:
    print('error:', e)    
else:
    file.close()
    print('file colse:', file)    
    

  
