#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

sql = '''
delete from EMPLOYEE where FIRST_NAME = 'bili2'
'''

try:
    # 执行删除语句
    row = cursor.execute(sql)
    print('row: %s' % row)
    
    # 提交操作
    db.commit()
    print('提交')
except:
    # 异常就回滚
    db.rollback()
    print('回滚')
        

# 关闭数据库连接
db.close()