#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-28 18:34:02
# @copyright by hoojo@2018
# @changelog Added python3 `if else->if elif else` example


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
运算符				描述	实例
in				如果在指定的序列中找到值返回 True，否则返回 False。	x 在 y 序列中 , 如果 x 在 y 序列中返回 True。
not in			如果在指定的序列中没有找到值返回 True，否则返回 False。	x 不在 y 序列中 , 如果 x 不在 y 序列中返回 True。

## string、list和tuple都属于sequence（序列）
------------------------------------------------
运算符				描述	实例
is				is是判断两个标识符是不是引用自一个对象	x is y, 如果 id(x) 等于 id(y) , is 返回结果 1
is not			is not是判断两个标识符是不是引用自不同对象	x is not y, 如果 id(x) 不等于 id(y). is not 返回结果 1
'''

# 0、None、 []、(,) 一切空对象在if条件语句中都为False
# 相反，则为True
x = 0
if x:
	print('Number 0, Yes')
else:
	print('Number 0, No')

x = None
if x:
	print('None, Yes')
else:
	print('None, No')

x = []
if x:
	print('List, Yes')
else:
	print('List, No')

x = ()
if x:
	print('tuple, Yes')
else:
	print('tuple, No')

print()

# if elif else 语句
age = 20
if age < 18:
	print('未成年')
elif age > 18 and age < 21:
	print('中学生')
else:
	print('社会青年')
	
print()

# 客户端输入参数进行if判断
age = int(input('输入你的年龄：')) # 因为input的输出都是字符串，所以要进行类型转换

if age < 18:
	print('未成年')
elif age > 18 and age < 21:
	print('中学生')
else:
	print('社会青年')
	
print()	

# 逻辑运算符
if True and True:
	print('True and True -> True')	
else:
	print('True and True -> False')	

print()	

if True and False:
	print('True and False -> True')	
else:
	print('True and False -> False')	

print()	

if True or False:
	print('True or False -> True')	
else:
	print('True or False -> False')	

print()

if not (True or False):
	print('not (True or False) -> True')	
else:
	print('not (True or False) -> False')	

print()

# 成员运算
print("2 in [ 2, 3, '4' ] ->", 2 in [ 2, 3, '4' ])
print("4 not in [ 2, 3, '4' ] ->", 4 not in [ 2, 3, '4' ])
print("'a' in 'abcd' ->", 'a' in 'abcd')
print("'a' not in 'abcd' ->", 'a' not in 'abcd')

print()

# 身份运算, id() 指向内存地址
a = 10
b = 10

if a is b:
	print('a is b -> True')
else:
	print('a is b -> False')

if id(a) is id(b):
	print('id(a) is id(b) -> True')
else:
	print('id(a) is id(b) -> False')	
		
print()
		
b = 22
if a is b:
	print('a is b -> True')
else:
	print('a is b -> False')

if id(a) is id(b):
	print('id(a) is id(b) -> True')
else:
	print('id(a) is id(b) -> False')

e = '22'	
print(id('22'), id(a), id(b), id(e))	

# 三元运算
x  = 2
print('x if x > 2 else 3:', x if x > 2 else 3)
print('x if x == 2 else 3:', x if x == 2 else 3)