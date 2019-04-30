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

    def Login_ZMS_UI(self, name="15050563690", password="888888", title_e="众能后台管理系统"):
        """

        :param name: 登录的用户名
        :param password: 登录的密码
        :param 登录期望的页面title
        :return:
        """
        try:
            self.open_browser()
            self.wd.get(self.url + "/#/login")
            self.Input("css", 'input[type*="text"]', name)
            self.Input("css", 'input[type*="password"]', password)
            self.Click("css", "div.login-btn")
            time.sleep(5)
            title_a = self.wd.title
            if "{}".format(title_e) in title_a:
                pass
            else:
                raise Exception("登录页面出现异常")
        except:
            self.Login_ZMS_UI()


if __name__ == '__main__':
    wo = LoginUi()
    wo.Login_ZMS_UI()
