#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-23 23:19:04
# @copyright by hoojo@2018
# @changelog Added python3 `os -> path` example

'''
os.path.isabs(path)  #判断是否为绝对路径
os.path.islink(path)  #判断路径是否为链接
os.path.ismount(path)  #判断路径是否为挂载点（）
os.path.isfile(path)  #判断文件是否存在？如果path是一个存在的文件，返回True。否则返回False。
os.path.isdir(path)  #判断目录是否存在？如果path是一个存在的目录，则返回True。否则返回False。
os.path.exists(path)  #路径存在则返回True,路径损坏返回False
os.path.lexists  #路径存在则返回True,路径损坏也返回True
os.path.samefile(path1, path2)  #判断目录或文件是否相同
os.path.sameopenfile(fp1, fp2)  #判断fp1和fp2是否指向同一文件
os.path.samestat(stat1, stat2)  #判断stat tuple stat1和stat2是否指向同一个文件


os.path.split(path) —— 将全路径分解为(文件夹,文件名)的元组
os.path.splitext(path)  #分割全路径，返回路径名和文件扩展名的元组
os.path.split(path)  #把路径分割成dirname和basename，返回一个元组
os.path.splitdrive(path)   #一般用在windows下，返回驱动器名和路径组成的元组
os.path.splitunc(path)  #把路径分割为加载点与文件


os.path.realpath(path)  #返回path的真实路径
os.path.relpath(path[, start])  #从start开始计算相对路径
os.path.abspath(path) #返回绝对路径（包含文件名的全路径）
os.path.basename(path) —— 去掉目录路径获取(带后缀的)文件名
os.path.dirname(path) —— 去掉文件名获取目录
os.path.join(path1[, path2[, ...]])  #把目录和文件名合成一个路径
os.path.commonprefix(list) #返回多个路径中，所有path共有的最长的路径。


os.path.expanduser(path)  #把path中包含的"~"和"~user"转换成用户目录
os.path.expandvars(path)  #根据环境变量的值替换path中包含的”name”和”{name}”
os.path.normcase(path)  #转换path的大小写和斜杠
os.path.normpath(path)  #规范path字符串形式


os.path.walk(path, visit, arg)  #遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
os.path.supports_unicode_filenames  #设置是否支持unicode路径名


os.path.getatime(path)  #返回最后一次进入此path的时间。
os.path.getmtime(path)  #返回在此path下最后一次修改的时间。
os.path.getctime(path)  #返回修改的时间
os.path.getsize(path)  #返回文件大小，如果文件不存在就返回错误
'''

print(os.sep)     # \ : 获取路径的分割符
print(os.extsep)  # . : 获取文件名与扩展名分割符
print(os.pardir)  # .. :返回上层目录
print(os.curdir)  # . : 当前目录