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


class CarBascInfoUI(CarBascInfoUItool):

    def test_add_car(self):
        try:
            self.menuIndex("物流管理", "车辆基本信息")
            sleep(2)
            self.actionbuttons("新增")  # 点击新增按钮
            ran_str = self.ran_num(6)  # 生成6位随机数（数字，大写字母，小写字母）
            self.Input("css", self.carinfo(1), "苏{}".format(ran_str))
            self.Input("css", self.carinfo(7), 2)
            self.Input("css", self.carinfo(8), 2)
            self.Input("css", self.carinfo(9), 2)
            self.Input("css", self.carinfo(10), 2)
            self.Input("css", self.carinfo(11), 2)  # 添加车辆信息
            self.Click("css", ".dialog-footer>button:nth-child(2)")  # 点击确定按钮
            sleep(2)
            self.wd.refresh()
            text = self.Get_text("css", CarBascInfoUItool().carlist(2))
            if text == "苏" + ran_str:
                print(f"添加车辆的车牌号是苏{ran_str}，页面上正确显示")
            else:
                self.Screenshots()  # 截图
                raise Exception("添加车辆的功能异常")
        except:
            self.Screenshots()  # 截图
            raise Exception("添加车辆的功能异常")


if __name__ == '__main__':
    car = CarBascInfoUI()
    car.Login_ZMS_UI()
    car.test_add_car()
