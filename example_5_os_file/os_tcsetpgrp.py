#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
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

