#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-10-27
# @copyright by hoojo@2020
# @changelog python3 `progress bar` example


# ===============================================================================
# 标题：python3 progress bar example
# ===============================================================================
# 使用：利用python在控制台输出进度条
# -------------------------------------------------------------------------------
# 描述：在加载或下载、读取的场景中使用进度条
# -------------------------------------------------------------------------------
import sys
import time


# help(global)
# -------------------------------------------------------------------------------
# 简单进度条
# -------------------------------------------------------------------------------
i = 60


def process_bar():
    global i
    i += 1
    text = "\r%d%%[%s%s]" % (i, "*" * i, " " * (100 - i))
    sys.stdout.write(text)
    sys.stdout.flush()


process_bar()
time.sleep(0.3)

process_bar()
time.sleep(0.3)

process_bar()
time.sleep(0.3)

process_bar()
time.sleep(0.3)

process_bar()
print()

# output:
# ---------------------------------------------------------------------------
# 71%[***********************************************************************                             ]


# -------------------------------------------------------------------------------
# 简单进度条
# -------------------------------------------------------------------------------
for index in range(80, 101):
    text = "\r%d%%[%s%s]" % (index, "=" * index, " " * (100 - index))
    sys.stdout.write(text)
    sys.stdout.flush()
    time.sleep(0.2)
print()

# output:
# ---------------------------------------------------------------------------
# 16%[==============                                                               ]


# -------------------------------------------------------------------------------
# 简单进度条
# -------------------------------------------------------------------------------
j = '#'
for l in range(40, 61):
    j = '#' * l
    sys.stdout.write(str(int((l / 60) * 100)) + '% ||' + j + '->' + "\r")
    sys.stdout.flush()
    time.sleep(0.2)
print()

# output:
# ---------------------------------------------------------------------------
# 100% ||############################################################->


# -------------------------------------------------------------------------------
# 简单进度条
# -------------------------------------------------------------------------------
for i in range(1, 61):
    sys.stdout.write('#' + '->' + "\b\b")
    sys.stdout.flush()
    time.sleep(0.1)


# output:
# ---------------------------------------------------------------------------
# ############################################################



# -------------------------------------------------------------------------------
# 固定在底部的进度条
# -------------------------------------------------------------------------------
class ProgressBar:
    def __init__(self, count=0, total=0, width=50):
        self.count = count
        self.total = total
        self.width = width

    def move(self):
        self.count += 1

    def log(self, s):
        sys.stdout.write(' ' * (self.width + 9))
        sys.stdout.write('\r')
        sys.stdout.flush()
        print(s)
        progress = int(self.width * self.count / self.total)
        sys.stdout.write('{0:3}/{1:3}: '.format(self.count, self.total))
        sys.stdout.write('\r')
        sys.stdout.write('#' * progress + '-' * (self.width - progress))
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()


total = 10
bar = ProgressBar(total=total)
for i in range(total):
    bar.move()
    bar.log('We have arrived at: ' + str(i + 1))
    time.sleep(1)