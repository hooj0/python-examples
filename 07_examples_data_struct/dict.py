#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2017-10-29 12:15:26
# @copyright by hoojo@2018
# @changelog Added python3 `data struct->dict` example


'''
dict 数据字典，全名：dictionary。
    数据结构形式是键值对key-value的形式，在其他语言中是map去表现的。

特点：    
    1、其查找速度快是主要表现之一
    2、插入速度快
    3、占用的内存比list、tuple多
    4、key 必须是不可变对象，如：字符串、整数等

example：
    dict = { 'name': 'jack', 'age': 22, 'brithday': (2010, 10, 22) }
            构造形式相当于 json字符串的构造，key必须要用引号  
            
API：
    1、dict.get(key)    获取dict中key的值
    2、dict.get(key, default)    获取dict中key的值，如果没有key的值，将返回默认值default
    3、dict[key]        获取dict中key的值
    4、key in dict, key not in dict     判断key是否在dict中存在
    5、dict[key] = value    对dict的key进行赋值
    6、dict.keys()    获取所有的键
    7、dict.values()    获取所有的值
    8、sorted(dict)    排序
    9、dict.clear()    清空
    10、dict.pop(key)    删除指定key元素
    11、del dict[key]    删除指定key元素
    
    12、dict.copy()    浅复制
    13、dict.fromkeys(seq) dict.fromkeys(seq, default)    创建一个新字典，默认值为default；default不传默认值为None
    14、dict.items() 返回可以直接遍历键值对
    15、dict.setdefault(key, value))    和get类似，可以获取值，如果值不存在就设置默认值
    16、dict.update(src)    将src字典数据更新到dict上，如果src的键在dict中存在的话就替换掉值，不存在就不处理
'''

# 构造一个dict 数据字典
user_info = { 'name': 'jason', 'age': 27, 'brithday': (1990, 10, 22) }
print('user information: ', user_info) # {'name': 'jason', 'age': 27, 'brithday': (1990, 10, 22)}

# 构造dict 方法2，用列表List 嵌套 元组
tmp = dict([ ('a', 10), ('b', 20), ('c', 30) ])
print("tmp:", tmp) # {'a': 10, 'b': 20, 'c': 30}

# 构造dict 方法3，有点像属性和值的对应
tmp = dict(name = 'tom', age = 22, address = 'china')
print("tmp:", tmp) # {'name': 'tom', 'age': 22, 'address': 'china'}

# 构造dict 动态方法
tmp = { key: key + 1 for key in [ 2, 4, 6 ] }
print("tmp:", tmp) # {2: 3, 4: 5, 6: 7}

print('-----------------------')

# 通过get去获取key值
print('user age information: ', user_info.get('age')) # 27
print('user age information: ', user_info.get('classes')) # None
# 也可以通过 obj['xxx'] 这种形式取值，类似JavaScript中的对象取值
print('user name information: ', user_info['name']) # jason
print('-----------------------')

############# 处理不存在的key ################
# KeyError: 'email'
#print('不存在的key：', user_info['email'])

# 'key' in obj，可以判断obj中是否存在key
print('exist email key:', 'email' in user_info) # exist email key: False
if 'email' in user_info:
    print('email', user_info['email'])  
else:
    print('not exist email key') 

# 不存在    
print('not in name:', 'name' not in user_info)    # not in name: False

# 通过get 方法，设置默认值。如果存在就返回值，不存在就返回默认值 = None
print('不存在的key：', user_info.get('email')) # 不存在的key： None
# 设置不存在的时候，默认值为 empty
print('不存在的key：', user_info.get('email', 'empty')) # 不存在的key： empty
print('-----------------------')

# 设置值
user_info['sex'] = 'girl'
print('user sex information: ', user_info['sex'])
user_info['name'] = 'alex'
print('user name information: ', user_info['name'])

print('set default:', user_info.setdefault('wechat', '134234234'))
print(user_info)
print('-----------------------')

# 删除元素
user_info.pop('name')
print('user information: ', user_info)

# 删除元素，和JavaScript类似
del user_info['sex']
print('user information: ', user_info)
print('-----------------------')

# 返回所有key
print("all keys:", user_info.keys())

# 返回所有value
print('all values:', user_info.values())

# 将value转换list
print('将value转换list：', list(user_info.values()))

# 排序
user_info['xyz'] = None
user_info['good'] = 1
print(sorted(user_info.keys()))
print('-----------------------')

# 清空字典
user_info.clear()
print('user information: ', user_info)

tmp = dict(name = 'tom', age = 22, address = 'china')
del tmp
#print('del tmp: ', tmp) #name 'tmp' is not defined


print('#########################内置API###########################')

tmp = dict(name = 'tom', age = 22, address = 'china')
print(tmp)
print('len(dict) 长度:', len(tmp))
print('str(len) 输出字典以可打印的字符串表示:', str(tmp))
print('type(dict) 类型:', type(tmp))

# 字典浅拷贝
L = tmp.copy()
print('copy dict:', L)

seq = ('age', 'name', 'sex', 'qq', 'phone')
# 创建一个字典对象，key值为seq对象，value为None
N = dict.fromkeys(seq)
print('new dict:', N)
# 创建一个字典对象，key值为seq对象，value为2
N = dict.fromkeys(seq, 2)
print('new dict:', N)

print('---------------')
# 将存在键值的字典N更新到字典tmp
tmp.update(N)
print('tmp.update(N):', tmp)
print('---------------')

# 返回可以直接遍历键值对
print('dict.items:', tmp.items())
for e in tmp:
    print(e)
for e in tmp.items():
    print(e)    
    
