#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
import pymysql
  
# 打开数据库连接  
db = pymysql.connect(host="localhost", user="root", password="root", db="test", port=3306)

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute() 方法执行 SQL，如果表存在则删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 使用预处理语句创建表
create_table_sql = """
    CREATE TABLE EMPLOYEE (
     FIRST_NAME  CHAR(20) NOT NULL primary key,
     LAST_NAME  CHAR(20),
     AGE INT,  
     SEX CHAR(1),
     INCOME FLOAT )
"""

# 执行创建表语句
print(cursor.execute(create_table_sql))


# 关闭数据库连接
db.close()