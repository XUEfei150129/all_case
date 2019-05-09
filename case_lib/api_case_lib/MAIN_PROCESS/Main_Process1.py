#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/3/27 9:52
# @Author : XueFei
from login_api.Login import Login, LoginShort
from Mysql_db.connect_db import OperationMysql
from method.checkmethod import isJson, checktype
from login_api.Read_Ini import Read_Ini
import string
import random
import json
import requests
import time
from datetime import datetime
from pprint import pprint
from time import sleep
import re


class Main_Process(LoginShort, Login):
    """
    主流程测试用例
    """

    num_order = 1  # 订单设备数据
    enter_order = 1  # 发起进场的设备数量
    cCode = "CUST112589"  # 创建订单是要选的客户
    devhours = 107  # 设备使用时长,每次运行的时候需要填一个大于上一次的数字

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
        nowT = re.sub(r"\D", "", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        global projectname
        projectname = "auto" + nowT  # 生成一个以当前时间命名的工程名
        values = {
            "projectFullName": "{}".format(projectname),
            "address": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
            "longitude": "118.7790948694178",
            "latitude": "31.991562671134364",
            "filePath": [],
            "projectTrade": 1,
            "constructionStage": 0,
            "infoSource": 1,
            "forkCount": 1,
            "armCount": 1,
            "custCode": "",
            "creatFlag": 1}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-crm/api/v2/crm/project/add",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>生成的工程单号是：{}>>>>>>>>>>".format(result.json()["data"]))
        return result.json()["data"]

    def test_crmCustomerAndProject(self):
        """
        工程关联客户
        :return:
        """
        pcode = self.test_addproject()  # 获取到生成的工程单号
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {"custCode": self.cCode, "projectCode": "{}".format(pcode)}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-crm/api/v2/crm/project/crmCustomerAndProject",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>工程关联客户成功>>>>>>>>>>")

    def test_projectListUnderCust(self):
        """
        获取用户关联的工程里的第一个工程，即为刚创建的工程
        :return:
        """
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10,
            "custCode": "{}".format(self.cCode),
            "projectName": ""
        }
        result = requests.get(
            self.url +
            "/api-crm/api/v2/crm/project/projectListUnderCust",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        firstpName = result.json()["data"]["list"][0]["projectName"]
        firstpCode = result.json()["data"]["list"][0]["projectCode"]
        print(
            ">>>>>>>>>>成功获取到刚创建的工程名:{};工程id:{}>>>>>>>>>>".format(
                firstpName,
                firstpCode))
        return [firstpName, firstpCode]

    def test_ceratorder(self):
        '''调用端：移动端
            应用访问地址：
            平台应用场景：客户经理在订单管理模块创建订单
            "isTransport": "1"是设备的台数
        '''
        self.test_crmCustomerAndProject()  # 创建工程并关联客户
        global pnaemcode
        pnaemcode = self.test_projectListUnderCust()  # 获取创建的工程名和工程id
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        nowtime = datetime.now().strftime('%Y-%m-%d')
        values = {"createName": "薛飞",
                  "customerName": "薛飞",
                  "storeCode": "DEP18020003",
                  "customerCode": "{}".format(self.cCode),
                  "enterpriseCode": "",
                  "enterpriseName": "",
                  "estimatePriceUpdateFlag": 0,
                  "orderInfo": {"projectName": "{}".format(pnaemcode[0]),
                                "fileid": "",
                                "lon": "118.7790948694178",
                                "estimatePrice": "500",
                                "jobAddress": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                                "balanceTypeName": "后付",
                                "projectCode": "{}".format(pnaemcode[0]),
                                "businessPolicyChangeReason": "",
                                "kilometre": "50",
                                "jobType": "1",
                                "jobTypeName": "钢结构",
                                "balanceType": 3,
                                "lat": "31.991562671134364",
                                "city": "",
                                "accountPeriod": "30",
                                "isTransport": "{}".format(self.num_order),
                                "creditLevel": "A",
                                "creditScore": "",
                                "remarks": ""},
                  "orderCode": "",
                  "orderDevList": [{"monthInfoFee": "0",
                                    "rentPriceCommission": "87",
                                    "categoryName": "剪叉",
                                    "minDayPrice": "130",
                                    "warehouseName": "南京仓",
                                    "days": "30",
                                    "shighNameAndCategoryName": "10米 剪叉",
                                    "maxMonthPrice": "4350",
                                    "guidePriceCommission": "87",
                                    "category": "FORK",
                                    "shigh": "10",
                                    "minMonthPrice": "2610",
                                    "shighName": "10米",
                                    "monthGuidePrice": "2900",
                                    "useDate": "{}".format(nowtime),
                                    "monthRentPrice": "2900",
                                    "warehouseCode": "DEP1802000106",
                                    "dayGuidePrice": "145",
                                    "kzCount": "17",
                                    "num": "{}".format(self.num_order),
                                    "maxDayPrice": "435",
                                    "shighAndCategory": "10 FORK",
                                    "dayRentPrice": "145",
                                    "dayInfoFee": "0"}]}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-oms/api/order/create",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(
            "订单创建成功！",
            result.json()['meta']["message"],
            msg="验证订单是否创建成功")
        print(">>>>>>>>>>订单创建成功>>>>>>>>>>")

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
        result = requests.get(
            self.url +
            "/api-wfe/api/proc/selectNeed",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        bizNo = result.json()["data"]["list"][0]["bizNo"]
        instNo = result.json()["data"]["list"][0]["instNo"]
        print(">>>>>>>>>>bizNo:{},instNo:{} 获取成功>>>>>>>>>>".format(bizNo, instNo))
        return [bizNo, instNo]

    def test_submitAuditInst(self):
        """
        客户经理发起订单
        城市经理审批运订单流程
        :return:
        """
        self.test_ceratorder()  # 创建订单
        info = self.test_needlist()  # 获取订单信息
        global bizNo
        bizNo = info[0]
        instNo = info[1]
        token = self.test_Login("huangfei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "status": 1,
            "submitUserCode": "USER180301007",
            "submitUserName": "黄飞",
            "bizNo": bizNo,
            "updateUserCode": "USER180301007",
            "updateUserName": "黄飞",
            "instNo": instNo,
            "comment": "测试"}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-wfe/api/proc/submitAuditInst",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>城市经理审核通过>>>>>>>>>>")

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
        values = {"contractStatus": 1,
                  "contractTargetCode": "CUST110359",
                  "contractTargetName": "薛飞",
                  "contractTargetType": 1,
                  "licenseFilePath": [],
                  "filePath": ["{}".format({"localUrl": (None,
                                                         "1.png"),
                                            "imgFile": ("1.png",
                                                        open(r"d:\1.png",
                                                             "rb"),
                                                        "image/png")})],
                  "orderCode": bizNo,
                  "orderSignPersonVoList": [{"idcard": "320882198810292412",
                                             "mobile": "15151864744",
                                             "name": "薛飞",
                                             "images": ["lpt/0/1108990759794774016.jpg",
                                                        "lpt/1/1108990760113541120.jpg"]}]}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-oms/api/order/sign/save",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(
            '签约信息保存成功',
            result.json()['meta']['message'],
            msg="验证签约信息保存成功")
        print(">>>>>>>>>客户经理上传合同成功>>>>>>>>>>")
        print(">>>>>>>>>>让服务器休息5秒钟>>>>>>>>>>")
        sleep(5)
        print(">>>>>>>>>>好，继续工作>>>>>>>>>>")

    def test_list(self):
        """
        合同管理专员获取最新的合同,
        :return:第一个订单号
        """
        token = self.test_Login("chenyanyan")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(
            self.url +
            "/api-wfe/api/proc/selectNeed",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        return result.json()['data']['list'][0]['instNo']

    def test_ubmitAuditInst(self):
        """
        合同管理专员审批通过最新的合同
        :return:
        """
        self.test_ordersignsave()
        instNo = self.test_list()
        token = self.test_Login("chenyanyan")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "status": 1,
            "submitUserCode": "USER1804001207",
            "submitUserName": "陈艳艳",
            "bizNo": bizNo,
            "updateUserCode": "USER1804001207",
            "updateUserName": "陈艳艳",
            "instNo": instNo,
            "comment": "测试"}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-wfe/api/proc/submitAuditInst",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>合同专员审核合同通过>>>>>>>>>>")

    def test_createDevEnter(self):
        self.test_ubmitAuditInst()
        token = self.test_Login("xuefei")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M')
        values = {"orderCode": bizNo,
                  "isAdd": "0",
                  "balanceTypeName": "后付",
                  "addBailFee": "",
                  "warehouseCode": "DEP1802000106",
                  "balanceType": "3",
                  "serDevEnterDemandList": [{"lockedNum": "1",
                                             "notEnterNumTe": "1",
                                             "storeCode": "DEP18020003",
                                             "categoryName": "剪叉",
                                             "warehouseName": "南京仓",
                                             "days": "30",
                                             "orderDevCode": "DEV190517738",
                                             "addNum": 0,
                                             "category": "FORK",
                                             "isExit": False,
                                             "rentingNum": "14",
                                             "shigh": "10",
                                             "orderDevType": "0",
                                             "shighName": "10米",
                                             "type": "0",
                                             "monthRentPrice": "2900",
                                             "warehouseCode": "DEP1802000106",
                                             "num": "{}".format(self.enter_order),
                                             "stockNum": "20",
                                             "dayRentPrice": "145"}],
                  "warehouseName": "南京仓",
                  "storeCode": "DEP18020003",
                  "storeName": "南京店",
                  "addTransFee": "",
                  "remarks": "",
                  "planQuitDate": "{}".format(nowtime)}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-ser/api/ser/enter/createDevEnter",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>客户经理发起进场成功>>>>>>>>>>")

    def test_jclist(self):
        """
        服务经理获取列表中第一个进程需求
        :return: 进场单号
        """
        token = self.test_Login("zhukuankuan")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "pageNo": 1,
            "pageSize": 10
        }
        result = requests.get(
            self.url +
            "/api-wfe/api/proc/selectNeed",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>进场单号是：{}>>>>>>>>>>".format(
            result.json()["data"]["list"][0]["bizNo"]))
        return result.json()["data"]["list"][0]["bizNo"]

    def test_enterAssign(self):
        """
        服务经理分配进场给服务工程师
        :return:
        """
        self.test_createDevEnter()  # 发起进场，获取第一个进场单
        global fwj
        fwj = self.test_jclist()  # 获取进场单号
        token = self.test_Login("zhukuankuan")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "devEnterCode": fwj,
            "loadingStaff": "USER180301156",
            "loadingStaffName": "江凤余",
            "deliveryStaff": "USER180301156",
            "deliveryStaffName": "江凤余"}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-ser/api/ser/enter/enterAssign",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>服务经理成功分配进场需求>>>>>>>>>>")

    def test_getserDevEnterByCode(self):
        """
        服务工程师验机：先根据进场单号获取devEnterDemandCode的值
        :return:
        """
        token = self.test_Login("jiangfengyu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "devEnterCode": fwj,
        }
        result = requests.get(
            self.url +
            "/api-ser/api/ser/enter/serDevEnterByCode",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        global devEnterDemandCode
        devEnterDemandCode = result.json(
        )["data"]["serDevEnterDemandList"][0]["devEnterDemandCode"]
        print(">>>>>>>>>>成功获取devEnterDemandCode的值：{}".format(devEnterDemandCode))
        return devEnterDemandCode

    def test_selectEnterMatchDev(self):
        """
        根据devEnterDemandCode值，获取第一台设备的出厂编号
        :return:设备的出厂编号
        """
        self.test_getserDevEnterByCode()  # 获取devEnterDemandCode值，这个函数有全局变量
        token = self.test_Login("jiangfengyu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "devEnterDemandCode": devEnterDemandCode,
        }
        result = requests.get(
            self.url +
            "/api-ser/api/ser/enter/selectEnterMatchDev",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        pprint(">>>>>>>>>>成功获取设备的出厂编号：{}>>>>>>>>>>".format(
            result.json()["data"][0]["devCode"]))
        return result.json()["data"][0]["devCode"]

    def test_addEnterMatchDev(self):
        """
        服务工程师选择设备
        这个接口的传参方式是：www-form-urlencoded
        :return:
        """
        self.test_enterAssign()  # 服务经理分配进场给服务工程师
        global devCode
        devCode = self.test_selectEnterMatchDev()  # 获取出厂编号
        token = self.test_Login("jiangfengyu")
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-Auth-Token": token,
        }
        values = {
            "devEnterCode": fwj,  # 进场单号
            "devEnterDemandCode": devEnterDemandCode,  #
            "devCode": devCode  # 出厂编号
        }
        result = requests.post(
            self.url +
            "/api-ser/api/ser/enter/addEnterMatchDev",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        pprint(">>>>>>>>>>选择设备成功,并正常返回devEnterMatchCode：{}>>>>>>>>>>".format(
            result.json()["data"][0]["devEnterMatchCode"]))
        return result.json()["data"][0]["devEnterMatchCode"]

    def test_addone(self):
        """
        为下一个函数服务，每次执行后。数量加1
        :return:
        """
        with open('devhours.txt', "r") as f:
            last_hours = f.read()
        with open('devhours.txt', "w") as f:
            f.write(str(int(last_hours) + 1))
        return int(last_hours)

    def test_enterMatchDev(self):
        """
        将选好的设备验机
        :return:
        """
        dEMC = self.test_addEnterMatchDev()
        last_hours = self.test_addone()
        token = self.test_Login("jiangfengyu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {"devEnterCode": fwj, "devEnterDemandCode": devEnterDemandCode,
                  "devEnterMatchCode": dEMC, "devCode": devCode, "model": "R10", "matchFlg": 0,
                  "hours": int(last_hours),
                  "filePath": ["{}".format(
                      {"localUrl": (None, "2.png"),
                       "imgFile": ("2.png", open(r"d:\2.png", "rb"), "image/png")})],
                  "remarks": "", "checkList": [{"name": "清洁", "value": "正常"}, {"name": "篮筐变形", "value": "正常"},
                                               {"name": "轮胎", "value": "新轮胎"}, {"name": "电量", "value": "电量100%"},
                                               {"name": "电池液位", "value": "正常"}, {"name": "电池", "value": "完好"},
                                               {"name": "400标贴", "value": "完整"}, {"name": "急停开关", "value": "正常"},
                                               {"name": "升降开关", "value": "正常"}, {"name": "钥匙开关", "value": "正常"},
                                               {"name": "深坑限位开关", "value": "正常"}, {"name": "紧急拉线", "value": "正常"},
                                               {"name": "液压油", "value": "正常"}, {"name": "操作手柄", "value": "标签清晰"},
                                               {"name": "地面操作面板", "value": "标签清晰"}, {"name": "GPS", "value": "正常"}]}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-ser/api/ser/enter/enterMatchDev",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        pprint(">>>>>>>>>>服务工程师成功验机>>>>>>>>>>")

    def test_getwarehousecode(self):
        """
        获取仓库code和仓库name
        :return:
        """
        token = self.test_Login("jiangfengyu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {
            "demandType": 1,
            "demandRelationCode": fwj
        }
        result = requests.get(
            self.url +
            "/api-ser/api/v1/transportdemand/queryDemand",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        whCode = result.json()["data"]["warehouseCode"]
        whname = result.json()["data"]["warehouseName"]
        print(
            ">>>>>>>>>>成功获取仓库code：{}和仓库name：{}>>>>>>>>>>".format(
                whCode, whname))
        return [whCode, whname]

    def test_getaftertime(self, n):  # 精确到分钟
        """
        获取当前时间往后的时间
        :param n: 当前时间后的n分钟
        :return: 返回当前时间后的时间，精确当分钟
        """
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
        c = time.strptime(nowtime, "%Y-%m-%d %H:%M:%S")
        timeStamp = int(time.mktime(c))
        timeStamp += (n * 60)
        timeArray = time.localtime(timeStamp)
        aftertime = time.strftime("%Y-%m-%d %H:%M", timeArray)
        return aftertime

    def test_createtransportdemand(self, name="jiangfengyu", cname="江凤余"):
        """
        发起物流需求单
        :param name: 填入配置表里面的名字，用来获取他的手机号码
        :param cname: 中文名
        :return:物流需求单号
        """
        telnum = Read_Ini().get_value(name)[0]  # 获取手机号码
        self.test_enterMatchDev()  # 完成进场验机等工作
        global warehouseinfo
        warehouseinfo = self.test_getwarehousecode()  # 获取仓库信息
        global PlanDeliveryTime
        PlanDeliveryTime = self.test_getaftertime(1)
        token = self.test_Login("jiangfengyu")
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = {"demandCode": "",
                  "demandDeliveryAddress": "江宁区淳化街道茶岗社区104省道",
                  "demandDeliveryAddressLatitude": 31.950859,
                  "demandDeliveryAddressLongitude": 119.014704,
                  "demandDeliveryContactCode": "USER180301156",
                  "demandDeliveryContactName": cname,
                  "demandDeliveryContactMobile": telnum,
                  "demandPlanDeliveryTime": PlanDeliveryTime,
                  "demandPlanReceiptTime": self.test_getaftertime(2),
                  "demandReceiptAddress": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                  "demandReceiptAddressLatitude": 31.991562671134364,
                  "demandReceiptAddressLongitude": 118.7790948694178,
                  "demandReceiptContactCode": "USER180301156",
                  "demandReceiptContactName": cname,
                  "demandReceiptContactMobile": telnum,
                  "demandRelationCode": fwj,
                  "demandType": "1",
                  "warehouseCode": warehouseinfo[0],
                  "warehouseName": warehouseinfo[1],
                  "remarks": "",
                  "devices": [{"category": "FORK",
                               "categoryName": "剪叉",
                               "shigh": "10",
                               "shighName": "10米",
                               "totalAmount": "1",
                               "usedAmount": "1"}]}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-ser/api/v1/transportdemand/create",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(
            "成功",
            result.json()['message'],
            msg="验证'message': 成功,")
        print(
            ">>>>>>>>>>发起物流需求单成功，成功获取到物流需求单号：{}>>>>>>>>>>".format(
                result.json()['data']["code"]))
        return result.json()['data']["code"]

    # 下面是为发起物流运输单做准备
    def test_queryTransportOrder(self):
        """
        根据物流需求单号获取物流运输单号
        :return:物流运输单号
        """
        global demandCode
        demandCode = self.test_createtransportdemand()  # 获取物流需求单号
        token = self.test_Login("zhuchunjiao")
        headers = {
            "X-Auth-Token": token,
        }
        values = {
            "demandCode": demandCode
        }
        result = requests.get(
            self.url +
            "/api-tms/api/v1/transportorder/queryTransportOrder",
            params=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        pprint(">>>>>>>>>>成功获取物流运输单号：{}>>>>>>>>>>".format(
            result.json()["data"]["transportCode"]))
        return result.json()["data"]["transportCode"]

    def test_getRecommendTrucks(self):
        """
        获取推荐车型，便于发起物流运输单的时候传值
        :return:返回9.6米，13米，17,5米物流车的truckCode，为获取承运商信息做准备
        """
        token = self.test_Login("zhuchunjiao")
        headers = {
            "X-Auth-Token": token,
        }
        values = {
            "demandCode": demandCode
        }
        result = requests.get(
            self.url +
            "/api-tms/api/v1/transportdemand/getRecommendTrucks",
            params=values,
            headers=headers)
        wuliuche96 = result.json()["data"][4]["truckCode"]
        wuliuche13 = result.json()["data"][5]["truckCode"]
        wuliuche175 = result.json()["data"][6]["truckCode"]
        print(
            f">>>>>>>>>>成功获取物流车的truckCode，分别是：{wuliuche96}，{wuliuche13}，{wuliuche175}>>>>>>>>>>")
        return [wuliuche96, wuliuche13, wuliuche175]

    def test_carrierlist(self):
        """
        根据仓库code和车辆信息获取承运商信息
        :return:返回承运商code，和承运商的名字，为发起物流运输单做准备
        """
        global RecommendTrucks_info
        RecommendTrucks_info = self.test_getRecommendTrucks()
        token = self.test_Login("zhuchunjiao")
        headers = {
            "X-Auth-Token": token,
            'Content-Type': 'application/json',
        }
        values = {"warehouseCode": warehouseinfo[0],
                  "truckCodes": RecommendTrucks_info}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-tms/api/v1/carrier/list",
            data=values,
            headers=headers)
        carrierCode = result.json()["data"][0]["carrierCode"]
        carrierName = result.json()["data"][0]["carrierName"]
        print(
            ">>>>>>>>>>成功获取到承运商code：{}，和承运商的名字：{}>>>>>>>>>>".format(
                carrierCode,
                carrierName))
        return [carrierCode, carrierName]

    def test_calcMileage(self):
        """
        点击导航服务，获取公里数
        :return: 公里数
        """
        token = self.test_Login("zhuchunjiao")
        headers = {
            "X-Auth-Token": token,
            'Content-Type': 'application/json',
        }
        values = {"plateNumber": "苏A",
                  "isMerged": False,
                  "recommendedTruckCodes": RecommendTrucks_info,
                  "navigationType": "2",
                  "navigationRules": [],
                  "positions": [{"demandCode": demandCode,
                                 "address": "江宁区淳化街道茶岗社区104省道",
                                 "latitude": "31.950859",
                                 "longitude": "119.014704",
                                 "kilometers": 0,
                                 "order": "1",
                                 "type": "0",
                                 "mergedCodes": None,
                                 "demandHandTypes": None},
                                {"demandCode": demandCode,
                                 "address": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                                 "latitude": "31.991563",
                                 "longitude": "118.779095",
                                 "kilometers": 0,
                                 "order": "2",
                                 "type": "1",
                                 "mergedCodes": None,
                                 "demandHandTypes": None}]}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-tms/api/v1/transportorder/calcMileage",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        pprint(">>>>>>>>>>成功获取到公里数：{}>>>>>>>>>>".format(
            result.json()["data"]["paths"][1]["kilometers"]))
        return result.json()["data"]["paths"][1]["kilometers"]

    def test_freightcalculate(self):
        """
        获取推荐运费
        :return:
        """
        global transportCode  # 物流运输单单号
        transportCode = self.test_queryTransportOrder()  # 流程进展到：发起物流需求单
        global codeandname
        codeandname = self.test_carrierlist()  # 获取承运商信息
        global kilometers
        kilometers = self.test_calcMileage()  # 获取公里数
        token = self.test_Login("zhuchunjiao")
        headers = {
            "X-Auth-Token": token,
            'Content-Type': 'application/json',
        }
        values = {"transportCode": transportCode,
                  "originalDemandCode": demandCode,
                  "kilometers": kilometers,
                  "carrierCode": codeandname[0],
                  "carrierName": codeandname[1],
                  "demands": [{"demandCode": demandCode,
                               "demandDeliveryAddress": "江宁区淳化街道茶岗社区104省道",
                               "demandDeliveryAddressLatitude": 31.950859,
                               "demandDeliveryAddressLongitude": 119.014704,
                               "demandReceiptAddress": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                               "demandReceiptAddressLatitude": 31.991563,
                               "demandReceiptAddressLongitude": 118.779095,
                               "demandType": "1",
                               "kilometers": "0",
                               "demandRelationCode": fwj,
                               "devices": [{"category": "FORK",
                                            "categoryName": "剪叉",
                                            "shigh": "10",
                                            "shighName": "10米",
                                            "usedAmount": "1"}]}],
                  "positions": [{"demandCode": demandCode,
                                 "address": "江宁区淳化街道茶岗社区104省道",
                                 "latitude": "31.950859",
                                 "longitude": "119.014704",
                                 "kilometers": 0,
                                 "order": "1",
                                 "type": "0",
                                 "mergedCodes": [],
                                 "demandHandTypes": [{"demandCode": demandCode,
                                                      "type": "0",
                                                      "orderIndex": 1}]},
                                {"demandCode": demandCode,
                                 "address": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                                 "latitude": "31.991563",
                                 "longitude": "118.779095",
                                 "kilometers": kilometers,
                                 "order": "2",
                                 "type": "1",
                                 "mergedCodes": [],
                                 "demandHandTypes": [{"demandCode": demandCode,
                                                      "type": "1",
                                                      "orderIndex": 2}]}],
                  "truckCodes": RecommendTrucks_info}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-tms_calc/api/tms/calc/freight/calculate",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>成功获取推荐运费：{}>>>>>>>>>>".format(
            result.json()["data"]["freightRecommended"]))
        return result.json()["data"]["freightRecommended"]



    def test_createtransportorder(self):
        """
        创建物流运输单
        :return:
        """
        freightRecommended = self.test_freightcalculate()  # 流程进展到发起物流需求单，返回推荐运费
        token = self.test_Login("zhuchunjiao")
        headers = {
            "X-Auth-Token": token,
            'Content-Type': 'application/json',
        }
        values = {"transportCode": transportCode,
                  "carrierCode": codeandname[0],
                  "carrierName": codeandname[1],
                  "planDeliveryTime": PlanDeliveryTime,
                  "freightRecommended": freightRecommended,
                  "freightPayable": freightRecommended,
                  "dockFee": "0.00",
                  "kilometers": kilometers,
                  "originalDemandCode": demandCode,
                  "reasonForFreightModified": "",
                  "remarks": "",
                  "plateNumber": "苏A",
                  "takeDeliveryTime": self.test_getaftertime(91),  # 精确到分钟

                  "navigationType": "2",
                  "recommendedTruckCodes": RecommendTrucks_info,
                  "demands": [{"demandCode": demandCode,
                               "demandDeliveryAddress": "江宁区淳化街道茶岗社区104省道",
                               "demandDeliveryAddressLatitude": 31.950859,
                               "demandDeliveryAddressLongitude": 119.014704,
                               "demandReceiptAddress": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                               "demandReceiptAddressLatitude": 31.991563,
                               "demandReceiptAddressLongitude": 118.779095,
                               "demandType": "1",
                               "kilometers": "0",
                               "demandRelationCode": fwj,
                               "devices": [{"category": "FORK",
                                            "categoryName": "剪叉",
                                            "shigh": "10",
                                            "shighName": "10米",
                                            "usedAmount": "1"}]}],
                  "positions": [{"demandCode": demandCode,
                                 "address": "江宁区淳化街道茶岗社区104省道",
                                 "latitude": "31.950859",
                                 "longitude": "119.014704",
                                 "kilometers": 0,
                                 "order": "1",
                                 "type": "0",
                                 "mergedCodes": [],
                                 "demandHandTypes": [{"demandCode": demandCode,
                                                      "type": "0",
                                                      "orderIndex": 1}]},
                                {"demandCode": demandCode,
                                 "address": "江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府",
                                 "latitude": "31.991563",
                                 "longitude": "118.779095",
                                 "kilometers": kilometers,
                                 "order": "2",
                                 "type": "1",
                                 "mergedCodes": [],
                                 "demandHandTypes": [{"demandCode": demandCode,
                                                      "type": "1",
                                                      "orderIndex": 2}]}],
                  "navigationRules": []}
        values = json.dumps(values)
        result = requests.post(
            self.url +
            "/api-tms/api/v1/transportorder/create",
            data=values,
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        print(">>>>>>>>>>成功创建物流运输单>>>>>>>>>>".format(result.json()))
