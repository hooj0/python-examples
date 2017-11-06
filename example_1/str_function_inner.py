#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-04 17:32:25
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
string.startswith(obj, beg=0,end=len(string))         检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
string.strip([obj])                                   在 string 上执行 lstrip()和 rstrip()
string.swapcase()                                     翻转 string 中的大小写
string.title()                                        返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
string.translate(str, del="")                         根据 str 给出的表(包含 256 个字符)转换 string 的字符,要过滤掉的字符放到 del 参数中
string.upper()                                        转换 string 中的小写字母为大写
string.zfill(width)                                   返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
string.isdecimal()                                    isdecimal()方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。
'''


#string.capitalize() 把字符串的第一个字符大写
print('capitalize:', 'python'.capitalize()) # Python
print('capitalize:', 'Jython'.capitalize())   # Jython

#string.center(width) 
#返回一个原字符串居中,并使用空格填充至长度 width 的新字符串
print('center: #%s#' % 'python'.center(10)) # #  python  #
print('center: #%s#' % 'i like python'.center(10)) # #i like python#

#string.count(str, beg=0, end=len(string))  
#返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
print('count:', 'python is good'.count('o')) # 3
print('count:', 'python is good'.count('o', 10, 20)) # 2

#string.encode(encoding='UTF-8', errors='strict')      
#以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'
print('encode:', '哈喽'.encode(encoding='utf_8', errors='strict'))    # b'\xe5\x93\x88\xe5\x96\xbd'

#string.decode(encoding='UTF-8', errors='strict')      
#以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除 非 errors 指 定 的 是 'ignore' 或 者'replace'
print('decode:', b'\xe5\x93\x88\xe5\x96\xbd'.decode('utf-8')) # 哈喽

#string.endswith(obj, beg=0, end=len(string))          
#检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.
print('endswith:', 'python'.endswith('on')) # True
print('endswith:', 'python'.endswith('aon'))    # False
print('endswith:', 'python'.endswith('on', 10))    # False

#string.expandtabs(tabsize=8)                          
#把字符串 string 中的 tab 符号转为空格，默认的空格数 tabsize 是 8.
print('expandtabs:', 'i    like    python'.expandtabs(tabsize=4))

#string.find(str, beg=0, end=len(string))              
#检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
print('find:', 'python'.find('o'))  # 4
print('find:', 'python'.find('o', 1, 3))    # -1

#string.index(str, beg=0, end=len(string))             
#跟find()方法一样，只不过如果str不在 string中会报一个异常.
print('index:', 'python'.index('o'))    # 4
#print('index:', 'python'.index('o', 1, 3))  # ValueError: substring not found

#string.isalnum()                                      
#如果 string 所有字符都是字母或数字则返回 True,否则返回 False
print('isalnum:', 'abc'.isalnum())  # True
print('isalnum:', 'abc2dds'.isalnum())  # True
print('isalnum:', '23!dds'.isalnum())   # False

#string.isalpha()                                      
#如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False
print('isalpha:', 'abc'.isalpha())  # True
print('isalpha:', '123'.isalpha())  # False

#string.isdecimal()                                    
#如果 string 只包含十进制数字则返回 True 否则返回 False.
print('isdecimal:', '123'.isdecimal()) # True
print('isdecimal:', '123a'.isdecimal())# False

#string.isdigit()                                      
#如果 string 只包含数字则返回 True 否则返回 False.
print('isdigit:', '123'.isdigit()) # True
print('isdigit:', '123a'.isdigit())# False

#string.islower()                                      
#如果 string 都是小写，则返回 True，否则返回 False
print('islower:', '123'.islower())  # False
print('islower:', 'abc'.islower())  # True
print('islower:', 'ABC'.islower())  # False
print('islower:', 'ABCabc123'.islower())  # False

#string.isnumeric()                                    
#如果 string 中只包含数字字符，则返回 True，否则返回 False
print('isnumeric:', '123'.isnumeric())  # True
print('isnumeric:', '123abc'.isnumeric())  # False

#string.isspace()                                      
#如果 string 中只包含空格，则返回 True，否则返回 False.
print('isspace:', '123 abc'.isspace())  # False
print('isspace:', '    '.isspace())  # TAB False
print('isspace:', '  '.isspace())  # True

#string.istitle()                                      
#如果 string 是单词形式，首字母大写，其他小写。则返回 True，否则返回 False
print('istitle:', 'Python'.istitle())  # True
print('istitle:', 'Python Jython'.istitle())  # True
print('istitle:', 'python Jython'.istitle())  # False

#string.isupper()                                      
#如果 string 中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False
print('isupper:', '1 标题A'.isupper())  # True
print('isupper:', 'aA23'.isupper())  # False
print('isupper:', 'abc'.isupper())  # False
print('isupper:', 'ABC'.isupper())  # True

#string.join(seq)                                      
#Merges (concatenates)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
print('join:', ','.join(set('abcdef13'))) # c,e,f,1,a,b,d,3
print('join:', ';'.join(set('abcdef13')))   # c;e;b;f;d;a;1;3

#string.ljust(width)                                   
#返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
print('ljust:%s;' % 'python'.ljust(10)) #python    ;
print('ljust:%s;' % 'python'.ljust(5))  #python;

#string.lower()                                        
#转换 string 中所有大写字符为小写.
print('lower:', 'PYTHON'.lower()) #python

#string.lstrip()                                       
#截掉 string 左边的空格
print('lstrip: <%s>' % '  python is good  '.lstrip()) #<python is good  >

#string.maketrans(intab, outtab])                      
#maketrans() 方法用于创建字符映射的转换表，对于接受两个参数的最简单的调用方式，
#第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。
intab = "aeiou"
outtab = "12345"
str = "this is string example....wow!!!"
trantab = ''.maketrans(intab, outtab)
print('maketrans:', trantab) # {97: 49, 101: 50, 105: 51, 111: 52, 117: 53} tips: ascii 值的转换键值对进行匹配转换
print('translate:', str.translate(trantab)) # th3s 3s str3ng 2x1mpl2....w4w!!!  进行转换

#max(str)                                              
#返回字符串 str 中最大的字母。
print('max:', max('idea'))  #i

#min(str)                                              
#返回字符串 str 中最小的字母。
print('min:', min('idea'))  #a

#string.partition(str)                                 
#有点像 find()和 split()的结合体,从 str 出现的第一个位置起,
#把 字 符 串 string 分 成 一 个 3 元 素 的 元 组 (string_pre_str,str,string_post_str),
#如果 string 中不包含str 则 string_pre_str == string.
print('partition:', "I'an".partition("'"))  # ('I', "'", 'an')
print('partition:', "name=jack".partition("=")) #('name', '=', 'jack')

#string.replace(str1, str2,  num=string.count(str1))   
#把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
print('replace:', 'python'.replace('p', 'j'))   #jython
print('replace:', 'python is good'.replace('o', '()', 1))   #pyth()n is good
print('replace:', 'python is good'.replace('o', '()', 10))   #pyth()n is g()()d

#string.rfind(str, beg=0,end=len(string) )             
#类似于 find()函数，不过是从右边开始查找.
print('rfind:', 'python is good'.rfind('o'))    # 12
print('rfind:', 'python is good'.rfind('o', 1))    # 12
print('rfind:', 'python is good'.rfind('o', 1, 5))    # 4

#string.rindex( str, beg=0,end=len(string))            
#类似于 index()，不过是从右边开始.
print('rindex:', 'python is good'.rindex('o'))    # 12
print('rindex:', 'python is good'.rindex('o', 1))    # 12
print('rindex:', 'python is good'.rindex('o', 1, 5))    # 4

#string.rjust(width)                                   
#返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串
print('rjust:<%s>' % 'python'.rjust(10))  #<    python>

#string.rpartition(str)                                
#类似于 partition()函数,不过是从右边开始查找.
print('rpartition:', "I'an It's".rpartition("'"))  # ("I'an It", "'", 's')
print('rpartition:', "name=jack,age=5".rpartition("=")) #('name=jack,age', '=', '5')

#string.rstrip()                                       
#删除 string 字符串末尾的空格.
print('rstrip:', 'python  '.rstrip())   #python

#string.split(str="", num=string.count(str))           
#以 str 为分隔符切片 string，如果 num有指定值，则仅分隔 num 个子字符串
print('split:', 'python is good'.split())   #['python', 'is', 'good']
print('split:', 'python, is good'.split(','))   #['python', ' is good']
print('split:', 'a,b,c,d,e,f'.split(',', 3))   #['a', 'b', 'c', 'd,e,f']

#string.splitlines(num=string.count('\n'))             
#按照行分隔，返回一个包含各行作为元素的列表，如果 num 指定则仅切片 num 个行.
print('splitlines:', 'aaa\rbbbb\ncccc\n111111'.splitlines())    #['aaa', 'bbbb', 'cccc', '111111']

#string.startswith(obj, beg=0,end=len(string))         
#检查字符串是否是以 obj 开头，是则返回 True，否则返回 False。如果beg 和 end 指定值，则在指定范围内检查.
print('startswith:', 'python'.startswith('py')) # True
print('startswith:', 'python'.startswith('on', 10))    # False

#string.strip([obj])                                   
#在 string 上执行 lstrip()和 rstrip()
print('strip: <%s>' % ' hello py  '.strip()) #<hello py>

#string.swapcase()                                     
#翻转 string 中的大小写
print('swapcase：', 'Python OH'.swapcase()) #pYTHON oh

#string.title()                                        
#返回"标题化"的 string,就是说所有单词都是以大写开始，其余字母均为小写(见 istitle())
print('title:', 'python is good'.title()) #Python Is Good
print('title:', 'Python is Good'.title()) #Python Is Good

#string.upper()                                        转换 string 中的小写字母为大写
print('upper:', 'abCD'.upper()) #ABCD

#string.zfill(width)                                   
#返回长度为 width 的字符串，原字符串 string 右对齐，前面填充0
print('zfill:', 'python'.zfill(10)) #0000python

