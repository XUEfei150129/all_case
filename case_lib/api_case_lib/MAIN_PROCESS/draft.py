#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/3/27 11:39
# @Author : XueFei
from pprint import pprint

# # from datetime import datetimep
#
# a = {"contractStatus":1,"contractTargetCode":"CUST110359","contractTargetName":"薛飞","contractTargetType":1,"licenseFilePath":[],"filePath":["merchant/header_201903271159137001.jpg"],"orderCode":"ZNLHZL-2019-28228","orderSignPersonVoList":[{"idcard":"320882198810292412","mobile":"15151864744","name":"薛飞","images":["lpt/0/1108990759794774016.jpg","lpt/1/1108990760113541120.jpg"]}]}
# pprint(a)


# from datetime import datetime
#
# a = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# print(a)
# 文件上传：content-Type：  multipart/form-data类型
# import requests
#
# class SendFile():
#     def __init__(self, s):
#         self.s = s
#
#     def sendImg(self, jpgpath, jpgname='1.jpg', jpgtype='image/jpeg'):
#
#         # 登录并更新cookies
#         f = open('1.jpg', 'rb')  # 绝对路径
#         url2 = ''
#         body = {
#             'localurl': (None, jpgname),
#             'imgFile': ('1.jpg', open(jpgpath, 'rb'), jpgtype)
#             # 1、绝对路径  2、open('1.jpg', 'rb')  3、content-type的值
#             }
#         # 上传图片的时候，不data和json，用files
#         r = self.s.post(url2, files=body)    # 1、调用全局的s，用self.s   2、files
#         print(r.text)
#         # 上传到服务器，每传一次地址都不一样
#
#         # 解决抛异常
#         try:
#             jpg_url = r.json()['url']   # （相对路径）
#             print(jpg_url)
#             return jpg_url
#
#         except Exception as msg:    # 返回报错信息
#             print('图片上传失败，原因：%s'%msg)   # 打印报错信息
#         #    raise   # 主动抛原始异常
#         #    raise  ··· # 抛出异常内容为：“···”
#             return ''
#
# if __name__=='__main__':
#     s = requests.session()
#     from test.test_009_003_zentaologin import LoginZentao
#     # 调登录方法
#     login = LoginZentao(s)      # 实例化类LoginZentao为对象
#     login.login()
#     # 上传文件
#     send = SendFile(s)      # 把类sendfile()实例化为对象
#     send.sendImg()          # 调用sendfile()里面的sendImg方法
# a = {"contractStatus": 1, "contractTargetCode": "CUST110359", "contractTargetName": "薛飞", "contractTargetType": 1,
#      "licenseFilePath": [], "filePath": ["{}".format(("1.png", open("d:\1.png", "rb"), "image/png"))],
#      "orderCode": "ZNLHZL-2019-28290",
#      "orderSignPersonVoList": [{"idcard": "320882198810292412", "mobile": "15151864744", "name": "薛飞",
#                                 "images": ["lpt/0/1108990759794774016.jpg", "lpt/1/1108990760113541120.jpg"]}]}
# a = {"contractStatus": 1, "contractTargetCode": "CUST110359", "contractTargetName": "薛飞", "contractTargetType": 1,
#      "licenseFilePath": [], "filePath": ["merchant/header_201903290109065091.jpg"], "orderCode": "ZNLHZL-2019-28305",
#      "orderSignPersonVoList": [{"idcard": "320882198810292412", "mobile": "15151864744", "name": "薛飞",
#                                 "images": ["lpt/0/1108990759794774016.jpg", "lpt/1/1108990760113541120.jpg"]}]}
#
#
# values = {"contractStatus": 1, "contractTargetCode": "CUST110359", "contractTargetName": "薛飞",
#           "contractTargetType": 1, "licenseFilePath": [],
#           "filePath": [
#               "{}".format({"localUrl": (None, "1.png"), "imgFile": ("1.png", open(r"d:\1.png", "rb"), "image/png")})],
#           "orderCode": bizNo,
#           "orderSignPersonVoList": [{"idcard": "320882198810292412", "mobile": "15151864744", "name": "薛飞",
#                                      "images": ["lpt/0/1108990759794774016.jpg",
#                                                 "lpt/1/1108990760113541120.jpg"]}]}


# from datetime import datetime
#
# a = datetime.now().strftime('%Y-%m-%d %H:%M')
#
# print(a)

# a = {'data': {'id': 60041, 'revise': 0, 'orderCode': 'ZNLHZL-2019-28348', 'devEnterCode': 'FWJ190360041', 'approvalStatus': None, 'planQuitDate': '2019-03-29 15:17', 'planArriveDate': '2019-03-29 15:17', 'arriveDate': None, 'rentDate': None, 'status': 10, 'delFlag': None, 'fileid': None, 'filePath': None, 'createBy': 'USER1903030886', 'createDate': None, 'updateBy': 'USER1903030886', 'updateDate': None, 'auditStatus': None, 'staff': None, 'serviceStaff': None, 'serviceStaffName': None, 'staffPhone': None, 'loadingStaff': None, 'loadingStaffName': None, 'loadingStaffPhone': None, 'customerManagerCode': None, 'customerManager': None, 'customerManagerPhone': None, 'custCode': None, 'custName': None, 'contactName': None, 'contactPhone': None, 'jobAddress': None, 'jobType': None, 'jobTypeName': None, 'projectCode': None, 'projectName': None, 'projectLongitude': None, 'projectLatitude': None, 'signPersonList': None, 'serDevEnterDemandList': [{'id': 54093, 'revise': None, 'approvalStatus': None, 'source': None, 'addNum': 0, 'devEnterCode': 'FWJ190360041', 'devEnterDemandCode': 'FWJ_DEMAND_190354093', 'shigh': '6', 'shighName': '6米', 'category': 'FORK', 'categoryName': '剪叉', 'num': 1, 'createBy': 'USER1903030886', 'createDate': None, 'updateDate': None, 'updateBy': 'USER1903030886', 'dayRentPrice': '125', 'monthRentPrice': '2500', 'storeCode': 'DEP18020003', 'storeName': None, 'orderDevCode': 'DEV190316856', 'orderCode': None, 'days': 30, 'notEnterNum': None, 'notEnterNumTe': 1, 'rentingNum': 2, 'lockedNum': 1, 'stockNum': 6, 'type': 0, 'orderDevType': 0, 'soureType': None, 'status': None, 'warehouseCode': 'DEP1802000106', 'warehouseName': '南京仓', 'orderNum': None, 'lockFlag': None, 'matchList': None, 'matchCount': None}], 'addTransFee': None, 'addBailFee': None, 'bond': None, 'estimatePrice': None, 'storeName': '南京店', 'storeCode': 'DEP18020003', 'remarks': '', 'query': None, 'pageNo': None, 'isAdd': 0, 'isTransport': None, 'isToDay': None, 'reason': None, 'prepayBond': None, 'prepayRent': None, 'prepayFreight': None, 'balanceType': 3, 'source': 0, 'orderSource': None, 'balanceTypeName': '后付', 'cautionMoneyPercent': None, 'cautionMoneyValue': None, 'accountPeriod': None, 'warehouseCode': 'DEP1802000106', 'warehouseName': '南京仓', 'pageSize': None, 'jobAddressLongitude': None, 'jobAddressLatitude': None, 'enterpriseCode': None, 'enterpriseName': None, 'transportDemands': None, 'traineeList': None, 'filePathList': None, 'modPlanArriveDateFlag': None, 'opRole': None, 'loadingModifyFlag': None, 'signType': None, 'signInFlag': None, 'fenceFlag': None, 'isArchived': None, 'showSignInIcon': 0, 'approveTime': None, 'contractId': None}, 'message': 'ok', 'success': True, 'errCode': 0}
# pprint(a)

A = 1
B = A
A = 2

print(B)
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d*%d=%d" % (col, row, col * row), end="\t")  # 打印99乘法表
#         col += 1
#     print("")
#     row += 1
import requests
import itchat
from threading import Timer


# 获取金山词霸每日一句，英文和翻译
def get_news():
    url = "http://open.iciba.com/dsapi"
    r = requests.get(url)
    contents = r.json()['content']
    translation = r.json()['translation']
    return contents, translation


# 发送消息
def send_news():
    try:
        itchat.auto_login()  # 会弹出网页二维码，扫描即可，登入你的微信账号，True保持登入状态
        my_girfriend = itchat.search_friends(name='张玉文')  # name改成你心爱的人在你微信的备注
        mylover = my_girfriend[0]["UserName"]
        message1 = str(get_news()[0])  # 获取金山字典的内容
        content = str(get_news()[1][17:])
        message2 = str(content)
        message3 = "来自你最爱的人"
        itchat.send(message1, toUserName=mylover)
        itchat.send(message2, toUserName=mylover)
        itchat.send(message3, toUserName=mylover)
        Timer(0.5, send_news).start()  # 每隔86400秒发送一次，也就是每天发一次
    except:
        message4 = "最爱你的人出现啦~~"
        itchat.send(message4, toUserName=mylover)


if __name__ == "__main__":
    send_news()