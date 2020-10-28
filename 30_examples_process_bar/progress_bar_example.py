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
#
#   pip install progressbar
#
# -------------------------------------------------------------------------------
# 描述：在加载或下载、读取的场景中使用进度条
# -------------------------------------------------------------------------------
from progressbar import *
import time
import sys


# help(progressbar)
# -------------------------------------------------------------------------------
# progressbar 使用示例
# -------------------------------------------------------------------------------
examples = []


def example(fn):
    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % fn.__name__)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')

    examples.append(wrapped)
    return wrapped


# -------------------------------------------------------------------------------
# @example
def with_example0():
    with ProgressBar(max_value=100) as progress:
        for i in range(100):
            # do something
            time.sleep(0.01)
            progress.update(i)
# output:
# --------------------------------------------------------------------------------
# Running: with_example0
# 100% (100 of 100) |######################| Elapsed Time: 0:00:00 Time:  0:00:00


# -------------------------------------------------------------------------------
# @example
def with_example1():
    with ProgressBar(max_value=100, redirect_stdout=True) as p:
        for i in range(100):
            # do something
            p.update(i)
            time.sleep(0.01)
# output:
# --------------------------------------------------------------------------------
# Running: with_example1
# 100% (1000 of 1000) |####################| Elapsed Time: 0:00:01 Time:  0:00:01


# -------------------------------------------------------------------------------
# @example
def example0():
    pbar = ProgressBar(widgets=[Percentage(), Bar()], max_value=10).start()
    for i in range(10):
        # do something
        time.sleep(0.1)
        pbar.update(i + 1)
    pbar.finish()
# output:
# --------------------------------------------------------------------------------
# Running: example0
# 100%|#########################################################################|


# -------------------------------------------------------------------------------
# @example
def example1():
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        # do something
        pbar.update(10 * i + 1)
        time.sleep(0.01)
    pbar.finish()
# output:
# --------------------------------------------------------------------------------
# Running: example1
# Test:  85% |/                                        | ETA:   0:00:01 100.1 B/s


# -------------------------------------------------------------------------------
# @example
def example2():
    class CrazyFileTransferSpeed(FileTransferSpeed):
        "It's bigger between 45 and 80 percent"

        def update(self, pbar):
            if 45 < pbar.percentage() < 80:
                return 'Bigger Now ' + FileTransferSpeed.update(self, pbar)
            else:
                return FileTransferSpeed.update(self, pbar)

    widgets = [CrazyFileTransferSpeed(), ' <<<', Bar(), '>>> ',
               Percentage(), ' ', ETA()]
    pbar = ProgressBar(widgets=widgets, max_value=1000)
    # maybe do something
    pbar.start()
    for i in range(200):
        # do something
        pbar.update(5 * i + 1)
        time.sleep(0.01)
    pbar.finish()
# output:
# --------------------------------------------------------------------------------
# Running: example2
#  50.1 B/s <<<|##############                           |>>>  34% ETA:   0:00:13


# -------------------------------------------------------------------------------
# @example
def example3():
    widgets = [Bar('>'), ' ', ETA(), ' ', ReverseBar('<')]
    pbar = ProgressBar(widgets=widgets, max_value=1000).start()
    for i in range(100):
        # do something
        pbar.update(10 * i + 1)
        time.sleep(0.01)
    pbar.finish()
# output:
# --------------------------------------------------------------------------------
# Running: example3
# |>>>>>>>>>>>>>>>>>>>>>>>       | ETA:   0:00:02 |       <<<<<<<<<<<<<<<<<<<<<<|


# -------------------------------------------------------------------------------
# @example
def example4():
    widgets = ['Test: ', Percentage(), ' ',
               Bar(marker='0', left='[', right=']'),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, max_value=500)
    pbar.start()
    for i in range(100, 500 + 1, 50):
        time.sleep(0.08)
        pbar.update(i)
    pbar.finish()
# output:
# --------------------------------------------------------------------------------
# Running: example4
# Test: 100% [00000000000000000000000000000000000000000] Time:  0:00:00 554.3 B/s


# -------------------------------------------------------------------------------
# @example
def example5():
    pbar = ProgressBar(widgets=[SimpleProgress()], max_value=17).start()
    for i in range(17):
        time.sleep(0.1)
        pbar.update(i + 1)
    pbar.finish()
# output:
# --------------------------------------------------------------------------------
# Running: example5
# 12 of 17


# -------------------------------------------------------------------------------
# @example
def example6():
    pbar = ProgressBar().start()
    for i in range(100):
        time.sleep(0.02)
        pbar.update(i + 1)
    pbar.finish()
# output:
# -------------------------------------------------------------------------------
# Running: example6
# | |  #                                              | 100 Elapsed Time: 0:00:10


# -------------------------------------------------------------------------------
# @example
def example7():
    pbar = ProgressBar()  # Progressbar can guess max_value automatically.
    for i in pbar(range(8)):
        time.sleep(0.01)
# output:
# -------------------------------------------------------------------------------
# Running: example7
# 100% (8 of 8) |##########################| Elapsed Time: 0:00:00 Time:  0:00:00


# -------------------------------------------------------------------------------
# @example
def example8():
    pbar = ProgressBar(max_value=8)  # Progressbar can't guess max_value.
    for i in pbar((i for i in range(8))):
        time.sleep(0.2)
# output:
# -------------------------------------------------------------------------------
# Running: example8
# 100% (8 of 8) |##########################| Elapsed Time: 0:00:04 Time:  0:00:04


# -------------------------------------------------------------------------------
# @example
def example9():
    pbar = ProgressBar(widgets=['Working: ', AnimatedMarker()])
    for i in pbar((i for i in range(10))):
        time.sleep(0.2)
# output:
# -------------------------------------------------------------------------------
# Working: \


# -------------------------------------------------------------------------------
# @example
def example10():
    widgets = ['Processed: ', Counter(), ' lines (', Timer(), ')']
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(15))):
        time.sleep(0.1)
# output:
# -------------------------------------------------------------------------------
# Running: example10
# Processed: 14 lines (Elapsed Time: 0:00:07)


# -------------------------------------------------------------------------------
# @example
def example11():
    widgets = [FormatLabel('Processed: %(value)d lines (in: %(elapsed)s)')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(15))):
        time.sleep(0.5)
# output:
# -------------------------------------------------------------------------------
# Running: example11
# Processed: 14 lines (in: 0:00:01)


# -------------------------------------------------------------------------------
# @example
def example12():
    widgets = ['Balloon: ', AnimatedMarker(markers='.。o0O@*@O0o。. ')]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(39))):
        time.sleep(0.1)
# output:
# -------------------------------------------------------------------------------
# Running: example12
# Balloon: 0


# -------------------------------------------------------------------------------
# @example
def example13():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='←↖↑↗→↘↓↙')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
# output:
# -------------------------------------------------------------------------------
# Running: example13
# Arrows: ←


# -------------------------------------------------------------------------------
# @example
def example14():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Arrows: ', AnimatedMarker(markers='◣◤◥◢')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
# output:
# -------------------------------------------------------------------------------
# Running: example14
# Arrows: ◣


# -------------------------------------------------------------------------------
# @example
def example15():
    # You may need python 3.x to see this correctly
    try:
        widgets = ['Wheels: ', AnimatedMarker(markers='◐◓◑◒')]
        pbar = ProgressBar(widgets=widgets)
        for i in pbar((i for i in range(24))):
            time.sleep(0.1)
    except UnicodeError:
        sys.stdout.write('Unicode error: skipping example')
# output:
# -------------------------------------------------------------------------------
# Running: example15
# Wheels: ◐


# -------------------------------------------------------------------------------
# @example
def example16():
    widgets = [FormatLabel('Bouncer: value %(value)d - '), BouncingBar()]
    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(100))):
        time.sleep(0.1)
# output:
# -------------------------------------------------------------------------------
# Running: example16
# Bouncer: value 99 - |             #                                           |


# -------------------------------------------------------------------------------
# @example
def example17():
    widgets = [FormatLabel('Animated Bouncer: value %(value)d - '),
               BouncingBar(marker=RotatingMarker())]

    pbar = ProgressBar(widgets=widgets)
    for i in pbar((i for i in range(18))):
        time.sleep(0.1)
# output:
# -------------------------------------------------------------------------------
# Running: example17
# Animated Bouncer: value 17 - |                  |                             |


# -------------------------------------------------------------------------------
# @example
def with_example18():
    with ProgressBar(max_value=10, term_width=20, left_justify=False) as progress:
        # assert progress._env_size() is not None
        for i in range(10):
            progress.update(i)
            time.sleep(0.1)
# output:
# -------------------------------------------------------------------------------
# Running: with_example18
# 100% (10 of 10) || Elapsed Time: 0:00:01 Time:  0:00:01


# -------------------------------------------------------------------------------
# @example
def with_example19():
    with ProgressBar(max_value=10) as progress:
        try:
            progress.update(1)
        except ValueError:
            pass
# output:
# -------------------------------------------------------------------------------
# Running: with_example19
# 100% (10 of 10) |########################| Elapsed Time: 0:00:00 Time:  0:00:00


# -------------------------------------------------------------------------------
# @example
def with_example20():
    progress = ProgressBar(max_value=10)
    try:
        progress.update(1)
    except RuntimeError:
        pass
# output:
# -------------------------------------------------------------------------------
# Running: with_example20
# 100% (10 of 10) |########################| Elapsed Time: 0:00:00 Time:  0:00:00


# -------------------------------------------------------------------------------
# @example
def with_example21a():
    with ProgressBar(max_value=10, redirect_stdout=True) as progress:
        print('', file=sys.stdout)
        progress.update(0)
# output:
# -------------------------------------------------------------------------------
# Running: with_example21a
# 100% (10 of 10) |########################| Elapsed Time: 0:00:00 Time:  0:00:00


# -------------------------------------------------------------------------------
# @example
def with_example21b():
    with ProgressBar(max_value=1, redirect_stderr=True) as progress:
        print('', file=sys.stderr)
        progress.update(0)
# output:
# -------------------------------------------------------------------------------
# Running: with_example21b
# 100% (1 of 1) |##########################| Elapsed Time: 0:00:00 Time:  0:00:00


# -------------------------------------------------------------------------------
# @example
def with_example22():
    try:
        with ProgressBar(max_value=10) as progress:
            progress.start()
    except ValueError:
        pass
# output:
# -------------------------------------------------------------------------------
# Running: with_example22
# 100% (10 of 10) |########################| Elapsed Time: 0:00:01 Time:  0:00:01


# -------------------------------------------------------------------------------
# @example
def example23():
    widgets = [BouncingBar(marker=RotatingMarker())]
    with ProgressBar(widgets=widgets, max_value=20, term_width=10) as progress:
        for i in range(20):
            progress.update(i)
            time.sleep(0.1)

    widgets = [BouncingBar(marker=RotatingMarker(), fill_left=False)]
    with ProgressBar(widgets=widgets, max_value=20, term_width=10) as progress:
        for i in range(20):
            progress.update(i)
            time.sleep(0.1)

# output:
# -------------------------------------------------------------------------------
# Running: example23
# |    |   |
# |/       |


# -------------------------------------------------------------------------------
# @example
def example24():
    pbar = ProgressBar(widgets=[Percentage(), Bar()], max_value=10).start()
    for i in range(10):
        # do something
        time.sleep(0.1)
        pbar += 1
    pbar.finish()
# output:
# -------------------------------------------------------------------------------
# Running: example24
#  90%|#################################################################        |


# -------------------------------------------------------------------------------
# @example
def example25():
    widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()), ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, max_value=1000, redirect_stdout=True).start()
    for i in range(100):
        # do something
        pbar += 10
        time.sleep(0.05)
    pbar.finish()
# output:
# -------------------------------------------------------------------------------
# Running: example25
# Test:  47% |\                                        | ETA:   0:00:02 204.2 B/s


# -------------------------------------------------------------------------------
# @example
def example26():
    widgets = [
        Percentage(),
        ' ', Bar(),
        ' ', ETA(),
        ' ', AdaptiveETA(),
        ' ', AdaptiveTransferSpeed(),
    ]
    pbar = ProgressBar(widgets=widgets, max_value=500)
    pbar.start()
    for i in range(500):
        time.sleep(0.001 + (i < 100) * 0.0001 + (i > 400) * 0.009)
        pbar.update(i + 1)
    pbar.finish()
# output:
# -------------------------------------------------------------------------------
# Running: example26
#  91% |#############################   | ETA:   0:00:00 ETA:   0:00:00 431.0 B/s


# -------------------------------------------------------------------------------
# @example
def example27():
    # Testing AdaptiveETA when the value doesn't actually change
    pbar = ProgressBar(widgets=[AdaptiveETA(), AdaptiveTransferSpeed()], max_value=10, poll=0.1)
    pbar.start()
    for _ in range(10):
        pbar.update(1)
        time.sleep(0.5)
    pbar.finish()
# output:
# -------------------------------------------------------------------------------
# Running: example27
# Time:  0:00:01  1.0 B/s


# -------------------------------------------------------------------------------
# @example
def example28():
    # Testing using progressbar as an iterator with a max value
    pbar = ProgressBar()

    for n in pbar(iter(range(100)), 100):
        # iter range is a way to get an iterator in both python 2 and 3
        time.sleep(0.1)
# output:
# -------------------------------------------------------------------------------
# Running: example28
#  38% (38 of 100) |########               | Elapsed Time: 0:00:03 ETA:   0:00:06


# -------------------------------------------------------------------------------
# @example
def example29():
    widgets = ['Test: ', Percentage(), ' | ', ETA(), ' | ', AbsoluteETA()]
    pbar = ProgressBar(widgets=widgets, maxval=500).start()
    for i in range(500):
        time.sleep(0.01)
        pbar.update(i + 1)
    pbar.finish()
# output:
# -------------------------------------------------------------------------------
# Running: example29
# Test:  87% | ETA:   0:00:00 | Estimated finish time: 2020-10-27 15:11:06


# -------------------------------------------------------------------------------
# @example
def example30():
    def custom_len(value):
        # These characters take up more space
        characters = {
            '进': 2,
            '度': 2,
        }

        total = 0
        for c in value:
            total += characters.get(c, 1)

        return total

    bar = ProgressBar(
        widgets=[
            '进度: ',
            Bar(),
            ' ',
            Counter(format='%(value)02d/%(max_value)d'),
        ],
        len_func=custom_len,
    )

    for i in bar(range(10)):
        time.sleep(0.1)
# output:
# -------------------------------------------------------------------------------
# Running: example30
# 进度: |###################################################################| 10/10


# -------------------------------------------------------------------------------
# @example
def example31():
    bar = ProgressBar(max_value=UnknownLength)
    for i in range(20):
        time.sleep(0.1)
        bar.update(i)
# output:
# -------------------------------------------------------------------------------
# Running: example31
# | |                   #                              | 19 Elapsed Time: 0:00:01


# -------------------------------------------------------------------------------
# @example
def example32():
    for i in progressbar(range(10), redirect_stdout=True):
        print()
        print('Some text', i)
        time.sleep(0.1)

# output:
# -------------------------------------------------------------------------------
# Running: example32
#   1% (1 of 100) |                        | Elapsed Time: 0:00:00 ETA:   0:00:09
# Some text 0
#
# Some text 1
#   3% (3 of 100) |                        | Elapsed Time: 0:00:00 ETA:   0:00:09
# Some text 2



# -------------------------------------------------------------------------------
def test():
    for example in examples:
        example()


if __name__ == '__main__':
    try:
        test()
    except KeyboardInterrupt:
        sys.stdout('\nQuitting examples.\n')