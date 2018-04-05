#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-05 22:02:22
# @copyright by hoojo@2018
# @changelog Added python3 `standand lib -> zlib lib` example


import zlib


'''
直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile
'''

s = b'witch which has which witches wrist watch'
print('un compress length: %s' % len(s))

# 压缩
s = zlib.compress(s)
print('compress length: %s' % len(s))

# 解压缩
s = zlib.decompress(s)
print('compress length: %s' % len(s))

# 加密
print('crc32： %s' % zlib.crc32(s))
print('adler32： %s' % zlib.adler32(s))