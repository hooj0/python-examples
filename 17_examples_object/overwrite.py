#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-02 22:53:00
# @copyright by hoojo@2018
# @changelog Added python3 `object->overwrite` example


class Phone:  
    
    def getMessage(self):
        print('My Phone Message')
        

# 继承 Phone
class Mobile(Phone):
    
    # 覆盖重写Phone的方法
    def getMessage(self):
        print('My Mobile Message')


mobile = Mobile()
mobile.getMessage()            