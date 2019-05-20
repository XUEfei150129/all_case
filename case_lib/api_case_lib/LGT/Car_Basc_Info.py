# coding=utf-8
from login_api.Login import Login
from Mysql_db.connect_db import OperationMysql
from method.checkmethod import isJson, checktype
import string
import random
import json
import requests
from pprint import pprint


class Car_Basc_Info(Login):
    def test_getIndexMenuAndButton(self):
        '''调用端：web
            应用访问地址：/#/LGT/carBaseInfo
            平台应用场景：进入物流管理，点击车辆基本信息
        '''
        token = self.test_Login("autozms", "薛飞")
        headers = {
            "X-Auth-Token": token,
        }
        restype = {
            'data': {'id': 'str', 'username': 'str', 'name': 'str', 'description': 'NoneType', 'image': 'NoneType',
                     'menus': 'list', 'elements': 'list'}, 'message': 'str', 'success': 'bool', 'errCode': 'int'}
        result = requests.get(self.url + "/zms/api-sso/api/v1/getIndexMenuAndButton", headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual(restype, checktype(result.json()), msg='返回值参数类型验证')

    def test_addDeleteTruck(self):
        '''调用端：web
            应用访问地址：#/LGT/carBaseInfo
            平台应用场景：添加/删除车辆信息
        '''
        token = self.test_Login("uatzms", "薛飞")
        ran_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        values = {"truckPlateNumber": "浙{}".format(ran_str),
                  "source": "1",
                  "truckTypeValue": "1",
                  "truckWeightTypeValue": "3",
                  "powerTypeValue": "1",
                  "brand": "",
                  "truckLoad": "2",
                  "weight": "2",
                  "length": "2",
                  "truckWidth": "2",
                  "height": "2",
                  "axisValue": "3",
                  "vin": "",
                  "ein": "",
                  "vdl": ""}
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = json.dumps(values)
        result = requests.post(self.url + "/api-tms/api/v1/bd/truck/addTruck", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual("成功", result.json()['message'], msg="验证新增车辆是否成功")
        # 删除添加的车辆信息，避免污染数据环境
        Truckcode = result.json()["data"]['truckCode']
        values = {"codes": ['{}'.format(Truckcode)]}
        values = json.dumps(values)
        result = requests.post(self.url + "/api-tms/api/v1/bd/truck/deleteTrucks", data=values, headers=headers)
        self.assertEqual("成功", result.json()['message'], msg="验证删除车辆是否成功")

    def test_updateTruck(self):
        '''调用端：web
            应用访问地址：#/LGT/carBaseInfo
            平台应用场景：修改车辆信息
        '''
        token = self.test_Login("uatzms", "薛飞")
        values = {"truckPlateNumber": "冀A1T2C6", "source": "1", "truckTypeValue": "1", "truckWeightTypeValue": "3",
                  "powerTypeValue": "1", "brand": "", "truckLoad": "4.5", "weight": "3", "length": "5.95",
                  "truckWidth": "2.4", "height": "2.4", "axisValue": "2", "vin": "", "ein": "", "vdl": "",
                  "truckCode": "TRUCK2019000019", "truckType": "3T清障车", "truckWeightType": "中型货车", "axis": "2轴",
                  "powerType": "燃油", "sourceName": "外包", "creator": "", "createDate": "", "updater": "",
                  "updateDate": ""}
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        restype = {'data': 'bool', 'message': 'str', 'errCode': 'int', 'success': 'bool'}
        values = json.dumps(values)
        result = requests.post(self.url + "/api-tms/api/v1/bd/truck/updateTruck", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual(True, result.json()['data'], msg="验证'data': True,")
        self.assertEqual(restype, checktype(result.json()), msg='返回值参数类型验证')

    def test_SearchTruck(self):
        '''调用端：web
            应用访问地址：#/LGT/carBaseInfo
            平台应用场景：搜索车辆信息
        '''
        token = self.test_Login("uatzms", "薛飞")
        values = {"pageNo": "1",
                  "pageSize": "20",
                  "truckPlateNumber": "冀A1T2C6",
                  "truckType": "",
                  "truckBelong": "",
                  "truckLoad": ""
                  }
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        restype = {
            'data': {'searchKey': 'NoneType', 'pageNum': 'int', 'pageSize': 'int', 'total': 'int', 'pages': 'int',
                     'list': 'list', 'firstPage': 'bool', 'lastPage': 'bool'}, 'message': 'str', 'errCode': 'int',
            'success': 'bool'}
        result = requests.get(self.url + "/api-tms/api/v1/bd/truck/loadTrucks", params=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual("3T清障车", result.json()['data']["list"][0]["truckType"], msg="验证车型为3T3T清障车")
        self.assertEqual(restype, checktype(result.json()), msg='返回值参数类型验证')

    def test_transportcreat(self):
        '''调用端：移动端
            应用访问地址：
            平台应用场景：发起物流运输单
        '''
        token = self.test_Login("江凤余")
        values = {"demandCode": "", "demandDeliveryAddress": "江宁区淳化街道茶岗社区104省道",
                  "demandDeliveryAddressLatitude": 31.950859, "demandDeliveryAddressLongitude": 119.014704,
                  "demandDeliveryContactCode": "USER180301156", "demandDeliveryContactName": "江凤余",
                  "demandDeliveryContactMobile": "18900001156", "demandPlanDeliveryTime": "2019-03-26 11:59",
                  "demandPlanReceiptTime": "2019-03-26 13:00",
                  "demandReceiptAddress": "江苏省南京市雨花台区中国南京软件谷郁金香路25号南京(雨花)国际软件外包产业园",
                  "demandReceiptAddressLatitude": 31.9837794, "demandReceiptAddressLongitude": 118.779574,
                  "demandReceiptContactCode": "USER180301156", "demandReceiptContactName": "江凤余",
                  "demandReceiptContactMobile": "18900001156", "demandRelationCode": "FWJ190360029", "demandType": "1",
                  "warehouseCode": "DEP1802000106", "warehouseName": "南京仓", "remarks": "", "devices": [
                {"category": "FORK", "categoryName": "剪叉", "shigh": "8", "shighName": "8米", "totalAmount": "1",
                 "usedAmount": "1"}]}
        headers = {
            'Content-Type': 'application/json',
            "X-Auth-Token": token,
        }
        values = json.dumps(values)
        result = requests.post(self.url + "/api-ser/api/v1/transportdemand/create", data=values, headers=headers)
        self.assertEqual(True, isJson(jsonstr=result), msg='判断返回值是否为json格式')
        self.assertEqual(0, result.json()['errCode'], msg="验证'errCode': 0,")
        self.assertEqual(True, result.json()['success'], msg="验证'success': True,")
        self.assertEqual("3T清障车", result.json()['data']["list"][0]["truckType"], msg="验证车型为3T3T清障车")


"""
验证分3步走
1.最基础的验证状态码+json格式
2.验证数据返回值格式，为了避免返回值参数丢失导致功能不可用的情况----这种情况一般是研发直接修改接口导致的，与底层代码没有关系
3.第三部验证返回值数据，这种需要选择性去验证，要理清楚接口的每个返回值参数的意义----因为验证的太多，代码稍微一改就会失败，验证太少发现不了问题
要结合业务场景去断言



消息体   #前3种最常见，决定消息体是什么格式，通常早消息头里面有一个字段根器对应的叫：Content-Type(消息提的格式)
    application/x-www-form-urlencoded      #Content-Type；application/x-www-form-urlencoded，跟URL里面用&隔开键值对一样。view source可以查看原始的，原始的Unicode转码的，只是把位置移到消息体里面了
    application/json(序列化）#json和xml都是一种数据的表现形式。结构比较复杂的数据可以用json来传输
    application/xml
    multipart/form-data




"""
