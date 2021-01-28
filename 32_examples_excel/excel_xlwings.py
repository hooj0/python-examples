#!/usr/bin/env python3
# encoding: utf-8
# @author:   hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create:   2021/1/22 0022
# @copyright by hoojo @2018
# @changelog Added `excel -> xlwings` python example


# ===============================================================================
# 标题：use xlwings lib read/write excel file
# ===============================================================================
# 使用：
#      网友博客：https://www.cnblogs.com/Renyi-Fan/p/13233572.html
#      官方手册：https://docs.xlwings.org/en/stable/quickstart.html
# -------------------------------------------------------------------------------
# 描述：xlwings 支持excel读写，比较全面高效快捷
# -------------------------------------------------------------------------------
import xlwings as xw


# ===============================================================================
# 示例：excel 写入数据
# ===============================================================================
# 写到Excel中去
# add_book也就是是否增加excel 的book
# visible=True 表示操作过程是否可显示
app = xw.App(visible=True, add_book=False)
# 工作簿
wb = app.books.add()

# 页sheet1
# sht = wb.sheets['sheet1']
sht = wb.sheets.add('test_sets')

# 单个值插入
sht.range('A1').value = '产品名称'
sht.range('B1').value = '编号'
sht.range('C1').value = '价格'
sht.range('A2').value = '不告诉你'
sht.range('B2').value = 'n110110'
sht.range('C2').value = '688.26'
sht.range('A3').value = '不告诉你1'
sht.range('B3').value = 'n1101101'
sht.range('C3').value = '688.261'

# 插入一行
sht.range('a1').value = [1, 2, 3, 4]
# 等同于
sht.range('a1:d4').value = [1, 2, 3, 4]

# 插入一列
sht.range('a2').options(transpose=True).value = [5, 6, 7, 8]

# 同时插入行列
sht.range('a6').expand('table').value = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]

# 在当前目录下生成文件
wb.save('demo1.xlsx')
wb.close()
app.quit()

# import os
# path1=os.path.abspath('.')   # 表示当前所处的文件夹的绝对路径
# print(path1)
# path2=os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
# print(path2)

# 关于路径问题，切换到指定目录即可

# output:
# -------------------------------------------------------------------------------
#
