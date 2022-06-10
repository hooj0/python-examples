#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-06 22:33:42
# @copyright by hoojo@2018
# @changelog Added python3 `datetime -> date time` example


import datetime

'''
时间日期对象
     time 和 calendar 模块可以用于格式化日期和时间
     
特点：    
    1、时间格式化输出
    2、时间输入

example：
    iter = iter({ 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) })
        使用iter()方法进行构造    
API：
    next() 下一个元素
    
-----------------------------------------------------------------------------
时间元组

序号                                     属性                                                字段                                            值
0                tm_year              4位数年                                      2008
1                tm_mon                月                                              1 到 12
2                tm_mday               日                                              1到31
3                tm_hour               小                                              0到23
4                tm_min                分                                              0到59
5                tm_sec                 秒                                            0到61 (60或61 是闰秒)
6                tm_wday               一周的第几日                    0到6 (0是周一)
7                tm_yday               一年的第几日                    1到366 (儒略历)
8                tm_isdst              夏令时                                    -1, 0, 1, -1是决定是否为夏令时的旗帜    

-------------------------------------------------------------------------------

时间日期格式化符号：

    %y             两位数的年份表示（00-99）
    %Y             四位数的年份表示（000-9999）
    %m             月份（01-12）
    %d             月内中的一天（0-31）
    %H             24小时制小时数（0-23）
    %I             12小时制小时数（01-12）
    %M             分钟数（00=59）
    %S             秒（00-59）
    %a             本地简化星期名称
    %A             本地完整星期名称
    %b             本地简化的月份名称
    %B             本地完整的月份名称
    %c             本地相应的日期表示和时间表示
    %j             年内的一天（001-366）
    %p             本地A.M.或P.M.的等价符
    %U             一年中的星期数（00-53）星期天为星期的开始
    %w             星期（0-6），星期天为星期的开始
    %W             一年中的星期数（00-53）星期一为星期的开始
    %x             本地相应的日期表示
    %X             本地相应的时间表示
    %Z             当前时区的名称
    %%             %号本身            
--------------------------------------------------------------------------------

Time 模块包含了以下内置函数

1、time.altzone
        返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
        
以下实例展示了 altzone()函数的使用方法：

>>> import time
>>> print("time.altzone %d " % time.altzone)

time.altzone -28800
 

2、time.asctime([tupletime])
        接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
        
以下实例展示了 asctime()函数的使用方法：

>>> import time
>>> t = time.localtime()
>>> print("time.asctime(t): %s " % time.asctime(t))

time.asctime(t): Thu Apr  7 10:36:20 2016 


3、time.clock()
        用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
    

4、time.ctime([secs])
        作用相当于asctime(localtime(secs))，未给参数相当于asctime()
        
以下实例展示了 ctime()函数的使用方法：

>>> import time
>>> print("time.ctime() : %s" % time.ctime())

time.ctime() : Thu Apr  7 10:51:58 2016


5、time.gmtime([secs])
        接收时间辍（1970纪元后经过的浮点秒数）并返回格林威治天文时间下的时间元组t。注：t.tm_isdst始终为0    
    
以下实例展示了 gmtime()函数的使用方法：

>>> import time
>>> print("gmtime :", time.gmtime(1455508609.34375))

gmtime : time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=3, tm_min=56, tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)


6、 time.localtime([secs]
        接收时间辍（1970纪元后经过的浮点秒数）并返回当地时间下的时间元组t（t.tm_isdst可取0或1，取决于当地当时是不是夏令时）。    

以下实例展示了 localtime()函数的使用方法：

>>> import time
>>> print("localtime(): ", time.localtime(1455508609.34375))

localtime():  time.struct_time(tm_year=2016, tm_mon=2, tm_mday=15, tm_hour=11, tm_min=56, tm_sec=49, tm_wday=0, tm_yday=46, tm_isdst=0)


7、time.mktime(tupletime)
        接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）。    

8、time.sleep(secs)
        推迟调用线程的运行，secs指秒数。    
        
以下实例展示了 sleep()函数的使用方法：

import time

print("Start : %s" % time.ctime())
time.sleep( 5 )

print("End : %s" % time.ctime())

9、time.strftime(fmt[,tupletime])
        接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。  
          
以下实例展示了 strftime()函数的使用方法：

>>> import time
>>> print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

2016-04-07 11:18:05

10、time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')
        根据fmt的格式把一个时间字符串解析为时间元组。    
        
以下实例展示了 strftime()函数的使用方法：

>>> import time
>>> struct_time = time.strptime("30 Nov 00", "%d %b %y")
>>> print("返回元组: ", struct_time)

返回元组:  time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

11、time.time( )
        返回当前时间的时间戳（1970纪元后经过的浮点秒数）。    
        
以下实例展示了 time()函数的使用方法：
>>> import time
>>> print(time.time())

1459999336.1963577

12、time.tzset()
        根据环境变量TZ重新初始化时间相关设置。    

'''
# 时间戳

import time


print('timestamp:', time.time()) # 1510066354.2148845

# 当前时间，t.tm_isdst可取0或1，取决于当地当时是不是夏令时
print('current local time:', time.localtime()) # time.struct_time(tm_year=2017, tm_mon=11, tm_mday=7, tm_hour=22, tm_min=52, tm_sec=34, tm_wday=1, tm_yday=311, tm_isdst=0)
print('current local time:', time.localtime(time.time())) # time.struct_time(tm_year=2017, tm_mon=11, tm_mday=7, tm_hour=22, tm_min=52, tm_sec=34, tm_wday=1, tm_yday=311, tm_isdst=0)
print('current local time:', time.localtime(60 * 60 * 24 * 360 * 10)) # current local time: time.struct_time(tm_year=1979, tm_mon=11, tm_mday=10, tm_hour=8, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=314, tm_isdst=0)

# 可读时间
print('asctime:', time.asctime())   # asctime: Mon Sep 24 12:26:56 2018
print('asctime:', time.asctime(time.localtime())) # asctime: Mon Sep 24 12:26:56 2018
print('asctime:', time.asctime(time.localtime(60 * 60 * 24 * 360 * 10))) # 1970 + 10年, asctime: Sat Nov 10 08:00:00 1979

# 格式化时间
print('format:', time.strftime('%Y-%m-%d %H:%M:%S'))    # format: 2018-09-24 12:26:56
print('format:', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time() - 60 * 30)))    # format: 2018-09-24 11:56:56
print('format:', time.strftime('%a %b %d %H:%M:%S %Y', time.localtime(time.time() - 60 * 30))) # format: Mon Sep 24 11:56:56 2018

# 字符串转时间
timestamp = time.localtime() 

print('timestamp:', timestamp) # timestamp: time.struct_time(tm_year=2018, tm_mon=9, tm_mday=24, tm_hour=12, tm_min=26, tm_sec=56, tm_wday=0, tm_yday=267, tm_isdst=0)
print('mktime:', time.mktime(timestamp)) # mktime: 1537763216.0

# 字符格式化成时间
print('strptime:', time.strptime('2017', '%Y')) # strptime: time.struct_time(tm_year=2017, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=-1) 
print('strptime:', time.strptime('2017-11-07 22:04:08', '%Y-%m-%d %H:%M:%S')) # strptime: time.struct_time(tm_year=2017, tm_mon=11, tm_mday=7, tm_hour=22, tm_min=4, tm_sec=8, tm_wday=1, tm_yday=311, tm_isdst=-1)


# 时区
print('time.altzone:', time.altzone) # time.altzone: -32400

# 休眠时间
print('start：', time.ctime()) # start： Mon Sep 24 12:26:56 2018
time.sleep(3)
print('end：', time.ctime()) # end： Mon Sep 24 12:26:59 2018

# 用以浮点数计算的秒数返回当前的CPU时间
'''
这个需要注意，在不同的系统上含义不同。
在UNIX系统上，它返回的是"进程时间"，它是用秒表示的浮点数（时间戳）。

而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。
而第二次之后的调用是自第一次调用以后到现在的运行时间。
'''
print('time.clock:', time.clock())

# 返回每次运行的时间
for i in range(3):
    time.sleep(1)
    print('time.clock:', time.clock())
else:
    print('time.clock:', time.clock())
    
# 当前时间；未给参数相当于asctime()
print('time.ctime:', time.ctime()) # time.ctime: Mon Sep 24 12:27:02 2018
# 指定某个时间，传秒数；相当于asctime(localtime(secs))
print('time.ctime:', time.ctime(60 * 60 * 24 * 360 * 10)) # time.ctime: Sat Nov 10 08:00:00 1979 

# 接收时间戳，返回格林时间，t.tm_isdst始终为0
print('time.gmtime:', time.gmtime()) # 相差8个时区，8小时 time.gmtime: time.struct_time(tm_year=2018, tm_mon=9, tm_mday=24, tm_hour=4, tm_min=27, tm_sec=2, tm_wday=0, tm_yday=267, tm_isdst=0)
print('time.gmtime:', time.gmtime(60 * 60 * 24 * 360 * 10)) # time.gmtime: time.struct_time(tm_year=1979, tm_mon=11, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=5, tm_yday=314, tm_isdst=0)

print(time.tzname)
print(time.daylight)
print(time.get_clock_info('clock')) # namespace(adjustable=False, implementation='QueryPerformanceCounter()', monotonic=True, resolution=4.5289301263073323e-07)
print(time.monotonic())     # 16429.728
print(time.perf_counter()) # 3.0229956427163254
print(time.process_time()) # 0.156001

t = time.time()
print(t)                       #原始时间数据
print(int(t))                  #秒级时间戳
print(int(round(t * 1000)))    #毫秒级时间戳

nowTime = lambda: int(round(time.time() * 1000))
print(nowTime())              #毫秒级时间戳，基于lambda