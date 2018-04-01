#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-01 16:19:25
# @copyright by hoojo@2018
# @changelog Added python3 `os file -> tcsetpgrp` example


import os


fd = os.open("/dev/tty", os.O_RDONLY)

f = os.tcgetpgrp(fd)
print('tcgetpgrp: %s' % f)

# 设置pgrp
pid = os.fork()
print('pid: %s' % pid)
os.tcsetpgrp(fd, pid)

f = os.tcgetpgrp(fd)
print('tcgetpgrp: %s' % f)

