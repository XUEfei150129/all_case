# coding=utf-8
from login_api.Read_Ini import Read_Ini
import unittest
import requests
import json


class Login(unittest.TestCase):

    url = "http://api.zuul.autotest.znlhzl.org"  # 不同环境测试，需要改url

    def test_Login(self, name):
        result = requests.get(
            "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                self.url,
                Read_Ini().get_value(name)[0],
                Read_Ini().get_value(name)[1],
                timeout=10),
        )
        return result.json()["data"]["token"]


class LoginShort(unittest.TestCase):  # 小程序
    url = "http://api.zuul.autotest.znlhzl.org"  # 不同环境测试，需要改url

    def test_Login_short(self, name):
        headers = {
            'Content-Type': 'application/json',
            "charset": "UTF - 8"
        }
        values = {
            "password": Read_Ini().get_value(name)[1],
            "mobile": Read_Ini().get_value(name)[0]
        }
        values = json.dumps(values)
        result = requests.post(
            "{}/api-sso/api/v2/pc/creditUser/custLogin".format(
                self.url), data=values, headers=headers)
        return result.json()["data"]["userInfo"]["tokenId"]







