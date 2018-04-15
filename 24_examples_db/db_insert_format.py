#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-15 14:19:29
# @copyright by hoojo@2018
# @changelog Added python3 `db -> db insert format` example


import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = "insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) values('%s', '%s', '%d', '%s', '%d')" % ('alex', 'alex chen', 21, 'M', 567777)

print(sql)
try:
    # 执行插入语句
    cursor.execute(sql)
    
    # 提交操作
    db.commit()
    print('提交')
except OSError as e:
    print('error: %s' % e)
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close()