#!/usr/bin/env python3
# encoding: utf-8
# @author: hoojo
# @email: hoojo_@126.com
# @github: https://github.com/hooj0
# @create date: 2018-04-06 11:01:59
# @copyright by hoojo@2018
# @changelog Added python3 `standand lib -> doctest lib` example


import doctest
import unittest

def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.01
    """
    return sum(values) / len(values)


# 运行测试，通过doc的结果和代码运行结果进行比较
print(doctest.testmod())   # 自动验证嵌入测试

'''
**********************************************************************
File "F:\Example Exercise\Python\example_8_standand_lib\doctest_lib.py", line 9, in __main__.average
Failed example:
    print(average([20, 30, 70]))
Expected:
    40.01 # 错误的结果
Got:
    40.0 # 正确结果
**********************************************************************
1 items had failures:
   1 of   1 in __main__.average
***Test Failed*** 1 failures.
TestResults(failed=1, attempted=1) # 1个错误
'''


# TestCase 测试用例
class TestStatisticalFunctions(unittest.TestCase):

    # 测试方法
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)
        print('result: ', average([20, 30, 70]))
    
    # 执行方法2    
    def test_average2(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)
        print('result: ', average([20, 30, 70])) 
        

unittest.main() # Calling from the command line invokes all tests