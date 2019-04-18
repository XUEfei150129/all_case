#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/4/17 14:41
# @Author : XueFei

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


def mysort(alist):
    for i in range(0, len(alist) - 1):  # 需要遍历的次数是所有元素的少一次，比如5个元素，去最大值，要比较4次
        for j in range(0, len(alist) - i - 1):  #每一个元素要遍历的次数
                  #只是交换次数，但是要不要交换取决于相邻值的大小
            if alist[j] > alist[j + 1]:   #如果前面大于后面的值，就换位置
                alist[j], alist[j + 1] = alist[j + 1], alist[j]
    return alist
