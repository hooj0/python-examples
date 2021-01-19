#!/usr/bin/env python3
# encoding: utf-8
# @author:   hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create:   2021/1/21 0021
# @copyright by hoojo @2018
# @changelog python `request -> send` example


# ===============================================================================
# 标题：python HTTP requests lib send request example
# ===============================================================================
# 使用：https://requests.readthedocs.io/zh_CN/latest/
#    安装：pip install requests
#    快速上手：https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
# -------------------------------------------------------------------------------
# 描述：利用 request 完成 http 请求
# -------------------------------------------------------------------------------
import requests


# ===============================================================================
# 示例：利用 requests 完成 GET 请求
# ===============================================================================
response = requests.get("http://www.baidu.com")

print("response ok:", response.ok)
print("response links:", response.links)
print("response content:", len(response.content))
print("response text:", len(response.text))
print("response apparent_encoding:", response.apparent_encoding)
print("response next:", response.next)
print("\n\n")


# output:
# -------------------------------------------------------------------------------
# response ok: True
# response links: {}
# response content: 2381
# response text: 2381
# response apparent_encoding: utf-8
# response next: None


# ===============================================================================
# 示例：利用 requests 完成 POST 请求
# ===============================================================================
response = requests.post("https://www.baidu.com/s", data={"wd": "aop"})

print("response ok:", response.ok)
print("response links:", response.links)
print("response content:", len(response.content))
print("response text:", len(response.text))
print("response apparent_encoding:", response.apparent_encoding)
print("response next:", response.next)


# output:
# -------------------------------------------------------------------------------
# response ok: True
# response links: {}
# response content: 15469
# response text: 15469
# response apparent_encoding: utf-8
# response next: None



# ===============================================================================
# 示例：利用 requests 完成 PUT/DELETE/HEAD/OPTIONS 请求
# ===============================================================================
r = requests.put("http://httpbin.org/put", data={"key": "value"})
r = requests.delete("http://httpbin.org/delete")
r = requests.head("http://httpbin.org/get")
r = requests.options("http://httpbin.org/get")