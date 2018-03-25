#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-25 12:06:31
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> lchflags` example


import os

'''
概述
  os.lchflags() 方法用于设置路径的标记为数字标记，类似 chflags()，但是没有软链接。
    只支持在 Unix 下使用。

语法
    lchflags()方法语法格式如下：
    os.lchflags(path, flags)

参数
    path -- 设置标记的文件路径
    flags -- 可以由一个或多个标记组合，多个使用"|"隔开：
    UF_NODUMP: 非转储文件
    UF_IMMUTABLE: 文件是只读的
    UF_APPEND: 文件只能追加内容
    UF_NOUNLINK: 文件不可删除
    UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
    SF_ARCHIVED: 可存档文件(超级用户可设)
    SF_IMMUTABLE: 文件是只读的(超级用户可设)
    SF_APPEND: 文件只能追加内容(超级用户可设)
    SF_NOUNLINK: 文件不可删除(超级用户可设)
    SF_SNAPSHOT: 快照文件(超级用户可设)

返回值
    该方法没有返回值。
'''

# 打开文件
path = "/tmp/foo.txt"
fd = os.open( path, os.O_RDWR|os.O_CREAT )

# 关闭文件
os.close( fd )

# 修改文件标记
ret = os.lchflags(path, os.UF_IMMUTABLE )

print ("修改文件标记成功!!")