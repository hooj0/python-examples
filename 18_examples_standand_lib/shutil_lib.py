#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-03 22:15:30
# @copyright by hoojo@2018
# @changelog Added python3 `standand lib -> shutil lib` example


import shutil

print(help(shutil))

print(help(shutil.move))

# 统计使用空间
print(shutil.disk_usage('c:\\Intel')) # usage(total=120031539200, used=83122790400, free=36908748800)

# 移动目录
#shutil.move('C:\Intel\Logs', 'C:\Logs')

# 复制文件
shutil.copy('F:\\foo.txt', 'F:\\foo.txt2')
# copyfile

# 复制目录
# shutil.copytree('C:\Logs', 'C:\Logs4')

# 压缩文件
shutil.make_archive('C:\Logs', 'zip', root_dir='C:\Logs')
# shutil.make_archive('C:\Logs', 'xztar')