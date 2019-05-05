#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/3/27 9:52
# @Author : XueFei
from login_api.Login import Login, LoginShort
from Mysql_db.connect_db import OperationMysql
from method.checkmethod import isJson, checktype
import string
import random
import json
import requests
from datetime import datetime
from pprint import pprint
from time import sleep
import re


class Main_Process(LoginShort, Login):
    """
    主流程测试用例
    """
    # 订单设备数据和发起进场的设备数量一致
    num_order = 1
    enter_order = 1

    def test_addproject(self):
        """
        创建工程
        :return: 返回值为工程号
        """
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        nowT = re.sub("\D", "", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        projectname = "auto" + nowT  # 生成一个以当前时间命名的工程名
        values = {"projectFullName": "{}".format(projectname), "address": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                  "longitude": "118.7790948694178", "latitude": "31.991562671134364", "filePath": [], "projectTrade": 1,
                  "constructionStage": 0, "infoSource": 1, "forkCount": 1, "armCount": 1, "custCode": "",
                  "creatFlag": 1}
        values = json.dumps(values)
        result = requests.post(self.url + "/api-crm/api/v2/crm/project/add", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print("生成的工程单号是：{}".format(result.json()["data"]))
        return result.json()["data"]

    def test_ceratorder(self):
        '''调用端：移动端
            应用访问地址：
            平台应用场景：客户经理在订单管理模块创建订单
            "isTransport": "1"是设备的台数
        '''
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        nowtime = datetime.now().strftime('%Y-%m-%d')
        values = {"createName": "薛飞", "customerName": "薛飞", "storeCode": "DEP18020003", "customerCode": "CUST110359",
                  "enterpriseCode": "", "enterpriseName": "", "estimatePriceUpdateFlag": 0,
                  "orderInfo": {"projectName": "测试一下", "fileid": "", "lon": "118.780588", "estimatePrice": "200",
                                "jobAddress": "江苏省南京市雨花台区中国南京软件谷郁金香路25号南京(雨花)国际软件外包产业园", "balanceTypeName": "后付",
                                "projectCode": "PROJECT101179", "businessPolicyChangeReason": "测试", "kilometre": "100",
                                "jobType": "1", "jobTypeName": "钢结构", "balanceType": 3, "lat": "31.983009", "city": "",
                                "accountPeriod": "30", "isTransport": "{}".format(self.num_order), "creditLevel": "A",
                                "creditScore": "",
                                "remarks": ""}, "orderCode": "", "orderDevList": [
                {"monthInfoFee": "0", "rentPriceCommission": "75", "categoryName": "剪叉", "minDayPrice": "100",
                 "warehouseName": "南京仓", "days": "30", "shighNameAndCategoryName": "6米 剪叉", "maxMonthPrice": "3750",
                 "guidePriceCommission": "75", "category": "FORK", "shigh": "6", "minMonthPrice": "2000",
                 "shighName": "6米", "monthGuidePrice": "2500", "useDate": "{}".format(nowtime),
                 "monthRentPrice": "2500",
                 "warehouseCode": "DEP1802000106", "dayGuidePrice": "125", "kzCount": "10",
                 "num": "{}".format(self.num_order),
                 "maxDayPrice": "375", "shighAndCategory": "6 FORK", "dayRentPrice": "125", "dayInfoFee": "0"}]}
        values = json.dumps(values)
        result = requests.post(self.url + "/api-oms/api/order/create", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual("订单创建成功！", result.json()['meta']["message"], msg="验证订单是否创建成功")
        print("订单创建成功")

    def test_needlist(self):
        '''调用端：移动端
        应用访问地址：
        平台应用场景：客户经理创建订单之后，店长刷新代办审批，在响应中获取到相应的数据
        '''
        token = self.test_Login("huangfei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(self.url + "/api-wfe/api/proc/selectNeed", params=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        bizNo = result.json()["data"]["list"][0]["bizNo"]
        instNo = result.json()["data"]["list"][0]["instNo"]
        print(bizNo, instNo + " 获取成功")
        return [bizNo, instNo]

    def test_submitAuditInst(self):
        """
        客户经理发起订单
        城市经理审批运订单流程
        :return:
        """
        self.test_ceratorder()  # 创建订单
        info = self.test_needlist()
        global bizNo
        bizNo = info[0]
        instNo = info[1]
        token = self.test_Login("huangfei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {"status": 1, "submitUserCode": "USER180301007", "submitUserName": "黄飞", "bizNo": bizNo,
                  "updateUserCode": "USER180301007", "updateUserName": "黄飞",
                  "instNo": instNo, "comment": "测试"}
        values = json.dumps(values)
        result = requests.post(self.url + "/api-wfe/api/proc/submitAuditInst", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print("城市经理审核通过")

    def test_ordersignsave(self):
        """
        客户经理上传合同

        :return:
        """
        self.test_submitAuditInst()
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {"contractStatus": 1, "contractTargetCode": "CUST110359", "contractTargetName": "薛飞",
                  "contractTargetType": 1, "licenseFilePath": [],
                  "filePath": ["{}".format(
                      {"localUrl": (None, "1.png"),
                       "imgFile": ("1.png", open(r"d:\1.png", "rb"), "image/png")})],
                  "orderCode": bizNo,
                  "orderSignPersonVoList": [{"idcard": "320882198810292412", "mobile": "15151864744", "name": "薛飞",
                                             "images": ["lpt/0/1108990759794774016.jpg",
                                                        "lpt/1/1108990760113541120.jpg"]}]}
        print(bizNo)
        values = json.dumps(values)
        result = requests.post(self.url + "/api-oms/api/order/sign/save", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual('签约信息保存成功', result.json()['meta']['message'], msg="验证签约信息保存成功")
        print("客户经理上传合同成功")

    def test_list(self):
        """
        合同管理专员获取最新的合同,
        :return:第一个订单号
        """
        token = self.test_Login("qinchuanxiu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(self.url + "/api-wfe/api/proc/selectNeed", params=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        # pprint(result.json()['data']['list'])
        return result.json()['data']['list'][0]['instNo']

    def test_list0(self):
        """
        合同管理专员获取最新的合同
        :return:
        """
        token = self.test_Login("qinchuanxiu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(self.url + "/api-wfe/api/proc/selectNeed", params=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        for i in result.json()['data']['list']:
            print("第{}单号是：{}".format(((result.json()['data']['list']).index(i)) + 1, i["bizNo"]))

    # break
    def test_list1(self):
        """
        合同管理专员获取最新的合同
        :return:
        """
        token = self.test_Login("qinchuanxiu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(self.url + "/api-wfe/api/proc/selectNeed", params=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        # pprint(result.json()['data']['list'][6])
        for i in result.json()['data']['list']:
            if "415" in i["bizNo"]:
                break
            print("销售单号依次是{}：{}".format(((result.json()['data']['list']).index(i)) + 1, i["bizNo"]))

    # 销售单号依次是1：ZNLHZL - 2019 - 28526
    # 销售单号依次是2：REPAIR19032110997
    # 销售单号依次是3：REPAIR19031051006
    # 销售单号依次是4：REPAIR19030781316
    # 销售单号依次是5：REPAIR19031229802

    # continue
    def test_list2(self):
        """
        合同管理专员获取最新的合同
        :return:
        """
        token = self.test_Login("qinchuanxiu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(self.url + "/api-wfe/api/proc/selectNeed", params=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        # pprint(result.json()['data']['list'])
        for i in result.json()['data']['list']:
            if "415" in i["bizNo"]:
                continue
            print("销售单号依次是{}：{}".format(((result.json()['data']['list']).index(i)) + 1, i["bizNo"]))

    # 销售单号依次是1：ZNLHZL - 2019 - 28526
    # 销售单号依次是2：REPAIR19032110997
    # 销售单号依次是3：REPAIR19031051006
    # 销售单号依次是4：REPAIR19030781316
    # 销售单号依次是5：REPAIR19031229802
    # 销售单号依次是7：REPAIR19030360302
    # 销售单号依次是8：REPAIR19030696232
    # 销售单号依次是9：REPAIR19031031734
    # 销售单号依次是10：REPAIR19030967080

    def test_list3(self):
        """
        合同管理专员获取最新的合同
        :return:
        """
        token = self.test_Login("qinchuanxiu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(self.url + "/api-wfe/api/proc/selectNeed", params=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        # pprint(result.json()['data']['list'])
        for i in result.json()['data']['list']:
            if "415" in i["bizNo"]:
                print("销售单号是{}：{}".format(((result.json()['data']['list']).index(i)) + 1, i["bizNo"]))
                break
                # continue      (同break效果一样)

    # 销售单号依次是6：CHA_CONT222

    def test_ubmitAuditInst(self):
        """
        合同管理专员审批通过最新的合同
        :return:
        """
        self.test_ordersignsave()
        instNo = self.test_list()
        token = self.test_Login("qinchuanxiu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {"status": 1, "submitUserCode": "USER180301077", "submitUserName": "秦传秀",
                  "bizNo": bizNo, "updateUserCode": "USER180301077", "updateUserName": "秦传秀",
                  "instNo": instNo, "comment": "测试"}
        values = json.dumps(values)
        result = requests.post(self.url + "/api-wfe/api/proc/submitAuditInst", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print("合同专员审核合同通过")

    def test_createDevEnter(self):
        self.test_ubmitAuditInst()
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M')
        values = {"orderCode": bizNo, "isAdd": "0", "balanceTypeName": "后付", "addBailFee": "",
                  "warehouseCode": "DEP1802000106", "balanceType": "3", "serDevEnterDemandList": [
                {"lockedNum": "1", "notEnterNumTe": "1", "storeCode": "DEP18020003", "categoryName": "剪叉",
                 "warehouseName": "南京仓", "days": "30", "orderDevCode": "DEV190316856", "addNum": 0, "category": "FORK",
                 "isExit": False, "rentingNum": "2", "shigh": "6", "orderDevType": "0", "shighName": "6米", "type": "0",
                 "monthRentPrice": "2500", "warehouseCode": "DEP1802000106", "num": "{}".format(self.enter_order),
                 "stockNum": "6",
                 "dayRentPrice": "125"}], "warehouseName": "南京仓", "storeCode": "DEP18020003", "storeName": "南京店",
                  "addTransFee": "", "remarks": "", "planQuitDate": "{}".format(nowtime)}
        values = json.dumps(values)
        result = requests.post(self.url + "/api-ser/api/ser/enter/createDevEnter", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        pprint(result.json())
        print("客户经理发起进场成功")

    # def test_devGpsPosition(self):
    #     token = self.test_Login("xuefei")
    #     headers = {
    #         'Content-Type': 'application/json',
    #         "X-Auth-Token": token,
    #     }
    #     # values = {
    #     #     "type": 1
    #     # }
    #     # values = json.dumps(values)
    #     result = requests.get(self.url + "/api-sku/api/ims/getDevGpsPosition?type=1", headers=headers)
    #     pprint(result.json())
