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
        return ".el-table__header-wrapper+div>table>tbody>tr>td:nth-child({})>div".format(
            col)

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
                    if menuname_next in li_next_text:
                        li_next.click()
                        break
            except BaseException:
                self.wd.get(
                    "http://zms.autotest.znlhzl.org/#/logistics/carBaseInfo")
        except BaseException:
            raise Exception("通过链接和按钮都无法登陆")

    def actionbuttons(self, button_name):
        try:
            sleep(2)
            buttons = self.Check_element("css", "div.shopRight")
            button_list = buttons.find_elements("css", "button")  # 这里不需要组选择器
            for button in button_list:
                buttonname = button.find_element_by_css_selector("span")
                if button_name in buttonname.text:
                    button.click()
                    break
            createVehicle = self.Get_text(
                "css",
                "div.content-box>div:nth-child(2)>div:nth-child(2)>div:nth-child(2)>div>div>div>span")
            if "新建车辆信息" == createVehicle:
                print("点击新增按钮正常")
            else:
                self.wd.get(
                    "http://zms.autotest.znlhzl.org/#/logistics/carBaseInfo")
                self.actionbuttons(button_name)  # 通过递归，确保正常执行下去
        except BaseException:
            raise Exception("点击按钮异常")


if __name__ == '__main__':
    car = CarBascInfoUItool()
    car.Login_ZMS_UI()
    car.menuIndex("物流管理", "车辆基本信息")
    car.actionbuttons("新增")
