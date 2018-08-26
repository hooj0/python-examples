#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-21 20:59:23
# @copyright by hoojo@2018
# @changelog Added python3 `string->str escape` example


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
# r"..." 表示字符串原样输出，忽略特殊字符
print(r"\r\n\t")
print(R"this is content \r\n\t")

# 多行输出 '''......''' 中间可以进行换行
print('''line
line2
line3''')

print(
'''
    1line
2line
 3line
''')

# \ 进行续行, 当一行不够显示，要换行而又不进行拼接
str = 'hello world,\
new world'
print('续行字符串：', str)

# 加号拼接
str = 'a' + 'b'
print('拼接字符串：', str)

# 相邻字符在同一行也可以拼接
str = 'a' 'b'
print('拼接字符串：', str)

# u'......' 表示Unicode编码字符串
print(u"中国") # 中国
print(U"中国") # 中国


print('\a')
print('\e')
print('00')