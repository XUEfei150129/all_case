#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/4/17 14:41
# @Author : XueFei

import random
import string

"""
open参数




"""

# import logging  # 引入logging模块
# # 将信息打印到控制台上
# logging.debug(u"苍井空")
# logging.info(u"麻生希")
# logging.warning(u"小泽玛利亚")
# logging.error(u"桃谷绘里香")
# logging.critical(u"泷泽萝拉")
#


# def mysort(alist):
#     for i in range(0, len(alist) - 1):  # 需要遍历的次数是所有元素的少一次，比如5个元素，去最大值，要比较4次
#         for j in range(0, len(alist) - i - 1):  #每一个元素要遍历的次数
#                   #只是交换次数，但是要不要交换取决于相邻值的大小
#             if alist[j] > alist[j + 1]:   #如果前面大于后面的值，就换位置
#                 alist[j], alist[j + 1] = alist[j + 1], alist[j]
#     return alist

"""
文件的打开
file_object = open(file_name,access_mode="r" )
file_name
    文件路径：相对路径和绝对路径
access_mode
    读   (定义时等于号指定的值，缺省参数)
    写
    读加写




"""


# file = open(r"D:\test_python\test.txt", 'r', encoding="gb18030")  # 打开test1.txt 文件
# a = str(file.readlines())
# b = a.count("宝钗")
# print(b)
# file.close()  # 关闭文件


# print(str(open(r"D:\test_python\test.txt", 'r', encoding="gb18030").readlines()))

# b = str(open(r"D:\test_python\test.txt", 'r', encoding="gb18030").readlines())
# for i in range(1, 10):
#     a = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=60))
#     fileDir = "D:/test_python/test/{}.txt".format(a)  # 文件内容为：12345  换行abcde
#     fo = open(fileDir, "w")  # 打开文件，已二进制的格式打开
#     fo.write(a)

#
# dict = {'Name': 'Runoob', 'Age': 7}
# for i, j in dict.items():
#     print(i, ":\t", j)


# 先自定义两个异常
# class NameTooLongError(Exception):
#     pass
#
#
# class NameTooshortError(Exception):
#     pass
#
#
# def inputname():
#     name = input("请输入姓名：")
#     if len(name) > 10:
#         raise NameTooLongError
#     if len(name) < 6:
#         raise NameTooshortError
#
#
# # 主体部分调用
# try:  # 捕获异常
#     ret = inputname()
# except NameTooshortError:
#     print("太短了")
# except NameTooLongError:
#     print("太长了")

# 结果：
# 请输入姓名：1111111111111111111111
# 太长了

# 当输的名字长度大于10的时候，在函数里面会抛出NameTooLongError异常，函数后面的代码都不执了，因为它没有捕获异常。直接跑到上层去，调用它的地方去。调用的地方代码被try监控着，expect里面匹配这个错误类型。匹配到了，就会打印一个太长了



"""





"""
# import unittest
# import sys
# class SeleniumTest(unittest.TestCase):
#     ...
#
#     def tearDown(self):
#         if sys.exc_info()[0]:
#             test_method_name = self._testMethodName
#             self.driver.save_screenshot("Screenshots/%s.png" % test_method_name)
#         super(SeleniumTest, self).tearDown()

# from datetime import datetime
# png_name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# png_name = png_name.replace("-","")
# png_name = png_name.replace(":","")
# png_name = png_name.replace(" ","")
# print(png_name)

import re

from datetime import datetime
png_name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

png_name = re.sub("\D", "", png_name)
print(png_name)
