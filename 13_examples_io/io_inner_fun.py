#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-11-19
# @author: hoojo

'''
文件操作内置函数
       
    1、file.close()
                    关闭文件。关闭后文件不能再进行读写操作。
    
    2、file.flush()
                    刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
    
    3、file.fileno()
                    返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
    
    4、file.isatty()
                    如果文件连接到一个终端设备返回 True，否则返回 False。
    
    5、file.next()
                    返回文件下一行。
    
    6、file.read([size])
                    从文件读取指定的字节数，如果未给定或为负则读取所有。
    
    7、file.readline([size])
                    读取整行，包括 "\n" 字符。
    
    8、file.readlines([sizehint])
                    读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大, 因为需要填充缓冲区。
    
    9、file.seek(offset[, whence])
                    设置文件当前位置
    
    10、file.tell()
                    返回文件当前位置。
    
    11、file.truncate([size])
                    截取文件，截取的字节通过size指定，默认为当前文件位置。
    
    12、file.write(str)
                    将字符串写入文件，没有返回值。
    
    13、file.writelines(sequence)
                    向文件写入一个序列字符串列表，如果需要换行则要自己加入每行的换行符。           
'''

try:
    file = open('/tmp/open.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open.txt', 'wb')
    except:
        print('not open file')
    
try:
    print('file open:', file)
    file.write('new line content')
    # 刷新文件内部缓冲，立即写入到文件
    file.flush()
    
    #print('文件下一行:', file.next())

    # 文件当前位置
    print('tell:', file.tell())
    
    # 文件描述符
    print('fileno:', file.fileno())
    
    file.write('再写一行！')
    
    file.writelines(['又是一行文件', '再来一行'])
    # 文件当前位置
    print('tell:', file.tell())
    
    print('isatty:', file.isatty())
    
    file.seek(0)
    print('truncate: ', file.truncate(20))

    # 设置文件当前位置
    print('tell:', file.tell())
    
    print('truncate: ', file.truncate(40))
except NameError as e:
    print('error:', e)    
else:
    file.close()
    print('file colse:', file)
        