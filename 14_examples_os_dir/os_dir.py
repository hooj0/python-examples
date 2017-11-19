#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-19 22:17:16
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> dir` example


import os
import stat


'''
处理文件和目录

    1、os.access(path, mode)
                    检验权限模式
    
    2、os.chdir(path)
                    改变当前工作目录
    
    3、os.chflags(path, flags)
                    设置路径的标记为数字标记。
    
    4、os.chmod(path, mode)
                    更改权限
    
    5、os.chown(path, uid, gid)
                    更改文件所有者
    
    6、os.chroot(path)
                    改变当前进程的根目录
    
    7、os.close(fd)
                    关闭文件描述符 fd
    
    8 os.closerange(fd_low, fd_high)
                    关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
    
    9、os.dup(fd)
                    复制文件描述符 fd
    
    10、os.dup2(fd, fd2)
                    将一个文件描述符 fd 复制到另一个 fd2
    
    11、os.fchdir(fd)
                    通过文件描述符改变当前工作目录
    
    12、os.fchmod(fd, mode)
                    改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
    
    13、os.fchown(fd, uid, gid)
                    修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
    
    14、os.fdatasync(fd)
                    强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。
    
    15、os.fdopen(fd[, mode[, bufsize]])
                    通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
    
    16、os.fpathconf(fd, name)
                    返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
    
    17、os.fstat(fd)
                    返回文件描述符fd的状态，像stat()。
    
    18、os.fstatvfs(fd)
                    返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()
    
    19、os.fsync(fd)
                    强制将文件描述符为fd的文件写入硬盘。
    
    20、os.ftruncate(fd, length)
                    裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
    
    21、os.getcwd()
                    返回当前工作目录
    
    22、os.getcwdu()
                    返回一个当前工作目录的Unicode对象
                    
    23、os.isatty(fd)
                    如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
    
    24、os.lchflags(path, flags)
                    设置路径的标记为数字标记，类似 chflags()，但是没有软链接
    
    25、os.lchmod(path, mode)
                    修改连接文件权限
    
    26、os.lchown(path, uid, gid)
                     更改文件所有者，类似 chown，但是不追踪链接。
    
    27、os.link(src, dst)
                    创建硬链接，名为参数 dst，指向参数 src
    
    28、os.listdir(path)
                    返回path指定的文件夹包含的文件或文件夹的名字的列表。
    
    29、os.lseek(fd, pos, how)
                    设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; 
        SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效
        
    30、os.lstat(path)
                    像stat(),但是没有软链接
    
    31、os.major(device)
                    从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
    
    32、os.makedev(major, minor)
                    以major和minor设备号组成一个原始设备号
    
    33、os.makedirs(path[, mode])
                    递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。
    
    34、os.minor(device)
                    从原始的设备号中提取设备minor号码 (使用stat中的st_dev或者st_rdev field )。
    
    35、os.mkdir(path[, mode])
                    以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。
    
    36、os.mkfifo(path[, mode])
                    创建命名管道，mode 为数字，默认为 0666 (八进制)
    
    37、os.mknod(filename[, mode=0600, device])
                    创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。
    
    38、os.open(file, flags[, mode])
                    打开一个文件，并且设置需要的打开选项，mode参数是可选的
    
    39、os.openpty()
                    打开一个新的伪终端对。返回 pty 和 tty的文件描述符。
    
    40、os.pathconf(path, name)
                    返回相关文件的系统配置信息。
    
    41、os.pipe()
                    创建一个管道. 返回一对文件描述符(r, w) 分别为读和写
    
    42、os.popen(command[, mode[, bufsize]])
                    从一个 command 打开一个管道
    
    43、os.read(fd, n)
                    从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
    
    44、os.readlink(path)
                    返回软链接所指向的文件
    
    45、os.remove(path)
                    删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。
    
    46、os.removedirs(path)
                    递归删除目录。
    
    47、os.rename(src, dst)
                    重命名文件或目录，从 src 到 dst
    
    48、os.renames(old, new)
                    递归地对目录进行更名，也可以对文件进行更名。
    
    49、os.rmdir(path)
                    删除path指定的空目录，如果目录非空，则抛出一个OSError异常。
    
    50、os.stat(path)
                    获取path指定的路径的信息，功能等同于C API中的stat()系统调用。
    
    51、os.stat_float_times([newvalue])
                    决定stat_result是否以float对象显示时间戳
    
    52、os.statvfs(path)
                    获取指定路径的文件系统统计信息
    
    53、os.symlink(src, dst)
                   创建一个软链接
    
    54、os.tcgetpgrp(fd)
                   返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组
    
    55、os.tcsetpgrp(fd, pg)
                   设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。
    
    56、os.tempnam([dir[, prefix]])
                   返回唯一的路径名用于创建临时文件。
    
    57、os.tmpfile()
                   返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。
    
    58、os.tmpnam()
                   为创建一个临时文件返回一个唯一的路径
    
    59、os.ttyname(fd)
                    返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。
    
    60、os.unlink(path)
                    删除文件路径
    
    61、os.utime(path, times)
                    返回指定的path文件的访问和修改的时间。
    
    62、os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
                    输出在文件夹中的文件名通过在树中游走，向上或者向下。
    
    63、os.write(fd, str)
                    写入字符串到文件描述符 fd中. 返回实际写入的字符串长度

'''

# 改变当前工作目录
print('当前目录：', os.getcwd())
print('切换目录：', os.chdir('f:/'))
print('当前目录：', os.getcwd())


# 更改文件所有者
#print('更改文件所有者:', os.chown('f:/tmp.txt', 121, 1))

# 改变当前进程的根目录
#print('改变当前进程的根目录:', os.chroot('f:/'))

# 关闭文件描述符
#fd = os.open('f:/tmp.txt', os.O_RDWR|os.O_CREAT)
'''
fd = open('f:/write.txt', 'r+')
os.write(fd, 'test line')
os.close(fd)
print('关闭文件成功')
'''

# 关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
# 打开文件
fd = os.open("f:/foo.txt", os.O_RDWR|os.O_CREAT)
# 关闭文件
os.closerange(fd, fd)
print ("关闭文件成功!!")

#复制文件描述符 fd
print('复制文件描述', os.dup(os.open("foo.txt", os.O_RDWR|os.O_CREAT)))

#将一个文件描述符 fd 复制到另一个 fd2
print('fd 复制到另一个 fd2', os.dup2(os.open("foo.txt", os.O_RDWR|os.O_CREAT), os.open("foo2.txt", os.O_RDWR|os.O_CREAT)))

#通过文件描述符改变当前工作目录
#print('改变当前工作目录', os.fchdir(os.open("foo.txt", os.O_RDWR|os.O_CREAT)))

#改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
#print(os.fchmod(os.open("foo.txt", os.O_RDWR|os.O_CREAT), stat.S_IREAD))

#修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
#os.fchown(fd, uid, gid)

print('cpu 数量：', os.cpu_count())
print('当前路径：', os.curdir)
print('定义路径：', os.defpath)

# 返回描述终端文件描述符编码的字符串。文件描述符必须附加到终端。 如果设备不是终端，则返回无。
print('文件描述符编码: ', os.device_encoding(os.open("foo.txt", os.O_RDWR|os.O_CREAT)))

print('系统变量：', os.environ)

# 打开文件
fd = os.open("f:/foo.txt", os.O_RDWR|os.O_CREAT)
#通过文件描述符 fd 创建一个文件对象，并返回这个文件对象
'''
参数

fd -- 打开的文件的描述符，在Unix下，描述符是一个小整数。
mode -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
bufsize -- 可选，指定返回的文件对象是否带缓冲：buffersize=0，表示没有带缓冲；bufsize=1，表示该文件对象是行缓冲的；bufsize=正数，表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，对于tty字元设备一般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。
'''
file = os.fdopen(fd, "r", 512)
print(file)

#返回一个打开的文件的系统配置信息。
#name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。
fd = os.open("f:/config.properties", os.O_RDWR|os.O_CREAT)
#print(os.fpathconf(fd, "user"))

# 返回文件描述符fd的状态
print(os.fstat(fd))

#强制将文件描述符为fd的文件写入硬盘。
os.fsync(fd)

#裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。
os.ftruncate(fd, 20)

#如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
print(os.isatty(fd))

#返回path指定的文件夹包含的文件或文件夹的名字的列表
print(os.listdir("f://"))

#设置文件描述符 fd当前位置为pos, how方式修改: SEEK_SET 或者 0 设置从文件开始的计算的pos; 
#SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 

#从开始位置读取字符串
os.lseek(fd, 0, 0)

str = os.read(fd, 100)
print ("Read String is : ", str)

# 递归文件夹创建函数
#os.makedirs('f:/111/222/333')
# 文件夹权限
#os.makedirs('f:/111/222/333', 0755)

print(os.pipe())

