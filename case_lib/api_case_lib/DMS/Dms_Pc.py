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
    def test_SysDictList(self):
        '''调用端：web
            应用访问地址：/#/DMS/sysDictList
            平台应用场景：设备生命周期管理下拉框
        '''
        token = self.test_Login_DMS("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        restype = {'meta': {'success': 'bool', 'message': 'str'}, 'data': 'list', 'newDate': 'str', 'success': 'bool',
                   'message': 'str', 'errCode': 'int'}
        result = requests.get(self.url + "/zms/api-vip/sysDictList", headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual(restype, checktype(result.json()), msg='返回值参数类型验证')

    def test_GetServiceDynamicDepartInfo(self):
        '''调用端：web
            应用访问地址：/#/DMS/GetServiceDynamicDepartInfo
            平台应用场景：获取部门信息
        '''
        token = self.test_Login_DMS("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        result = requests.get(self.url + "/zms/api-vip/api/dept/getServiceDynamicDepartInfo", headers=headers)
        restype = {'data': {'regionList': 'list', 'storeList': 'list', 'userList': 'list', 'dataAuthFlag': 'bool'},
                   'message': 'str', 'success': 'bool', 'errCode': 'int'}
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual(restype, checktype(result.json()), msg='返回值参数类型验证')

    def test_SerDevLifelist(self):
        '''调用端：web
            应用访问地址：/#/DMS/sysDictList
            平台应用场景：设备列表
        '''
        token = self.test_Login_DMS("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        result = requests.get(
            self.url + "/zms/api-ser/api/dev/lifeCycle/serDevLifelist?regionId=&warehouseCode=&category=&shigh=&brand=&devStatus=&currStatus=&devCode=&selfIdentity=&pageNo=1&pageSize=20",
            headers=headers)
        restype = {'data': {'pageNum': 'int', 'pageSize': 'int', 'total': 'int', 'pages': 'int', 'list': 'list',
                            'isFirstPage': 'bool', 'isLastPage': 'bool'}, 'message': 'str', 'errCode': 'int',
                   'success': 'bool'}
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual(restype, checktype(result.json()), msg='返回值参数类型验证')

    def test_DevInfo(self):
        '''调用端：web
            应用访问地址：/#/DMS/DevInfo
            平台应用场景：设备信息
        '''
        token = self.test_Login_DMS("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        result = requests.get(self.url + "/zms/api-iot/api/iot/alarm/devInfo?devCode=0300209442", headers=headers)
        restype = {'data': {'devCode': 'str', 'selfDevCode': 'NoneType', 'category': 'NoneType', 'categoryName': 'str',
                            'devPic': 'str', 'high': 'str', 'productModel': 'str', 'brand': 'str', 'storehouse': 'str',
                            'leaseStatus': 'int', 'leaseStatusName': 'str', 'purchaseDate': 'str', 'longitude': 'str',
                            'latitude': 'str', 'address': 'str', 'gps': 'str', 'gpsCode': 'str', 'gpsStrength': 'str',
                            'gpsStatus': 'str', 'gsm': 'str', 'simCode': 'str', 'gsmStrength': 'str',
                            'gsmStatus': 'str', 'devStatus': 'str', 'lockStatus': 'str', 'runStatus': 'NoneType',
                            'runDynamic': 'str', 'batteryType': 'str', 'electricQuantity': 'str', 'voltage': 'str',
                            'liquidLevel': 'str', 'platformSize': 'str', 'extension': 'str', 'lenWidHeight': 'str',
                            'platformLoad': 'str', 'deadWeight': 'str', 'certificatePath': 'list',
                            'inspectionPath': 'list', 'insurancePath': 'list'}, 'message': 'str', 'errCode': 'int'}
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(restype, checktype(result.json()), msg='返回值参数类型验证')
        self.assertEqual("成功", result.json()['message'], msg="验证'message': 成功,")

    def test_SerDevEnterAndExitList(self):
        '''调用端：web
            应用访问地址：/#/DMS/serDevEnterAndExitList
            平台应用场景：进退场列表
        '''
        token = self.test_Login_DMS("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        result = requests.get(self.url + "/zms/api-ser/api/dev/work/serDevEnterAndExitList?pageNo=1&pageSize=20&typeArr[]=2&typeArr[]=3&type=2,3&devCode=0300209442", headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual("ok", result.json()['message'], msg="验证'message': ok,")

    def test_AlarmFaultList(self):
        '''调用端：web
            应用访问地址：/#/DMS/alarmFaultList
            平台应用场景：报警故障列表
        '''
        token = self.test_Login_DMS("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        result = requests.get(
            self.url + "/zms/api-iot/api/iot/alarm/alarmFaultList?pageNo=1&pageSize=20&startDate=2019-04-29+00:00:00&endDate=2019-05-06+23:59:59&type=2,3&devCode=0300209442",
            headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual("成功", result.json()['message'], msg="验证'message': 成功,")


    def test_Devorder_List(self):
        '''调用端：web
            应用访问地址：/#/DMS/GetServiceDynamicDepartInfo
            平台应用场景：订单列表
        '''
        token = self.test_Login_DMS("jiangchao")
        headers = {
            "X-Auth-Token": token,
        }
        result = requests.get(self.url + "/zms/api-oms/api/devorder/list?pageNo=1&pageSize=20&devCode=0300209442", headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual("成功", result.json()['message'], msg="验证'message': 成功,")
