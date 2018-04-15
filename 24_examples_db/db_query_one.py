#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-15 14:27:15
# @copyright by hoojo@2018
# @changelog Added python3 `db -> query one` example


'''
Python查询Mysql使用 fetchone() 方法获取单条数据, 使用fetchall() 方法获取多条数据。
    fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    fetchall(): 接收全部的返回结果行.
    rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
'''

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
select FIRST_NAME, LAST_NAME, AGE, SEX, INCOME from EMPLOYEE limit 1
'''

try:
    # 执行查询语句
    cursor.execute(sql)
    
    # 获取查询记录
    result = cursor.fetchone()
    
    print('result: FIRST_NAME->%s, LAST_NAME->%s, AGE->%s, SEX->%s, INCOME->%s' % result)
except OSError as e:
    print('error: %s' % e)
        
# 关闭数据库连接
db.close()