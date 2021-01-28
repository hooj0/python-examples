#!/usr/bin/env python3
# encoding: utf-8
# @author:   hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create:   2021/1/22 0022
# @copyright by hoojo @2018
# @changelog Added `torrent-search` python example


# ===============================================================================
# 标题：magnet & torrent resource searcher tool
# ===============================================================================
# 使用：
# -------------------------------------------------------------------------------
# 描述：磁力资源搜索器，一键搜索整合磁力资源
# -------------------------------------------------------------------------------
import os
import json
import asyncio
import requests
import xlwings as xw
from pyquery import PyQuery as pq
from jinja2 import Environment, select_autoescape, FileSystemLoader


# -------------------------------------------------------------------------------
# 定义搜索器父类对象，其他搜索继承该对象
# -------------------------------------------------------------------------------
class TorrentSearcher:
    """
    搜索器父类
    """

    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"}

    def __init__(self, site, url, keyword, view="TEXT"):
        """
        初始化方法，完成必要参数收集初始化
        """

        self.url = url
        self.site = site
        self.keyword = keyword
        self.view = view

    def search(self):
        """
        搜索方法，完成搜索请求
        """
        info("%s -> start search keyword %s data......" % (self.site, self.keyword))

        response = requests.get(self.url % self.keyword, headers=self.headers)
        response.encoding = "UTF-8"

        debug("%s -> send request URL: " % response.url)
        debug("%s -> send request status_code: " % response.status_code)

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
            return json.dumps(content)
        else:
            return pq(content)

    def viewer(self, records):
        """
        展示方法，完成转换后的结果进行统一显示操作
        """

        info("%s -> start view %s records......" % (self.site, self.keyword))

        view = Viewer(self.site, self.keyword, records)
        if self.view == "TEXT":
            view.text()
        elif self.view == "HTML":
            view.html()
        elif self.view == "EXCEL":
            view.excel()
        else:
            view.text()

    def executor(self):
        """
        执行
        """

        info("%s -> start executor %s operation ......" % (self.site, self.keyword))

        content = self.search()
        records = self.parser(content)
        self.viewer(records)

    async def request(self):
        """
        异步请求
        """

        info("%s -> start executor %s operation ......" % (self.site, self.keyword))

        content = self.search()
        records = self.parser(content)

        return records


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
        app = xw.App(visible=True, add_book=False)

        # 工作簿
        wb = app.books.add()

        # 页sheet1
        for site, items in self.records.items():
            sht = wb.sheets.add(site)

            # 单个值插入
            sht.range("A1").value = ["名称", "大小", "日期", "下载"]

            row = 2
            for item in items:
                sht.range("A%s" % row).value = [item["title"], item["size"], item["date"], item["magnet"]]
                row = row + 1

        # 在当前目录下生成文件
        wb.save("%s 的搜索结果.xlsx" % self.keyword)
        wb.close()
        app.quit()

    def html(self):
        """
        html 方式展示结果
        """
        info("%s -> view %s HTML record" % (self.site, self.keyword))

        # 从指定位置加载模板的环境
        loader = FileSystemLoader(".")
        # 更多配置参考：http://jinja.pocoo.org/docs/2.10/api/#high-level-api
        env = Environment(loader=loader,
                          autoescape=select_autoescape(["html", "xml"]),
                          line_statement_prefix="#",
                          line_comment_prefix="##",
                          trim_blocks=True, keep_trailing_newline=True, lstrip_blocks=True)

        # 获取模板
        template = env.get_template("template.html")

        # 渲染模板
        result = template.render(data=self.records, keyword=self.keyword)

        file_path = "./%s 的搜索结果.html" % self.keyword
        realpath = os.path.realpath(file_path)
        dirname = os.path.dirname(realpath)
        info('generator file to absolute path: %s' % realpath)

        if not os.path.exists(dirname):
            os.makedirs(dirname)

        with open(file_path, 'w', encoding=u'utf-8') as file:
            file.seek(0)
            file.truncate()   # 清空文件

            file.write(result)

            file.flush()
            file.close()

    def text(self):
        """
        text 文本方式展示结果
        """
        info("%s -> view %s TEXT record" % (self.site, self.keyword))

        for site, items in self.records.items():
            print("=" * 40 + site + "=" * 40)
            print("title\t\tmagnet\t\tsize\t\tdate")
            print("-" * 80)

            for item in items:
                print("%s\t\t%s\t\t%s\t\t%s" % (item["title"], item["magnet"], item["size"], item["date"]))

        print("-" * 80)
        print("\n\n")


def debug(message, *args):
    print("[DEBUG]" + message, *args)


def info(message, *args):
    print("[INFO]" + message, *args)


# ===============================================================================
# 定义 查询器 对象，继承
# ===============================================================================
class DaatkkTorrentSearcher(TorrentSearcher):

    site = "daatkk"

    def __init__(self, keyword, view="TEXT"):
        TorrentSearcher.__init__(self, self.site, "https://daatkk.cyou/list.php?q=%s", keyword, view)

    def parser(self, content):
        """
        转换方法，完成搜索结果转换统一标准
        将结果提取到数据数据集合列表：[{title, magnet, size, date}]
        """

        doc = TorrentSearcher.parser(self, content)
        rows = doc.find("ul.list-group li:gt(1)")

        records = []
        for row in rows:
            records.append({"title": pq(row).text().split("文件链接")[0].strip(), "magnet": row.find("a").attrib["href"], "size": None, "date": None})

        return {self.site: records}


class ZooqleTorrentSearcher(TorrentSearcher):

    site = "zooqle"

    def __init__(self, keyword, view="TEXT"):
        TorrentSearcher.__init__(self, self.site, "https://zooqle.com/search?q=%s", keyword, view)

    def parser(self, content):
        """
        转换方法，完成搜索结果转换统一标准
        将结果提取到数据数据集合列表：[{title, magnet, size, date}]
        """

        doc = TorrentSearcher.parser(self, content)
        rows = doc.find(".table-torrents tr")

        records = []
        for i in range(len(rows)):
            if i == 0:
                continue

            records.append({
                "title": pq(rows[i]).find("td a").text().replace("\n", ''),
                "magnet": pq(rows[i]).find("td a[title='Magnet link']").attr["href"],
                "size": pq(rows[i]).find("td div.prog-blue").text(),
                "date": None
            })
        return {self.site: records}

async def executor(keyword, view="TEXT"):

    daatkkTorrentSearcher = DaatkkTorrentSearcher(keyword, view)
    zooqleTorrentSearcher = ZooqleTorrentSearcher(keyword, view)

    results = await asyncio.gather(daatkkTorrentSearcher.request(), zooqleTorrentSearcher.request())

    daatkkTorrentSearcher.viewer({**results[0], **results[1]})

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(executor("流浪地球", view="HTML"))
    finally:
        loop.close()

