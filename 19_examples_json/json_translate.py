#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-06-30 19:48:03
# @copyright by hoojo@2018
# @changelog Added python3 `json->json translate` example


import json



#===============================================================================
# 示例：gitmojis.json 和 git-emoji-list.rst 进行读取和转换
#===============================================================================
# 描述：将gitmojis.json文件中的 emoji、description 属性，
#        替换成 git-emoji-list.rst 文件中的中文描述。
#-------------------------------------------------------------------------------




#-------------------------------------------------------------------------------
# 读取git-emoji-list.rst文件内容
#-------------------------------------------------------------------------------
data = None
with open('gitmojis.json', 'r', encoding=u'utf-8') as f:
    data = json.load(f)
    
print("json 原始数据：", data) 




#-------------------------------------------------------------------------------
# 读取gitmojis.json文件内容
#-------------------------------------------------------------------------------
chineses = {}
with open('git-emoji-list.rst', 'r', encoding=u'utf-8') as f:
    text = f.readline()
    text = f.readline()

    while len(text) > 0:
        text = f.readline()
        
        items = text.split("|")
        if len(items) > 3:
            names = items[1].strip().split("(")
            chineses[names[0].strip()] = { "emoji": names[1].strip().replace(")", ""), "description": items[3].strip() }
    
    
    
    
    
#-------------------------------------------------------------------------------
# 数据替换
#-------------------------------------------------------------------------------
size = 0
for item in data:
    record = chineses[item["code"]]
    if size < len(record["emoji"]):
        size = len(record["emoji"]) 
        
    item["emoji"] = record["emoji"].ljust(10)
    item["code"] = item["code"].ljust(30)
    item["description"] = record["description"]

#print(size)    
#print(data)    
print(json.dumps(data))    
