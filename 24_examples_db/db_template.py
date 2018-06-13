#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo

import pymysql

import contextlib

#定义上下文管理器，连接后自动关闭连接
@contextlib.contextmanager
def mysql_template(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8'):
  
    # 打开数据库连接  
    db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306, charset='utf8')
    
    # 使用 cursor() 方法创建一个游标对象 cursor
    # 游标设置为字典类型
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    
    try:
        yield cursor
    
        db.commit()
    except OSError as e:
        print('error: %s' % e)
        
    finally:
        cursor.close()
        # 关闭数据库连接
        db.close()
        

# 使用模板查询        
with mysql_template() as cursor:
    print(cursor)
    
    row_count = cursor.execute("select * from EMPLOYEE")
    row = cursor.fetchone()
    
    print(row_count)
    print(row)  