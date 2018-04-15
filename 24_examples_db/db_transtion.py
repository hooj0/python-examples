#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-15 14:46:45
# @copyright by hoojo@2018
# @changelog Added python3 `db -> transtion` example


import pymysql
  
'''
执行事务

事务机制可以确保数据一致性。
    事务应该具有4个属性：原子性、一致性、隔离性、持久性。这四个属性通常称为ACID特性。
            原子性（atomicity）。一个事务是一个不可分割的工作单位，事务中包括的诸操作要么都做，要么都不做。
            一致性（consistency）。事务必须是使数据库从一个一致性状态变到另一个一致性状态。一致性与原子性是密切相关的。
            隔离性（isolation）。一个事务的执行不能被其他事务干扰。即一个事务内部的操作及使用的数据对并发的其他事务是隔离的，并发执行的各个事务之间不能互相干扰。
            持久性（durability）。持续性也称永久性（permanence），指一个事务一旦提交，它对数据库中数据的改变就应该是永久性的。接下来的其他操作或故障不应该对其有任何影响。
Python DB API 2.0 的事务提供了两个方法 commit 或 rollback。
'''  
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