#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo

import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
# 游标设置为字典类型
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

try:
    #无参数存储过程
    cursor.callproc('p1')  #等价于cursor.execute("call p1()")
    
    # 获取第一条记录
    row = cursor.fetchone()
    print('row: ', row)

    db.commit()
except OSError as e:
    print('error: %s' % e)
        
# 关闭数据库连接
db.close()