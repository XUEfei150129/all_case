#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/3/22 12:40
# @Author : XueFei
import unittest
import time
import os
import sys
import time
import unittest
from UI_Element_Tool.Find_Elements import Tool_Element
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class LoginUi(Tool_Element):
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    url = "http://zms.autotest.znlhzl.org"  # 不同的坏境，需更换地址


    def open_browser(self):
        self.wd.maximize_window()  # 最大化窗口
        self.wd.implicitly_wait(15)

    def Login_ZMS_UI(self, name="15050563690", password="888888"):
        self.open_browser()
        self.wd.get(self.url + "/#/login")
        self.Input("css", 'input[type*="text"]', name)
        self.Input("css", 'input[type*="password"]', password)
        self.Click("css", "div.login-btn")
        time.sleep(5)


if __name__ == '__main__':
    wo = LoginUi()
    wo.Login_ZMS_UI()
