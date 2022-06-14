#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-18 22:59:56
# @copyright by hoojo@2018
# @changelog Added python3 `object -> Enum` example

class LogLevel(Enum):
    debug = 10
    info = 20
    warn = 30
    error = 40


print(LogLevel.debug)
print(LogLevel.debug.value)
print(LogLevel.debug.name)
print(type(LogLevel.debug))
print(repr(LogLevel.debug))
print(LogLevel(20))
print(list(LogLevel))

LogLevel.debug = 50 # error