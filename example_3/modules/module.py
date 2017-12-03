#!/usr/bin/env python
# encoding: utf-8
# Created on 2017-11-14
# @author: hoojo

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
print('module name：', __name__)

print('using_name:', using_name)

# 查看一个模块里的方法和全局变量
print('dir using_name:', dir(using_name))
print('dir module_center:', dir(module_center))

a = [1, 2, 3]
# 列举当前模块的方法、变量、以及导入的模块和变量
print('current module dir:', dir())

a = 1
print('current module dir:', dir())

del a
print('current module dir:', dir()) # 发现a被删除不在dir中

print(sys.api_version)
print(sys.base_prefix)