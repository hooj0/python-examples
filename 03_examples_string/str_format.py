#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-23 23:19:04
# @copyright by hoojo@2018
# @changelog Added python3 `string->str format` example


'''
            符   号                        描述
      %c     格式化字符及其ASCII码
      %s     格式化字符串
      %d     格式化整数
      %u     格式化无符号整型
      %o     格式化无符号八进制数
      %x     格式化无符号十六进制数
      %X     格式化无符号十六进制数（大写）
      %f     格式化浮点数字，可指定小数点后的精度
      %e     用科学计数法格式化浮点数
      %E     作用同%e，用科学计数法格式化浮点数
      %g     %f和%e的简写
      %G     %f 和 %E 的简写
      %p     用十六进制数格式化变量的地址
---------------------------------------------------------------------
符号                            功能
*            定义宽度或者小数点精度
-            用做左对齐
+            在正数前面显示加号( + )
<sp>         在正数前面显示空格
#            在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0            显示的数字前面填充'0'而不是默认的空格
%            '%%'输出一个单一的'%'
(var)        映射变量(字典参数)
m.n.         m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)      
'''
import math
import datetime
import time

### % 用来格式化字符串的 ###
# %s 用来格式化参：字符串
# %d 用来格式化参：整数
# %f 用来格式化参：浮点数
# %x 用来格式化参：十六进制数
# %? 用来格式化参：任意参数 python2

# % 字符串替换传参， 格式化
print('hello，%s' % 'world')
# 多个字符串用 % (参数1，参数2...)
print('I am %s python %s' % ('like', '3.6'))
print()

# %d 进行整数格式化操作
print('string count %d' % 55)
# %2d 表示前面补空字符串 2个；%15d 表示补空格15个
# %04 表示位数不够4个，前面补0
print('你有存款美元： %12d，人民币：%04d' % (1, 2))
print('你有存款美元： %12d，人民币：%04d' % (12345678910123, 21543))

print()

# %f 浮点数格式化，可以进行小数位的保留
# %f 默认保留6位小数，不够6位用0代替
print('你有余额：%f' % 1113)
print('你有余额：%f' % 1113.14159267)
# %.f 不保留小数
print('你有余额：%.f' % 7.898)
# %.2f 保留2位小数
print('你有余额：%.2f' % 137.518)
# %.4f 如果小数位不够4位会进行补0
print('你有余额：%.4f' % 137.518)

print()


# %x 十六进制
# %x 会将十六进制数值直接输出
print('code %x' % 0x232ff)
# %s 会进行数学转换到十进制
print('hello，%s' % 0x12af)

# %%进行百分号转义
print('百分比 %d %%' % 30)


print('------------------------------------------------------')
#*            定义宽度或者小数点精度
#-            用做左对齐
print('hhahah sfdfd %-s' % 'sdfffff')
# 在正数前面显示加号( + )
print('number: %+d' % 100)
#<sp>         在正数前面显示空格
##            在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
#0            显示的数字前面填充'0'而不是默认的空格
#%            '%%'输出一个单一的'%'
#(var)        映射变量(字典参数)
var = { 'age': 22, 'name': 'jack' }
#m.n.         m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)

# format
print('{1}, {2}, {0}'.format('python', 'is', 'good'))
print('{age}, {name}'.format(age = 22, name = 'jack'))

# 混合模式
print('{0} {age}, {1} {name}'.format('tom is', 'your', age = 22, name = 'jack'))

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:
print('PI: {}'.format(math.pi))
print('PI: {!r}'.format(math.pi))
print('PI: {!s}'.format(math.pi))
print('PI: {!a}'.format('c'))

# 小数格式化
print('PI: {0:.3f}, time: {1}'.format(math.pi, time.clock()))

# d 针对整数类型， {n:size} size代表空格宽度
var = { 'java': 234234, 'python': 34590}
for key, val in var.items():
    print('{0:9}-->{1:10d}'.format(key, val))
    
    
# 访问字典值，结合索引和key进行访问
print('A-> {0[java]}, B-> {0[python]:d}'.format(var))

# 直接用key访问字典，** 参数转换
print('A-> {java}, B-> {python:d}'.format(**var))    