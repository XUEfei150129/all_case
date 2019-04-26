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
# b = a.count("宝玉")
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

