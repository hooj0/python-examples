#!/usr/bin/env python3
# encoding: utf-8
# @author:   hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create:   2021/1/21 0021
# @copyright by hoojo @2018
# @changelog python `request -> param` example


# ===============================================================================
# 标题：python HTTP requests lib send request param example
# ===============================================================================
# 使用：https://requests.readthedocs.io/zh_CN/latest/
#    安装：pip install requests
#    快速上手：https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
# -------------------------------------------------------------------------------
# 描述：利用 request 完成 http 请求，带参数
# -------------------------------------------------------------------------------
import requests
import json


# ===============================================================================
# 示例：利用 requests 完成 GET 请求，添加参数
# ===============================================================================
payload = {"wd": "aop", "timed": "12234234234"}
response = requests.get("https://www.baidu.com/s", params=payload)

print("response ok:", response.ok)
print("response url:", response.url)
print("response links:", response.links)
print("response text:", response.text)


# ===============================================================================
# 示例：利用 requests 完成 POST 请求，添加参数
# ===============================================================================
response = requests.post("https://api.github.com/some/endpoint", data=json.dumps({"some": "data"}))
print("json: ", response.json())

headers = {'User-Agent' : 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}

response = requests.post("https://api.github.com/some/endpoint", json={"some": "data"}, headers=headers)
print("json: ", response.json())