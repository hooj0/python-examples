#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email:    hoojo_@126.com
# @github:   https://github.com/hooj0
# @create date: 2018-09-12
# @copyright by hoojo @2018
# @changelog unittest lib TestCase code


# ===============================================================================
# 标题：unittest TestCase
# ===============================================================================
# 描述：使用 unittest TestCase 测试框架测试用例代码
# -------------------------------------------------------------------------------


# -------------------------------------------------------------------------------
# 构建 fabric 网络配置生成工具 TestCase
# -------------------------------------------------------------------------------
import unittest


class TestStringMethods(unittest.TestCase):

    def setUp(self):
        print('init by setUp...')

    def tearDown(self):
        print('end by tearDown...')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        self.assertTrue('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
