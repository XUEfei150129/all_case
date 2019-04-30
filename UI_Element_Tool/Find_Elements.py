#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/3/22 12:27
# @Author : XueFei


import os
import sys
import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import string
import random
import re
from datetime import datetime


class Tool_Element:
    wd = webdriver.Chrome()

    # 跳转页面
    def Jumpwebpage(self, page, time_wait=3):
        self.wd.get(self.Getwebpage(page))
        self.wd.maximize_window()

        if isinstance(time_wait, int):
            time.sleep(time_wait)

    # def Getwebpage(self, page):
    # 	return R.ReadXmlData("%s.xml" % page, "page", 0, "url")

    # 浏览器前进操作
    def forward(self):
        self.wd.forward()

    # 浏览器后退操作
    def back(self):
        self.wd.back()

    # 隐式等待
    def wait(self, seconds):
        self.wd.implicitly_wait(seconds)

    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/screenshots/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.wd.get_screenshot_as_file(screen_name)
        except NameError as e:
            self.get_windows_img()

    def Current_handel(self):
        # 这时切换到新窗口
        all_handles = self.wd.window_handles
        for handle in all_handles:
            self.wd.switch_to.window(handle)

    # 打开浏览器的方法
    # def Openbrowser(self):
    #     if self.browser_type == 'Firefox':
    #         self.wd = webdriver.Firefox()
    #     elif self.browser_type == 'Chrome':
    #         self.wd = webdriver.Chrome()
    #     elif self.browser_type == 'IE':
    #         self.wd = webdriver.Ie()
    #     elif self.browser_type == '':
    #         self.wd = webdriver.Chrome()
    #     self.wd.maximize_window()

    def open_browser(self):
        self.wd.maximize_window()  # 最大化窗口
        self.wd.implicitly_wait(15)

    # 关闭浏览器
    def close_browser(self):
        self.wd.quit()

    # 输入内容方法
    # send_keys 方法
    def Input(self, type, value, inputvalue):
        if type == "xpath":
            res = self.wd.find_element_by_xpath(value).send_keys(inputvalue)
        elif type == "class_name":
            res = self.wd.find_element_by_class_name(
                value).send_keys(inputvalue)
        elif type == "id":
            res = self.wd.find_element_by_id(value).send_keys(inputvalue)
        elif type == "name":
            res = self.wd.find_element_by_name(value).send_keys(inputvalue)
        elif type == "link_text":
            res = self.wd.find_element_by_link_text(
                value).send_keys(inputvalue)
        elif type == "partial_link_text":
            res = self.wd.find_element_by_partial_link_text(
                value).send_keys(inputvalue)
        elif type == "css":
            res = self.wd.find_element_by_css_selector(
                value).send_keys(inputvalue)
        return res

    # 鼠标事件方法一
    # click方法
    def Click(self, type, value):
        if type == "xpath":
            res = self.wd.find_element_by_xpath(value).click()
        elif type == "class_name":
            res = self.wd.find_element_by_class_name(value).click()
        elif type == "id":
            res = self.wd.find_element_by_id(value).click()
        elif type == "name":
            res = self.wd.find_element_by_name(value).click()
        elif type == "link_text":
            res = self.wd.find_element_by_link_text(value).click()
        elif type == "partial_link_text":
            res = self.wd.find_element_by_partial_link_text(value).click()
        elif type == "css":
            res = self.wd.find_element_by_css_selector(value).click()
        return res

    # 鼠标事件方法二
    # clear方法
    def Clear(self, type, value):
        if type == "xpath":
            self.wd.find_element_by_xpath(value).clear()
        elif type == "id":
            self.wd.find_element_by_id(value).clear()
        elif type == "name":
            self.wd.find_element_by_name(value).clear()
        elif type == "link_text":
            self.wd.find_element_by_link_text(value).clear()
        elif type == "partial_link_text":
            self.wd.find_element_by_partial_link_text(value).clear()
        elif type == "css":
            self.wd.find_elements_by_css_selector(value).clear()

    # 验证元素是否存在
    def Check_element(self, type, value):
        if type == "xpath":
            res = self.wd.find_element_by_xpath(value)
        elif type == "id":
            res = self.wd.find_element_by_id(value)
        elif type == "name":
            res = self.wd.find_element_by_name(value)
        elif type == "link_text":
            res = self.wd.find_element_by_link_text(value)
        elif type == "partial_link_text":
            res = self.wd.find_element_by_partial_link_text(value)
        elif type == "css":
            res = self.wd.find_element_by_css_selector(value)
        return res

    # 获取子元素
    def Select_child_elements(self, type, value1, value2):
        if type == "xpath":
            Select(self.wd.find_element_by_xpath(value1)
                   ).select_by_visible_text(value2)
        elif type == "id":
            Select(self.wd.find_element_by_id(value1)
                   ).select_by_visible_text(value2)
        elif type == "name":
            Select(self.wd.find_element_by_name(value1)
                   ).select_by_visible_text(value2)
        elif type == "link_text":
            Select(self.wd.find_element_by_link_text(
                value1)).select_by_visible_text(value2)
        elif type == "partial_link_text":
            Select(self.wd.find_element_by_partial_link_text(
                value1)).select_by_visible_text(value2)

    # 获取输入框的值
    def Get_attribute(self, type, value1, value2):
        if type == "xpath":
            Value = self.wd.find_element_by_xpath(value1).get_attribute(value2)
            return Value
        elif type == "name":
            Value = self.wd.find_element_by_name(value1).get_attribute(value2)
            return Value
        elif type == "link_text":
            Value = self.wd.find_element_by_link_text(
                value1).get_attribute(value2)
            return Value
        elif type == "class_name":
            Value = self.wd.find_element_by_class_name(
                value1).get_attribute(value2)
            return Value
        elif type == "id":
            Value = self.wd.find_element_by_id(value1).get_attribute(value2)
            return Value

    # 获取下拉框的文本的值

    def Get_text(self, type, value):
        if type == "xpath":
            text = self.wd.find_element_by_xpath(value).text
            return text
        elif type == "name":
            text = self.wd.find_element_by_name(value).text
            return text
        elif type == "link_text":
            text = self.wd.find_element_by_link_text(value).text
            return text
        elif type == "class_name":
            text = self.wd.find_element_by_class_name(value).text
            return text
        elif type == "id":
            text = self.wd.find_element_by_id(value).text
            return text
        elif type == "css":
            text = self.wd.find_element_by_css_selector(value).text
            return text

    # 显性等待时间
    def WebDriverWait(self, MaxTime, Mimtime, value):
        element = self.wd.find_element(By.ID, value)
        WebDriverWait(
            self.wd, MaxTime, Mimtime).until(
            EC.presence_of_element_located(element))

    # # 鼠标移动点击机制
    def Move_action(self, type, value):
        if type == "xpath":
            xm = self.wd.find_element_by_xpath(value)
            webdriver.ActionChains(self.wd).click(xm).perform()
        elif type == "id":
            xm = self.wd.find_element_by_id(value)
            webdriver.ActionChains(self.wd).click(xm).perform()
        elif type == "name":
            xm = self.wd.find_element_by_name(value)
            webdriver.ActionChains(self.wd).click(xm).perform()
        elif type == "link_text":
            xm = self.wd.find_element_by_link_text(value)
            webdriver.ActionChains(self.wd).click(xm).perform()
        elif type == "css":
            xm = self.wd.find_element_by_css_selector(value)
            webdriver.ActionChains(self.wd).click(xm).perform()

    # 校验按钮是否为选中状态
    def Is_selected(self, type, value):
        if type == "id":
            self.wd.find_element_by_id(value).is_selected()
        elif type == "xpath":
            self.wd.find_element_by_xpath(value).is_selected()
        elif type == "class_name":
            self.wd.find_element_by_class_name(value).is_selected()
        elif type == "name":
            self.wd.find_element_by_name(value).is_selected()
        elif type == "link_text":
            self.wd.find_element_by_link_text(value).is_selected()

    # 验证元素是否存在  (返回值是列表)
    def Check_elements(self, type, value1, value2):
        if type == "xpath":
            res = (self.wd.find_element_by_xpath(value1)
                   ).find_elements_by_xpath(value2)
        elif type == "id":
            res = (self.wd.find_element_by_id(value1)
                   ).find_elements_by_id(value2)
        elif type == "name":
            res = (self.wd.find_element_by_name(value1)
                   ).find_elements_by_name(value2)
        elif type == "link_text":
            res = (self.wd.find_element_by_link_text(value1)
                   ).find_elements_by_link_text(value2)
        elif type == "partial_link_text":
            res = (self.wd.find_element_by_partial_link_text(value1)
                   ).find_elements_by_partial_link_text(value2)
        elif type == "css":
            res = (self.wd.find_element_by_css_selector(value1)
                   ).find_elements_by_css_selector(value2)
        return res

    # # 获取下拉框的文本的值
    #
    # def Get_texts(self, type, value1, value2):
    #     if type == "xpath":
    #         text = (self.wd.find_element_by_xpath(value1)).find_element_by_xpath(value2).text
    #         return text
    #     elif type == "name":
    #         text = (self.wd.find_element_by_name(value1)).find_element_by_name(value2).text
    #         return text
    #     elif type == "link_text":
    #         text = (self.wd.find_element_by_link_text(value1)).find_element_by_link_text(value2).text
    #         return text
    #     elif type == "class_name":
    #         text = (self.wd.find_element_by_class_name(value1)).find_element_by_class_name(value2).text
    #         return text
    #     elif type == "id":
    #         text = (self.wd.find_element_by_id(value1)).find_element_by_id(value2).text
    #         return text
    #     elif type == "css":
    #         text = ((self.wd.find_element_by_css_selector(value1)).find_element_by_css(value2)).text
    #         return text

    def ran_num(self, num):
        ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=num))
        return ran_str

    def Screenshots(self):
        """

        :return: 以当前时间为截图名称
        """
        self.wd.save_screenshot(
            r"D:\errorpng\{}.png".format(re.sub("\D", "", (datetime.now().strftime('%Y-%m-%d %H:%M:%S')))))


if __name__ == '__main__':
    wo = Tool_Element()
