#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-03 21:05:08
# @copyright by hoojo@2018
# @changelog Added python3 `object -> @staticmethod` example
# 
class RuntimeEnv:

    BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self):
        self.__BASE_PATH1 = os.path.dirname(os.path.abspath(__file__))
        self.BASE_PATH2 = os.path.abspath(__file__)

    # 需要 new 创建对象调用
    def path(self):
        print(f"项目根目录路径为：{self.BASE_PATH}")
        print(f"当前执行脚本的目录路径为：{self.__BASE_PATH1}")
        print(f"当前执行脚本的路径为：{self.BASE_PATH2}")

    # get 属性，直接当做属性方法 RuntimeEnv.basepath
    @property
    def basepath(self):
        return self.BASE_PATH

    # set 属性，可以赋值
    @basepath.setter
    def basepath(self, path):
        self.BASE_PATH = path

    # 静态方法，直接调用，也能 new 实例访问
    @staticmethod
    def dir():
        return "abcde"

    # 直接访问，不能new 创建实例访问
    def name():
        print("name method")



print(RuntimeEnv.BASE_PATH)
RuntimeEnv.BASE_PATH = "abc"
RuntimeEnv().path()

print(RuntimeEnv().basepath)
env = RuntimeEnv()
env.basepath = "def"
print(env.basepath)
print(RuntimeEnv.dir())
print(RuntimeEnv().dir())
RuntimeEnv.name()