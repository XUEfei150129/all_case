# #! /usr/bin/env/python3
# # coding=utf-8
# # @Time : 2019/3/27 11:39
# # @Author : XueFei
# from pprint import pprint
#
# # # from datetime import datetimep
# #
# # a = {"contractStatus":1,"contractTargetCode":"CUST110359","contractTargetName":"薛飞","contractTargetType":1,"licenseFilePath":[],"filePath":["merchant/header_201903271159137001.jpg"],"orderCode":"ZNLHZL-2019-28228","orderSignPersonVoList":[{"idcard":"320882198810292412","mobile":"15151864744","name":"薛飞","images":["lpt/0/1108990759794774016.jpg","lpt/1/1108990760113541120.jpg"]}]}
# # pprint(a)
#
#
# # from datetime import datetime
# #
# # a = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# # print(a)
# # 文件上传：content-Type：  multipart/form-data类型
# # import requests
# #
# # class SendFile():
# #     def __init__(self, s):
# #         self.s = s
# #
# #     def sendImg(self, jpgpath, jpgname='1.jpg', jpgtype='image/jpeg'):
# #
# #         # 登录并更新cookies
# #         f = open('1.jpg', 'rb')  # 绝对路径
# #         url2 = ''
# #         body = {
# #             'localurl': (None, jpgname),
# #             'imgFile': ('1.jpg', open(jpgpath, 'rb'), jpgtype)
# #             # 1、绝对路径  2、open('1.jpg', 'rb')  3、content-type的值
# #             }
# #         # 上传图片的时候，不data和json，用files
# #         r = self.s.post(url2, files=body)    # 1、调用全局的s，用self.s   2、files
# #         print(r.text)
# #         # 上传到服务器，每传一次地址都不一样
# #
# #         # 解决抛异常
# #         try:
# #             jpg_url = r.json()['url']   # （相对路径）
# #             print(jpg_url)
# #             return jpg_url
# #
# #         except Exception as msg:    # 返回报错信息
# #             print('图片上传失败，原因：%s'%msg)   # 打印报错信息
# #         #    raise   # 主动抛原始异常
# #         #    raise  ··· # 抛出异常内容为：“···”
# #             return ''
# #
# # if __name__=='__main__':
# #     s = requests.session()
# #     from test.test_009_003_zentaologin import LoginZentao
# #     # 调登录方法
# #     login = LoginZentao(s)      # 实例化类LoginZentao为对象
# #     login.login()
# #     # 上传文件
# #     send = SendFile(s)      # 把类sendfile()实例化为对象
# #     send.sendImg()          # 调用sendfile()里面的sendImg方法
# # a = {"contractStatus": 1, "contractTargetCode": "CUST110359", "contractTargetName": "薛飞", "contractTargetType": 1,
# #      "licenseFilePath": [], "filePath": ["{}".format(("1.png", open("d:\1.png", "rb"), "image/png"))],
# #      "orderCode": "ZNLHZL-2019-28290",
# #      "orderSignPersonVoList": [{"idcard": "320882198810292412", "mobile": "15151864744", "name": "薛飞",
# #                                 "images": ["lpt/0/1108990759794774016.jpg", "lpt/1/1108990760113541120.jpg"]}]}
# # a = {"contractStatus": 1, "contractTargetCode": "CUST110359", "contractTargetName": "薛飞", "contractTargetType": 1,
# #      "licenseFilePath": [], "filePath": ["merchant/header_201903290109065091.jpg"], "orderCode": "ZNLHZL-2019-28305",
# #      "orderSignPersonVoList": [{"idcard": "320882198810292412", "mobile": "15151864744", "name": "薛飞",
# #                                 "images": ["lpt/0/1108990759794774016.jpg", "lpt/1/1108990760113541120.jpg"]}]}
# #
# #
# # values = {"contractStatus": 1, "contractTargetCode": "CUST110359", "contractTargetName": "薛飞",
# #           "contractTargetType": 1, "licenseFilePath": [],
# #           "filePath": [
# #               "{}".format({"localUrl": (None, "1.png"), "imgFile": ("1.png", open(r"d:\1.png", "rb"), "image/png")})],
# #           "orderCode": bizNo,
# #           "orderSignPersonVoList": [{"idcard": "320882198810292412", "mobile": "15151864744", "name": "薛飞",
# #                                      "images": ["lpt/0/1108990759794774016.jpg",
# #                                                 "lpt/1/1108990760113541120.jpg"]}]}
#
#
# # from datetime import datetime
# #
# # a = datetime.now().strftime('%Y-%m-%d %H:%M')
# #
# # print(a)
#
# # a = {'data': {'id': 60041, 'revise': 0, 'orderCode': 'ZNLHZL-2019-28348', 'devEnterCode': 'FWJ190360041', 'approvalStatus': None, 'planQuitDate': '2019-03-29 15:17', 'planArriveDate': '2019-03-29 15:17', 'arriveDate': None, 'rentDate': None, 'status': 10, 'delFlag': None, 'fileid': None, 'filePath': None, 'createBy': 'USER1903030886', 'createDate': None, 'updateBy': 'USER1903030886', 'updateDate': None, 'auditStatus': None, 'staff': None, 'serviceStaff': None, 'serviceStaffName': None, 'staffPhone': None, 'loadingStaff': None, 'loadingStaffName': None, 'loadingStaffPhone': None, 'customerManagerCode': None, 'customerManager': None, 'customerManagerPhone': None, 'custCode': None, 'custName': None, 'contactName': None, 'contactPhone': None, 'jobAddress': None, 'jobType': None, 'jobTypeName': None, 'projectCode': None, 'projectName': None, 'projectLongitude': None, 'projectLatitude': None, 'signPersonList': None, 'serDevEnterDemandList': [{'id': 54093, 'revise': None, 'approvalStatus': None, 'source': None, 'addNum': 0, 'devEnterCode': 'FWJ190360041', 'devEnterDemandCode': 'FWJ_DEMAND_190354093', 'shigh': '6', 'shighName': '6米', 'category': 'FORK', 'categoryName': '剪叉', 'num': 1, 'createBy': 'USER1903030886', 'createDate': None, 'updateDate': None, 'updateBy': 'USER1903030886', 'dayRentPrice': '125', 'monthRentPrice': '2500', 'storeCode': 'DEP18020003', 'storeName': None, 'orderDevCode': 'DEV190316856', 'orderCode': None, 'days': 30, 'notEnterNum': None, 'notEnterNumTe': 1, 'rentingNum': 2, 'lockedNum': 1, 'stockNum': 6, 'type': 0, 'orderDevType': 0, 'soureType': None, 'status': None, 'warehouseCode': 'DEP1802000106', 'warehouseName': '南京仓', 'orderNum': None, 'lockFlag': None, 'matchList': None, 'matchCount': None}], 'addTransFee': None, 'addBailFee': None, 'bond': None, 'estimatePrice': None, 'storeName': '南京店', 'storeCode': 'DEP18020003', 'remarks': '', 'query': None, 'pageNo': None, 'isAdd': 0, 'isTransport': None, 'isToDay': None, 'reason': None, 'prepayBond': None, 'prepayRent': None, 'prepayFreight': None, 'balanceType': 3, 'source': 0, 'orderSource': None, 'balanceTypeName': '后付', 'cautionMoneyPercent': None, 'cautionMoneyValue': None, 'accountPeriod': None, 'warehouseCode': 'DEP1802000106', 'warehouseName': '南京仓', 'pageSize': None, 'jobAddressLongitude': None, 'jobAddressLatitude': None, 'enterpriseCode': None, 'enterpriseName': None, 'transportDemands': None, 'traineeList': None, 'filePathList': None, 'modPlanArriveDateFlag': None, 'opRole': None, 'loadingModifyFlag': None, 'signType': None, 'signInFlag': None, 'fenceFlag': None, 'isArchived': None, 'showSignInIcon': 0, 'approveTime': None, 'contractId': None}, 'message': 'ok', 'success': True, 'errCode': 0}
# # pprint(a)
#
# # A = 1
# # B = A
# # A = 2
# #
# # print(B)
# # # row = 1
# # while row <= 9:
# #     col = 1
# #     while col <= row:
# #         print("%d*%d=%d" % (col, row, col * row), end="\t")  # 打印99乘法表
# #         col += 1
# #     print("")
# #     row += 1
# #
#
# """
# 面向对象编程(Object Oriented Programming )简写OOP
#  相比较函数，面向对象是更大的封装，根据职责在一个对象中封装多个方法
#     1.在完成摸一个需求前，首先要确定职责 --- 要做的的事情（方法）
#     2.根据职责确定不同的对象，在对象内部封装不同的方法（多个）
#     3.最后完成代码，就是顺序的让不同的对象调用不同的方法
#
# 面向对象的特点：
#     1.注重对象和职责，不同的对象承担不同的职责
#     2.更适合应对复杂的需求变化，是专门应对复杂项目开发，提供的固定套路
#     3.需要在面向过程的基础上，在学习一些面向对象的语法
#
# 类和对象
#     类和对象是面向对象编程的两个核心概念
#
#
# 类：
#     类 是对一群具有 相同特征 或者 行为 的事物的一个统称，是抽象的，不能直接使用
#         特征 被称为 属性
#         行为 被称为 方法
#
#     类 就相当于制造飞机时的 图纸，是一个 模板，是 负责创建对象的
# 对象：
#     对象 是由类创建出来的一个具体存在，可以直接使用
#     是由哪个类创建出来的 对象，就拥有在 哪一个类 中定义的：
#      属性
#      方法
#     对象就相对于 图纸制造的飞机
#     在程序开发中，应该先有类，再有对象
# 类和对象的关系
#     类是模板， 对象是根据类这个模板创建出来的，应该先有类，再有对象
#     类只有一个，而，对象有很多个
#         不同的对象之间的属性可能会各不相同
#     类中定义了什么属性和方法，对象中就有什么属性和方法，不可能多，也不可能少
# 类的设计
#     在程序开发中，要设计一个类，要满足三个要素：
#         1.类名 这类事物的名字，满足大驼峰命名法
#             大驼峰命名法：
#                 1.每个单词的首字母大写
#                 2.单词与单词之间没有下划线
#         2.属性 这类事物具有什么样的特征
#         3.方法 这类食物具有什么样的行为
#
#     类名的确定
#         名词提炼法 分析整个业务流程，出现的名词，通常就是找到的类
#     属性和方法的确定
#         对 对象的特征描述，通常可以定义成属性
#         对象具有的行为（动词），通常可以定义为方法
#             提示：需求中没有涉及的属性或者是方法在设计类时，不需要考虑
#
# 面向对象基础语法
#     dir内置函数
#      使用内置函数dir传入标识符/数据，可以查看对象内的所有属性及方法
#      提示：__方法名__ 格式的方法是python提供的内置方法/属性
#         验证了函数也是对象，对象是由对象的方法或是属性的
#         def aaa():
#             pass
#         print(dir(aaa()))
#         #结果：['__bool__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
#
#
#     引用的概念：
#         在面向对象开发中，引用的概念是同样适用的！
#         ·在python中使用类创建对象之后，tom变量中仍然记录的是对象在内存中的地址
#         ·也就是tom变量引用了新建的猫对象
#         ·使用print输出对象变量，默认情况下，是能够输出这个变量引用的对象是由那一个类创建的对象，
#           以及在内存中的地址（16进制表示）
#            提示：在计算机中，通常使用16进制表示内存地址
#
#             ·十进制和十六进制都是用来表达数字的，只是表示的方式不一样
#             ·十进制和十六进制的数字之间可以来回转换
#         ·%d 可以以10进制输出数字
#         ·%x 可以以16进制输出数字
#
#
# class Cat:
# def eat(self):
#     print("小猫哎吃鱼")
#
# def drink(self):
#     print("小猫要喝水")
#
# tom = Cat()
# tom.eat()
# tom.drink()
# print(tom)
# print("%d"%(id(tom)))           #%d打印的是10进制的
# print("%x"%(id(tom)))           #%X打印的是16进制的
# #结果   （计算机中喜欢用16进制表示地址）
# # 小猫哎吃鱼
# # 小猫要喝水
# # <__main__.Cat object at 0x03161330>
# # 51778352
# # 3161330
#
#     初始化方法
#     当使用类名()创建对象的时候，会自动执行以下操作：
#         1.为对象在内存中分配空间 -- 创建对象
#         2.为对象的属性设置初始值 --初始化方法（init）
#     这个初始化方法就是__init__方法，__init__是对象的 内置方法
#      __init__方法是专门用来定义一个类具有哪些属性的方法
#
# """
#
# #
# # class Cat:
# #     def __init__(self):
# #         print("这是初始化方法")
# #
# # #使用类名()创建对象的时候，会自动调用初始化方法__init__
# # tom = Cat()
#
#
# # result = 0
# # i = 0
# # while i<=100:
# #     if i % 2 == 0:
# import time
# from datetime import datetime
#
#
# def getaftertime(n):  # 精确到分钟
#     """
#     获取当前时间往后的时间
#     :param n: 当前时间后的n分钟
#     :return: 返回当前时间后的时间，精确当分钟
#     """
#     nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # 获取当前时间
#     c = time.strptime(nowtime, "%Y-%m-%d %H:%M:%S")
#     timeStamp = int(time.mktime(c))
#     timeStamp += (n * 60)
#     timeArray = time.localtime(timeStamp)
#     aftertime = time.strftime("%Y-%m-%d %H:%M", timeArray)
#     return aftertime
#
#
# a = getaftertime(91)
# print(a)

#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in a:
#     print(i, end="")
import decimal


# 修改舍入方式为四舍五入
# decimal.getcontext().rounding = "ROUND_HALF_UP"

# 使用字符串来储存小数不会有精度误差，Decimal可以正确处理这种方法表示的数字
# def sishewuru(num, precision = "0.00"):
#     swnum = decimal.Decimal("{}".format(num)).quantize(decimal.Decimal("{}".format(precision)))
#     return swnum
#
# print(sishewuru(12.12612355))
