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
from docx import Document


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

    def new_doc(fee_data, doc_path, fee):  # 新建一个word文档,写入汇总表的数据
        document = Document()
        p_total = document.add_paragraph()
        r_total = p_total.add_run(u'测试订单费用汇总表：')
        r_total.font.bold = True
        table = document.add_table(1, 5, style="Light List Accent 5")
        heading_cells = table.rows[0].cells
        heading_cells[0].text = u'序号'
        heading_cells[1].text = u'订单号'
        heading_cells[2].text = u'订单总额'
        heading_cells[3].text = u'运费'
        heading_cells[4].text = u'实付金额'
        total = 0
        for i in range(0, len(fee_data)):
            cells = table.add_row().cells
            cells[0].text = str(i + 1)
            cells[1].text = str(fee_data[i][0])
            cells[2].text = str(float(fee_data[i][1]) / 100)
            cells[3].text = str(float(fee_data[i][2]) / 100)
            cells[4].text = str(float(fee_data[i][3]) / 100)
            total = total + fee_data[i][3]
            if total > fee:  # 如果实付总额大于传入的金额，终止写入数据,并记录序号
                number = i
                break
        total = str(float(total) / 100)
        document.add_paragraph(u'实付金额总计：' + total + u' 元。')
        document.add_paragraph()
        p_detail = document.add_paragraph()
        r_detail = p_detail.add_run(u'测试订单明细：')
        r_detail.font.bold = True
        for i in range(0, number + 1):
            order_no = str(fee_data[i][0])
            paid_amount = str(float(fee_data[i][3]) / 100)
            row_str = str(i + 1) + '.' + u'订单号：' + order_no + u'实付金额：' + paid_amount + u'元。'
            document.add_paragraph(row_str)
        document.save(doc_path)


if __name__ == "__main__":
    util = SqlFile2WordUtils()
    util.read_sql_file("quartz.sql")
