#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-14 23:01:28
# @copyright by hoojo@2018
# @changelog Added python3 `db->db insert` example


import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
            values('jack', 'jack chen', 33, 'M', 3000)
'''

try:
    # 执行插入语句
    cursor.execute(sql)
    
    # 提交操作
    db.commit()
    print('提交')
except:
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close()