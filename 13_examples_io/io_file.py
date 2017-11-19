#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-19 13:23:57
# @copyright by hoojo@2018
# @changelog Added python3 `io -> file overview` example


'''
文件操作


    打开文件
    open(filename, mode)
            第一个参数为要打开的文件名。
            第二个参数描述文件如何使用的字符。
        mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除清空内容), 和 'a' 用于追加文件内容; 
                     所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。
                     
        'r'       open for reading (default)
        'w'       open for writing, truncating the file first
        'x'       create a new file and open it for writing
        'a'       open for writing, appending to the end of the file if it exists
        'b'       binary mode
        't'       text mode (default)
        '+'       open a disk file for updating (reading and writing)
        'U'       universal newline mode (deprecated)
             
                     
    读文件
    f.read()
           为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
    size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
    
    f.readline()
          会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
          
    f.readlines() 将返回该文件中包含的所有行。
           如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。       
          
           
     写文件
    f.write()
           将 string 写入到文件中, 然后返回写入的字符数。非字符串字符需要进行转换。
  
     读取位置         
    f.tell()
           返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
  
     移动位置         
    f.seek()
           如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。
    from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，
           例如：
        seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
        seek(x,1) ： 表示从当前位置往后移动x个字符
        seek(-x,2)：表示从文件的结尾往前移动x个字符     
    
    
     关闭释放文件        
    f.close()
           在文本文件中 (那些打开文件的模式下没有 b 的), 只会相对于文件起始位置进行定位。
           当你处理完一个文件后, 调用 f.close() 来关闭文件并释放系统的资源。
        
-------------------------------------------------------------------------------------------------    

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

# 打开文件-----------------------------------------------------
'''
# 打开一个文件，文件不存发生在异常
openf = open('f:/open.txt')
print('file open:', openf)

# 默认mode = r，w 是写入模式，并且指针移动到文件头部会清空里面的内容
writef = open('f:/write.txt', 'w')
print('file write:', writef)

# 创建新文件并打开写入，文件已存在会发生异常
new = open('f:/new.txt', 'x')
print('file new:', new)

# 打开文件并追加内容，不存在会自动创建
appendf = open('f:/append.txt', 'a')
print('file append:', appendf)

# 读写模式，文件不存发生在异常
updating = open('f:/updating.txt', 'r+')
print('file updating:', updating)

# 二进制模式，组合使用 读二进制、写二进制
binary = open('f:/binary.txt', 'wb')
print('file binary:', binary)

# 文本模式
text = open('f:/text.txt', 'wt')
print('file text:', text)
'''

# 创建新文件--------------------------------------------------
tmp = open('f:/tmp.txt', 'r+')
print('fileno:', tmp.fileno())

# 写文件 -----------------------------------------------------
tmp.write('This is a new line\n')
tmp.write('This is a new line2\n')
tmp.write('This is a new line3')
tmp.write('This is a new line4')

tmp.write('新行内容')

# 其他非字符串内容需要转换
tmp.write(str([1, 'a', 'c', ('aaa', 'bbb')]))

# 读文件 -----------------------------------------------------
# 读取10个字节
print('read 10 byte:', tmp.read(10))
# 读取所有内容
print(tmp.read())

# 取得文件指针位置
print('指针位置：', tmp.tell())

# 移动指针位置
print('移动指针位置：', tmp.seek(0))
print('指针位置：', tmp.tell())

print('-----------------------')
# 读取一行
print(tmp.readline())

# 读取当前指针后的所有内容，列表方式返回
print(tmp.readlines())

# 关闭释放 -------------------------------------------------
tmp.close()