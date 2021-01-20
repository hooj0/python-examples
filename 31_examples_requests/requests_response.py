#!/usr/bin/env python3
# encoding: utf-8
# @author:   hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create:   2021/1/21 0021
# @copyright by hoojo @2018
# @changelog python `request -> response` example


# ===============================================================================
# 标题：python HTTP requests lib send request response content example
# ===============================================================================
# 使用：https://requests.readthedocs.io/zh_CN/latest/
#    安装：pip install requests
#    快速上手：https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
# -------------------------------------------------------------------------------
# 描述：利用 request 完成 http 请求，获取返回响应的结果
# -------------------------------------------------------------------------------
import requests


# ===============================================================================
# 示例：利用 requests 完成 GET 请求，获取返回响应的结果
# ===============================================================================
payload = {"wd": "aop", "timed": "12234234234"}
response = requests.get("https://www.baidu.com/s", params=payload, timeout=100) # 设置秒数超时，仅对于连接有效

# 查看r.ok的布尔值便可以知道是否登陆成功
print("response ok:", response.ok)
# 响应状态码，如果不是200，可以使用 r.raise_for_status() 抛出异常
print("response status_code:", response.status_code)
# 当前请求的完整链接，包含参数
print("response url:", response.url)
# 返回响应的已解析标头链接（如果有）
print("response links:", response.links)
# 获取当前的编码
print("response encoding:", response.encoding)
# 设置编码
response.encoding = "utf-8"

# 以 encoding 解析返回内容。字符串方式的响应体，会自动根据响应头部的字符编码进行解码
print("response text:", response.text)
# 以字节形式（二进制）返回。字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
print("response content:", len(response.content))
# 以字典对象存储服务器响应头，但是这个字典比较特殊，字典键不区分大小写，若键不存在则返回None
print("response headers:", response.headers)
# 返回原始响应体，也就是 urllib 的 response 对象，使用 r.raw.read()
print("response raw:", response.raw)

# 返回cookie
print("response cookie:", response.cookies)
# 返回重定向信息,当然可以在请求是加上allow_redirects = false 阻止重定向
print("response history:", response.history)
# 返回发送到服务器的头信息
print("response request:", response.request)


# -------------------------------------------------------------------------------
# 特殊方法
# -------------------------------------------------------------------------------
# 失败请求(非200响应)抛出异常
print("response raise_for_status:", response.raise_for_status())
# Requests中内置的JSON解码器，以json形式返回,前提返回的内容确保是json格式的，不然解析出错会抛异常
# print("response json:", response.json())
