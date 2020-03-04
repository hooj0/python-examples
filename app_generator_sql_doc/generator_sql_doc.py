#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2020-03-04
# @copyright by hoojo @2020
# @changelog Generator SQL shell to Office word document
import os
import re


# ===============================================================================
#     Generator SQL shell to Office word document
# ===============================================================================
# 描述：读取sql脚本，生成word文档
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 读取SQL脚本生成 word的文档 工具类
# -------------------------------------------------------------------------------

class SqlFile2WordUtils:

    def __init__(self):
        print("init....")

    def read_sql_file(self, sql_file):

        if sql_file is None:
            print("sql file path 为空")
        elif not os.path.exists(sql_file):
            print('%s is not found!' % sql_file)
            raise IOError('%s is not found!' % sql_file)

        with open(sql_file, 'r', encoding=u'utf-8') as file:
            data = file.read()

        return "settings"


if __name__ == "__main__":
    util = SqlFile2WordUtils()
    util.read_sql_file("quartz.sql")
