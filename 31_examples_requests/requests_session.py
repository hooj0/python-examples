#!/usr/bin/env python3
# encoding: utf-8
# @author:   hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create:   2021/1/21 0021
# @copyright by hoojo @2018
# @changelog python `request -> session` example


# ===============================================================================
# 标题：python HTTP requests lib send request session example
# ===============================================================================
# 使用：https://requests.readthedocs.io/zh_CN/latest/
#    安装：pip install requests
#    快速上手：https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
# -------------------------------------------------------------------------------
# 描述：会话对象，能够跨请求保持某些参数
# -------------------------------------------------------------------------------
import requests
import json


# ===============================================================================
# 示例：利用 session 完成 保持参数不丢失
# ===============================================================================
session = requests.Session()
session.auth = ('auth', 'passwd')
session.headers = {'key': 'value'}

payload = {"wd": "aop", "timed": "12234234234"}
response = session.get("https://dict.baidu.com/s", params=payload)

print("response ok:", response.ok)
print("response url:", response.url)
print("response links:", response.links)
print("response text:", len(response.text))
print("response headers:", response.headers)
print("\n\n")


payload = {"wd": "bbc", "timed": "14345556667"}
response = session.get("https://dict.baidu.com/s", params=payload)

print("response ok:", response.ok)
print("response url:", response.url)
print("response links:", response.links)
print("response text:", len(response.text))
print("response headers:", response.headers)
