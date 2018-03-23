#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-23 22:41:40
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> chmod` example


import os
import stat


# 更改权限
'''
概述
    os.chmod() 方法用于更改文件或目录的权限。
语法
    chmod()方法语法格式如下：
    os.chmod(path, mode)
参数
path -- 文件名路径或目录路径。
flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用
mode -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， 
    执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，
    文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
    stat.S_IXOTH: 其他用户有执行权0o001
    stat.S_IWOTH: 其他用户有写权限0o002
    stat.S_IROTH: 其他用户有读权限0o004
    stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
    
    stat.S_IXGRP: 组用户有执行权限0o010
    stat.S_IWGRP: 组用户有写权限0o020
    stat.S_IRGRP: 组用户有读权限0o040
    stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
    
    stat.S_IXUSR: 拥有者具有执行权限0o100
    stat.S_IWUSR: 拥有者具有写权限0o200
    stat.S_IRUSR: 拥有者具有读权限0o400
    stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
    
    stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
    stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
    stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
    
    stat.S_IREAD: windows下设为只读
    stat.S_IWRITE: windows下取消只读
'''

# 其他用户赋予权限
print('其他用户赋予权限')
print('赋予执行权：%s' % os.chmod('/tmp/open.txt', stat.S_IXOTH))
print('赋予写权限：%s' % os.chmod('/tmp/open.txt', stat.S_IWOTH))
print('赋予读权限：%s' % os.chmod('/tmp/open.txt', stat.S_IROTH))
print('赋予全部权限：%s' % os.chmod('/tmp/open.txt', stat.S_IRWXO))


print('组用户赋予权限')
print('赋予执行权：%s' % os.chmod('/tmp/open.txt', stat.S_IXGRP))
print('赋予写权限：%s' % os.chmod('/tmp/open.txt', stat.S_IXGRP))
print('赋予读权限：%s' % os.chmod('/tmp/open.txt', stat.S_IXGRP))
print('赋予全部权限：%s' % os.chmod('/tmp/open.txt', stat.S_IXGRP))


print('拥有者赋予权限')
print('赋予执行权：%s' % os.chmod('/tmp/open.txt', stat.S_IXUSR))
print('赋予写权限：%s' % os.chmod('/tmp/open.txt', stat.S_IWUSR))
print('赋予读权限：%s' % os.chmod('/tmp/open.txt', stat.S_IRUSR))
print('赋予全部权限：%s' % os.chmod('/tmp/open.txt', stat.S_IRWXU))

print('-----------------')
print('目录里文件目录只有拥有者才可删除更改：%s' % os.chmod('/tmp/open.txt', stat.S_ISVTX))
print('执行此文件其进程有效组为文件所在组：%s' % os.chmod('/tmp/open.txt', stat.S_ISGID))
print('执行此文件其进程有效用户为文件所有者：%s' % os.chmod('/tmp/open.txt', stat.S_ISUID))

print('windows下设为只读赋予权限')
print('windows下设为只读：%s' % os.chmod('/tmp/open.txt', stat.S_IREAD))
print('windows下取消只读：%s' % os.chmod('/tmp/open.txt', stat.S_IWRITE))
