#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-03-23 22:28:54
# @copyright by hoojo@2018
# @changelog Added python3 `os dir -> chflags` example


import os


# 设置路径的标记为数字标记。
'''
path -- 文件名路径或目录路径。
flags -- 可以是以下值：
    stat.UF_NODUMP: 非转储文件
    stat.UF_IMMUTABLE: 文件是只读的
    stat.UF_APPEND: 文件只能追加内容
    stat.UF_NOUNLINK: 文件不可删除
    stat.UF_OPAQUE: 目录不透明，需要通过联合堆栈查看
    stat.SF_ARCHIVED: 可存档文件(超级用户可设)
    stat.SF_IMMUTABLE: 文件是只读的(超级用户可设)
    stat.SF_APPEND: 文件只能追加内容(超级用户可设)
    stat.SF_NOUNLINK: 文件不可删除(超级用户可设)
    stat.SF_SNAPSHOT: 快照文件(超级用户可设)
'''

print('非转储文件：%s' % os.chflags('/tmp/open.txt', stat.UF_NODUMP))