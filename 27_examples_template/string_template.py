#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-10
# @copyright by hoojo @2018
# @changelog string Built-in template


# ===============================================================================
# 标题：string Built-in template
# ===============================================================================
# 使用：string.Template('$who is $role')
# -------------------------------------------------------------------------------
# 描述：python 内置模板，通过string包导入使用，可以重复使用替换变量返回字符串
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 模板的定义与使用
# -------------------------------------------------------------------------------
import string

template = string.Template('$who is $role')

result = template.substitute(who='jack', role='Linux')
print(result)

result = template.substitute(who='tom', role='cat')
print(result)
