#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-15 15:55:05
# @copyright by hoojo@2018
# @changelog Added python3 `db->db call proc` example


import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')

# 使用 cursor() 方法创建一个游标对象 cursor
# 游标设置为字典类型
cursor = db.cursor(cursor=pymysql.cursors.DictCursor)

try:
    cursor.callproc('p2', args=(1, 22, 3, 4))
    
    #获取执行完存储的参数,参数@开头
    cursor.execute("select @p1, @_p1_1, @_p1_2, @_p1_3")  #{u'@_p1_1': 22, u'@p1': None, u'@_p1_2': 103, u'@_p1_3': 24}
    
    # 获取第一条记录
    row = cursor.fetchone()
    print('row: ', row)

    db.commit()
except OSError as e:
    print('error: %s' % e)
        
# 关闭数据库连接
db.close()