#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-03 21:05:08
# @copyright by hoojo@2018
# @changelog Added python3 `object->private` example


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
        