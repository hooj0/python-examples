#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
print("ABC".encode("UTF-8")) # b'ABC'

# decode 对字符串进行解码，decode解码前的字符串加b'......'.decode()
# b 表示byte字符串
print(b'ABC'.decode('UTF-8')) # ABC
print(b'\xe4\xb8\xad\xe5\x9b\xbd'.decode('UTF-8')) # 中国
print(u"中国".encode("utf-8").decode('UTF-8')) # 中国

# len 字符串长度
print(len('abc')) # 3
print(len(u'中国')) # 2
print(len('中国')) # 2
print(len(b'\xe4\xb8\xad\xe5\x9b\xbd')) # 6
print(len('\xe4\xb8\xad\xe5\x9b\xbd')) # 6

# 字符串重复出现： str * int
print('ab * 3:', 'ab' * 3) # ababab
# 字符串拼接，字符串不能和非字符串拼接
print('ab + ce:', 'ab' + 'ce') # abce

# 取字符串中特定字符
str = 'hello world!'
print(str[0], str[3], str[-1]) # h l !
#str[0] = 'L' # 不能进行赋值，字符串是不可变对象 TypeError: 'str' object does not support item assignment


# 字符串分片切块: str[头下标:尾下标] 不包含尾下标元素
'''
 +---+---+---+---+---+
 | H | e | l | l | o |
 +---+---+---+---+---+
 0   1   2   3   4   5
-5  -4  -3  -2  -1
'''
print('str[1: 3] ->', str[1: 3]) # el
print('str[1: 9] ->', str[1: 9]) # ello wor
print('str[1: -1] ->', str[1: -1]) # ello world

print('str[100:] ->', str[100:]) # ""
print('str[:100] ->', str[:100]) # hello world!
print('str[100:1] ->', str[100:1]) # ""

# 默认的分切索引很有用：默认的第一个索引为零，第二个索引默认为字符串可以被分切的长度
# 不输入结束的尾下标就表示直接截取到最后的元素
print('str[3:] ->', str[3:]) # lo world!
# 不输出起始位置，默认是0
print('str[:3] ->', str[:3]) # hel
# 全部字符串
print('str[:] ->', str[:]) # hello world!
# 规律
print('str == str[:5] + str[5:] ->', str == str[:5] + str[5:]) # True
print('str == str[:2] + str[2:] ->', str == str[:2] + str[2:]) # True

# in / not in 成员运算
h = 'e'
print('h in str ->', h in str) # True
h = '2'
print('h not in str ->', h not in str) # True
print('ll' in str) # True

# replace
print('replace:', str.replace('!', '??')) # hello world??


input("按任意键退出")
