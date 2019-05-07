#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/5/5 19:37
# @Author : XueFei

# coding=utf-8
from login_api.Login import Login, LoginShort
from Mysql_db.connect_db import OperationMysql
from method.checkmethod import isJson, checktype
import string
import random
import json
import requests
from pprint import pprint


class Dev_Life(Login, LoginShort):
    def test_sysDictList(self):
        '''调用端：web
            应用访问地址：/#/DMS/sysDictList
            平台应用场景：设备生命周期管理下拉框
        '''
        token = self.test_Login("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        result = requests.get(self.url + "/zms/api-vip/sysDictList", headers=headers)
        print(result.json())
