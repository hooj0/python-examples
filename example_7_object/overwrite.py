#!/usr/bin/env python
# encoding: utf-8
# @author: hoojo


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