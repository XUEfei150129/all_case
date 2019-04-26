# coding=utf-8
import os
import sys
import time
import unittest
import string
import random
from case_lib.UI_case_lib.LGT.CarBascInfoUITool import CarBascInfoUItool
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from UI_Element_Tool.Find_Elements import *
from login_ui.Login_UI import LoginUi


class CarBascInfoUI(LoginUi):

    def test_add_car(self):
        sleep(3)
        self.wd.refresh()
        li_list = self.Check_elements(
            "css", "ul[role*=menubar]", "ul[role*=menubar]>li")
        for li in li_list:
            text = li.find_element_by_css_selector("span").text
            if text == "物流管理":
                li.click()
                break
        else:
            raise Exception("页面打开异常")
        self.wd.get(self.url + "/#/logistics/carBaseInfo")
        sleep(2)
        self.Click("css", ".shopRight>button:nth-child(1)")
        ran_str = ''.join(
            random.choices(
                string.ascii_uppercase +
                string.digits,
                k=6))
        print(ran_str)
        self.Input(
            "css",
            CarBascInfoUItool().carinfo(1),
            "苏{}".format(ran_str))
        self.Input("css", CarBascInfoUItool().carinfo(7), 2)
        self.Input("css", CarBascInfoUItool().carinfo(8), 2)
        self.Input("css", CarBascInfoUItool().carinfo(9), 2)
        self.Input("css", CarBascInfoUItool().carinfo(10), 2)
        self.Input("css", CarBascInfoUItool().carinfo(11), 2)
        self.Click("css", ".dialog-footer>button:nth-child(2)")  # 点击确定按钮
        sleep(2)
        self.wd.refresh()
        text = self.Get_text("css", CarBascInfoUItool().carlist(2))
        if text == "苏" + ran_str:
            print(f"添加车辆的车牌号是苏{ran_str}，页面上正确显示")
        else:
            raise Exception("添加车辆的功能异常")


car = CarBascInfoUI()
car.Login_ZMS_UI()
car.test_add_car()
