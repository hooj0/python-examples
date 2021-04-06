#!/usr/bin/env python3
# encoding: utf-8
# @create:   2021/4/6 0006
# @copyright by hoojo @2021
# @changelog Added  `gdgpo-searcher` python example


# ===============================================================================
# 标题：gdgpo purchase intention resource searcher tool
# ===============================================================================
# 使用：
# -------------------------------------------------------------------------------
# 描述：一键提取广东 采购意向 搜索的结果数据
# -------------------------------------------------------------------------------
import json
import sys
import getopt
import requests
import time
import xlwings as xw
from pyquery import PyQuery as pq


# -------------------------------------------------------------------------------
# 定义搜索器父类对象，其他搜索继承该对象
# -------------------------------------------------------------------------------
class GDgpoSearcher:
    """
    搜索器父类
    """

    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    def __init__(self, site, url, keyword):
        """
        初始化方法，完成必要参数收集初始化
        """

        self.url = url
        self.site = site
        self.keyword = keyword

    def search(self):
        """
        搜索方法，完成搜索请求
        """
        info("%s -> start search keyword %s data......" % (self.site, self.keyword))

        response = requests.get(self.url % self.keyword, headers=self.headers)
        response.encoding = "UTF-8"

        debug("%s -> send request URL: %s" % (self.site, response.url))
        debug("%s -> send request status_code: %s" % (self.site, response.status_code))

        if response.ok:
            debug("%s -> send request OK" % self.site)

            if response.status_code == 200:
                debug("%s -> search keyword: %s success" % (self.site, self.keyword))
                return response.text
            else:
                debug("%s -> send request failure." % self.site)
                response.raise_for_status()
        else:
            debug("%s -> send request DONT OK." % self.site)
            return None

    def parser(self, content):
        """
        转换方法，完成搜索结果转换统一标准
        将结果提取到数据数据集合列表：[{title, magnet, size, date}]
        """

        info("%s -> start parser %s content......." % (self.site, len(content)))
        if content.startswith("{") or content.startswith("["):
            debug("%s -> json parser." % self.site)
            return json.loads(content)
        else:
            debug("%s -> text parser." % self.site)
            return pq(content)

    def viewer(self, records):
        """
        展示方法，完成转换后的结果进行统一显示操作
        """

        info("%s -> start view %s records......" % (self.site, self.keyword))

        view = Viewer(self.site, self.keyword, records)
        view.excel()

    def executor(self):
        """
        执行
        """

        info("%s -> start executor %s operation ......" % (self.site, self.keyword))

        content = self.search()
        records = self.parser(content)
        self.viewer(records)


class Viewer:
    """
    视图器父类，完成搜索结果统一展示操作；
    分别提供text展示、html展示、excel展示

    展示数据集：title, magnet, size, date
    """

    def __init__(self, site, keyword, records):
        self.site = site
        self.keyword = keyword
        self.records = records

        info("%s -> view %s record %s" % (self.site, self.keyword, len(self.records)))

    def excel(self):
        """
        excel 方式展示结果
        """
        info("%s -> view %s EXCEL record" % (self.site, self.keyword))

        # visible=True 表示操作过程是否可显示
        app = xw.App(visible=False, add_book=False)

        # 工作簿
        wb = app.books.add()

        # 页sheet1
        for site, items in self.records.items():
            sht = wb.sheets.add(site)

            # 单个值插入
            sht.range("A1").value = ["标题", "地址", "发布机构", "发布时间", "采购项目名称",	"采购需求概况", "预算金额(元)", "预计采购时间", "备注"]

            row = 2
            for item in items:
                sht.range("A%s" % row).value = [item["title"], item["url"], item["purchaser"], item["noticeTime"],
                                                item["project_name"], item["general_situation"], item["amount"], item["time"], item["remark"]]
                row = row + 1

        # 在当前目录下生成文件
        wb.save("数据抓取结果-%s.xlsx" % time.time())
        wb.close()
        app.quit()


def debug(message, *args):
    # print("[DEBUG]" + message, *args)
    pass


def info(message, *args):
    print("[INFO]" + message, *args)


# ===============================================================================
# 定义 查询器 对象，继承
# ===============================================================================
class GDgpoPurchaseIntentionSearcher(GDgpoSearcher):

    site = "Detail"

    url = "https://gdgpo.czt.gd.gov.cn/freecms/rest/v1/notice/selectInfoMoreChannel.do?"
    url += "&siteId=cd64e06a-21a7-4620-aebc-0576bab7e07a&channel=fca71be5-fc0c-45db-96af-f513e9abda9d"
    url += "&selectTimeName=noticeTime&noticeType=%s"
    # url += "&currPage=%s&pageSize=%s"

    def __init__(self, keyword, start, count):
        self.url = self.url + "&currPage=%s&pageSize=%s" % (start, count)
        GDgpoSearcher.__init__(self, self.site, self.url, keyword)

    def request_detail(self, url):
        info("%s -> start request detail url: %s" % (self.site, url))

        response = requests.get(url, headers=self.headers)
        response.encoding = "UTF-8"

        debug("%s -> send request URL: %s" % (self.site, response.url))
        debug("%s -> send request status_code: %s" % (self.site, response.status_code))

        if response.ok:
            debug("%s -> send request OK" % self.site)

            if response.status_code == 200:
                return response.text
            else:
                debug("%s -> send request failure." % self.site)
                response.raise_for_status()
        else:
            debug("%s -> send request DONT OK." % self.site)
            return None

    def parser(self, content):
        """
        转换方法，完成搜索结果转换统一标准
        """

        doc = GDgpoSearcher.parser(self, content)
        rows = doc["data"]

        site = "https://gdgpo.czt.gd.gov.cn"
        records = []
        for row in rows:

            detail_url = site + row["pageurl"]
            detail_result = self.request_detail(detail_url)
            doc = pq(detail_result)
            tr = doc.find("table.noticeTable tr:eq(1)")

            records.append({
                "title": row["title"],
                "url": detail_url,
                "purchaser": row["fieldValues"]["f_purchaser"],
                "noticeTime": row["fieldValues"]["f_noticeTime"],
                "project_name": pq(tr.find("td")[1]).text(),
                "general_situation": pq(tr.find("td")[2]).text(),
                "amount": pq(tr.find("td")[3]).text(),
                "time": pq(tr.find("td")[4]).text(),
                "remark": pq(tr.find("td")[5]).text(),
            })

        return {self.site: records}


def executor(start=1, count=100):

    # 采取页号，起始页
    # start = 1
    # 单次采取数据量，越大越慢
    # count = 100

    # 59 采购意向
    # 001051 单一来源公示

    info("提取数据，提取页：%s，提取条数：%s" % (start, count))
    searcher = GDgpoPurchaseIntentionSearcher("59", start, count)
    searcher.executor()

def main(argv):
    # print('argv: %s' % argv)

    help_usage = '''
    USAGE: python gdgpo-searcher.py [OPTIONS] start count
    
    OPTIONS: 
      -h,--help         use the help manual.
      
    COMMANDS:
      help        use the help manual
        
    EXAMPLES: 
      python gdgpo-searcher.py -h
      python gdgpo-searcher.py help
    
      python gdgpo-searcher.py
      python gdgpo-searcher.py 1
      
      python gdgpo-searcher.py 1 100
    '''

    # default run current path
    if len(argv) < 1:
        executor()
        sys.exit()

    try:
        long_opts = ["help"]
        opts, args = getopt.getopt(argv, "h", long_opts)
        print('opts: %s, args: %s' % (opts, args))
    except getopt.GetoptError:
        print(help_usage)
        sys.exit(2)

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_usage)
            sys.exit()

    for arg in args:
        if arg == 'help':
            print(help_usage)
        else:
            executor(args[0], args[1])
        sys.exit()

    if len(args) < 0:
        print(help_usage)
        sys.exit()


if __name__ == "__main__":
    main(sys.argv[1:])