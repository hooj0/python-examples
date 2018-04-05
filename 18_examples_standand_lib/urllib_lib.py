#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-05 17:53:02
# @copyright by hoojo@2018
# @changelog Added python3 `standand lib -> urllib lib` example


import urllib
import urllib.request
import urllib.parse


# 打开url，读取内容
for line in urllib.request.urlopen('http://www.baidu.com'):
    line = line.decode('utf-8') # 编码
    if '网页' in line or '清明节' in line:
        print(line)
        
# 读取300个字符        
with urllib.request.urlopen('http://www.baidu.com') as f:
    print(f.read(300))    # 不转码读取
    print(f.read(300).decode('utf-8')) #转码    
    
    
f = urllib.request.urlopen('http://www.python.org/')
print(f.read(100).decode('utf-8')) 

# 请求状态
print('status: %s' % f.status)
print('status str: %s' % f.reason)

# 带参数的请求
'''
req = urllib.request.Request(url='http://www.baidu.com/s?wd=', data=b'python')
with urllib.request.urlopen(req) as f:
    print(f.read(1000).decode('utf-8'))   
    

# 设置密码的请求方式
auth_handler = urllib.request.HTTPBasicAuthHandler()
auth_handler.add_password(realm='PDQ Application',
                          uri='http://web-api.poco.cn/v1_1/member/login',
                          user='klem',
                          passwd='kadidd!ehopper')

opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
urllib.request.install_opener(opener)

f = urllib.request.urlopen('http://www.poco.cn/follow/follow_list')
print(f.read(1000).decode('utf-8'))     
'''


# 转换参数进行查询
params = urllib.parse.urlencode({'wd': 'python', 'ie': 'utf-8'})
url = "http://www.baidu.com/s?%s" % params
with urllib.request.urlopen("http://www.baidu.com/s") as f:
    print(f.read().decode('utf-8'))
    
    
# 转换参数进行查询    
data = urllib.parse.urlencode({'wd': 'python', 'ie': 'utf-8'})
data = data.encode('utf-8') # 转码
with urllib.request.urlopen("http://www.baidu.com/s", data) as f:
    print(f.read().decode('utf-8'))    
    
    

# 代理
proxies = {'http': 'http://proxy.example.com:8080/'}
proxies = {}
opener = urllib.request.FancyURLopener(proxies)
with opener.open("http://www.python.org") as f:
    f.read().decode('utf-8')    
    
    
    
    