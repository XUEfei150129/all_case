#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/4/2 16:51
# @Author : XueFei
import os
import sys
import time
import unittest
import string
import random
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from UI_Element_Tool.Find_Elements import *
from login_ui.Login_UI import LoginUi


class CarBascInfoUItool(LoginUi):

    def carinfo(self, row):
        """
        添加车辆，对应的每一行的元素
        """
        return f"div.el-dialog__body>form>div:nth-child({row})>div>div>input"

    def carlist(self, col):

        """
        车辆列表页，第一行每一列的元素
        """
        return ".el-table__header-wrapper+div>table>tbody>tr>td:nth-child({})>div".format(col)

    def BindMenuLevel(self, menu_name):
        """
        平台访问场景：http://zms.autotest.znlhzl.org/#/dashboard
        根据根据左侧一级菜单的名称，选择点击该菜单
        :param menu_name:左侧一级菜单的名称
        :return:
        """
        sleep(3)
        self.wd.refresh()
        li_list = Tool_Element().Check_elements(
            "css", "ul[role*=menubar]", "ul[role*=menubar]>li")
        for li in li_list:
            text = li.find_element_by_css_selector("span").text
            if text == f"{menu_name}":
                li.click()
                break
        else:
            raise Exception("页面打开异常")

    def menuIndex(self, menuname, menuname_next):
        """
        # 平台访问场景：http://zms.autotest.znlhzl.org/#/dashboard
        # 根据根据左侧一级菜单的名称，选择点击该菜单
        :param menuname:一级菜单名称(可模糊填写，满足in的语法即可)
        :param menuname_next:二级菜单名称(可模糊填写，满足in的语法即可)
        :return:
        """
        try:
            try:
                sleep(3)
                self.wd.refresh()
                lis = self.Check_element("css", 'ul[role*="menubar"]')
                li_list = lis.find_elements("css", "li")
                for li in li_list:
                    li_text = (li.find_element("css", "i+span")).text
                    if "{}".format(menuname) in li_text:
                        li.click()
                        break
                li_list_next = li.find_elements("css", "div+ul>li")
                sleep(2)
                for li_next in li_list_next:
                    li_next_text = li_next.text
                    if "{}".format(menuname_next) in li_next_text:
                        li_next.click()
                        break
            except:
                self.wd.get("http://zms.autotest.znlhzl.org/#/logistics/carBaseInfo")
        except:
            raise Exception("通过链接和按钮都无法登陆")


if __name__ == '__main__':
    car = CarBascInfoUItool()
    car.Login_ZMS_UI()
    car.menuIndex("物流管理", "物流对内管理时效")
