# 00_examples_helloworld 
[**00_examples_helloworld**](./00_examples_helloworld)
## hello_world 
[`hello_world`](./00_examples_helloworld/hello_world.py)

```python 

# hello_world.py

############################################
#              hello world                 #
############################################

print("hello world")

print('hello world')

print('hello world');
 
```
# 01_examples_variable 
[**01_examples_variable**](./01_examples_variable)
## variables 
[`variables`](./01_examples_variable/variables.py)

```python 

#===============================================================================
#     variable 变量
#===============================================================================
# 描述：变量是存储任何类型数据的一种媒介
#-------------------------------------------------------------------------------
# API：
#    del var    删除变量
#    del var, var2, varN...    删除多个变量
#    a = b = c = 1    多个变量赋值
#    a, b, c = 1, 'a', False
#-------------------------------------------------------------------------------
#  变量 用大小写字母、_、数字进行表示，且不能用 数字开头
#  常量，由全大写字符串和下划线、数字组成
#-------------------------------------------------------------------------------


# 纯小写字符变量
a = '123'
print('var a =', a)

# 不能以数字开头
# 23b = 'no think'
# print('', 23b)

# 大小写混合变量
Name = 'python'
print('var Name =', Name)

# 带_组合变量
user_age = 22
print('var user_age =', user_age)

# 带_和数字、字母组合变量
t_0 = -1
print('var t_0 =', t_0)

# _ 下划线开头变量
_super = 2
print('var _super =', _super)

 
```
# 02_examples_in_out 
[**02_examples_in_out**](./02_examples_in_out)
## io_input 
[`io_input`](./02_examples_in_out/io_input.py)

```python 

# input.py

'''
input输入流

        接受控制台输入参数，参数以字符串形式接受。
 
'''

# input 接收输入参数，可以输入文本
print("plase input your name")
print("your name:", input())

# 变量接收输入参数
name = input("请输入名称：")
print("name:", name)

# 输入之前可以打印输入提示文本
age = input("plase enter your age:")
print("your age:", age)
 
```
## io_print 
[`io_print`](./02_examples_in_out/io_print.py)

```python 

# print.py

'''
print 输出流 

    将文本内容输出到控制台，在默认情况下。
    如果设置了file会把内容输出到指定的地方，如：文件中。
'''

import sys

# 直接输入内容
print("i like python") #i like python
# 中间的 “,” 会用空格进行输出，相当于是拼接字符串
print("i like python,", 'you ?') #i like python, you ?
# "\n" 就是换行
print("i like python,\nyou ?") 
#i like python,
#you ?

# 多个字符串拼接输出
print("I", "like", 'python', "\n", "you?")
#I like python 
# you?
 
# 传递数字或变量
print("10 + 1 =", 10 + 1) #10 + 1 = 11

# 设置分隔符，默认的是‘ ’空格；设置结束符号，默认是 '\n'
print('a', 'b', 'c', sep = ', ', end = '! \n') #a, b, c! 
print('a', 'b', 'c', sep = ', ', end = '! \n', file = sys.stdout, flush = True) #a, b, c! 

# 设置打印内容输出流，默认是 sys.stdout，输出到屏幕控制台；
# open(path, mode) 可以指定输出到文件中，path 指定路径，mode = w 表示写入且每次覆盖，a 表示追加写入，+ 表示指针移到末尾行
print('a', 'b', 'c', sep = ', ', end = '! \n', file = open(r'c:\a.txt', 'w'), flush = True)
print('a2', 'b2', 'c2', sep = ', ', end = '! \n', file = open(r'c:\a.txt', 'a+'), flush = True)
print('a3', 'b3', 'c3', sep = ', ', end = '! \n', file = open(r'c:\a.txt', 'a+'), flush = False)

input("按任意键退出")
 
```
# 03_examples_string 
[**03_examples_string**](./03_examples_string)
## str_escape 
[`str_escape`](./03_examples_string/str_escape.py)

```python 

# str_escape.py

'''
字符串转义
    \'     输出'
    \"     输出"
    \n     换行
    \r     换行
    \t     制表符空格
    r'' R''        原样输出，忽略转义字符
    \              继续上一行输出
    'a' 'b'        拼接字符串
    'a' + 'b'      拼接字符串
    u'......'      表示Unicode编码字符串
'''

#转义字符                                                  描述
#\(在行尾时)              续行符
#\\                      反斜杠符号
#\'                      单引号
#\"                      双引号
#\a                      响铃
#                                                            退格(Backspace)
#\e                      转义
#00                      空
#\n                      换行
#\v                      纵向制表符
#\t                      横向制表符
#\r                      回车
#\f                      换页
#\oyy                    八进制数，yy代表的字符，例如：\o12代表换行
#\xyy                    十六进制数，yy代表的字符，例如：\x0a代表换行
#\other                  其它的字符以普通格式输出

# 转义字符、多行输出

# 字符转义
print("转义字符\"")

print("转义字符\\n")
 
```
## str_fmt_func 
[`str_fmt_func`](./03_examples_string/str_fmt_func.py)

```python 

import sys

'''
    文件输入输出：
            磁盘文件输出输入
            
            
  输出格式美化
    Python两种输出值的方式: 表达式语句和 print() 函数。(第三种方式是使用文件对象的 write() 方法; 标准输出文件可以用 sys.stdout 引用。)
          如果你希望输出的形式更加多样，可以使用 str.format() 函数来格式化输出值。
          如果你希望将输出的值转成字符串，可以使用 repr() 或 str() 函数来实现。
    str() 函数返回一个用户易读的表达形式，转换为字符串 可以进行字符串拼接。
    repr() 产生一个解释器易读的表达形式，以转义字符串中的特殊字符。          
'''

# 字符串输出
a = "I'am is python!"
print("str(a):", str(a))

b = dict([ ('a', 10), ('b', 20), ('c', 30) ])
print("str(b):", str(b))

print('path: ' + str(sys.path))

print('1/7:', 1/7)
print('1/7:', str(1/7))

# 表达式输出
print('repr():', repr(a))
print('repr():', repr(b))
print('repr():', repr(sys.path))
print('repr 1/7:', type(repr(1/7)))

x = 3 ** 4.2
y = 13 // 3
result = 'x = ' + repr(x) + ', y = ' + repr(y)
print('result:', result)

result = 'x = ' + str(x) + ', y = ' + str(y)
print('result:', result)
 
```
## str_format 
[`str_format`](./03_examples_string/str_format.py)

```python 

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
 
```
## str_function 
[`str_function`](./03_examples_string/str_function.py)

```python 

# str_function.py

'''
字符串函数
    # char 将ASCII数字转换为字符串
    # ord  将字符串转换为ASCII的值
    # u'xxx' Unicode编码输出
    # b'xxx' 表示二进制字符串
    # encode 进行字符串编码
    # decode 进行字符串解码
    # len 获取字符串长度
    # str * Number 重复某个字符串Number次数
    # str + str2 字符串拼接
    # 'xxx' 'yyy' 字符串拼接
    # str[start:end] 进行字符串分割
    # in / not in 成员运算，判断字符串是否在字符串中出现
    # replace 进行字符串替换



操作符                                                            描述                                                                                                                          实例
+                         字符串连接                                                                                                          a + b 输出结果： HelloPython
*                         重复输出字符串                                                                                                a*2 输出结果：HelloHello
[]                        通过索引获取字符串中字符                                                                       a[1] 输出结果 e
[ : ]                     截取字符串中的一部分                                                                                 a[1:4] 输出结果 ell
in                        成员运算符 - 如果字符串中包含给定的字符返回 True     H in a 输出结果 1
not in                    成员运算符 - 如果字符串中不包含给定的字符返回 True   M not in a 输出结果 1
r/R                       原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符。 原始字符串除在字符串的第一个引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。    print r'\n' prints \n 和 print R'\n' prints \n
%                         格式字符串                                                                                                            请看下一章节 
'''

# chr() 可以将ASCII数字转换为字符串
print(chr(65)) # A

# ord() 可以将字符串转换为ASCII的值
print(ord('A')) # 65

# encode 可以进行字符串编码
print(u"中国".encode("utf-8")) # b'\xe4\xb8\xad\xe5\x9b\xbd'
print(u"ABC".encode("UTF-8")) # b'ABC'
 
```
## str_function_inner 
[`str_function_inner`](./03_examples_string/str_function_inner.py)

```python 

import string

'''
                字符串内置函数

方法                                                                                                                                                描述
string.capitalize()                                   把字符串的第一个字符大写
string.center(width)                                  返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
string.count(str, beg=0, end=len(string))             返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
string.decode(encoding='UTF-8', errors='strict')      以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'
string.encode(encoding='UTF-8', errors='strict')      以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
string.endswith(obj, beg=0, end=len(string))          检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
string.expandtabs(tabsize=8)                          把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.
string.find(str, beg=0, end=len(string))              检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
string.index(str, beg=0, end=len(string))             跟find()方法一样，只不过如果str不在 string中会报一个异常.
string.isalnum()                                      如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False
string.isalpha()                                      如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
string.isdecimal()                                    如果 string 只包含十进制数字则返回 True 否则返回 False.
string.isdigit()                                      如果 string 只包含数字则返回 True 否则返回 False.
string.islower()                                      如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False
string.isnumeric()                                    如果 string 中只包含数字字符，则返回 True，否则返回 False
string.isspace()                                      如果 string 中只包含空格，则返回 True，否则返回 False.
string.istitle()                                      如果 string 是标题化的(见 title())则返回 True，否则返回 False
string.isupper()                                      如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
string.join(seq)                                      Merges (concatenates)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
string.ljust(width)                                   返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
string.lower()                                        转换 string 中所有大写字符为小写.
string.lstrip()                                       截掉 string 左边的空格
string.maketrans(intab, outtab])                      maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
max(str)                                              返回字符串 str 中最大的字母。
min(str)                                              返回字符串 str 中最小的字母。
string.partition(str)                                 有点像 find()和 split()的结合体,从 str 出现的第一个位置起,把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),如果 string 中不包含str 则 string_pre_str == string.
string.replace(str1, str2,  num=string.count(str1))   把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
string.rfind(str, beg=0,end=len(string) )             类似于 find()函数，不过是从右边开始查找.
string.rindex( str, beg=0,end=len(string))            类似于 index()，不过是从右边开始.
string.rjust(width)                                   返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
string.rpartition(str)                                类似于 partition()函数,不过是从右边开始查找.
string.rstrip()                                       删除 string 字符串末尾的空格.
string.split(str="", num=string.count(str))           以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
string.splitlines(num=string.count('\n'))             按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
 
```
# 04_examples_data_type 
[**04_examples_data_type**](./04_examples_data_type)
## cast_type 
[`cast_type`](./04_examples_data_type/cast_type.py)

```python 

'''
类型转换

函数                                                                描述
int(x [,base])            将x转换为一个整数
float(x)                  将x转换到一个浮点数
complex(real [,imag])     创建一个复数
str(x)                    将对象 x 转换为字符串
repr(x)                   将对象 x 转换为表达式字符串
eval(str)                 用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)                  将序列 s 转换为一个元组
list(s)                   将序列 s 转换为一个列表
set(s)                    转换为可变集合
dict(d)                   创建一个字典。d 必须是一个序列 (key,value)元组。
chr(x)                    将一个整数转换为一个字符
ord(x)                    将一个字符转换为它的整数值
hex(x)                    一个整数转换为一个十六进制字符串
oct(x)                    将一个整数转换为一个八进制字符串            
'''

# int类型转换
print('int(n)', int('123') + 1) # int(n) 124
print('int(n)', int('123', base = 10) + 1) # int(n) 124
print('int(n)', int('10', base = 36) + 1) # int(n) 37

# float类型转换
print('float(n)', float('123') + 1) # float(n) 124.0
print('float(n)', float(30) + 1) # float(n) 31.0

# complex 复数转换
print('complex:', complex(34.6)) # complex: (34.6+0j)

# 字符串转换
print('str:', str(12.34)) # str: 12.34
print('str:', str(tuple('abcdefg')) + 'oh') # str: ('a', 'b', 'c', 'd', 'e', 'f', 'g')oh

# 表达式转换
print('repr:', repr('0 == 1')) # repr: '0 == 1'

# 元组转换
 
```
## data_type 
[`data_type`](./04_examples_data_type/data_type.py)

```python 

# data_type.py

'''
数据类型

    数据类型有：整型、浮点型、字符串、布尔类型、空值类型、复数类型
    
    特点：
    1、都不是不可变数据，不能进行改变内容，但可以改变内存地址指向
    2、都是基本数据类型    
    

int                   float        complex
10                     0.0          3.14j
100                   15.20         45.j
-786                  -21.9         9.322e-36j
080                   32.3+e18    .876j
-0490                  -90.        -.6545+0J
-0x260                 -32.54e100    3e+26J
0x69                   70.2-E12      4.53e-7j    
'''

############## 整数类型 ##############
print('整数：', 0)
print('整数：', 100)
print('整数：', -100)

# 十六进制 ox前缀开头, 0-9/a-f 表示
print('整数：', 0xa100)
print('整数：', 0xa1b0c0f)
print()

'''
输出：
        整数： 0
        整数： 100
        整数： -100
        整数： 41216
        整数： 169544719
'''
 
```
## object_type 
[`object_type`](./04_examples_data_type/object_type.py)

```python 

'''
以下类型是指对象类型，也就是数据在内存中的类型；

六个标准的数据类型：
    Numbers（数字）
    String（字符串）
    List（列表）
    Tuple（元组）
    Sets（集合）
    Dictionaries（字典）
    
    1、Numbers：
        int、float、bool、complex（复数）
    2、String：
        'str'、"str2"
    3、List:
        [ 'element1', 'element2', 'element..' ]
    4、Tuple：
        ( a, b, c, ... )
    5、Sets:
        set([ 1, 2, 3, .... ])
    6、Dict:
        { 1: 'a', 2: 'b', 3: 'c', ....}

数据类型有：整型、浮点型、字符串、布尔类型、空值类型、复数类型

'''

a, b, c, d = 2, 3.12, False, 2.1 + 3j
print(type(a), type(b), type(c), type(d))   

s1, s2 = 'haha', r"wowow\r\n"
print(type(s1), type(s2)) 

list = [ 1, 2, 3, 4 ]
print(type(list))

tuple = ('a', 'b', 'c')
print(type(tuple))

 
```
# 05_examples_math 
[**05_examples_math**](./05_examples_math)
## math_function 
[`math_function`](./05_examples_math/math_function.py)

```python 

import math
from random import choice, randrange, random, seed, shuffle, uniform
from math import sin, acos, asin

# math_function.py

'''
---------------------------------数学函数------------------------------------
函数                                                                                                                  返回值 ( 描述 )
abs(x)                                    返回数字的绝对值，如abs(-10) 返回 10
ceil(x)                                   返回数字的上入整数，如math.ceil(4.1) 返回 5
exp(x)                                    返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)                                   返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)                                  返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)                                    如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)                                  返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)                           返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)                           返回给定参数的最小值，参数可以为序列。
modf(x)                                   返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)                                 x**y 运算后的值。
round(x [,n])                             返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)                                   返回数字x的平方根，数字可以为负数，返回类型为实数，如math.sqrt(4)返回 2+0j

---------------------------------随机数函数------------------------------------
函数                                                                                                                        描述
choice(seq)                                从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])          从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()                                   随机生成下一个实数，它在[0,1)范围内。
seed([x])                                  改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)                               将序列的所有元素随机排序
uniform(x, y)                              随机生成下一个实数，它在[x,y]范围内。

---------------------------------三角函数------------------------------------
函数                                                                                                                        描述
acos(x)                                   返回x的反余弦弧度值。
asin(x)                                   返回x的反正弦弧度值。     
atan(x)                                   返回x的反正切弧度值。
atan2(y, x)                               返回给定的 X 及 Y 坐标值的反正切值。
cos(x)                                    返回x的弧度的余弦值。
hypot(x, y)                               返回欧几里德范数 sqrt(x*x + y*y)。
 
```
## math_operator 
[`math_operator`](./05_examples_math/math_operator.py)

```python 

# math_operator.py

'''
---------------------------------算术运算-----------------------------------------------
运算符                        描述                                                                                                                       实例
+        加 - 两个对象相加                                                                                        a + b 输出结果 31
-        减 - 得到负数或是一个数减去另一个数                                           a - b 输出结果 -11
*        乘 - 两个数相乘或是返回一个被重复若干次的字符串             a * b 输出结果 210
/        除 - x 除以 y                                     b / a 输出结果 2.1
%        取模 - 返回除法的余数                                                                              b % a 输出结果 1
**       幂 - 返回x的y次幂                                                                                        a**b 为10的21次方
//       取整除 - 返回商的整数部分                                                                    9//2 输出结果 4 , 9.0//2.0 输出结果 4.0
---------------------------------赋值运算------------------------------------------------
运算符                        描述                                                            实例
=         简单的赋值运算符            c = a + b 将 a + b 的运算结果赋值为 c
+=        加法赋值运算符                c += a 等效于 c = c + a
-=        减法赋值运算符                c -= a 等效于 c = c - a
*=        乘法赋值运算符                c *= a 等效于 c = c * a
/=        除法赋值运算符                c /= a 等效于 c = c / a
%=        取模赋值运算符                c %= a 等效于 c = c % a
**=       幂赋值运算符                     c **= a 等效于 c = c ** a
//=       取整除赋值运算符           c //= a 等效于 c = c // a
---------------------------------位运算符-----------------------------------------------
运算符    描述    实例
&        按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0                        (a & b) 输出结果 12 ，二进制解释： 0000 1100
|        按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。                                                                                                    (a | b) 输出结果 61 ，二进制解释： 0011 1101
^        按位异或运算符：当两对应的二进位相异时，结果为1                                                  (a ^ b) 输出结果 49 ，二进制解释： 0011 0001
~        按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1                                      (~a ) 输出结果 -61 ，二进制解释： 1100 0011， 在一个有符号二进制数的补码形式。
<<       左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。              a << 2 输出结果 240 ，二进制解释： 1111 0000
>>       右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数                                          a >> 2 输出结果 15 ，二进制解释： 0000 1111
--------------------------------------------------------------------------------
Python运算符优先级

以下表格列出了从最高到最低优先级的所有运算符：
运算符                                                                                        描述
**                                指数 (最高优先级)
~ + -                             按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)
* / % //                          乘，除，取模和取整除
+ -                               加法减法
>> <<                             右移，左移运算符
 
```
# 06_examples_datetime 
[**06_examples_datetime**](./06_examples_datetime)
## date_calendar 
[`date_calendar`](./06_examples_datetime/date_calendar.py)

```python 

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

 
```
## date_time 
[`date_time`](./06_examples_datetime/date_time.py)

```python 

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
 
```
# 07_examples_data_struct 
[**07_examples_data_struct**](./07_examples_data_struct)
## data_struct 
[`data_struct`](./07_examples_data_struct/data_struct.py)

```python 

from _collections import deque

'''
列表：有序
堆栈：先进后出
队列：先进先出

元组和序列：
集合：集合是一个无序不重复元素的集
字典：

'''

# 将列表当做堆栈使用，结合append、pop方法，达到先进后出的目的
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print('stack:', stack)

print('stack:', stack.pop()) # 3
print('stack:', stack.pop()) # 2

# 将列表当作队列使用
queue = deque([1, 2, 3, 4])
queue.append(5)
queue.append(6)
# 添加到最前面
queue.appendleft(-1)

print('queue:', queue)
# 弹出最前面的
print('queue.popleft:', queue.popleft())
print('queue.popleft:', queue.popleft())
# 弹出最后面的
print('queue.popleft:', queue.pop())
print('queue:', queue)

# 添加到最前面
 
```
## dict 
[`dict`](./07_examples_data_struct/dict.py)

```python 

'''
dict 数据字典，全名：dictionary。
    数据结构形式是键值对key-value的形式，在其他语言中是map去表现的。

特点：    
    1、其查找速度快是主要表现之一
    2、插入速度快
    3、占用的内存比list、tuple多
    4、key 必须是不可变对象，如：字符串、整数等

example：
    dict = { 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) }
            构造形式相当于 json字符串的构造，key必须要用引号  
            
API：
    1、dict.get(key)    获取dict中key的值
    2、dict.get(key, default)    获取dict中key的值，如果没有key的值，将返回默认值default
    3、dict[key]        获取dict中key的值
    4、key in dict, key not in dict     判断key是否在dict中存在
    5、dict[key] = value    对dict的key进行赋值
    6、dict.keys()    获取所有的键
    7、dict.values()    获取所有的值
    8、sorted(dict)    排序
    9、dict.clear()    清空
    10、dict.pop(key)    删除指定key元素
    11、del dict[key]    删除指定key元素
    
    12、dict.copy()    浅复制
    13、dict.fromkeys(seq) dict.fromkeys(seq, default)    创建一个新字典，默认值为default；default不传默认值为None
    14、dict.items() 返回可以直接遍历键值对
    15、dict.setdefault(key, value))    和get类似，可以获取值，如果值不存在就设置默认值
    16、dict.update(src)    将src字典数据更新到dict上，如果src的键在dict中存在的话就替换掉值，不存在就不处理
'''

# 构造一个dict 数据字典
user_info = { 'name': 'jason', 'age': 27, 'brithday': (1990, 10, 22) }
print('user information: ', user_info) # {'name': 'jason', 'age': 27, 'brithday': (1990, 10, 22)}

# 构造dict 方法2，用列表List 嵌套 元组
tmp = dict([ ('a', 10), ('b', 20), ('c', 30) ])
 
```
## iter 
[`iter`](./07_examples_data_struct/iter.py)

```python 

from symbol import except_clause
import sys

'''
迭代器

特点：    
    1、对任意集合进行迭代遍历
    2、只能向前不能后退

example：
    iter = iter({ 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) })
        使用iter()方法进行构造    
API：
    next() 下一个元素
'''


# iter 构造迭代器
it = iter({ 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) })

# next下一个元素
print('next element:', next(it))
print('next element:', next(it))

list = [1, 3, 2, 5]
# 循环遍历
it = iter(list)
for el in it:
    print('iter el:', el, end = ',\t')
print()    

# 循环遍历
it = iter(list)
while True:
    try:
        print(next(it))
    except Exception:
        print('exit')
        sys.exit()     
```
## list 
[`list`](./07_examples_data_struct/list.py)

```python 

'''
 list 有序集合/有序列表

example：
    names = [ 'jack', 'jason', 'tom' ]

特点：
    1、有序
    2、支持随意添加、删除
    3、速度比dict数据字典、set要慢
    
API：
    1、len(list)     list长度，元素数量
    2、list[+-index]     取值
    3、 list.append(el)    添加新元素
    4、list.insert(index, el)    在list的index插入元素，如果存在就替换；当索引比长度还大时，元素会添加到末尾
    5、list.pop()    删除末尾的元素
    6、list.pop(index)    删除index位置的元素
    7、list + list2    两个list进行拼接
    8、list[start:end]    对list进行分割切片
    9、el in list, el not in    判断el是否在list中出现
    10、list.sort(key=None, reverse=True)     对list进行排序
    11、sorted(list)     对list进行排序
    12、del list[index]     删除指定index位置的元素
    13、list[index] = 'last element'     对已知存在的元素进行赋值，index必须是存在元素的下标
    14、list[start:end] = []    删除某个区间的元素
    15、list[start:end] = [ el, el2, el...]    将某个区间的元素进行覆盖（start:end存在就覆盖）或插入
    16、list.clear()  list[:] = []     清空元素
    
    17、del list_ref    删除指定list对象
    18、list * Number    将list复制指定次数Number
    19、list.copy()    浅复制
    20、list.count(el)    判断el元素出现的次数
    21、max(list)    找到最大的元素
    22、min(list)    找到最小的元素
    23、list.index(el, start, end)    判断el元素首次出现的下标索引，start/end可不传，不包含end位置
    24、list.extend(iter)     继承某个集合，合并一个新的list
    25、list.remove(el)    删除一个存在的元素，每次仅删除一个
    26、list.reverse()    倒序，按照默认插入先后顺序倒序
'''
 
```
## range 
[`range`](./07_examples_data_struct/range.py)

```python 

#################################################
#                   range 序列                                                 #
#################################################
'''
range 函数 可以生成一个list集合
	
example：
	range(5) -> 生成0 到 4的整数集合	
	range(1, 5) -> 生成 1到4的整数序列集合
	range(1, 10, 2) -> 生成1到9，每个元素+2的序列集合
	
range 函数像是一个for 循环，它可以有循环的起止位置和步长	
'''

# 生成指定截止区间的整数集合
print('range(5): ', end = '')
ranges = range(5)
for x in ranges:
	print(x, end = '; ')
print()
	
# 生成指定区间，带有起始位置的序列集合	
print('range(3, 7): ', end = '')
ranges = range(3, 7)
for x in ranges:
	print(x, end = '; ')
print()

# 生成指定区间，带有起始位置，并且有步长的序列集合	
print('range(3, 11, 2): ', end = '')
ranges = range(3, 11, 2)
for x in ranges:
	print(x, end = '; ')
print()

 
```
## set 
[`set`](./07_examples_data_struct/set.py)

```python 

'''
set 和dict类似，key集合。set 不能存放value，但key是不可重复的数据

特点：    
    1、key 不可重复，重复的将被过滤
    2、无序
    3、set 可以进行 交集 "&"、差集 "-"、并集"|"、排除交集 "^" 运算

example：
    numbers = set([ 1, 2, 2, 3, 1 ])
    
API:
    1、set.add(el)    添加新元素
    2、set.remove(el)    删除元素
    3、set.clear()    清空元素
    4、set1 & set2    交集
    5、set1 - set2    差集
    6、set1 | set2    并集
    7、set1 ^ set2    排除交集后的元素
'''

# 构造 set，通过set(iterable)方法构造，参数是一个iterable集合
numbers = set([ 1, 2, 2, 3, 1 ])
print('numbers set:', numbers)

numbers = set((2, 2, 4, 5, 1, 4))
print('numbers set:', numbers)

numbers = set({ 2: '', 3: '22', 5: '32' })
print('numbers set:', numbers)


# 添加元素 add，通过add方法添加新元素
numbers.add(6)
print('numbers set:', numbers)

# 删除元素
numbers.remove(6)
print('numbers set:', numbers)

 
```
## tuple 
[`tuple`](./07_examples_data_struct/tuple.py)

```python 

'''
tuple 元组  不可变列表
    
example:
    objects = ( 1, 2, [ 'a', 'b' ], 'd' )
    tuples = 'e', 'a', 'b', 'c', 'd'
    
API:
    1、tuple[index]    取值
    2、tuple[start:end]    切片取值
    3、(value, )    构建一个值的tuple
    4、tuple1 + tuple2    连接两个元组，并集
    5、del tmp    删除定义的元组对象
    6、len(tuple)    元组长度
    7、tuple * Number    将元组复制Number次
    8、el in tuple / el not in tuple     判断元素是否在元组中
    9、for x in tuple: print(x)        遍历
    
    10、tuple.count(el)    统计元素出现次数
    11、tuple.index(el, start, end)    统计元素首次出现位置，可以设置起止索引
    12、max(tuple)    找到最大的元素
    13、min(tuple)    找到最小的元素
    14、tuple([el, el1, el...])    list转tuple元组
'''

# tuple 和 list 雷同，但是它创建数据后不能随意修改
classes = ( 1, 2, 3)
print('classes: ', classes)

#构建元组
classes2 = 'e', 'a', 'b', 'c', 'd'
print('classes2: ', classes2)

# TypeError: 'tuple' object does not support item assignment
# classes[1] = 4
# AttributeError: 'tuple' object has no attribute 'append'
# classes.append(4)

# 取值方法，用索引下标的方式
print('first element:', classes[1]);
 
```
# 08_examples_if_else 
[**08_examples_if_else**](./08_examples_if_else)
## if_elif_else 
[`if_elif_else`](./08_examples_if_else/if_elif_else.py)

```python 

#################################################
#                   条件语句                                                      #
#################################################

'''

基本语法
	单条件语句
	if <条件>:
		doSomething...
	
	
	if <条件>:
		doSomething...
	else:
		doSomething...
	
	
	多条件语句
	if <条件>:
		doSomething...
	elif <条件>:
		doSomething...
	elif <条件>:
		doSomething...

---------------------------------------------
操作符：
	<	小于
	<=	小于或等于
	>	大于
	>=	大于或等于
	==	等于，比较对象是否相等
	!=	不等于
---------------------------------------------	
运算符			逻辑表达式			描述	实例
and				x and y			布尔"与" - 如果 x 为 False，x and y 返回 False，否则它返回 y 的计算值。	(a and b) 返回 20。
or				x or y			布尔"或" - 如果 x 是 True，它返回 x的值，否则它返回 y 的计算值。	(a or b) 返回 10。
not				not x			布尔"非" - 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。	not(a and b) 返回 False	
---------------------------------------------
 
```
# 09_examples_loop 
[**09_examples_loop**](./09_examples_loop)
## for_while 
[`for_while`](./09_examples_loop/for_while.py)

```python 

'''
遍历循环

for i in list:
    print(i)
    
for i in list:
    print(i)
else:
    print('xxx')
    
while i > 0:
    i += 1
    print(i)
    
'''

names = [ 'jack', 'tom', 'alex', 'charry' ]

# for 循环
for name in names:
    print('element: ', name)
print()

# 通过下标进行迭代循环
for i in range(len(names)):
    print('index: %s, val: %s' % (i, names[i]))
print()    
    
# range 序列函数，range可以生成一个指定区间的list集合    
ints = range(5)    
for i in ints:
    print('i: ', i)         
print()

# for...else...
for w in 'abcdef':
    print(w)
else:
    print('循环结束时执行')    
 
```
# 10_examples_func 
[**10_examples_func**](./10_examples_func)
## function 
[`function`](./10_examples_func/function.py)

```python 

import string

'''
函数
    可以重复调用执行的代码片段
    
语法：
        
        定义函数：
    def function_name(args):
        do something...

        执行函数：
    function_name(values)
    
参数

以下是调用函数时可使用的正式参数类型：

    必备参数：必备参数须以正确的顺序传入函数。调用时的数量必须和声明时的一样。    
    命名参数：命名参数和函数调用关系紧密，调用方用参数的命名确定传入的参数值。你可以跳过不传的参数或者乱序传参，因为Python解释器能够用参数名匹配参数值
    缺省参数：调用函数时，缺省参数的值如果没有传入，则被认为是默认值。
    不定长参数：你可能需要一个函数能处理比当初声明时更多的参数

'''

# 定义函数（必备参数）
def hello(arg):
    print('hello, ', arg)

# 执行函数
hello('world!')    
    
# 带返回值的函数
def say(content):
    return 'say ' + content

print('exec say:', say('hi~'))    
    
# 函数变量作用域
 
```
# 11_examples_pkg_modules/modules 
[**11_examples_pkg_modules/modules**](./11_examples_pkg_modules/modules)
## module 
[`module`](./11_examples_pkg_modules/modules/module.py)

```python 

# import sys引入python标准库中的sys.py模块；这是引入某一模块的方法
import sys
# 导入模块
import module_center

# 导入模块中的方法
from module_center import min_value, kw, module_name

# 导入时，会允许模块中的if代码块
import using_name


'''
模块
    包含变量和方法的文件，方便任何时间进行交互
'''

print('命令行参数如下：')
# sys.argv是一个包含命令行参数的列表
for x in sys.argv:
    print('param:', x)
         
# sys.path包含了一个Python解释器自动查找所需模块的路径的列表         
print('python path:', '\n'.join(sys.path))

# 定义自定义模块，并导入使用其中定义的方法
module_center.say('hi python') 

# 定义一个变量，接收模块方法
say = module_center.say
say('hi china')        

# 调用模块中的方法
min_value(1, 2, 5, 2, 3)
kw()

# 输出模块中的变量
print('module_name:', module_name)

# 输出当前模块主程序函数名称
 
```
## module_center 
[`module_center`](./11_examples_pkg_modules/modules/module_center.py)

```python 

import keyword

module_name = 'module_center'

print('module name：', __name__)

def say(content):
    print('you say:', content)
    
def kw():
    print('key word:', keyword.kwlist)   
    
def min_value(*args):
    print('min:', min(args))     
```
## using_name 
[`using_name`](./11_examples_pkg_modules/modules/using_name.py)

```python 

# Filename: using_name.py

# 一个模块被另一个程序第一次引入时，其主程序将运行。
# 如果我们想在模块被引入时，模块中的某一程序块不执行，我们可以用__name__属性来使该程序块仅在该模块自身运行时执行。
# 说明： 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入
if __name__ == '__main__':
    print('程序自身在运行')
else:
    print('我来自另一模块')

 
```
# 11_examples_pkg_modules/packages/core/files 
[**11_examples_pkg_modules/packages/core/files**](./11_examples_pkg_modules/packages/core/files)
## a 
[`a`](./11_examples_pkg_modules/packages/core/files/a.py)

```python 

print('import files.a') 
```
## b 
[`b`](./11_examples_pkg_modules/packages/core/files/b.py)

```python 

print('import files.b') 
```
## c 
[`c`](./11_examples_pkg_modules/packages/core/files/c.py)

```python 

print('import files.c') 
```
## d 
[`d`](./11_examples_pkg_modules/packages/core/files/d.py)

```python 

print('import files.d') 
```
## file 
[`file`](./11_examples_pkg_modules/packages/core/files/file.py)

```python 

def say_files():
    print('files module') 
```
## __init__ 
[`__init__`](./11_examples_pkg_modules/packages/core/files/__init__.py)

```python 

print('import core.files')

__all__ = [ "a", "b", "c" ]

 
```
# 11_examples_pkg_modules/packages/core/filters 
[**11_examples_pkg_modules/packages/core/filters**](./11_examples_pkg_modules/packages/core/filters)
## filter 
[`filter`](./11_examples_pkg_modules/packages/core/filters/filter.py)

```python 

def say_filters():
    print('filters module') 
```
## __init__ 
[`__init__`](./11_examples_pkg_modules/packages/core/filters/__init__.py)

```python 

print('import core.filters') 
```
# 11_examples_pkg_modules/packages/core/parser 
[**11_examples_pkg_modules/packages/core/parser**](./11_examples_pkg_modules/packages/core/parser)
## parser 
[`parser`](./11_examples_pkg_modules/packages/core/parser/parser.py)

```python 

parser_name = 'my parser'

def say_parser():
    print('files parser') 
```
## __init__ 
[`__init__`](./11_examples_pkg_modules/packages/core/parser/__init__.py)

```python 

print('import core.parser') 
```
# 11_examples_pkg_modules/packages/core 
[**11_examples_pkg_modules/packages/core**](./11_examples_pkg_modules/packages/core)
## __init__ 
[`__init__`](./11_examples_pkg_modules/packages/core/__init__.py)

```python 

print('import core') 
```
# 11_examples_pkg_modules/packages 
[**11_examples_pkg_modules/packages**](./11_examples_pkg_modules/packages)
## run 
[`run`](./11_examples_pkg_modules/packages/run.py)

```python 

'''
    导入包下面的模块
        包可以避免与其他的模块或方法混淆，利用包可以存在相同的文件和方法
        
注意
        当使用from package import item这种形式的时候，对应的item既可以是包里面的子模块（子包），或者包里面定义的其他名称，比如函数，类或者变量。
    
   import语法会首先把item当作一个包定义的名称，如果没找到，再试图按照一个模块去导入。如果还没找到，恭喜，一个:exc:ImportError 异常被抛出了。
        反之，如果使用形如import item.subitem.subsubitem这种导入形式，除了最后一项，都必须是包，而最后一项则可以是模块或者是包，但是不可以是类，函数或者变量的名字        
'''


#-----------------------------------------------------
# 导入包名
import core.files.file
# 必须全名访问，packages.flie.method()
core.files.file.say_files()


#-----------------------------------------------------
# 导入包和模块
from core.filters import filter
# 名称会简短
filter.say_filters() 


#-----------------------------------------------------
# 直接导入方法和变量
from core.parser.parser import say_parser, parser_name
# 使用导入的方法和变量
say_parser()
print('parser name:', parser_name) 


#-----------------------------------------------------
# 导入后使用短名称
import core.files.file as f
# 必须全名访问，packages.flie.method()
f.say_files()

 
```
# 11_examples_pkg_modules 
[**11_examples_pkg_modules**](./11_examples_pkg_modules)
## run 
[`run`](./11_examples_pkg_modules/run.py)

```python 

print('files module') 
```
# 12_examples_serialization 
[**12_examples_serialization**](./12_examples_serialization)
## io_serialization 
[`io_serialization`](./12_examples_serialization/io_serialization.py)

```python 

import pickle
import pprint

'''
基本的数据序列和反序列化。
    通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
    通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象
'''

data = { 'list': [ 1, 2, 'a', 2.3, 4.3+4j ], 'dict': { 'a': 1, 'b': '222' }, 'tuple': ('a', 233, 666) }
list = [ 'a', '2', 3, 2.2+2j ]
list.append(list)

#序列化----------------------------------------
output = open('f:/serial.txt', 'wb')

pickle.dump(data, output)
pickle.dump(list, output, -1)

output.close()

#反序列化--------------------------------------
output = open('f:/serial.txt', 'rb')

# 加载序列化的数据
data = pickle.load(output)
print('data:', data)

# 格式化输出反序列数据
pprint.pprint(data)
print()

# 加载数据
data2 = pickle.load(output)
print('data2:', data2)

# 格式化输出反序列数据
pprint.pprint(data2)

output.close()
 
```
# 13_examples_io 
[**13_examples_io**](./13_examples_io)
## io_file 
[`io_file`](./13_examples_io/io_file.py)

```python 

'''
文件操作


    打开文件
    open(filename, mode)
            第一个参数为要打开的文件名。
            第二个参数描述文件如何使用的字符。
        mode 可以是 'r' 如果文件只读, 'w' 只用于写 (如果存在同名文件则将被删除清空内容), 和 'a' 用于追加文件内容; 
                     所写的任何数据都会被自动增加到末尾. 'r+' 同时用于读写。 mode 参数是可选的; 'r' 将是默认值。
                     
        'r'       open for reading (default)
        'w'       open for writing, truncating the file first
        'x'       create a new file and open it for writing
        'a'       open for writing, appending to the end of the file if it exists
        'b'       binary mode
        't'       text mode (default)
        '+'       open a disk file for updating (reading and writing)
        'U'       universal newline mode (deprecated)
             
                     
    读文件
    f.read()
           为了读取一个文件的内容，调用 f.read(size), 这将读取一定数目的数据, 然后作为字符串或字节对象返回。
    size 是一个可选的数字类型的参数。 当 size 被忽略了或者为负, 那么该文件的所有内容都将被读取并且返回。
    
    f.readline()
          会从文件中读取单独的一行。换行符为 '\n'。f.readline() 如果返回一个空字符串, 说明已经已经读取到最后一行。
          
    f.readlines() 将返回该文件中包含的所有行。
           如果设置可选参数 sizehint, 则读取指定长度的字节, 并且将这些字节按行分割。       
          
           
     写文件
    f.write()
           将 string 写入到文件中, 然后返回写入的字符数。非字符串字符需要进行转换。
  
     读取位置         
    f.tell()
           返回文件对象当前所处的位置, 它是从文件开头开始算起的字节数
 
```
## io_file_next 
[`io_file_next`](./13_examples_io/io_file_next.py)

```python 

try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
# next 读取文件内容      
try:
    print('next 读取内容')
    for index in range(5):
        line = next(file)
        print('读取文件 %s 第 %d 行，内容：%s' % (file.name, index, line))
    
    # 指针移动到0
    file.seek(0)
    
    print('read 读取内容')
    # 读取10 个字节
    print('read(10): %s' % file.read(10))
    
    file.seek(0)
    # 负则读取所有
    print('read(-10): %s' % file.read(-10))
    
except NameError as e:
    print('error:', e)    
else:
    file.close()
    print('file colse:', file)
    

  
 
```
## io_file_read 
[`io_file_read`](./13_examples_io/io_file_read.py)

```python 

try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
# read 读取内容      
try:
    # 读取10 个字节
    print('read(10): %s' % file.read(10))
    
    # 指针移动到0
    file.seek(0)
    # 负则读取所有
    print('read(-10): %s' % file.read(-10))
    
    file.seek(0)
    #  读取整行
    line = file.readline()
    print('read line: %s' % (line))
    
    file.seek(0)
    #  读取3个字节
    line = file.readline(3)
    print('read 3 line: %s' % (line))
    
    file.seek(0)
    # 读取所有行
    lines = file.readlines()
    for line in lines:
        print('read lines: %s' % (line))
        
    print('当前位置：%d' % file.tell())    
    
    file.seek(0)
    print('当前位置：%d' % file.tell())
 
```
## io_file_truncate 
[`io_file_truncate`](./13_examples_io/io_file_truncate.py)

```python 

try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
file.write('This is a new line\n')
file.write('This is a new line2\n')
file.write('This is a new line3\n')
file.write('This is a new line4\n')
file.write('This is a new line5\n')
            
# read 读取内容      
try:
    file.seek(0);
    print('1-tell: ', file.tell())
    # 读取第一行
    print('readline: %s' % file.readline())
    print('2-tell: ', file.tell())
    
    file.truncate() # 上面的readline后指针移动到第二行，截取的数据将第一行之后的都删除
    print('3-tell: ', file.tell())
    
    file.seek(0);
    print('4-tell: ', file.tell())
    print('file line: %s' % file.readlines()) # 读到的内容和上面的是一样的
    print('5-tell: ', file.tell())
    
except NameError as e:
    print('error:', e)    
    

file.seek(0, 0)
file.write('ABC def ghi jkl mno')
    
# read 读取内容      
 
```
## io_file_write 
[`io_file_write`](./13_examples_io/io_file_write.py)

```python 

try:
    file = open('/tmp/open2.txt', 'r+')
except:  
    try: 
        print('retry open file')
        file = open('/tmp/open2.txt', 'wb')
    except:
        print('not open file')
    
    
try:
    
    file.truncate() # 清空文件内容

    # 指针移动到最开始位置
    file.seek(0, 0)
    
    print('1-tell: ', file.tell())
    
    file.write('This is a new line\n')
    file.write('This is a new line2\n')
    file.write('This is a new line3\n')
    file.write('This is a new line4\n')
    file.write('This is a new line5\n')
          
    # 0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。       
    file.seek(0, 0)       
    print('readline: %s' % file.readline())
    print('2-tell: ', file.tell())
    
    # 代表从文件末尾算起
    file.seek(0, 2)    
    file.write('This is a new line666\n')
    
    # 读取所有
    file.seek(0, 0)   
    print('readline: %s' % file.read(-1))
    
except NameError as e:
    print('error:', e)    
 
```
## io_inner_fun 
[`io_inner_fun`](./13_examples_io/io_inner_fun.py)

```python 

'''
文件操作内置函数
       
    1、file.close()
                    关闭文件。关闭后文件不能再进行读写操作。
    
    2、file.flush()
                    刷新文件内部缓冲，直接把内部缓冲区的数据立刻写入文件, 而不是被动的等待输出缓冲区写入。
    
    3、file.fileno()
                    返回一个整型的文件描述符(file descriptor FD 整型), 可以用在如os模块的read方法等一些底层操作上。
    
    4、file.isatty()
                    如果文件连接到一个终端设备返回 True，否则返回 False。
    
    5、file.next()
                    返回文件下一行。
    
    6、file.read([size])
                    从文件读取指定的字节数，如果未给定或为负则读取所有。
    
    7、file.readline([size])
                    读取整行，包括 "\n" 字符。
    
    8、file.readlines([sizehint])
                    读取所有行并返回列表，若给定sizeint>0，返回总和大约为sizeint字节的行, 实际读取值可能比sizhint较大, 因为需要填充缓冲区。
    
    9、file.seek(offset[, whence])
                    设置文件当前位置
    
    10、file.tell()
                    返回文件当前位置。
    
    11、file.truncate([size])
                    截取文件，截取的字节通过size指定，默认为当前文件位置。
    
    12、file.write(str)
                    将字符串写入文件，没有返回值。
    
    13、file.writelines(sequence)
 
```
## io_rw 
[`io_rw`](./13_examples_io/io_rw.py)

```python 

# 写文件
with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")
 
# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()
 
print(text) 
```
# 14_examples_os_dir 
[**14_examples_os_dir**](./14_examples_os_dir)
## os_access 
[`os_access`](./14_examples_os_dir/os_access.py)

```python 

import os


# 检验权限模式
'''
语法
    access()方法语法格式如下：
        os.access(path, mode);
            
           参数
    path -- 要用来检测是否有访问权限的路径。
    mode -- mode为F_OK，测试存在的路径，或者它可以是包含R_OK, W_OK和X_OK或者R_OK, W_OK和X_OK其中之一或者更多。
        os.F_OK: 作为access()的mode参数，测试path是否存在。
        os.R_OK: 包含在access()的mode参数中 ， 测试path是否可读。
        os.W_OK 包含在access()的mode参数中 ， 测试path是否可写。
        os.X_OK 包含在access()的mode参数中 ，测试path是否可执行。
'''

print('是否存在：%s ' % os.access('/tmp', os.F_OK)) # True
print('是否可读：%s ' % os.access('/tmp', os.R_OK)) # True
print('是否可写：%s ' % os.access('/tmp', os.W_OK)) # True
print('是否可执行：%s ' % os.access('/tmp', os.X_OK)) # True

print('是否存在：%s ' % os.access('/tmp/open.txt', os.F_OK)) # True
print('是否可读：%s ' % os.access('/tmp/open.txt1', os.R_OK)) # False 文件不存在，不可读
print('是否可写：%s ' % os.access('/tmp/open.txt', os.W_OK)) # True
print('是否可执行：%s' % os.access('/tmp/open.txt', os.X_OK)) # False # txt 文件不能执行
print('是否可执行：%s' % os.access('/tmp/open.sh', os.X_OK)) # True # *.sh 文件可以执行


print('是否可执行可写可读：%s' % os.access('/tmp/open.sh', os.X_OK|os.W_OK|os.R_OK)) # True # *.sh 文件可以执行 
```
## os_chdir 
[`os_chdir`](./14_examples_os_dir/os_chdir.py)

```python 

import os


'''
概述
    os.chdir() 方法用于改变当前工作目录到指定的路径。

语法
    chdir()方法语法格式如下：
    os.chdir(path)

参数
    path -- 要切换到的新路径。

返回值
        如果允许访问返回 True , 否则返回False。
'''

print('当前目录位置：%s' % os.getcwd())

# 切换到目录
os.chdir('/var/tmp')

print('当前目录位置：%s' % os.getcwd()) 
```
## os_chmod 
[`os_chmod`](./14_examples_os_dir/os_chmod.py)

```python 

import os
import stat


# 更改权限
'''
概述
    os.chmod() 方法用于更改文件或目录的权限。
语法
    chmod()方法语法格式如下：
    os.chmod(path, mode)
参数
path -- 文件名路径或目录路径。
flags -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， ，执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用
mode -- 可用以下选项按位或操作生成， 目录的读权限表示可以获取目录里文件名列表， 
    执行权限表示可以把工作目录切换到此目录 ，删除添加目录里的文件必须同时有写和执行权限 ，
    文件权限以用户id->组id->其它顺序检验,最先匹配的允许或禁止权限被应用。
    stat.S_IXOTH: 其他用户有执行权0o001
    stat.S_IWOTH: 其他用户有写权限0o002
    stat.S_IROTH: 其他用户有读权限0o004
    stat.S_IRWXO: 其他用户有全部权限(权限掩码)0o007
    
    stat.S_IXGRP: 组用户有执行权限0o010
    stat.S_IWGRP: 组用户有写权限0o020
    stat.S_IRGRP: 组用户有读权限0o040
    stat.S_IRWXG: 组用户有全部权限(权限掩码)0o070
    
    stat.S_IXUSR: 拥有者具有执行权限0o100
    stat.S_IWUSR: 拥有者具有写权限0o200
    stat.S_IRUSR: 拥有者具有读权限0o400
    stat.S_IRWXU: 拥有者有全部权限(权限掩码)0o700
    
    stat.S_ISVTX: 目录里文件目录只有拥有者才可删除更改0o1000
    stat.S_ISGID: 执行此文件其进程有效组为文件所在组0o2000
    stat.S_ISUID: 执行此文件其进程有效用户为文件所有者0o4000
    
    stat.S_IREAD: windows下设为只读
    stat.S_IWRITE: windows下取消只读
'''

 
```
## os_chown 
[`os_chown`](./14_examples_os_dir/os_chown.py)

```python 

import os

'''
语法
  chown()方法语法格式如下：
        os.chown(path, uid, gid);
        
参数
    path -- 设置权限的文件路径
    uid -- 所属用户 ID
    gid -- 所属用户组 ID
'''

# 假定 /tmp/foo.txt 文件存在.
# 设置所有者 ID 为 1000

#linux 查看用户组
#tail /etc/group 
os.chown("/tmp/open.txt", 1000, -1) 
```
## os_chroot 
[`os_chroot`](./14_examples_os_dir/os_chroot.py)

```python 

import os

'''
概述
    os.chroot() 方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。
语法
    chroot()方法语法格式如下：
    os.chroot(path);
参数
    path -- 要设置为根目录的目录。
返回值
        该方法没有返回值。
'''

# 设置根目录为 /tmp

print('当前目录：%s' % os.getcwd())
os.chroot("/tmp")
print("修改根目录成功!!")
print('当前目录：%s' % os.getcwd()) 
```
## os_dir 
[`os_dir`](./14_examples_os_dir/os_dir.py)

```python 

import os
import stat


'''
处理文件和目录

    1、os.access(path, mode)
                    检验权限模式
    
    2、os.chdir(path)
                    改变当前工作目录
    
    3、os.chflags(path, flags)
                    设置路径的标记为数字标记。
    
    4、os.chmod(path, mode)
                    更改权限
    
    5、os.chown(path, uid, gid)
                    更改文件所有者
    
    6、os.chroot(path)
                    改变当前进程的根目录
    
    7、os.close(fd)
                    关闭文件描述符 fd
    
    8 os.closerange(fd_low, fd_high)
                    关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
    
    9、os.dup(fd)
                    复制文件描述符 fd
    
    10、os.dup2(fd, fd2)
                    将一个文件描述符 fd 复制到另一个 fd2
    
    11、os.fchdir(fd)
                    通过文件描述符改变当前工作目录
    
 
```
## os_fchdir 
[`os_fchdir`](./14_examples_os_dir/os_fchdir.py)

```python 

import os

'''
概述
    os.fchdir() 方法通过文件描述符改变当前工作目录。
    Unix, Windows 上可用。
    
语法
    fchdir()方法语法格式如下：
    os.fchdir(fd);

参数
    fd -- 文件描述符

返回值
        该方法没有返回值。
'''

# 切换到目录
os.chdir('/var/tmp')

print('当前目录位置：%s' % os.getcwd())

# 打开文件目录
fd = os.open('/tmp', os.O_RDONLY)

# fchdir 修改目录，必须是文件夹fd
os.fchdir(fd)

print('当前目录位置：%s' % os.getcwd())

os.close(fd)


 
```
## os_fchmod 
[`os_fchmod`](./14_examples_os_dir/os_fchmod.py)

```python 

import os
import stat


'''
概述
    os.fchmod() 方法用于改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。
    Unix上可用。
语法
    fchmod()方法语法格式如下：
    os.fchmod(fd, mode);
参数
    fd -- 文件描述符
    mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：
        stat.S_ISUID:设置 UID 位
        stat.S_ISGID: 设置组 ID 位
        stat.S_ENFMT: 系统文件锁定的执法行动
        stat.S_ISVTX: 在执行之后保存文字和图片
        
        stat.S_IREAD: 对于拥有者读的权限
        stat.S_IWRITE: 对于拥有者写的权限
        stat.S_IEXEC: 对于拥有者执行的权限
        
        stat.S_IRWXU:对于拥有者读、写、执行的权限
        stat.S_IRUSR: 对于拥有者读的权限
        stat.S_IWUSR: 对于拥有者写的权限
        stat.S_IXUSR: 对于拥有者执行的权限
        
        stat.S_IRWXG: 对于同组的人读写执行的权限
        stat.S_IRGRP: 对于同组读的权限
        stat.S_IWGRP:对于同组写的权限
        stat.S_IXGRP: 对于同组执行的权限
        
        stat.S_IRWXO: 对于其他组读写执行的权限
        stat.S_IROTH: 对于其他组读的权限
        stat.S_IWOTH: 对于其他组写的权限
        stat.S_IXOTH:对于其他组执行的权限
返回值
        该方法没有返回值。
'''
 
```
## os_fchown 
[`os_fchown`](./14_examples_os_dir/os_fchown.py)

```python 

import os

'''
概述
    os.fchown() 方法用于修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。
    Unix上可用。

语法
    fchown()方法语法格式如下：
    os.fchown(fd, uid, gid)

参数
    fd -- 文件描述符
    uid -- 文件所有者的用户id
    gid -- 文件所有者的用户组id

返回值
            该方法没有返回值
'''

# 打开文件
fd = os.open('/tmp/dir', os.O_RDONLY)

# 设置文件的用户id = 100
os.fchown(fd, 100, -1)

os.fchown(fd, -1, 50)

# cat /etc/group 查看权限，当前用户为1000
os.fchown(fd, 1000, 1000)

os.close(fd)

print('所有权修改完成') 
```
## os_fpathconf 
[`os_fpathconf`](./14_examples_os_dir/os_fpathconf.py)

```python 

import os

'''
概述
    os.fpathconf() 方法用于返回一个打开的文件的系统配置信息。
    Unix上可用。

语法
    fpathconf()方法语法格式如下：
    os.fpathconf(fd, name)
    
参数
    fd -- 打开的文件的描述符。
    name -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
    bufsize -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，传递一个数字作为名字，也是可以接受的。

返回值
        返回一个打开的文件的系统配置信息
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 配置名称列表
print('配置名称列表: %s' % os.pathconf_names)

print('文件最大连接数：%d' % os.fpathconf(fd, 'PC_LINK_MAX'))

print('文件名最大长度：%d' % os.fpathconf(fd, 'PC_NAME_MAX'))

os.close(fd) 
```
## os_fstat 
[`os_fstat`](./14_examples_os_dir/os_fstat.py)

```python 

import os

'''
概述
    os.fstat() 方法用于返回文件描述符fd的状态，类似 stat()。
    Unix，Windows上可用。
    
fstat 方法返回的结构:
    st_dev: 设备信息
    st_ino: 文件的i-node值
    st_mode: 文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)
    st_nlink: 硬连接数
    st_uid: 用户ID
    st_gid: 用户组 ID
    st_rdev: 设备 ID (如果指定文件)
    st_size: 文件大小，以byte为单位
    st_blksize: 系统 I/O 块大小
    st_blocks: 文件的是由多少个 512 byte 的块构成的
    st_atime: 文件最近的访问时间
    st_mtime: 文件最近的修改时间
    st_ctime: 文件状态信息的修改时间（不是文件内容的修改时间）
    
语法
    fstat()方法语法格式如下：
    os.fstat(fd)
    
参数
    fd -- 文件的描述符。
    
返回值
        返回文件描述符fd的状态。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT)

info = os.fstat(fd)
print('fd info: %s' % info)

# 文件gid
 
```
## os_fstatvfs 
[`os_fstatvfs`](./14_examples_os_dir/os_fstatvfs.py)

```python 

import os


'''
概述
    os.fstatvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息，类似 statvfs()。
    Unix上可用。

fstatvfs 方法返回的结构:
    f_bsize: 文件系统块大小
    f_frsize: 分栈大小
    f_blocks: 文件系统数据块总数
    f_bfree: 可用块数
    f_bavail:非超级用户可获取的块数
    f_files: 文件结点总数
    f_ffree: 可用文件结点数
    f_favail: 非超级用户的可用文件结点数
    f_fsid: 文件系统标识 ID
    f_flag: 挂载标记
    f_namemax: 最大文件长度

语法
    fstatvfs()方法语法格式如下：
    os.fstatvfs(fd)
    
参数
    fd -- 文件的描述符。
    
返回值
        返回包含文件描述符fd的文件的文件系统的信息。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT)

# 获取文件描述
info = os.fstatvfs(fd)

print('文件信息：%s' % info)

 
```
## os_getcwd 
[`os_getcwd`](./14_examples_os_dir/os_getcwd.py)

```python 

import os

'''
概述
    os.getcwd() 方法用于返回当前工作目录。
    
语法
    getcwd()方法语法格式如下：
    os.getcwd()
参数
        无
        
返回值
        返回当前进程的工作目录。
'''

# 切换目录
os.chdir('/var/tmp')

# 当前工作目录
print('当前工作目录: %s' % os.getcwd())

# 打开文件夹，文件夹不能用 os.O_RDWR
fd = os.open('/tmp', os.O_RDONLY) 

# 切换工作目录，fd 必须为文件夹
os.fchdir(fd)

print('当前工作目录: %s' % os.getcwd())

os.close(fd) 
```
## os_getcwdu 
[`os_getcwdu`](./14_examples_os_dir/os_getcwdu.py)

```python 

import os

'''
概述
    os.getcwdu() 方法用于返回一个当前工作目录的Unicode对象。
    Unix, Windows 系统下可用。

语法
    getcwdu()方法语法格式如下：
    os.getcwdu()

参数
            无
            
返回值
        返回一个当前工作目录的Unicode对象
'''

# 切换工作目录
os.chdir('/var/tmp/')

print('当前工作目录：', os.getcwdu())

# 打开文件夹
fd = os.open('/home', os.O_RDONLY)

# 切换工作目录
os.fchdir(fd)

print(u'当前工作目录：', os.getcwdu())

os.close(fd) 
```
## os_lchown 
[`os_lchown`](./14_examples_os_dir/os_lchown.py)

```python 

import os

'''
概述
    os.lchown() 方法用于更改文件所有者，类似 chown，但是不追踪链接。
        只支持在 Unix 下使用。

语法
    lchown()方法语法格式如下：
    os.lchown(path, uid, gid)
    
参数
    path -- 设置权限的文件路径
    uid -- 所属用户 ID
    gid -- 所属用户组 ID
    
返回值
        该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)
print('状态：%s' % os.fstat(fd))

os.lchown('/tmp/foo.txt', 100, -1)
print('状态：%s' % os.fstat(fd))

os.lchown('/tmp/foo.txt', 1000, 1000)
print('状态：%s' % os.fstat(fd))

os.close(fd) 
```
## os_link 
[`os_link`](./14_examples_os_dir/os_link.py)

```python 

import os

'''
概述
   os.link() 方法用于创建硬链接，名为参数 dst，指向参数 src。
        该方法对于创建一个已存在文件的拷贝是非常有用的。
        只支持在 Unix, Windows 下使用。

语法
    link()方法语法格式如下：
    os.link(src, dst)

参数
    src -- 用于创建硬连接的源地址
    dst -- 用于创建硬连接的目标地址

返回值
        该方法没有返回值
'''

# 创建快捷方式链接
#os.link('/tmp/mydir', '/tmp/dir/tmp_my_dir')

os.link('/tmp/foo.txt', '/tmp/dir/foo.txt') 
```
## os_listdir 
[`os_listdir`](./14_examples_os_dir/os_listdir.py)

```python 

import os

'''
概述
    os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。
    只支持在 Unix, Windows 下使用。

语法
    listdir()方法语法格式如下：
    os.listdir(path)

参数
    path -- 需要列出的目录路径
    
返回值
        返回指定路径下的文件和文件夹列表。
'''

dirs = os.listdir('/var/')

for dir in dirs:
    print('dir: %s' % dir)
    
    
print('-----------------------------')    
dirs = os.listdir('/tmp/')

for dir in dirs:
    print('dir: %s' % dir) 
```
## os_lstat 
[`os_lstat`](./14_examples_os_dir/os_lstat.py)

```python 

import os

'''
概述
    os.lstat() 方法用于类似 stat() 返回文件的信息,但是没有符号链接。在某些平台上，这是fstat的别名，例如 Windows。

语法
    lstat()方法语法格式如下：
    os.lstat(path)

参数
    path -- 要返回信息的文件。

返回值
        返回文件信息。
'''

print('stat：%s' % os.lstat('/tmp/foo.txt'))

print('stat：%s' % os.lstat('/tmp/')) 
```
## os_makedirs 
[`os_makedirs`](./14_examples_os_dir/os_makedirs.py)

```python 

import os


'''
概述
    os.makedirs() 方法用于递归创建目录。像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。

语法
    makedirs()方法语法格式如下：
    os.makedirs(path, mode=0o777)

参数
    path -- 需要递归创建的目录。
    mode -- 权限模式。

返回值
        该方法没有返回值。
'''

# 递归创建文件夹
os.makedirs('/tmp/da/db', 0x755)

print('创建文件夹') 
```
## os_mkdir 
[`os_mkdir`](./14_examples_os_dir/os_mkdir.py)

```python 

import os

'''
概述
    os.mkdir() 方法用于以数字权限模式创建目录。默认的模式为 0777 (八进制)。
    
语法
    mkdir()方法语法格式如下：
    os.mkdir(path[, mode])
    
参数
    path -- 要创建的目录
    mode -- 要为目录设置的权限数字模式
    
返回值
            该方法没有返回值。
'''

# 创建文件夹，不能递归创建
os.mkdir('/tmp/m', 0x777)

# 递归创建文件夹
os.makedirs('/tmp/mm/nn', 0x755)

print('创建文件夹完成') 
```
## os_readlink 
[`os_readlink`](./14_examples_os_dir/os_readlink.py)

```python 

import os


'''
概述
    os.readlink() 方法用于返回软链接所指向的文件。可能返回绝对火相对路径。
            在Unix中有效

语法
    readlink()方法语法格式如下：
    os.readlink(path)

参数
    path -- 要查找的软链接路径

返回值
        返回软链接所指向的文件
'''

# 创建软连接
os.symlink('/var/tmp', '/tmp/var_tmp')

lk = os.readlink('/tmp/var_tmp')
print('link: %s' % lk)
 
```
## os_removedirs 
[`os_removedirs`](./14_examples_os_dir/os_removedirs.py)

```python 

import os

'''
概述
    os.removedirs() 方法用于递归删除目录。像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。

语法
    removedirs()方法语法格式如下：
    os.removedirs(path)

参数
    path -- 要移除的目录路径

返回值
        该方法没有返回值
'''

# 列出目录
print ("目录为: %s" % os.listdir('/tmp'))

# 递归删除目录
os.removedirs('/tmp/da/db')
os.removedirs('/tmp/m')

print ("目录为: %s" % os.listdir('/tmp')) 
```
## os_rmdir 
[`os_rmdir`](./14_examples_os_dir/os_rmdir.py)

```python 

import os


'''
概述
    os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。

语法
    rmdir()方法语法格式如下：
    os.rmdir(path)

参数
    path -- 要删除的目录路径

返回值
        该方法没有返回值
'''

# 切换工作目录
os.chdir('/tmp')

# 文件列表
print('file list: %s' % os.listdir(os.getcwd()))
      
# 该目录不能包含文件或文件夹      
os.rmdir('ppf2')      

print('file list: %s' % os.listdir(os.getcwd())) 
```
## os_sys 
[`os_sys`](./14_examples_os_dir/os_sys.py)

```python 

###进程管理
###os模块提供了许多进程管理相关的操作，如果熟悉Unix下的系统编程的话，那么看到这些函数会觉得很熟悉，因为这些函数都是对相应的C API的Python实现，让我们看看都有些什么函数：

'''
os.abort()
向调用该函数的进程发送一个SIGABRT信号，在Unix系统上默认的行为是产生一个core文件。
注意：当调用os.abort()函数的时候不会调用python的信号处理函数signal.signal()。

os.exe系列函数
os.execl(path, arg0, arg1, ...)
os.execle(path, arg0, arg1, ..., env)
os.execlp(file, arg0, arg1, ...)
os.execlpe(file, arg0, arg1, ..., env)
os.execv(path, args)
os.execve(path, args, env)
os.execvp(file, args)
os.execvpe(file, args, env)

这些函数都执行一个新的程序，然后用新的程序替换当前子进程的进程空间，而该子进程从新程序的main函数开始执行。在Unix下，该新程序的进程id是原来被替换的子进程的进程id。在原来子进程中打开的所有描述符默认都是可用的，不会被关闭。
execv*系列的函数表示其接受的参数是以一个list或者是一个tuple表示的参数表
execl*系列的函数表示其接受的参数是一个个独立的参数传递进去的。
exec*p*系列函数表示在执行参数传递过去的命令时使用PATH环境变量来查找命令
exec*e系列函数表示在执行命令的时候读取该参数指定的环境变量作为默认的环境配置，最后的env参数必须是一个mapping对象，可以是一个dict类型的对象。

os._exit(n)
退出进程，并且返回退出状态n，在退出的时候不会执行清理工作，直接退出。
注意：正常的退出应该使用sys.exit(n)，而_exit()函数一般只用在fork之后的子进程中调用以退出。

可用的退出状态(并不适用所有的Unix平台都可用):
os.EX_OK - 正常退出
os.EX_USAGE - 命令执行不正确，如命令参数错误
os.EX_DATAERR - 输入数据有误
os.EX_NOINPUT - 输入文件不存在或者不可读
os.EX_NOUSER - 指定的用户不存在
os.EX_NOHOST - 指定的主机id不存在
os.EX_UNAVAILABLE - 请求的服务不可用
os.EX_SOFTWARE - 内部软件错误
os.EX_OSERR - 操作系统错误
os.EX_OSFILE - 系统文件不存在
os.EX_CANTCREAT - 无法创建指定的输出文件
 
```
## os_unlink 
[`os_unlink`](./14_examples_os_dir/os_unlink.py)

```python 

import os


'''
概述
    os.unlink() 方法用于删除文件,如果文件是一个目录则返回一个错误。

语法
    unlink()方法语法格式如下：
    os.unlink(path)

参数
    path -- 删除的文件路径

返回值
        该方法没有返回值
'''

# 列举目录
print('dirs: %s' % os.listdir('/tmp'))

# 取消软连接
os.unlink('/tmp/my_dir')

print('dirs: %s' % os.listdir('/tmp')) 
```
## os_utime 
[`os_utime`](./14_examples_os_dir/os_utime.py)

```python 

import os


'''
概述
    os.utime() 方法用于设置指定路径文件最后的修改和访问时间。
            在Unix，Windows中有效。

语法
    utime()方法语法格式如下：
    os.utime(path, times)

参数
    path -- 文件路径
    times -- 如果时间是 None, 则文件的访问和修改设为当前时间 。 否则, 时间是一个 2-tuple数字, (atime, mtime) 用来分别作为访问和修改的时间。

返回值
        该方法没有返回值
'''

info = os.stat('/tmp/foo.txt')

print('info: %s' % info)

print('st_ctime: %s' % info.st_ctime)
print('st_mtime: %s' % info.st_mtime)

os.utime('/tmp/foo.txt', (1522073000, 1522073000))

info = os.stat('/tmp/foo.txt')
print('st_ctime: %s' % info.st_ctime)
print('st_mtime: %s' % info.st_mtime) 
```
## _os_chflags 
[`_os_chflags`](./14_examples_os_dir/_os_chflags.py)

```python 

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
```
## _os_lchflags 
[`_os_lchflags`](./14_examples_os_dir/_os_lchflags.py)

```python 

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
```
## _os_lchmod 
[`_os_lchmod`](./14_examples_os_dir/_os_lchmod.py)

```python 

import os

'''
概述
    os.lchmod() 方法用于修改连接文件权限。
        只支持在 Unix 下使用。
    
语法
    lchmod()方法语法格式如下：
    os.lchmod(path, mode)

参数
    path -- 设置标记的文件路径
    mode -- 可以是以下一个或多个组成，多个使用 "|" 隔开：
    stat.S_ISUID:设置 UID 位
    stat.S_ISGID: 设置组 ID 位
    stat.S_ENFMT: 系统文件锁定的执法行动
    stat.S_ISVTX: 在执行之后保存文字和图片
    
    stat.S_IREAD: 对于拥有者读的权限
    stat.S_IWRITE: 对于拥有者写的权限
    stat.S_IEXEC: 对于拥有者执行的权限
    
    stat.S_IRWXU:对于拥有者读、写、执行的权限
    stat.S_IRUSR: 对于拥有者读的权限
    stat.S_IWUSR: 对于拥有者写的权限
    stat.S_IXUSR: 对于拥有者执行的权限
    
    stat.S_IRWXG: 对于同组的人读写执行的权限
    stat.S_IRGRP: 对于同组读的权限
    stat.S_IWGRP:对于同组写的权限
    stat.S_IXGRP: 对于同组执行的权限
    
    stat.S_IRWXO: 对于其他组读写执行的权限
    stat.S_IROTH: 对于其他组读的权限
    stat.S_IWOTH: 对于其他组写的权限
    stat.S_IXOTH:对于其他组执行的权限

返回值
        该方法没有返回值。
 
```
# 15_examples_os_file 
[**15_examples_os_file**](./15_examples_os_file)
## os_close 
[`os_close`](./15_examples_os_file/os_close.py)

```python 

'''
概述
    os.close() 方法用于关闭指定的文件描述符 fd。
语法
    close()方法语法格式如下：
    os.close(fd);
    
参数
    fd -- 文件描述符。
    
返回值
        该方法没有返回值。
'''

import os, sys

# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR|os.O_CREAT)

#  写入字符串
os.write(fd, "This is test")

# 关闭文件
os.close(fd)

print ("关闭文件成功!!") 
```
## os_closerange 
[`os_closerange`](./15_examples_os_file/os_closerange.py)

```python 

'''
概述
    os.closerange() 方法用于关闭所有文件描述符 fd，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略。

语法
    closerange()方法语法格式如下：
    os.closerange(fd_low, fd_high);

参数
    fd_low -- 最小文件描述符
    fd_high -- 最大文件描述符

该方法类似于：
    for fd in xrange(fd_low, fd_high):
        try:
            os.close(fd)
        except OSError:
            pass
            
返回值
        该方法没有返回值
'''

import os

# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR|os.O_CREAT)

# 写入字符串
os.write(fd, "This is test2")

# 关闭文件
os.closerange(fd, fd)

print("关闭文件成功!!") 
```
## os_dup 
[`os_dup`](./15_examples_os_file/os_dup.py)

```python 

import os

'''
概述
    os.dup() 方法用于复制文件内容 fd。
    
语法
    dup()方法语法格式如下：
    os.dup(fd);
    
参数
    fd -- 文件内容
    
返回值
        返回复制的文件内容。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 复制文件内容
dup_fd = os.dup(fd)

# 写入新文本
os.write(dup_fd, 'write new text')

# 关闭文件fd、dup_fd
os.closerange(fd, dup_fd)

print('操作完成') 
```
## os_dup2 
[`os_dup2`](./15_examples_os_file/os_dup2.py)

```python 

import os


'''
概述
    os.dup2() 方法用于将一个文件描述符 fd 复制到另一个 fd2。
    Unix, Windows 上可用。

语法
    dup2()方法语法格式如下：
    os.dup2(fd, fd2);
    
参数
    fd -- 要被复制的文件描述符
    fd2 -- 复制的文件描述符

返回值
    没有返回值
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 写入文件
os.write(fd, 'this is new line')

# 复制文件
fd2 = 1000
os.dup2(fd, fd2)

# 移动文件指针
os.lseek(fd2, 0, 0)
print('读取文件内容：%s' % os.read(fd2, 100))

# 关闭文件
os.close(fd)
#os.closerange(fd, fd2)
print('操作完成') 
```
## os_fdatasync 
[`os_fdatasync`](./15_examples_os_file/os_fdatasync.py)

```python 

import os


'''
概述
    os.fdatasync() 方法用于强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。如果你需要刷新缓冲区可以使用该方法。
    Unix上可用。

语法
    fdatasync()方法语法格式如下：
    os.fdatasync(fd);

参数
    fd -- 文件描述符

返回值
        该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 写入文件内容
os.write(fd, '新的内容写入')

# 同步文件到硬盘，防止文件内容丢失
os.fdatasync(fd)

# 移动文件指针
os.lseek(fd, 0, 0)

# 读取文件内容
str = os.read(fd, 100)
print('读到内容：%s' % str)

os.close(fd)
 
```
## os_fdopen 
[`os_fdopen`](./15_examples_os_file/os_fdopen.py)

```python 

import os


'''
概述
    os.fdopen() 方法用于通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。
    Unix, Windows上可用。
    
语法
    fdopen()方法语法格式如下：
    os.fdopen(fd, [, mode[, bufsize]]);
    
参数
    fd -- 打开的文件的描述符，在Unix下，描述符是一个小整数。
    mode -- 可选，和buffersize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
    bufsize -- 可选，指定返回的文件对象是否带缓冲：buffersize=0，表示没有带缓冲；bufsize=1，表示该文件对象是行缓冲的；bufsize=正数，表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，对于tty字元设备一般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。
    
返回值
        通过文件描述符返回的文件对象
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR)

# 打开文件fd，获取文件对象; 并且开启写入权限
file = os.fdopen(fd, 'w+')

print('当前位置: %d' % file.tell())

# 写入新内容
file.write('fdopen file write line\n')

# 移动指针
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print('读到文本：%s' % str)

# 当前位置
print('当前位置: %d' % file.tell())

 
```
## os_file 
[`os_file`](./15_examples_os_file/os_file.py)

```python 

import os
import stat


'''
处理文件和目录

    1、os.access(path, mode)
                    检验权限模式
    
    2、os.chdir(path)
                    改变当前工作目录
    
    3、os.chflags(path, flags)
                    设置路径的标记为数字标记。
    
    4、os.chmod(path, mode)
                    更改权限
    
    5、os.chown(path, uid, gid)
                    更改文件所有者
    
    6、os.chroot(path)
                    改变当前进程的根目录
    
    7、os.close(fd)
                    关闭文件描述符 fd
    
    8 os.closerange(fd_low, fd_high)
                    关闭所有文件描述符，从 fd_low (包含) 到 fd_high (不包含), 错误会忽略
    
    9、os.dup(fd)
                    复制文件描述符 fd
    
    10、os.dup2(fd, fd2)
                    将一个文件描述符 fd 复制到另一个 fd2
    
    11、os.fchdir(fd)
                    通过文件描述符改变当前工作目录
    
 
```
## os_fpathconf 
[`os_fpathconf`](./15_examples_os_file/os_fpathconf.py)

```python 

import os


'''
概述
    os.pathconf() 方法用于返回一个打开的文件的系统配置信息。
    Unix 平台下可用。
    
语法
    fpathconf()方法语法格式如下：
    os.fpathconf(fd, name)
    
参数
    name -- 文件描述符
    name -- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf_names的字典中。对于不在pathconf_names中的配置变量，传递一个数字作为名字，也是可以接受的。

返回值
        返回文件的系统信息。
'''
import os

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR|os.O_CREAT)

print('pathconf_names: %s' % os.pathconf_names)

# 最大连接数
print('最大连接数：%s' % os.fpathconf(fd, 'PC_LINK_MAX'))

os.close(fd) 
```
## os_fsync 
[`os_fsync`](./15_examples_os_file/os_fsync.py)

```python 

import os

'''
概述
    os.fsync() 方法强制将文件描述符为fd的文件写入硬盘。在Unix, 将调用fsync()函数;在Windows, 调用 _commit()函数。
    如果你准备操作一个Python文件对象f, 首先f.flush(),然后os.fsync(f.fileno()), 确保与f相关的所有内存都写入了硬盘.在unix，Windows中有效。
    Unix、Windows上可用。
    
语法
    fsync()方法语法格式如下：
    os.fsync(fd)

参数
    fd -- 文件的描述符。
    
返回值
            该方法没有返回值。
'''

# 打开读取文件
fd = os.open('/tmp/foo.txt', os.O_RDWR)

# 写入内容
os.write(fd, '写入内容试试看')

# 同步文件内容到物理硬盘
os.fsync(fd)

# 移动文件指针到最前面
os.lseek(fd, 0, 0)
print('读取文件内容：%s' % os.read(fd, 100))

os.close(fd) 
```
## os_ftruncate 
[`os_ftruncate`](./15_examples_os_file/os_ftruncate.py)

```python 

import os

'''
概述
    os.ftruncate() 裁剪文件描述符fd对应的文件, 它最大不能超过文件大小。
    Unix上可用。

语法
    ftruncate()方法语法格式如下：
    os.ftruncate(fd, length)¶

参数
    fd -- 文件的描述符。
    length -- 要裁剪文件大小。

返回值
        该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR)

# 写入内容
os.write(fd, '新生代文本内容')

# 截取文件内容
os.ftruncate(fd, 20)

# 移动文件指针
os.lseek(fd, 0, 0)
print('读取文件内容：%s' % os.read(fd, 100))

os.close(fd) 
```
## os_isatty 
[`os_isatty`](./15_examples_os_file/os_isatty.py)

```python 

import os

'''
概述
    os.isatty() 方法用于判断如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

语法
    isatty()方法语法格式如下：
    os.isatty()
    
参数
        无

返回值
        如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。
'''


# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

# 判断文件与设备相连
print('判断文件与设备相连: %s' % os.isatty(fd))

os.close(fd) 
```
## os_lseek 
[`os_lseek`](./15_examples_os_file/os_lseek.py)

```python 

import os

'''
概述
    os.lseek() 方法用于设置文件描述符 fd 当前位置为 pos, how 方式修改。
            在Unix，Windows中有效。
            
语法
    lseek()方法语法格式如下：
    os.lseek(fd, pos, how)

参数
    fd -- 文件描述符。
    pos -- 这是相对于给定的参数 how 在文件中的位置。。
    how -- 文件内参考位置。SEEK_SET 或者 0 设置从文件开始的计算的pos; SEEK_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始。

返回值
    该方法没有返回值。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_CREAT|os.O_RDWR)

os.write(fd, '写入seek文本')

# 所有 fsync() 方法
os.fsync(fd)

print('读取内容：%s' % os.read(fd, 100))

# 移动到文件行首
os.lseek(fd, 0, 0)
print('读取内容：%s' % os.read(fd, 100))

# 移动到文件末尾
os.lseek(fd, 0, 1)
print('读取内容：%s' % os.read(fd, 100)) 
```
## os_major 
[`os_major`](./15_examples_os_file/os_major.py)

```python 

import os

'''
概述
    os.major() 方法用于从原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。

语法
    major()方法语法格式如下：
    os.major(device)

参数
    device -- 原始的设备号中提取设备major号码 (使用stat中的st_dev或者st_rdev field)。
    
返回值
        返回设备major号码
'''


info = os.lstat('/tmp/foo.txt')

print('stat info: %s' % info)

print('major 设备号: %s' % os.major(info.st_dev))
print('minor 设备号: %s' % os.minor(info.st_dev)) 
```
## os_makedev 
[`os_makedev`](./15_examples_os_file/os_makedev.py)

```python 

import os

'''
概述
    os.makedev() 方法用于以major和minor设备号组成一个原始设备号。

语法
    makedev()方法语法格式如下：
    os.makedev(major, minor)

参数
    major -- Major 设备号。
    minor -- inor 设备号。

返回值
        返回设备号。
'''



info = os.lstat('/tmp/foo.txt')

print('stat info: %s' % info)

print('major 设备号: %s' % os.major(info.st_dev))
print('minor 设备号: %s' % os.minor(info.st_dev))

print('makedev 设备号: %s' % os.makedev(os.major(info.st_dev), os.minor(info.st_dev)))
 
```
## os_mkfifo 
[`os_mkfifo`](./15_examples_os_file/os_mkfifo.py)

```python 

import os

'''
概述
    os.mkfifo() 方法用于创建指令路径的管道，并设置权限模式。默认的模式为 0666 (八进制)。

语法
    mkfifo()方法语法格式如下：
    os.mkfifo(path[, mode])

参数
    path -- 要创建的目录
    mode -- 要为目录设置的权限数字模式

返回值
        该方法没有返回值。
'''

# 创建文件
os.mkfifo('/tmp/ab3.txt', 0x777)

os.mkfifo('/tmp/abe', 0x777)

print('创建完成') 
```
## os_mknod 
[`os_mknod`](./15_examples_os_file/os_mknod.py)

```python 

import os
import stat

'''
概述
    os.mknod() 方法用于创建一个指定文件名的文件系统节点（文件，设备特别文件或者命名pipe）。

语法
    mknod()方法语法格式如下：
    os.mknod(filename[, mode=0600[, device=0]])

参数
    filename -- 创建的文件系统节点
    mode -- mode指定创建或使用节点的权限, 组合 (或者bitwise) stat.S_IFREG, stat.S_IFCHR, stat.S_IFBLK, 和stat.S_IFIFO (这些常数在stat模块). 对于 stat.S_IFCHR和stat.S_IFBLK, 设备定义了 最新创建的设备特殊文件 (可能使用 os.makedev()),其它都将忽略。
    device -- 可选，指定创建文件的设备

返回值
        该方法没有返回值
'''

# 创建文件，无后缀
os.mknod('/tmp/dir/abcd', 0x600|stat.S_IFCHR)

# 创建文件
os.mknod('/tmp/dir/zz.txt', 0x600|stat.S_IFCHR)

 
```
## os_open 
[`os_open`](./15_examples_os_file/os_open.py)

```python 

import os


'''
概述
    os.open() 方法用于打开一个文件，并且设置需要的打开选项，模式参数mode参数是可选的，默认为 0777。

语法
    open()方法语法格式如下：
    os.open(file, flags[, mode]);

参数
    file -- 要打开的文件
    flags -- 该参数可以是以下选项，多个使用 "|" 隔开：
    os.O_RDONLY: 以只读的方式打开
    os.O_WRONLY: 以只写的方式打开
    os.O_RDWR : 以读写的方式打开
    os.O_NONBLOCK: 打开时不阻塞
    os.O_APPEND: 以追加的方式打开
    os.O_CREAT: 创建并打开一个新文件
    os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
    os.O_EXCL: 如果指定的文件存在，返回错误
    os.O_SHLOCK: 自动获取共享锁
    os.O_EXLOCK: 自动获取独立锁
    os.O_DIRECT: 消除或减少缓存效果
    os.O_FSYNC : 同步写入
    os.O_NOFOLLOW: 不追踪软链接
    mode -- 类似 chmod()。

返回值
        返回新打开文件的描述符。
'''

# 打开文件
fd = os.open('/tmp/foo.txt', os.O_NONBLOCK|os.O_APPEND)

print('打开文件：%s' % fd)

os.write(fd, '写入新数据')

 
```
## os_openpty 
[`os_openpty`](./15_examples_os_file/os_openpty.py)

```python 

import os


'''
概述
    os.openpty() 方法用于打开一个新的伪终端对。返回 pty 和 tty的文件描述符。

语法
    openpty()方法语法格式如下：
    os.openpty()

参数
        无

返回值
        返回文件描述符对，主从。
'''

# 打开终端
pty, tty = os.openpty()

print('pty: %s' % pty)
print('tty: %s' % tty)

print('ttyname: %s' % os.ttyname(pty)) 
```
## os_pipe 
[`os_pipe`](./15_examples_os_file/os_pipe.py)

```python 

'''
概述
    os.pipe() 方法用于创建一个管道, 返回一对文件描述符(r, w) 分别为读和写。

语法
    pipe()方法语法格式如下：
    os.pipe()

参数
    无

返回值
    返回文件描述符对。
'''

import os, sys

print ("The child will write text to a pipe and ")
print ("the parent will read the text written by child...")

# 文件描述符 r, w 用于读、写
r, w = os.pipe() 

# 获取线程id
processid = os.fork()
print('进程类型：%s' % processid)

if processid:
    # 父进程
    # 关闭文件描述符 w
    os.close(w)
    r = os.fdopen(r)
    print ("Parent reading")
    str = r.read()
    print ("text =", str)
    sys.exit(0)
else:
    # 子进程
    os.close(r)
    w = os.fdopen(w, 'w')
 
```
## os_popen 
[`os_popen`](./15_examples_os_file/os_popen.py)

```python 

import os


'''
概述
   os.popen() 方法用于从一个命令打开一个管道。
        在Unix，Windows中有效

语法
    popen()方法语法格式如下：
    os.popen(command[, mode[, bufsize]])

参数
    command -- 使用的命令。
    mode -- 模式权限可以是 'r'(默认) 或 'w'。
    bufsize -- 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。

返回值
        返回一个文件描述符号为fd的打开的文件对象
'''

# 执行命令行操作文件系统
fd = os.popen('mkdir /tmp/ppf2', 'r', 1)

print('fd：%s' % fd)

fd = os.popen('ping localhost', 'r', 1)

print('fd：%s' % fd) 
```
## os_read 
[`os_read`](./15_examples_os_file/os_read.py)

```python 

import os

'''
概述
    os.read() 方法用于从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。
            在Unix，Windows中有效

语法
    read()方法语法格式如下：
    os.read(fd,n)

参数
    fd -- 文件描述符。
    n -- 读取的字节。

返回值
        返回包含读取字节的字符串
'''



# 打开文件
fd = os.open('/tmp/foo.txt', os.O_RDWR|os.O_CREAT)

# 读取内容
print('read: %s' % os.read(fd, 100))

os.close(fd) 
```
## os_remove 
[`os_remove`](./15_examples_os_file/os_remove.py)

```python 

import os


'''
概述
    os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。
            在Unix, Windows中有效

语法
    remove()方法语法格式如下：
    os.remove(path)

参数
    path -- 要移除的文件路径

返回值
        该方法没有返回值
'''

# 删除文件，不能删除文件夹
os.remove('/tmp/ab')
os.remove('/tmp/ab.txt')

os.remove('/tmp/ab3.txt')
os.remove('/tmp/abe') 
```
## os_rename 
[`os_rename`](./15_examples_os_file/os_rename.py)

```python 

import os


'''
概述
    os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

语法
    rename()方法语法格式如下：
    os.rename(src, dst)

参数
    src -- 要修改的目录名
    dst -- 修改后的目录名

返回值
        该方法没有返回值
'''


# os.chroot("/tmp")
os.chdir("/tmp")

# 列出目录
print ("目录为: %s" % os.listdir(os.getcwd()))

os.rename('open2.txt', '123.txt')
os.rename('ppf', '123') 
```
## os_renames 
[`os_renames`](./15_examples_os_file/os_renames.py)

```python 

import os


'''
概述
    os.renames() 方法用于递归重命名目录或文件。类似rename()。

语法
    renames()方法语法格式如下：
    os.renames(old, new)

参数
    old -- 要重命名的目录
    new --文件或目录的新名字。甚至可以是包含在目录中的文件，或者完整的目录树。

返回值
        该方法没有返回值
'''

os.chdir('/tmp')

os.renames('123', '456/abc')

os.renames('123.txt', '456/abc.txt') 
```
## os_stat 
[`os_stat`](./15_examples_os_file/os_stat.py)

```python 

import os


'''
概述
    os.stat() 方法用于在给定的路径上执行一个系统 stat 的调用。

语法
    stat()方法语法格式如下：
    os.stat(path)

参数
    path -- 指定路径

返回值
    stat 结构:
    st_mode: inode 保护模式
    st_ino: inode 节点号。
    st_dev: inode 驻留的设备。
    st_nlink: inode 的链接数。
    st_uid: 所有者的用户ID。
    st_gid: 所有者的组ID。
    st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
    st_atime: 上次访问的时间。
    st_mtime: 最后一次修改的时间。
    st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
'''

st = os.stat('/tmp/foo.txt')

print('stat: %s' % st)

print('st_size: %s' % st.st_size)
print('st_mode: %s' % st.st_mode)
print('st_ctime: %s' % st.st_ctime) 
```
## os_statvfs 
[`os_statvfs`](./15_examples_os_file/os_statvfs.py)

```python 

import os


'''
概述
    os.statvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息。
    
语法
    statvfs()方法语法格式如下：
    os.statvfs([path])
    
参数
    path -- 文件路径。
    
返回值

    返回的结构:
    f_bsize: 文件系统块大小
    f_frsize: 分栈大小
    f_blocks: 文件系统数据块总数
    f_bfree: 可用块数
    f_bavail:非超级用户可获取的块数
    f_files: 文件结点总数
    f_ffree: 可用文件结点数
    f_favail: 非超级用户的可用文件结点数
    f_fsid: 文件系统标识 ID
    f_flag: 挂载标记
    f_namemax: 最大文件长度
'''

# 文件系统的信息
st = os.statvfs('/tmp/foo.txt')

print('st info: %s' % st)

print('f_namemax: %s' % st.f_namemax)
print('f_ffree: %s' % st.f_ffree) 
```
## os_stat_float_times 
[`os_stat_float_times`](./15_examples_os_file/os_stat_float_times.py)

```python 

import os


'''
概述
    os.stat_float_times() 方法用于决定stat_result是否以float对象显示时间戳。

语法
    stat_float_times()方法语法格式如下：
    os.stat_float_times([newvalue])

参数
    newvalue -- 如果为 True, 调用 stat() 返回 floats,如果 False, 调用 stat 返回 ints。如果没有该参数返回当前设置。

返回值
        返回 True 或 False。
'''

st = os.stat('/tmp/foo.txt')
print('stat: %s' % st)

st = os.stat_float_times()
print('stat_float_times: %s' % st)

print('stat: %s' % os.stat('/tmp/foo.txt'))

###########################################################
st = os.stat_float_times()
print('stat_float_times: %s' % st)

print('stat: %s' % os.stat('/tmp/foo.txt')) 
```
## os_symlink 
[`os_symlink`](./15_examples_os_file/os_symlink.py)

```python 

import os


'''
概述
    os.symlink() 方法用于创建一个软链接。
    
语法
    symlink()方法语法格式如下：
    os.symlink(src, dst)
    
参数
    src -- 源地址。
    dst -- 目标地址。
    
返回值
        该方法没有返回值
'''

# 创建软连接
os.symlink('/home/jojo', '/tmp/my_dir')

print('创建软连接完成') 
```
## os_tcgetpgrp 
[`os_tcgetpgrp`](./15_examples_os_file/os_tcgetpgrp.py)

```python 

import os


'''
概述
    os.tcgetpgrp() 方法用于回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组。

语法
    tcgetpgrp()方法语法格式如下：
    os.tcgetpgrp(fd)

参数
    fd -- 文件描述符。

返回值
        该方法返回进程组
'''


fd = os.open("/dev/tty", os.O_RDONLY)

f = os.tcgetpgrp(fd)

print('tcgetpgrp: %s' % f) 
```
## os_tcsetpgrp 
[`os_tcsetpgrp`](./15_examples_os_file/os_tcsetpgrp.py)

```python 

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

 
```
## os_tempnam 
[`os_tempnam`](./15_examples_os_file/os_tempnam.py)

```python 

import os


'''
概述
    os.tempnam() 方法用于返回唯一的路径名用于创建临时文件。

语法
    tempnam()方法语法格式如下：
    os.tempnam(dir, prefix)

参数
    dir -- 要创建的临时文件路径。
    prefix -- 临时文件前缀

返回值
        该方法返回唯一路径。
'''

# 生成某个文件夹下的带指定前缀的唯一路径
tmp = os.tempnam('/tmp/aiay', 'data')
print('tmp: %s' % tmp)

 
```
## os_tmpfile 
[`os_tmpfile`](./15_examples_os_file/os_tmpfile.py)

```python 

import os


'''
概述
    os.tmpfile() 方法用于返回一个打开的模式为(w+b)的临时文件对象，这文件对象没有文件夹入口，没有文件描述符，将会自动删除。

语法
    tmpfile()方法语法格式如下：
    os.tmpfile

参数
    无

返回值
        返回一个临时文件对象
'''


# 创建临时文件
tmp = os.tmpfile()

tmp.write('写入临时数据')

tmp.seek(0)
print('read: %s' % tmp.read())

tmp.close() 
```
## os_tmpnam 
[`os_tmpnam`](./15_examples_os_file/os_tmpnam.py)

```python 

import os


'''
概述
    os.tmpnam() 方法用于为创建一个临时文件返回一个唯一的路径。

语法
    tmpnam()方法语法格式如下：
    os.tmpnam

参数
        无

返回值
        返回一个唯一的路径
'''


# 生成临时路径
tmp = os.tmpnam()

print('临时唯一路径：%s' % tmp) 
```
## os_ttyname 
[`os_ttyname`](./15_examples_os_file/os_ttyname.py)

```python 

import os


'''
概述
    os.ttyname() 方法用于返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

语法
    ttyname()方法语法格式如下：
    os.ttyname(fd)

参数
    fd -- 文件描述符

返回值
        返回一个字符串，它表示与文件描述符fd 关联的终端设备
'''


fd = os.open('/dev/tty', os.O_RDONLY)

print('ttyname: %s' % os.ttyname(fd))

os.close(fd) 
```
## os_walk 
[`os_walk`](./15_examples_os_file/os_walk.py)

```python 

import os


'''
概述
    os.walk() 方法用于通过在目录树种游走输出在目录中的文件名，向上或者向下。
            在Unix，Windows中有效。
    
语法
    walk()方法语法格式如下：
    os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
    
参数
    top -- 根目录下的每一个文件夹(包含它自己), 产生3-元组 (dirpath, dirnames, filenames)【文件夹路径, 文件夹名字, 文件名】。
    topdown --可选，为True或者没有指定, 一个目录的的3-元组将比它的任何子文件夹的3-元组先产生 (目录自上而下)。如果topdown为 False, 一个目录的3-元组将比它的任何子文件夹的3-元组后产生 (目录自下而上)。
    onerror -- 可选，是一个函数; 它调用时有一个参数, 一个OSError实例。报告这错误后，继续walk,或者抛出exception终止walk。
    followlinks -- 设置为 true，则通过软链接访问目录。
    
返回值
        该方法没有返回值
'''


for root, dirs, files in os.walk("/tmp", topdown=False):
    for name in files:
        print('files: %s' % os.path.join(root, name))
    for name in dirs:
        print('dirs: %s' % os.path.join(root, name)) 
```
## os_write 
[`os_write`](./15_examples_os_file/os_write.py)

```python 

import os


'''
概述
    os.write() 方法用于写入字符串到文件描述符 fd 中. 返回实际写入的字符串长度。
            在Unix中有效。

语法
    write()方法语法格式如下：
    os.write(fd, str)

参数
    fd -- 文件描述符。
    str -- 写入的字符串。

返回值
        该方法返回写入的实际位数
'''


# 打开文件
fd = os.open("/tmp/foo.txt", os.O_RDWR|os.O_CREAT)

# 写入字符串
str = "new content"
ret = os.write(fd, str)

# 输入返回值
print ("写入的位数为: ")
print (ret)

print ("写入成功")

# 关闭文件
os.close(fd)
print ("关闭文件成功!!") 
```
# 16_examples_exception 
[**16_examples_exception**](./16_examples_exception)
## clean_exception 
[`clean_exception`](./16_examples_exception/clean_exception.py)

```python 

try:
    raise KeyboardInterrupt
except:
    print('exception!')
finally:
    print('clean！')    
    
    
    
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print('zero error:', e)
    else:
        print('result:', result)
    finally:
        print('divide execute finish!')             
    
    
divide(10, 1)
'''
result: 10.0
divide execute finish!
'''

divide(10, 0)
'''
zero error: division by zero
divide execute finish!
'''

divide('10', '2')
'''
error
'''  


for line in open("myfile.txt"):
    print(line, end="")
 
```
## custom_exception 
[`custom_exception`](./16_examples_exception/custom_exception.py)

```python 

class MyError(Exception):
    def __init__(self, value):
        self.value = value
        
    def __str__(self):
        return repr(self.value)  
    
    
try:
    raise MyError('boom!')
except MyError as e: # 捕获自定义异常
    print('炸裂', e.value)     
```
## exception 
[`exception`](./16_examples_exception/exception.py)

```python 

try:
    x = int(input('请输入一个数字：'))
except: # 捕获任意异常
    print('你输入的是一个非数字字符')
        

try:
    int('a')
except ValueError: # 捕获指导异常
    print('类型错误')


try:
    int('a')
except ValueError as e: # 转换异常数据
    print('类型错误: ', e)
    
try:
    #int('a')
    int(a)
except (RuntimeError, TypeError, NameError, ValueError) as e: # 捕获多个异常
    print('发生多个异常: ', e)  
    
    
import sys

# 多次捕获异常
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise # 未知异常，再次抛出         


 
```
## my_exception 
[`my_exception`](./16_examples_exception/my_exception.py)

```python 

class Error(Exception):
    '''base excption module'''
    pass

class InputError(Error):
    '''
    input error extends Error exception module

    Attribute:
        exception 异常信息
        message 自定义信息
    '''
    
    def __init__(self, exception, message):
        self.exception = exception
        self.message = message
        
        
class OutputError(Error):
    '''
    output exception extends Error exception module
    
    Attribute:
        prev 前一个输出内容 
        next 下一个输出内容
        message 消息内容
    '''        
    
    def __init__(self, prev, next, message):
        self.prev = prev
        self.next = next
        self.message = message
        

try:
    raise InputError('input error code', 'raise input exception!')
except InputError as e:
    print('捕获到异常：', e.exception, '，消息：', e.message)   
    

 
```
## raise_exception 
[`raise_exception`](./16_examples_exception/raise_exception.py)

```python 

# 抛出异常
#raise NameError('无效名称')

# 捕获抛出的异常
try:
    raise NameError('无效名称')
except NameError as e:
    print('捕获到异常：', e)
    raise 
```
# 17_examples_object 
[**17_examples_object**](./17_examples_object)
## class 
[`class`](./17_examples_object/class.py)

```python 

'''
面向对象技术简介

    类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
    类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
    数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
    方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
    实例变量：定义在方法中的变量，只作用于当前实例的类。
    继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
    实例化：创建一个类的实例，类的具体对象。
    方法：类中定义的函数。
    对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法
'''

# 创建一个‘Student’ Class类
class Student:
    ''' student class '''
    name = 'jack'
    age = 22
    
    def getInfo(self):
        return 'student class '
    


# 实例化类
stu = Student()
    
# 访问属性
print('student.name: %s' % stu.name)    
print('student.age: %s' % stu.age)   

# 访问方法
print('student info: %s' % stu.getInfo()) 
 
```
## extend 
[`extend`](./17_examples_object/extend.py)

```python 

class Person:
    ''' 定义基本属性 '''
    name = 'lucy'
    age = 22
    
    ''' 定义私有属性，外部无法访问 '''
    __height = 166
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.__height = height
        
    ''' 定义方法，访问私有属性和基本属性 '''    
    def info(self):
        print('I am name is %s, age %s , height %s' % (self.name, self.age, self.__height)) 
        

# 继承Person 对象
class Student(Person):
    # 新的属性
    grade = ''     
    
    def __init__(self, name, age, height, grade):
        # 为父类属性赋值   
        Person.__init__(self, name, age, height)
        
        # 为当前类属性赋值
        self.grade = grade
        
    # 覆盖父类方法
    def info(self):
        # 子类无法访问父类私有方法
        # print('I am name is %s, age %s , height %s, grade: %s' % (self.name, self.age, self.__height, self.grade))    
        print('I am name is %s, age %s, grade: %s' % (self.name, self.age, self.grade))    
        
    # 自定义的其他方法        
    def getMyGrade(self):
        print('my grade: %s' % self.grade)    
        
 
```
## init 
[`init`](./17_examples_object/init.py)

```python 

class Student:
    name = 'jack'
    age = 22
    
    ''' 初始化方法，构造方法 ，在实例化创建'''
    def __init__(self):
        self.name = 'jason'
        self.age = 33
        

# 创建实例化，init方法被执行        
stu = Student()
        
print('name: %s, age: %s' % (stu.name, stu.age))    




class Class:
    name = 'calss 1'
    
    # 有参构造函数
    def __init__(self, no, author):
        self.Num = no
        self.Author = author

cla = Class('453122645', 'tom')

print('name: %s' % cla.name)
print('Num: %s, Author: %s' % (cla.Num, cla.Author))     
```
## method 
[`method`](./17_examples_object/method.py)

```python 

class Person:
    ''' 定义基本属性 '''
    name = 'lucy'
    age = 22
    
    ''' 定义私有属性，外部无法访问 '''
    __height = 166
    
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.__height = height
        
    ''' 定义方法，访问私有属性和基本属性 '''    
    def info(self):
        print('I am name is %s, age %s , height %s' % (self.name, self.age, self.__height))    


person = Person('zhangsan', 33, 187)

person.info()

# 私有属性不能访问
# print(person.__height)

         
```
## overload 
[`overload`](./17_examples_object/overload.py)

```python 

'''
类的专有方法：
    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 称方
'''

class Conputer:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # 重载系统方法    
    def __str__(self):
        return 'Conputer(%s, %s)' % (self.a, self.b)
    
    # 重载系统方法    
    def __add__(self, c):
        return Conputer(self.a + c.a, self.b + c.b)
    

c1 = Conputer(1, 3)
print(c1)
c2 = Conputer(-3, 9)
print(c2)

print(c1 + c2)

 
```
## overwrite 
[`overwrite`](./17_examples_object/overwrite.py)

```python 

class Phone:  
    
    def getMessage(self):
        print('My Phone Message')
        

# 继承 Phone
class Mobile(Phone):
    
    # 覆盖重写Phone的方法
    def getMessage(self):
        print('My Mobile Message')


mobile = Mobile()
mobile.getMessage()             
```
## private 
[`private`](./17_examples_object/private.py)

```python 

class Private:
    
    __name = '私有属性'
    
    def __print(self):
        print('私有方法')
        
    def println(self):
        print(self.__name)
        
pri = Private()

# 私有属性无法访问
# print(pri.__name)

# 私有方法无法访问
# pri.__print()

# 公有方法访问私有属性
pri.println()
         
```
# 18_examples_standand_lib 
[**18_examples_standand_lib**](./18_examples_standand_lib)
## doctest_lib 
[`doctest_lib`](./18_examples_standand_lib/doctest_lib.py)

```python 

import doctest
import unittest

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.01
    """
    return sum(values) / len(values)


# 运行测试，通过doc的结果和代码运行结果进行比较
print(doctest.testmod())   # 自动验证嵌入测试

'''
**********************************************************************
File "F:\Example Exercise\Python\example_8_standand_lib\doctest_lib.py", line 9, in __main__.average
Failed example:
    print(average([20, 30, 70]))
Expected:
    40.01 # 错误的结果
Got:
    40.0 # 正确结果
**********************************************************************
1 items had failures:
   1 of   1 in __main__.average
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1) # 1个错误
'''


# TestCase 测试用例
class TestStatisticalFunctions(unittest.TestCase):

    # 测试方法
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
 
```
## glob_lib 
[`glob_lib`](./18_examples_standand_lib/glob_lib.py)

```python 

import glob
import os

# 显示方法帮助文档手册
print(help(glob))

print(glob.escape('c://a**?//*b*/c?/d')) # c://a[*][*][?]//[*]b[*]/c[?]/d


# 搜索当前目录下的*.py后缀的文件
print(glob.glob('*.py', recursive=True)) # ['glob_lib.py', 'os_lib.py', 'shutil_lib.py', 'sys_lib.py']

# 搜索路径包含lib字符的文件
os.chdir('F:\Example Exercise\Python')
print(glob.glob('*lib*', recursive=False)) # ['example_8_standand_lib']

print(glob.iglob('*.py', recursive=True)) # <generator object _iglob at 0x00000000029A3B48> 
```
## os_lib 
[`os_lib`](./18_examples_standand_lib/os_lib.py)

```python 

import os


print('当前位置：%s' % os.getcwd())

# 显示所有属性和方法
print('dir: %s' % dir(os))

# 显示该包的帮助手册
print(help(os))

# 显示某个方法帮助手册
print(help(os.chdir))

print(os.path)
print(os.name)
print(os.curdir)
print(os.pardir)

# 切换目录
os.chdir('c:\\')

# 调用系统命令
os.system('ping www.baidu.com -t')

# 调用系统命令
os.system('mkdir haha')

os.system('del haha') 
```
## random_lib 
[`random_lib`](./18_examples_standand_lib/random_lib.py)

```python 

import random

print(help(random))

# 随机取数组中一个值
print(random.choice(['apple', 'pear', 'banana'])) #banana

# 随机生成一个长度为10的数组
print(random.sample(range(100), 10)) # [84, 6, 62, 12, 79, 82, 86, 55, 27, 41]

# 产生随机float数
print(random.random()) #0.7395803807672576

# 随机生成一个小于6的随机数
print(random.randrange(6)) # 3

# 随机生成一个数组
print(random.choices(['apple', 'pear', 'banana'])) #['banana']

# 随机生成1~10的整数
print(random.randint(1, 10))

print(random.gauss(3, 10)) 
```
## re_lib 
[`re_lib`](./18_examples_standand_lib/re_lib.py)

```python 

import re

# 找到所有匹配的字符
print(re.findall(r'f[a-z]*', 'which foot or hand fell fastest')) # ['foot', 'fell', 'fastest']

# 转换表达式
print(re.escape(r'f[a-z]*')) # f\[a\-z\]\*

# 找到不重复的字符串
print(re.sub(r'([a-z]+) \1', r'\1', 'cat in the the hat')) #cat in the hat

# iter
iter = re.finditer(r'f[a-z]*', 'which foot or hand fell fastest')
for item in iter:
    print((item))
print()    

# 查找首个匹配的字符串
print(re.search(r'f[a-z]*', 'which foot or hand fell fastest'))

# match
print(re.match(r'f[a-z]*', 'which foot or hand fell fastest'))

# 拆分字符串
print(re.split(r'f[a-z]*', 'which foot or hand fell fastest'))

print(re.split(r' ', 'which foot or hand fell fastest'))
# 最大分割2个字符串
print(re.split(r' ', 'which foot or hand fell fastest', 2))

compile = re.compile(r'f[a-z]*', 0)
 
```
## shutil_lib 
[`shutil_lib`](./18_examples_standand_lib/shutil_lib.py)

```python 

import shutil

print(help(shutil))

print(help(shutil.move))

# 统计使用空间
print(shutil.disk_usage('c:\\Intel')) # usage(total=120031539200, used=83122790400, free=36908748800)

# 移动目录
#shutil.move('C:\Intel\Logs', 'C:\Logs')

# 复制文件
shutil.copy('F:\\foo.txt', 'F:\\foo.txt2')
# copyfile

# 复制目录
# shutil.copytree('C:\Logs', 'C:\Logs4')

# 压缩文件
shutil.make_archive('C:\Logs', 'zip', root_dir='C:\Logs')
# shutil.make_archive('C:\Logs', 'xztar') 
```
## sys_lib 
[`sys_lib`](./18_examples_standand_lib/sys_lib.py)

```python 

import sys


print(help(sys))

print(sys.argv) # ['F:\\Example Exercise\\Python\\example_8_standand_lib\\sys_lib.py']
print(sys.flags) # sys.flags(debug=0, inspect=0, interactive=0, optimize=0, dont_write_bytecode=0, no_user_site=0, no_site=0, ignore_environment=0, verbose=0, bytes_warning=0, quiet=0, hash_randomization=1, isolated=0)

print(sys.hash_info) # sys.hash_info(width=64, modulus=2305843009213693951, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)
print(sys.copyright)

print(sys.platform) # win32
print(sys.winver) # 3.6

# 日志输入输出
sys.stdin.read(10)
sys.stdout.write('Warning, log file not found starting a new one\n')
sys.stderr.write('Warning, log file not found starting a new one\n')

# 退出
sys.exit() 
```
## timeit_lib 
[`timeit_lib`](./18_examples_standand_lib/timeit_lib.py)

```python 

import timeit


print(help(timeit))

# 计算耗时
print(timeit.Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(timeit.Timer('a,b = b,a', 'a=1; b=2').timeit())

print(timeit.Timer('lambda x, y: x + y', 'x=10; y=5').timeit())

print(timeit.Timer('for i in range(10): oct(i)', 'gc.enable()').timeit())

print(timeit.timeit('"-".join(map(str, range(100)))', number=10000))

print(timeit.timeit('char in text', setup='text = "sample string"; char = "g"'))

print(timeit.timeit('text.find(char)', setup='text = "sample string"; char = "g"'))


t = timeit.Timer('char in text', setup='text = "sample string"; char = "g"')
print(t.timeit())
print(t.repeat(repeat = 3)) # 重复定时器的次数，每次结果以数组形式返回

s = '''\
for i in range(10):
    print(i)
print('done!')    
'''
# 执行一段代码 number=2 次
print(timeit.timeit(stmt=s, number=2)) 
```
## urllib_lib 
[`urllib_lib`](./18_examples_standand_lib/urllib_lib.py)

```python 

import urllib
import urllib.request
import urllib.parse


# 打开url，读取内容
for line in urllib.request.urlopen('http://www.baidu.com'):
    line = line.decode('utf-8') # 编码
    if '网页' in line or '清明节' in line:
        print(line)
        
# 读取300个字符        
with urllib.request.urlopen('http://www.baidu.com') as f:
    print(f.read(300))    # 不转码读取
    print(f.read(300).decode('utf-8')) #转码    
    
    
f = urllib.request.urlopen('http://www.python.org/')
print(f.read(100).decode('utf-8')) 

# 请求状态
print('status: %s' % f.status)
print('status str: %s' % f.reason)

# 带参数的请求
'''
req = urllib.request.Request(url='http://www.baidu.com/s?wd=', data=b'python')
with urllib.request.urlopen(req) as f:
    print(f.read(1000).decode('utf-8'))   
    

# 设置密码的请求方式
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='http://web-api.poco.cn/v1_1/member/login',
                          user='klem',
                          passwd='kadidd!ehopper')

opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
 
```
## zlib_lib 
[`zlib_lib`](./18_examples_standand_lib/zlib_lib.py)

```python 

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
```
# 19_examples_json 
[**19_examples_json**](./19_examples_json)
## json_sample 
[`json_sample`](./19_examples_json/json_sample.py)

```python 

import json


'''
JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式。它基于ECMAScript的一个子集。

Python3 中可以使用 json 模块来对 JSON 数据进行编解码，它包含了两个函数：
    json.dumps(): 对数据进行编码。
    json.loads(): 对数据进行解码
    
------------------------------------------------------------------------------

Python 编码为 JSON 类型转换对应表：

Python                                            JSON
dict                                             object
list, tuple                                      array
str                                              string
int, float, int- & float-derived Enums            number
True                                              true
False                                             false
None                                              null

--------------------------------------------------------------------------------
JSON 解码为 Python 类型转换对应表：
JSON                        Python
object                        dict
array                         list
string                        str
number (int)                  int
number (real)                float
true                         True
false                        False
null                         None
'''


# Python 字典类型转换为 JSON 对象
data = {
    'no' : 1,
 
```
## json_translate 
[`json_translate`](./19_examples_json/json_translate.py)

```python 

import json



#===============================================================================
# 示例：gitmojis.json 和 git-emoji-list.rst 进行读取和转换
#===============================================================================
# 描述：将gitmojis.json文件中的 emoji、description 属性，
#        替换成 git-emoji-list.rst 文件中的中文描述。
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# 读取git-emoji-list.rst文件内容
#-------------------------------------------------------------------------------
data = None
with open('gitmojis.json', 'r', encoding=u'utf-8') as f:
    data = json.load(f)
    
print("json 原始数据：", data) 




#-------------------------------------------------------------------------------
# 读取gitmojis.json文件内容
#-------------------------------------------------------------------------------
chineses = {}
with open('git-emoji-list.rst', 'r', encoding=u'utf-8') as f:
    text = f.readline()
    text = f.readline()

    while len(text) > 0:
        text = f.readline()
        
        items = text.split("|")
        if len(items) > 3:
            names = items[1].strip().split("(")
 
```
# 20_examples_regex 
[**20_examples_regex**](./20_examples_regex)
## regex 
[`regex`](./20_examples_regex/regex.py)

```python 

import re

'''
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

函数语法：
    re.match(pattern, string, flags=0)
    
函数参数说明：
            参数                    描述
    pattern    匹配的正则表达式
    string     要匹配的字符串。
    flags      标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
    
-----------------------------------------------------------------------------------------------    

        匹配对象方法                            描述
    group(num=0)        匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    groups()            返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。    
    
-----------------------------------------------------------------------------------------------    
        修饰符            描述
    re.I    使匹配对大小写不敏感
    re.L    做本地化识别（locale-aware）匹配
    re.M    多行匹配，影响 ^ 和 $
    re.S    使 . 匹配包括换行在内的所有字符
    re.U    根据Unicode字符集解析字符。这个标志影响 \w, \W, , \B.
    re.X    该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。    
    
-----------------------------------------------------------------------------------------------    
    
        模式            描述
    ^    匹配字符串的开头
    $    匹配字符串的末尾。
    .    匹配任意字符，除了换行符，当re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符。
    [...]    用来表示一组字符,单独列出：[amk] 匹配 'a'，'m'或'k'
    [^...]    不在[]中的字符：[^abc] 匹配除了a,b,c之外的字符。
    re*    匹配0个或多个的表达式。
    re+    匹配1个或多个的表达式。
    re?    匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式
 
```
# 21_examples_socket 
[**21_examples_socket**](./21_examples_socket)
## client 
[`client`](./21_examples_socket/client.py)

```python 

# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 和指定地址、端口的服务器建立链接
s.connect((HOST, PORT))

# 向服务器发送信息
s.send(b'Hello, world')

# 接受服务器消息
data = s.recv(1024)
s.close()

print('Received', repr(data)) 
```
## client2 
[`client2`](./21_examples_socket/client2.py)

```python 

# Echo client program
import socket
import sys

HOST = 'localhost'    # The remote host
PORT = 50007              # The same port as used by the server
s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM):
    print('res', res)
    
    af, socktype, proto, canonname, sa = res
    
    print('AddressFamily:', af)
    print('sockType:', socktype)
    print('proto:', proto)
    print('canonname', canonname)
    print('host/port:', sa)
    
    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    
    try:
        s.connect(sa)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)
    
s.send(b'Hello, world')
data = s.recv(1024)
s.close()

 
```
## server 
[`server`](./21_examples_socket/server.py)

```python 

# Echo server program
import socket

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

# 建立socket对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
s.bind((HOST, PORT))
# 最大建立一个监听
s.listen(1)

# 客户端链接
conn, addr = s.accept()
print('Connected by', addr)

while True:
    #客户端 发送的信息
    data = conn.recv(1024)
    if not data: break
    
    print('客户端消息：', repr(data))
    # 向客户端发送信息
    conn.send(data)
conn.close() 
```
## server2 
[`server2`](./21_examples_socket/server2.py)

```python 

# Echo server program
import socket
import sys

HOST = 'localhost'               # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port

s = None
for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    print('res', res)
    af, socktype, proto, canonname, sa = res
    # <AddressFamily.AF_INET6: 23>, <SocketKind.SOCK_STREAM: 1>, 0, '', ('::1', 50007, 0, 0)
    
    print('AddressFamily:', af)
    print('sockType:', socktype)
    print('proto:', proto)
    print('canonname', canonname)
    print('host/port:', sa)

    try:
        s = socket.socket(af, socktype, proto)
    except socket.error as msg:
        s = None
        continue
    
    try:
        s.bind(sa)
        s.listen(1)
    except socket.error as msg:
        s.close()
        s = None
        continue
    break

if s is None:
    print('could not open socket')
    sys.exit(1)
    
conn, addr = s.accept()
print('Connected by', addr)
 
```
## sk 
[`sk`](./21_examples_socket/sk.py)

```python 

import socket

print('hostname: ', socket.gethostname())

# the public network interface
HOST = socket.gethostbyname(socket.gethostname())
print('HOST: ', HOST)

# create a raw socket and bind it to the public interface
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
s.bind((HOST, 0))
print(s)

# Include IP headers
s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

# receive all packages
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

# receive a package
print(s.recvfrom(65565))

# disabled promiscuous mode
s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF) 
```
## socket_client 
[`socket_client`](./21_examples_socket/socket_client.py)

```python 

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = 'localhost'
port = 8080

client.connect((host, port))

print('开始接受消息')

while True:
    
    message = client.recv(1024)
    if message:
        print(message.decode('utf-8'))

client.close()

print('关闭链接') 
```
## socket_server 
[`socket_server`](./21_examples_socket/socket_server.py)

```python 

import socket
from threading import Timer

'''
socket()函数

Python 中，我们用 socket（）函数来创建套接字，语法格式如下：
    socket.socket([family[, type[, proto]]])
    
参数
    family: 套接字家族可以使AF_UNIX或者AF_INET
    type: 套接字类型可以根据是面向连接的还是非连接分为SOCK_STREAM或SOCK_DGRAM
    protocol: 一般不填默认为0.

Socket 对象(内建)方法

                函数                                        描述
    服务器端套接字
    s.bind()        绑定地址（host,port）到套接字， 在AF_INET下,以元组（host,port）的形式表示地址。
    s.listen()      开始TCP监听。backlog指定在拒绝连接之前，操作系统可以挂起的最大连接数量。该值至少为1，大部分应用程序设为5就可以了。
    s.accept()      被动接受TCP客户端连接,(阻塞式)等待连接的到来
    
    客户端套接字
    s.connect()     主动初始化TCP服务器连接，。一般address的格式为元组（hostname,port），如果连接出错，返回socket.error错误。
    s.connect_ex()  connect()函数的扩展版本,出错时返回出错码,而不是抛出异常
    
    公共用途的套接字函数
    s.recv()         接收TCP数据，数据以字符串形式返回，bufsize指定要接收的最大数据量。flag提供有关消息的其他信息，通常可以忽略。
    s.send()         发送TCP数据，将string中的数据发送到连接的套接字。返回值是要发送的字节数量，该数量可能小于string的字节大小。
    s.sendall()      完整发送TCP数据，完整发送TCP数据。将string中的数据发送到连接的套接字，但在返回之前会尝试发送所有数据。成功返回None，失败则抛出异常。
    s.recvform()     接收UDP数据，与recv()类似，但返回值是（data,address）。其中data是包含接收数据的字符串，address是发送数据的套接字地址。
    s.sendto()       发送UDP数据，将数据发送到套接字，address是形式为（ipaddr，port）的元组，指定远程地址。返回值是发送的字节数。
    s.close()        关闭套接字
    s.getpeername()    返回连接套接字的远程地址。返回值通常是元组（ipaddr,port）。
    s.getsockname()    返回套接字自己的地址。通常是一个元组(ipaddr,port)
    s.setsockopt(level, optname, value)    设置给定套接字选项的值。
    s.getsockopt(level, optname[.buflen])    返回套接字选项的值。
    
    s.settimeout(timeout)     设置套接字操作的超时期，timeout是一个浮点数，单位是秒。值为None表示没有超时期。一般，超时期应该在刚创建套接字时设置，因为它们可能用于连接的操作（如connect()）
    s.gettimeout()            返回当前超时期的值，单位是秒，如果没有设置超时期，则返回None。
 
```
# 22_examples_email 
[**22_examples_email**](./22_examples_email)
## mail_stmp 
[`mail_stmp`](./22_examples_email/mail_stmp.py)

```python 

'''
Python创建 SMTP 对象语法如下：
    import smtplib
    smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

参数说明：
    host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如:w3cschool.cn，这个是可选参数。
    port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下SMTP端口号为25。
    local_hostname: 如果SMTP在你的本机上，你只需要指定服务器地址为 localhost 即可。

Python SMTP对象使用sendmail方法发送邮件，语法如下：
    SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options]

参数说明：
    from_addr: 邮件发送者地址。
    to_addrs: 字符串列表，邮件接收地址。
    msg: 发送消息

这里要注意一下第三个参数，msg是字符串，表示邮件。
我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。
这个格式就是smtp协议中定义的格式。
'''

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'from@qq.com'
receivers = ['hoojo@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("W3Cschool教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')

subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')


try:
 
```
## send_mail 
[`send_mail`](./22_examples_email/send_mail.py)

```python 

from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.utils import parseaddr, formataddr

'''
使用第三方服务器发送邮件
'''

# 第三方SMTP服务
host = 'stmp@126.com'
user = 'hoojo_@126.com'
passwd = 'xxx'

# 发送人
sender = 'from@qq.com'
# 接收人
recveres = [ 'hoojo@qq.com' ]

charset = 'utf-8'

message = MIMEText('python 发送邮件测试', 'plain', charset)
message['From'] = formataddr(['Python From', 'aaa'])
message['To'] = formataddr(['Python To', 'bbb'])
#message['From'] = Header('Python send', charset)
#message['To'] = Header('revc python', charset)
message['Subject'] = Header('这是一份测试邮件', charset)

try:
    server = smtplib.SMTP_SSL()
    server.set_debuglevel(1)
    
    # 连接到stmp服务器
    server.connect(host, 25) # 25 为stmp 端口号
    # 登录到smtp服务器
    server.login(user, passwd)
    
    # 发送邮件
    server.sendmail(user, recveres, message.as_string())
    
 
```
## send_mail2 
[`send_mail2`](./22_examples_email/send_mail2.py)

```python 

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

host = "smtp.qq.com"
user = 'hoojo@qq.com'
passwd = 'xxx'  # 发件人邮箱密码(当时申请smtp给的口令)

sender = user  # 发件人邮箱账号
recv = 'hoojo@qq.com'  # 收件人邮箱账号，我这边发送给自己

def mail():
    ret = True
    
    try:
        message = MIMEText('填写邮件内容', 'plain', 'utf-8')
        message['From'] = formataddr(["发件人昵称", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人昵称", recv])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = Header("邮件主题-测试", 'utf-8')  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP(host, 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.set_debuglevel(1)
        server.login(user, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [recv, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print('Error: %s' % e)
        ret = False
    return ret

ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
 
```
## send_mail_html 
[`send_mail_html`](./22_examples_email/send_mail_html.py)

```python 

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header

host = "smtp.qq.com"
user = 'hoojo@qq.com'
passwd = 'xxx'  # 发件人邮箱密码(当时申请smtp给的口令)

sender = user  # 发件人邮箱账号
recv = 'hoojo@qq.com'  # 收件人邮箱账号，我这边发送给自己

content = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.hoojo.cn">这是一个链接</a></p>
"""

def mail():
    ret = True
    
    try:
        message = MIMEText(content, 'html', 'utf-8')
        message['From'] = formataddr(["发件人昵称", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人昵称", recv])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = Header("邮件主题-测试", 'utf-8')  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP(host, 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.set_debuglevel(1)
        server.login(user, passwd)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, [recv, ], message.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print('Error: %s' % e)
        ret = False
    return ret

ret = mail()
if ret:
    print("邮件发送成功")
 
```
## send_mail_image 
[`send_mail_image`](./22_examples_email/send_mail_image.py)

```python 

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

host = "smtp.qq.com"
user = 'hoojo@qq.com'
passwd = 'xxx'  # 发件人邮箱密码(当时申请smtp给的口令)

sender = user  # 发件人邮箱账号
recv = 'hoojo@qq.com'  # 收件人邮箱账号，我这边发送给自己

content = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.hoojo.cn">这是一个链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""

def mail():
    ret = True
    
    try:
        #创建一个带附件的实例
        message = MIMEMultipart('related')
        message['From'] = formataddr(["发件人昵称", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人昵称", recv])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = Header("邮件主题-测试", 'utf-8')  # 邮件的主题，也可以说是标题
        
        text = MIMEMultipart('alternative')
        # 邮件正文内容
        text.attach(MIMEText(content, 'html', 'utf-8'))
        # 添加正文
        message.attach(text)
        
        # 指定图片为当前目录
        fp = open('test.png', 'rb')
        image = MIMEImage(fp.read())
 
```
## send_mail_part 
[`send_mail_part`](./22_examples_email/send_mail_part.py)

```python 

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from email.header import Header
from email.mime.multipart import MIMEMultipart

host = "smtp.qq.com"
user = 'hoojo@qq.com'
passwd = 'xxx'  # 发件人邮箱密码(当时申请smtp给的口令)

sender = user  # 发件人邮箱账号
recv = 'hoojo@qq.com'  # 收件人邮箱账号，我这边发送给自己

content = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.hoojo.cn">这是一个链接</a></p>
"""

def mail():
    ret = True
    
    try:
        #创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = formataddr(["发件人昵称", sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        message['To'] = formataddr(["收件人昵称", recv])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        message['Subject'] = Header("邮件主题-测试", 'utf-8')  # 邮件的主题，也可以说是标题
        
        # 邮件正文内容
        message.attach(MIMEText(content, 'html', 'utf-8'))
        
        # 构造附件1，传送当前目录下的 mail_stmp.py 文件
        att1 = MIMEText(open('mail_stmp.py', 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        # 添加附件
        message.attach(att1)
        
        # 构造附件2，传送当前目录下的mail_stmp.py 文件
 
```
# 23_examples_thread 
[**23_examples_thread**](./23_examples_thread)
## thread_function 
[`thread_function`](./23_examples_thread/thread_function.py)

```python 

import _thread
import time

'''
函数式：
            调用 _thread 模块中的start_new_thread()函数来产生新线程。
            
语法如下:
    _thread.start_new_thread ( function, args[, kwargs] )

参数说明:
    function - 线程函数。
    args - 传递给线程函数的参数,他必须是个tuple类型。
    kwargs - 可选参数。
'''

# 为线程定义一个函数
def print_time(threadName, delay):
   count = 0
   while count < 5:
      time.sleep(delay)
      count += 1
      print ("%s: %s" % (threadName, time.ctime(time.time())))

# 创建两个线程
try:
   _thread.start_new_thread(print_time, ("Thread-1", 2,))
   _thread.start_new_thread(print_time, ("Thread-2", 4,))
except:
   print ("Error: 无法启动线程")

while 1:
   pass
 
```
## thread_module 
[`thread_module`](./23_examples_thread/thread_module.py)

```python 

import threading
import time


'''
threading 模块除了包含 _thread 模块中的所有方法外，还提供的其他方法：
    threading.currentThread(): 返回当前的线程变量。
    threading.enumerate(): 返回一个包含正在运行的线程的list。正在运行指线程启动后、结束前，不包括启动前和终止后的线程。
    threading.activeCount(): 返回正在运行的线程数量，与len(threading.enumerate())有相同的结果。
    
除了使用方法外，线程模块同样提供了Thread类来处理线程，Thread类提供了以下方法:
    run(): 用以表示线程活动的方法。
    start():启动线程活动。
    join([time]): 等待至线程中止。这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生。
    isAlive(): 返回线程是否活动的。
    getName(): 返回线程名。
    setName(): 设置线程名。
'''

exit_flag = False

class MyThread(threading.Thread):
    
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        self.name = name
        self.count = count
        
    def run(self):
        threading.Thread.run(self)    
        
        print('线程开始：%s', self.name)
        print_time(self, self.name, 1, self.count)
        print('线程退出：%s', self.name)
        
    def exit(self):
        print('exit')
        # threading.Thread.exit() 
 
```
## thread_queue 
[`thread_queue`](./23_examples_thread/thread_queue.py)

```python 

import queue
import threading
import time

'''
Python 的 Queue 模块中提供了同步的、线程安全的队列类，
包括FIFO（先入先出)队列Queue，LIFO（后入先出）队列LifoQueue，和优先级队列 PriorityQueue。

这些队列都实现了锁原语，能够在多线程中直接使用，可以使用队列来实现线程间的同步。

Queue 模块中的常用方法:
    Queue.qsize() 返回队列的大小
    Queue.empty() 如果队列为空，返回True,反之False
    Queue.full() 如果队列满了，返回True,反之False
    Queue.full 与 maxsize 大小对应
    Queue.get([block[, timeout]])获取队列，timeout等待时间
    Queue.get_nowait() 相当Queue.get(False)
    Queue.put(item) 写入队列，timeout等待时间
    Queue.put_nowait(item) 相当Queue.put(item, False)
    Queue.task_done() 在完成一项工作之后，Queue.task_done()函数向任务已经完成的队列发送一个信号
    Queue.join() 实际上意味着等到队列为空，再执行别的操作
'''

exit_flag = False

class MyThread(threading.Thread):
    
    def __init__(self, threadId, name, queue):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        self.name = name
        self.queue = queue
        
        print('---创建线程：%s-%s---' % (threadId, name))
        
    def run(self):
        threading.Thread.run(self)    
        
        print('线程开始：%s' % self.name)
 
```
## thread_schedul 
[`thread_schedul`](./23_examples_thread/thread_schedul.py)

```python 

import threading
from threading import Timer

data = threading.local()
data.x = 109

def hello():
    print("hello, world")


# 定时3秒后运行
t = Timer(3.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed 
```
## thread_sync 
[`thread_sync`](./23_examples_thread/thread_sync.py)

```python 

import threading
import time

'''
如果多个线程共同对某个数据修改，则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。
使用 Thread 对象的 Lock 和 Rlock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法，
对于那些需要每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。

如下：
多线程的优势在于可以同时运行多个任务（至少感觉起来是这样）。但是当线程需要共享数据时，可能存在数据不同步的问题。
考虑这样一种情况：一个列表里所有元素都是0，线程"set"从后向前把所有元素改成1，而线程"print"负责从前往后读取列表并打印。
那么，可能线程"set"开始改的时候，线程"print"便来打印列表了，输出就成了一半0一半1，这就是数据的不同步。为了避免这种情况，引入了锁的概念。
锁有两种状态——锁定和未锁定。每当一个线程比如"set"要访问共享数据时，必须先获得锁定；
如果已经有别的线程比如"print"获得锁定了，那么就让线程"set"暂停，也就是同步阻塞；
等到线程"print"访问完毕，释放锁以后，再让线程"set"继续。
经过这样的处理，打印列表时要么全部输出0，要么全部输出1，不会再出现一半0一半1的尴尬场面。
'''

class MyThread(threading.Thread):
    
    def __init__(self, threadId, name, count):
        threading.Thread.__init__(self)
        
        self.threadId = threadId
        self.name = name
        self.count = count
        
    def run(self):
        threading.Thread.run(self)    
        
        # 获取锁，用于线程同步
        threadLock.acquire()
        
        print('线程开始：%s', self.name)
        print_time(self, self.name, 1, self.count)
        print('线程退出：%s', self.name)
        
        # 释放锁，开启下一个线程
        threadLock.release()
        
 
```
# 24_examples_db 
[**24_examples_db**](./24_examples_db)
## db_call_proc 
[`db_call_proc`](./24_examples_db/db_call_proc.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
# 游标设置为字典类型
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

try:
    cursor.callproc('p2', args=(1, 22, 3, 4))
    
    #获取执行完存储的参数,参数@开头
    cursor.execute("select @p1, @_p1_1, @_p1_2, @_p1_3")  #{u'@_p1_1': 22, u'@p1': None, u'@_p1_2': 103, u'@_p1_3': 24}
    
    # 获取第一条记录
    row = cursor.fetchone()
    print('row: ', row)

    db.commit()
except OSError as e:
    print('error: %s' % e)
        
# 关闭数据库连接
db.close() 
```
## db_call_proc_params 
[`db_call_proc_params`](./24_examples_db/db_call_proc_params.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
# 游标设置为字典类型
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

try:
    #无参数存储过程
    cursor.callproc('p1')  #等价于cursor.execute("call p1()")
    
    # 获取第一条记录
    row = cursor.fetchone()
    print('row: ', row)

    db.commit()
except OSError as e:
    print('error: %s' % e)
        
# 关闭数据库连接
db.close() 
```
## db_connect 
[`db_connect`](./24_examples_db/db_connect.py)

```python 

import pymysql

'''
错误处理

    DB API中定义了一些数据库操作的错误及异常，下表列出了这些错误和异常:
    
            异常                                                                                描述
    Warning                  当有严重警告时触发，例如插入数据是被截断等等。必须是 StandardError 的子类。
    Error                    警告以外所有其他错误类。必须是 StandardError 的子类。
    InterfaceError           当有数据库接口模块本身的错误（而不是数据库的错误）发生时触发。 必须是Error的子类。
    DatabaseError            和数据库有关的错误发生时触发。 必须是Error的子类。
    DataError                当有数据处理时的错误发生时触发，例如：除零错误，数据超范围等等。 必须是DatabaseError的子类。
    OperationalError         指非用户控制的，而是操作数据库时发生的错误。例如：连接意外断开、 数据库名未找到、事务处理失败、内存分配错误等等操作数据库是发生的错误。 必须是DatabaseError的子类。
    IntegrityError           完整性相关的错误，例如外键检查失败等。必须是DatabaseError子类。
    InternalError            数据库的内部错误，例如游标（cursor）失效了、事务同步失败等等。 必须是DatabaseError子类。
    ProgrammingError         程序错误，例如数据表（table）没找到或已存在、SQL语句语法错误、 参数数量错误等等。必须是DatabaseError的子类。
    NotSupportedError        不支持错误，指使用了数据库不支持的函数或API等。例如在连接对象上 使用.rollback()函数，然而数据库并不支持事务或者事务已关闭。 必须是DatabaseError的子类。
'''
 
```
## db_create_table 
[`db_create_table`](./24_examples_db/db_create_table.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
create_table_sql = """
    CREATE TABLE EMPLOYEE (
     FIRST_NAME  CHAR(20) NOT NULL primary key,
     LAST_NAME  CHAR(20),
     AGE INT,  
     SEX CHAR(1),
     INCOME FLOAT )
"""

# 执行创建表语句
print(cursor.execute(create_table_sql))


# 关闭数据库连接
db.close() 
```
## db_delete 
[`db_delete`](./24_examples_db/db_delete.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
delete from EMPLOYEE where FIRST_NAME = 'bili2'
'''

try:
    # 执行删除语句
    row = cursor.execute(sql)
    print('row: %s' % row)
    
    # 提交操作
    db.commit()
    print('提交')
except:
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close() 
```
## db_inject 
[`db_inject`](./24_examples_db/db_inject.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
            values(%s, %s, %s, %s, %s)
'''

try:
    # 执行插入语句, 防止注入
    cursor.execute(sql, ('jack3', 'jack chen', 33, 'M', 3000))
    
    # 提交操作
    db.commit()
    print('提交')
except:
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close() 
```
## db_insert 
[`db_insert`](./24_examples_db/db_insert.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
            values('jack', 'jack chen', 33, 'M', 3000)
'''

try:
    # 执行插入语句
    cursor.execute(sql)
    
    # 提交操作
    db.commit()
    print('提交')
except:
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close() 
```
## db_insert_format 
[`db_insert_format`](./24_examples_db/db_insert_format.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) values('%s', '%s', '%d', '%s', '%d')" % ('alex', 'alex chen', 21, 'M', 567777)

print(sql)
try:
    # 执行插入语句
    cursor.execute(sql)
    
    # 提交操作
    db.commit()
    print('提交')
except OSError as e:
    print('error: %s' % e)
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close() 
```
## db_insert_many 
[`db_insert_many`](./24_examples_db/db_insert_many.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
            values(%s, %s, %s, %s, %s)
'''

try:
    # 执行插入语句
    row = cursor.executemany(sql, [('tom2', 'tom Li', 31, 'W', 21000), ('bili2', 'alex dk', 31, 'W', 21000)])
    print('row: ', row)
    
    # 提交操作
    db.commit()
    print('提交')
except OSError as e:
    print('error: %s' % e)
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close() 
```
## db_query_all 
[`db_query_all`](./24_examples_db/db_query_all.py)

```python 

'''
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
select FIRST_NAME, LAST_NAME, AGE, SEX, INCOME from EMPLOYEE
'''

try:
    # 执行查询语句
    cursor.execute(sql)
    
    # 获取查询记录
    result = cursor.fetchall()
    
    for row in result:
        print('row: FIRST_NAME->%s, LAST_NAME->%s, AGE->%s, SEX->%s, INCOME->%s' % row)
except OSError as e:
    print('error: %s' % e)
        
# 关闭数据库连接
db.close() 
```
## db_query_cursors 
[`db_query_cursors`](./24_examples_db/db_query_cursors.py)

```python 

'''
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
# 游标设置为字典类型
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

sql = '''
select FIRST_NAME, LAST_NAME, AGE, SEX, INCOME from EMPLOYEE
'''

try:
    # 执行查询语句
    cursor.execute(sql)
    
    # 获取第一条记录
    row = cursor.fetchone()
    print('row: ', row)

    # 下一条记录
    row = cursor.fetchone()
    print('row: ', row)
    
    # 下2条记录
    rows = cursor.fetchmany(2)
    print('rows: ', rows)
    
    # 其他记录
    result = cursor.fetchall()
    
    for row in result:
 
```
## db_query_fetch 
[`db_query_fetch`](./24_examples_db/db_query_fetch.py)

```python 

'''
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
select FIRST_NAME, LAST_NAME, AGE, SEX, INCOME from EMPLOYEE
'''

try:
    # 执行查询语句
    cursor.execute(sql)
    
    # 获取第一条记录
    row = cursor.fetchone()
    print('row: ', row)

    # 下一条记录
    row = cursor.fetchone()
    print('row: ', row)
    
    # 下2条记录
    rows = cursor.fetchmany(2)
    print('rows: ', rows)
    
    # 其他记录
    result = cursor.fetchall()
    
    for row in result:
        print('row: FIRST_NAME->%s, LAST_NAME->%s, AGE->%s, SEX->%s, INCOME->%s' % row)
 
```
## db_query_one 
[`db_query_one`](./24_examples_db/db_query_one.py)

```python 

'''
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
select FIRST_NAME, LAST_NAME, AGE, SEX, INCOME from EMPLOYEE limit 1
'''

try:
    # 执行查询语句
    cursor.execute(sql)
    
    # 获取查询记录
    result = cursor.fetchone()
    
    print('result: FIRST_NAME->%s, LAST_NAME->%s, AGE->%s, SEX->%s, INCOME->%s' % result)
except OSError as e:
    print('error: %s' % e)
        
# 关闭数据库连接
db.close() 
```
## db_template 
[`db_template`](./24_examples_db/db_template.py)

```python 

import pymysql

import contextlib

#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql_template(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8'):
  
    # 打开数据库连接  
    db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    # 游标设置为字典类型
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    
    try:
        yield cursor
    
        db.commit()
    except OSError as e:
        print('error: %s' % e)
        
    finally:
        cursor.close()
        # 关闭数据库连接
        db.close()
        

# 使用模板查询        
with mysql_template() as cursor:
    print(cursor)
    
    row_count = cursor.execute("select * from EMPLOYEE")
    row = cursor.fetchone()
    
    print(row_count)
    print(row)   
```
## db_transtion 
[`db_transtion`](./24_examples_db/db_transtion.py)

```python 

import pymysql
  
'''
执行事务

事务机制可以确保数据一致性。
    事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
            原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
            一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
            隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
            持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
'''  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
            values('jack', 'jack chen', 33, 'M', 3000)
'''

try:
    # 执行插入语句
    cursor.execute(sql)
    
    # 提交操作
    db.commit()
    print('提交')
except:
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close() 
```
## db_update 
[`db_update`](./24_examples_db/db_update.py)

```python 

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
update EMPLOYEE set SEX = 'M', INCOME = 10000
'''

try:
    # 执行更新语句
    row = cursor.execute(sql)
    print('row: %s' % row)
    
    # 提交操作
    db.commit()
    print('提交')
except:
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close() 
```
# 25_examples_shell 
[**25_examples_shell**](./25_examples_shell)
## shell_cmd 
[`shell_cmd`](./25_examples_shell/shell_cmd.py)

```python 

import subprocess

# help(subprocess)

print(subprocess.call('ls'))

'''
call(*popenargs, timeout=None, **kwargs)
        Run command with arguments.  Wait for command to complete or
        timeout, then return the returncode attribute.
        
        The arguments are the same as for the Popen constructor.  Example:
        
        retcode = call(["ls", "-l"])
    
    check_call(*popenargs, **kwargs)
        Run command with arguments.  Wait for command to complete.  If
        the exit code was zero then return, otherwise raise
        CalledProcessError.  The CalledProcessError object will have the
        return code in the returncode attribute.
        
        The arguments are the same as for the call function.  Example:
        
        check_call(["ls", "-l"])
    
    check_output(*popenargs, timeout=None, **kwargs)
        Run command with arguments and return its output.
        
        If the exit code was non-zero it raises a CalledProcessError.  The
        CalledProcessError object will have the return code in the returncode
        attribute and output in the output attribute.
        
        The arguments are the same as for the Popen constructor.  Example:
        
        >>> check_output(["ls", "-l", "/dev/null"])
        b'crw-rw-rw- 1 root root 1, 3 Oct 18  2007 /dev/null\n'
        
        The stdout argument is not allowed as it is used internally.
        To capture standard error in the result, use stderr=STDOUT.
        
 
```
# 50_samples_varables 
[**50_samples_varables**](./50_samples_varables)
## var_assignment_process 
[`var_assignment_process`](./50_samples_varables/var_assignment_process.py)

```python 

from _collections_abc import ItemsView

#===============================================================================
# 示例：可迭代对象赋值给多个变量
#===============================================================================


#-------------------------------------------------------------------------------
# 统计平均分，去掉最高低分
#-------------------------------------------------------------------------------
def drop_first_last(grades):
    first, *middle, last = grades
    # 只计算middle，去掉first和last
    return avg(middle)

def avg(args):
    total = 0
    for val in args:
        total += val
    
    return total / len(args)

print('平均分：', drop_first_last([100, 2, 5, 9, 33, 1]))


#-------------------------------------------------------------------------------
# 去掉部分数据
#-------------------------------------------------------------------------------
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
# 获取 name、email
name, email, *phones = record
print('name: ', name) # Dave
print('email: ', email) # dave@example.com

# phones 列表类型的，无论phones数据包含几个元素
print('phones: ', phones) # ['773-555-1212', '847-555-1212']



#-------------------------------------------------------------------------------
 
```
## var_multi_assignment 
[`var_multi_assignment`](./50_samples_varables/var_multi_assignment.py)

```python 

#===============================================================================
# 示例：多变量赋值
#===============================================================================
# 描述：唯一的前提就是变量的数量必须跟序列元素的数量是一样的
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
### tuple
#-------------------------------------------------------------------------------
data = ('a', 2, ('b', 10.2))

a, b, c = data
print('a: ', a) # a
print('b: ', b) # 2
print('c: ', c) # ('b', 10.2)
print()


#-------------------------------------------------------------------------------
###list
#-------------------------------------------------------------------------------
data = [ 'a', 2, ('c', 2.2) ]

a, b, c = data
print('a: ', a) # a
print('b: ', b) # 2
print('c: ', c) # ('b', 10.2)
print()


#-------------------------------------------------------------------------------
###进一步赋值
#-------------------------------------------------------------------------------
a, b, (c, d) = data
print('a: ', a) # a
print('b: ', b) # 2
print('c: ', c) # c
print('d: ', d) # 2.2
print()
 
```
# app_generator_copyright 
[**app_generator_copyright**](./app_generator_copyright)
## generator-copyright 
[`generator-copyright`](./app_generator_copyright/generator-copyright.py)

```python 

#===============================================================================
# Generator Copyright Information
#===============================================================================
# 描述：生成 copyright 信息，插入到文件中
#-------------------------------------------------------------------------------

import time
import os

#-------------------------------------------------------------------------------
# global env
#-------------------------------------------------------------------------------
'''
targetFolder="F:\\Example Exercise\\Python"
fiilter="py"

COPYRIGHT_INFORMATION = ''#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
%s
# @copyright by hoojo@2018
# @changelog %s
'''

targetFolder="F:\\Example Exercise\\Bash"
fiilter="sh"

COPYRIGHT_INFORMATION = '''#!/bin/bash
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
%s
# @copyright by hoojo@2018
# @changelog %s
'''


#-------------------------------------------------------------------------------
 
```
# app_generator_toc 
[**app_generator_toc**](./app_generator_toc)
## generator-toc 
[`generator-toc`](./app_generator_toc/generator-toc.py)

```python 
import re


#===============================================================================
#     Generator Project makedown —— TOC  table of Contents
#===============================================================================
# 描述：生成项目工程的 makedown 格式的 目录索引 TOC 的文档
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# 生成 目录索引 TOC 的文档 工具类
#-------------------------------------------------------------------------------
class GeneratorTOCUtils:
    
    __rootDirectory = ".";
    __makedownFile = ""
    
    __tableOfContents = []
    
    def __init__(self, rootDirectory, makedownFile):
        self.__rootDirectory = rootDirectory
        self.__makedownFile = makedownFile
        
        print("目标工程位置：%s，生成文件保存位置：%s" % (rootDirectory, makedownFile))
    
    #-------------------------------------------------------------------------------
    # generator makedown toc file
    #-------------------------------------------------------------------------------    
    def genMakedownTOC(self, suffix):
        self.__scan(self.__rootDirectory, suffix)
        self.__save()
    
    
    #-------------------------------------------------------------------------------
    # generator makedown readME file
    #-------------------------------------------------------------------------------    
    def genMakedownReadMe(self, suffix):
        self.__scan(self.__rootDirectory, suffix, isReadMe=True)
        self.__save()
    
 
```
#  
[****](./)
