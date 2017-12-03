#!/usr/bin/env python
# -*- coding: utf-8 -*-

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


#-----------------------------------------------------
# 由于 init的package文件中没有定义 d.py 所以导入的时候，d.py不被导入
# __all__ = [ "a", "b", "c" ]
from core.files import *

