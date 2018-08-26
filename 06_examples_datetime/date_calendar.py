#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-11-07 22:19:55
# @copyright by hoojo@2018
# @changelog Added python3 `datetime->date calendar` example


import calendar
import time

'''
日历模块

    可以方便的计算日历时间，常用处理年历和月历
    
1、calendar.calendar(year,w=2,l=1,c=6)
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
2、calendar.firstweekday( )
返回当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一。
3、calendar.isleap(year)
是闰年返回True，否则为false。
4、calendar.leapdays(y1,y2)
返回在Y1，Y2两年之间的闰年总数。
5、calendar.month(year,month,w=2,l=1)
返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
6、calendar.monthcalendar(year,month)
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
7、calendar.monthrange(year,month)
返回两个整数。第一个是该月的星期几的日期码，第二个是该月的日期码。日从0（星期一）到6（星期日）;月从1到12。
8、calendar.prcal(year,w=2,l=1,c=6)
相当于 print calendar.calendar(year,w,l,c).
9、calendar.prmonth(year,month,w=2,l=1)
相当于 print calendar.calendar（year，w，l，c）。
10、calendar.setfirstweekday(weekday)
设置每周的起始日期码。0（星期一）到6（星期日）。
11、calendar.timegm(tupletime)
和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
12、calendar.weekday(year,month,day)
返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。    

'''

# 返回一个多行字符串格式的year年month月日历
cal = calendar.month(2017, 11)
print("2017-11:")
print(cal)

# w 是每天之间宽度，l是每天之间高度
cal = calendar.month(2017, 11, w = 3, l = 1)
print("2017-11:")
print(cal)

# 一年的日历，c 表示每个月日历之前的宽度间距
cal = calendar.calendar(2017, w=2, l=1, c=30)
print("2017:")
print(cal)

# 当前每周起始日期的设置。默认情况下，首次载入caendar模块时返回0，即星期一
print('firstweekday:', calendar.firstweekday()) # 0

# 是否闰年
print('isleap:', calendar.isleap(2018)) # False
print('isleap:', calendar.isleap(2020)) # True

# 返回两年之间闰月数量
print('leapdays:', calendar.leapdays(2016, 2018)) # 1

# 返回这个月的日历的二维数组
print('monthcalendar：', calendar.monthcalendar(2017, 11)) # [[0, 0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18, 19], [20, 21, 22, 23, 24, 25, 26], [27, 28, 29, 30, 0, 0, 0]]

# 直接打印日历，相当于 prin(calendar.calendar(year,w,l,c))
calendar.prcal(2017, w=2, l=1, c=6)

# 返回当前月的最开始日期的前一天的星期和当前月日期的最后一天
print('monthrange：', calendar.monthrange(2017, 10)) # (6, 31) 6 为上个月最后一天的星期，31是本月的最后一天（天数）
print('monthrange：', calendar.monthrange(2017, 11)) # (2, 30)
print('monthrange：', calendar.monthrange(2017, 12)) # (4, 31)

# 打印某个月的日历，相当于 print calendar.calendar（year，w，l，c）
calendar.prmonth(2017, 11, w=2,l=1)

# 返回当前日期秒数
print('timegm:', calendar.timegm(time.localtime()))

#设置每周的起始日期码
calendar.setfirstweekday(1)

# 返回星期几
print('weekday:', calendar.weekday(2017, 11, 5))