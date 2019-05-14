#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/5/13 13:41
# @Author : XueFei


from login_api.Read_Ini import Read_Ini
import unittest
import requests
import json


class Login(unittest.TestCase):

    def test_Login(self, env, name):
        if env == "uat":
            self.url = "http://uatapi.znlhzl.cn"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "uatzms":
            self.url = "https://uatzms.znlhzl.cn"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "sal":
            self.url = "http://sit.sal.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "salzms":
            self.url = "http://sit.sal.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "dms":
            self.url = "http://sit.dms.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "dmszms":
            self.url = "http://sit.dms.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "sev":
            self.url = "http://sit.sev.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "sevzms":
            self.url = "http://sit.sev.zms.znlhzl.org"
            result = requests.get(
                "{}/zms//api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "lgt":
            self.url = "http://sit.lgt.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "lgtzms":
            self.url = "http://sit.lgt.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "iot":
            self.url = "http://sit.iot.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "iotzms":
            self.url = "http://sit.iot.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "fin":
            self.url = "http://sit.fin.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "finzms":
            self.url = "http://sit.fin.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "bi":
            self.url = "http://sit.bi.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "bizms":
            self.url = "http://sit.bi.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "opr":
            self.url = "http://sit.opr.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "oprzms":
            self.url = "http://sit.opr.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "crd":
            self.url = "http://sit.crd.api.znlhzl.org"
            result = requests.get(
                "{}/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "crdzms":
            self.url = "http://sit.crd.zms.znlhzl.org"
            result = requests.get(
                "{}/zms/api-sso/api/v1/login?name={}&pwd={}".format(
                    self.url,
                    Read_Ini().get_value(name)[0],
                    Read_Ini().get_value(name)[1],
                    timeout=10),
            )
            token = result.json()["data"]["token"]
        elif env == "xcx":
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
            token = result.json()["data"]["userInfo"]["tokenId"]
        return token

