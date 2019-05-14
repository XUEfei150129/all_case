#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/5/13 18:59
# @Author : XueFei
from login_api.Login import Login
from Mysql_db.connect_db import OperationMysql
from method.checkmethod import isJson, checktype
from login_api.Read_Ini import Read_Ini
import string
import random
import json
import requests
import time
import decimal
import re
from datetime import datetime
from pprint import pprint
from time import sleep


def Login():
    url = "http://api.zuul.uat.znlhzl.cn"
    result = requests.get(
        "http://api.zuul.uat.znlhzl.cn/api-sso/api/v1/login?name=15050563690&pwd=88888888",
        timeout=10,
    )
    token = result.json()["data"]["token"]
    return token


def load():
    headers = {
        'Content-Type': 'application/json',
        "X-Auth-Token": token,
    }
    values = {
        "contractStatus": 1,
        "contractTargetCode": "CUST112622",
        "contractTargetName": "薛飞",
        "contractTargetType": 1,
        "licenseFilePath": [],
        #"filePath": ["merchant/11magazine-unlock-01-2.3.1344-_BE5A591A1269887033F146E7A5754D0C.jpg"],
        "filePath": ["{}".format(("1.png", open("d:\\1.png", "rb"), "image/png"))],
        "orderCode": "ZNLHZL-2019-28905",
        "orderSignPersonVoList": [
            {
                "idcard": "320882198810292412",
                "mobile": "15151864744",
                "name": "薛飞",
                "images": [
                    "lpt/0/1108990759794774016.jpg",
                    "lpt/1/1108990760113541120.jpg"]}]}

    values = json.dumps(values)
    result = requests.post(
        "http://api.zuul.uat.znlhzl.cn/api-oms/api/order/sign/save",
        data=values,
        headers=headers)
    pprint(result.json())


token = Login()

load()
