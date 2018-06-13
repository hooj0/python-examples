#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo


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
        