#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
insert into EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) 
            values(%s, %s, %s, %s, %s)
'''

try:
    # 执行插入语句
    row = cursor.executemany(sql, [('tom2', 'tom Li', 31, 'W', 21000), ('bili2', 'alex dk', 31, 'W', 21000)])
    print('row: ', row)
    
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