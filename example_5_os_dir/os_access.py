#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
import os


# 检验权限模式
'''
语法
    access()方法语法格式如下：
        os.access(path, mode);
            
           参数
    path -- 要用来检测是否有访问权限的路径。
    mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
        os.F_OK: 作为access()的mode参数，测试path是否存在。
        os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
        os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
        os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
'''

print('是否存在：%s ' % os.access('/tmp', os.F_OK)) # True
print('是否可读：%s ' % os.access('/tmp', os.R_OK)) # True
print('是否可写：%s ' % os.access('/tmp', os.W_OK)) # True
print('是否可执行：%s ' % os.access('/tmp', os.X_OK)) # True

print('是否存在：%s ' % os.access('/tmp/open.txt', os.F_OK)) # True
print('是否可读：%s ' % os.access('/tmp/open.txt1', os.R_OK)) # False 文件不存在，不可读
print('是否可写：%s ' % os.access('/tmp/open.txt', os.W_OK)) # True
print('是否可执行：%s' % os.access('/tmp/open.txt', os.X_OK)) # False # txt 文件不能执行
print('是否可执行：%s' % os.access('/tmp/open.sh', os.X_OK)) # True # *.sh 文件可以执行


print('是否可执行可写可读：%s' % os.access('/tmp/open.sh', os.X_OK|os.W_OK|os.R_OK)) # True # *.sh 文件可以执行