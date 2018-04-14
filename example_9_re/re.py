#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo
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
    re{ n}    
    re{ n,}    精确匹配n个前面表达式。
    re{ n, m}    匹配 n 到 m 次由前面的正则表达式定义的片段，贪婪方式
    a| b    匹配a或b
    (re)    G匹配括号内的表达式，也表示一个组
    (?imx)    正则表达式包含三种可选标志：i, m, 或 x 。只影响括号中的区域。
    (?-imx)    正则表达式关闭 i, m, 或 x 可选标志。只影响括号中的区域。
    (?: re)    类似 (...), 但是不表示一个组
    (?imx: re)    在括号中使用i, m, 或 x 可选标志
    (?-imx: re)    在括号中不使用i, m, 或 x 可选标志
    (?#...)    注释.
    (?= re)    前向肯定界定符。如果所含正则表达式，以 ... 表示，在当前位置成功匹配时成功，否则失败。但一旦所含表达式已经尝试，匹配引擎根本没有提高；模式的剩余部分还要尝试界定符的右边。
    (?! re)    前向否定界定符。与肯定界定符相反；当所含表达式不能在字符串当前位置匹配时成功
    (?> re)    匹配的独立模式，省去回溯。
    \w    匹配字母数字
    \W    匹配非字母数字
    \s    匹配任意空白字符，等价于 [\t\n\r\f].
    \S    匹配任意非空字符
    \d    匹配任意数字，等价于 [0-9].
    \D    匹配任意非数字
    \A    匹配字符串开始
    \Z    匹配字符串结束，如果是存在换行，只匹配到换行前的结束字符串。c
    \z    匹配字符串结束
    \G    匹配最后匹配完成的位置。
        匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的 'er'。
    \B    匹配非单词边界。'er\B' 能匹配 "verb" 中的 'er'，但不能匹配 "never" 中的 'er'。
    \n, \t, 等.    匹配一个换行符。匹配一个制表符。等
    \1...\9    匹配第n个分组的子表达式。
    \10    匹配第n个分组的子表达式，如果它经匹配。否则指的是八进制字符码的表达式。    


-----------------------------------------------------------------------------------------------     
字符匹配

            实例                    描述
    python    匹配 "python".
----------------------------------------------------------------------------------------------- 

字符类

                实例                            描述
    [Pp]ython      匹配 "Python" 或 "python"
    rub[ye]        匹配 "ruby" 或 "rube"
    [aeiou]        匹配中括号内的任意一个字母
    [0-9]          匹配任何数字。类似于 [0123456789]
    [a-z]          匹配任何小写字母
    [A-Z]          匹配任何大写字母
    [a-zA-Z0-9]    匹配任何字母及数字
    [^aeiou]       除了aeiou字母以外的所有字符
    [^0-9]         匹配除了数字外的字符

----------------------------------------------------------------------------------------------- 

特殊字符类

            实例                        描述
    .         匹配除 "\n" 之外的任何单个字符。要匹配包括 '\n' 在内的任何字符，请使用象 '[.\n]' 的模式。
    \d        匹配一个数字字符。等价于 [0-9]。
    \D        匹配一个非数字字符。等价于 [^0-9]。
    \s        匹配任何空白字符，包括空格、制表符、换页符等等。等价于 [ \f\n\r\t\v]。
    \S        匹配任何非空白字符。等价于 [^ \f\n\r\t\v]。
    \w        匹配包括下划线的任何单词字符。等价于'[A-Za-z0-9_]'。
    \W        匹配任何非单词字符。等价于 '[^A-Za-z0-9_]'。    
'''

#print(help(re))

print('匹配到数据：', (re.match('www', 'www.cnblogs.cn').span()))  # 在起始位置匹配
print('匹配到数据：', re.match('com', 'www.cnblogs.cn'))           # 不在起始位置匹配


line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)


if matchObj:
   print ("matchObj.group(): %s" % matchObj.group())    # Cats are smarter than dogs
   print ("matchObj.group(1): %s" % matchObj.group(1))  # Cats
   print ("matchObj.group(2): %s" % matchObj.group(2))  # smarter
else:
   print ("No match!!")


# match 没有匹配到
matchObj = re.match( r'dogs', line, re.M|re.I) # 没有匹配到
if matchObj:
   print ("match --> matchObj.group(): %s" % matchObj.group())
else:
   print ("No match!!")


# search 能搜索到dogs
matchObj = re.search( r'dogs', line, re.M|re.I) # 成功匹配
if matchObj:
   print ("search --> matchObj.group(): %s" % matchObj.group()) # dogs
else:
   print ("No match!!")
   
   

phone = "2004-959-559 # 这是一个电话号码"
# 删除注释
num = re.sub(r'#.*$', "", phone)
print ("电话号码 : %s" % num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print ("电话号码 : %s" % num)   

# 剃除字母
print(re.sub(r'\w', "", '我们china 人'))