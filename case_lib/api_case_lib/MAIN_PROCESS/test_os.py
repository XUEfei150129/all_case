# #! /usr/bin/env/python3
# # coding=utf-8
# # @Time : 2019/4/17 14:41
# # @Author : XueFei
#
# import time
# import random
# import string
#
# """
# open参数
#
#
#
#
# """
#
# # import logging  # 引入logging模块
# # # 将信息打印到控制台上
# # logging.debug(u"苍井空")
# # logging.info(u"麻生希")
# # logging.warning(u"小泽玛利亚")
# # logging.error(u"桃谷绘里香")
# # logging.critical(u"泷泽萝拉")
# #
#
#
# # def mysort(alist):
# #     for i in range(0, len(alist) - 1):  # 需要遍历的次数是所有元素的少一次，比如5个元素，去最大值，要比较4次
# #         for j in range(0, len(alist) - i - 1):  #每一个元素要遍历的次数
# #                   #只是交换次数，但是要不要交换取决于相邻值的大小
# #             if alist[j] > alist[j + 1]:   #如果前面大于后面的值，就换位置
# #                 alist[j], alist[j + 1] = alist[j + 1], alist[j]
# #     return alist
#
# """
# 文件的打开
# file_object = open(file_name,access_mode="r" )
# file_name
#     文件路径：相对路径和绝对路径
# access_mode
#     读   (定义时等于号指定的值，缺省参数)
#     写
#     读加写
#
#
#
#
# """
#
# # file = open(r"D:\test_python\test.txt", 'r', encoding="gb18030")  # 打开test1.txt 文件
# # a = str(file.readlines())
# # b = a.count("宝钗")
# # print(b)
# # file.close()  # 关闭文件
#
#
# # print(str(open(r"D:\test_python\test.txt", 'r', encoding="gb18030").readlines()))
#
# # b = str(open(r"D:\test_python\test.txt", 'r', encoding="gb18030").readlines())
# # for i in range(1, 10):
# #     a = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=60))
# #     fileDir = "D:/test_python/test/{}.txt".format(a)  # 文件内容为：12345  换行abcde
# #     fo = open(fileDir, "w")  # 打开文件，已二进制的格式打开
# #     fo.write(a)
#
# #
# # dict = {'Name': 'Runoob', 'Age': 7}
# # for i, j in dict.items():
# #     print(i, ":\t", j)
#
#
# # 先自定义两个异常
# # class NameTooLongError(Exception):
# #     pass
# #
# #
# # class NameTooshortError(Exception):
# #     pass
# #
# #
# # def inputname():
# #     name = input("请输入姓名：")
# #     if len(name) > 10:
# #         raise NameTooLongError
# #     if len(name) < 6:
# #         raise NameTooshortError
# #
# #
# # # 主体部分调用
# # try:  # 捕获异常
# #     ret = inputname()
# # except NameTooshortError:
# #     print("太短了")
# # except NameTooLongError:
# #     print("太长了")
#
# # 结果：
# # 请输入姓名：1111111111111111111111
# # 太长了
#
# # 当输的名字长度大于10的时候，在函数里面会抛出NameTooLongError异常，函数后面的代码都不执了，因为它没有捕获异常。直接跑到上层去，调用它的地方去。调用的地方代码被try监控着，expect里面匹配这个错误类型。匹配到了，就会打印一个太长了
#
#
# """
#
#
#
#
#
# """
# # import unittest
# # import sys
# # class SeleniumTest(unittest.TestCase):
# #     ...
# #
# #     def tearDown(self):
# #         if sys.exc_info()[0]:
# #             test_method_name = self._testMethodName
# #             self.driver.save_screenshot("Screenshots/%s.png" % test_method_name)
# #         super(SeleniumTest, self).tearDown()
#
# # from datetime import datetime
# # png_name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# # png_name = png_name.replace("-","")
# # png_name = png_name.replace(":","")
# # png_name = png_name.replace(" ","")
# # print(png_name)
#
# # import re
# #
# # from datetime import datetime
# # png_name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# #
# # png_name = re.sub("\D", "", png_name)
# # print(png_name)
#
#
# """
# 装饰器
# 定义：本质是函数，功能是：装饰其他函数。就是为其他函数添加附加功能
# 原则：
#     1.不修改被装饰函数的源代码
#     2.不能修改被装饰的函数的调用方式
#     总结：装饰器对被修饰的函数是完全透明的
#
#
# 例题：
# def timmer(func):
#     def warpper(*args, **kwargs):
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("the func time is %s" % (stop_time - start_time))
#     return warpper
#
#
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
# test1()
# # 结果是：
# # in the test1
#
# 再看：
# def timmer(func):
#     def warpper(*args, **kwargs):
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print("the func time is %s" % (stop_time - start_time))
#     return warpper
#
# @timmer
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
# test1()
#
# #结果：
# # in the test1
# # the func time is 3.0004844665527344
#
#
#
# #可以看出：装饰器本身就是函数，装饰器不修改被装饰函数的源代码，不能修改被装饰的函数的调用方式
#
#
# 实现装饰器只是储备：
# 1.函数就是“变量”
#     python是解释型语言：定义函数和定义变量是一样的。先将消息体存放在内存中，在调用。只要在调用之前，内存地址里面有函数体。调用的时候就不会报错
#     下面介绍函数就是“变量”是啥意思：
#     把pass所代表的函数体，赋值给test变量。定义变量的时候，在内存里找一块地址，存放函数体。（跟变量的概念一样）
#     python的内存回收机制是解释器做的，当没有变量指向他的时候。
#     有的函数是不要起名字的叫匿名函数：lambda       匿名函数没有函数名，就会立马被回收掉
#     calc = lambda x:x * 3
#     print(calc(3))
#     #结果：
#     #9
#
# 2.高阶函数
#     满足下面两个条件之一就是高阶函数：
#         1.把一个函数名，当做实参传给另一个函数(在不修改被装饰函数源代码的情况下为其添加功能)
#         2.返回值中包含函数名（不修改函数的调用方式）
#         （理念就是函数就是“变量”）
# #下面演示，按第一个标准（把一个函数名，当做实参传给另一个函数）定义高阶函数
# def bar():
#     print("in the bar")
#
# def test1(func):
#     print(func)
#
# test1(bar)
#
# #结果：<function bar at 0x02AC3810>
# #结果是内存地址，类似于门牌号。加上小括号是就是调用这个函数
#
# 再看：
# def bar():
#     print("in the bar")
#
#
# def test1(func):
#     print(func)
#     func()  # func就是函数的门牌号，加上(),就是调用这个函数，类似于func = bar，所以func()就是bar(),可以想变量一样赋值
#
#
# test1(bar)
#
# # 结果：
# # <function bar at 0x00B63810>
# # in the bar
# # 结果是内存地址，类似于门牌号。加上小括号是就是调用这个函数
#
#
# 再看
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
#
# def test1(func):
#     start_time = time.time()
#     func()  # 运行的是bar函数
#     stop_time = time.time()
#     print("the func run time is %s" % (stop_time - start_time))  # test1函数就是给函数附加了一个计时的功能，统计bar的运行时间
#
#
# test1(bar)
# #不能实现装饰器的功能（因为不满足“不能修改被装饰的函数的调用方式”）。至少提供了一种思路：在不修改源代码的情况下，为源代码加上功能。
#
#
# #下面演示按第二个标准（返回值中包含函数名）定义高阶函数：
#
#
# import time
#
#
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
#
# def test2(func):
#     print(func)
#     return func
#
#
# print(test2(bar))
# #结果
# # <function bar at 0x01723810>      #print内存地址
# # <function bar at 0x01723810>      #print打印的返回值
# #想法就是：有了内存地址之后，加上括号就是调用函数
#
#
# test2(bar)      #意思是传的内存地址
# test2(bar())    #意思是传的bar()的返回值
#
# 再看
#
# import time
#
#
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
#
# def test2(func):
#     print(func)
#     return func
#
#
# t = test2(bar)  # 意思是传的内存地址，在test2函数里面在将他返回出来，可以通过变量获取到
# print(t)            #t变量就是bar的内存地址
#
# #结果
# # <function bar at 0x01D83810>
# # <function bar at 0x01D83810>
#
#
# #再看
# import time
#
#
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
#
# def test2(func):
#     print(func)
#     return func
#
#
# t = test2(bar)  # 意思是传的内存地址，在test2函数里面在将他返回出来，可以通过变量获取到
# t()    #就代表运行bar这个函数
#
#
# #结果：
# # <function bar at 0x033E3810>
# # in the bar
#
#
# 再看
# import time
#
#
# def bar():
#     time.sleep(3)
#     print("in the bar")
#
#
# def test2(func):
#     print(func)
#     return func
#
#
# bar = test2(bar)  # 这里相当于用test2加上了新的功能，(print理解为加了很多功能)
# bar()    #函数的调用方式没有改变。
#
#
# #结果：
# # <function bar at 0x033E3810>
# # in the bar
#
# 3.嵌套函数
# 定义：在函数的函数体内，用def申明一个新的函数，叫嵌套函数。（而不是去调用别的函数）
# 嵌套函数的作用域：
# import time
#
#
# def foo():
#     print("in the foo")
#
#     def bar():
#         print("in the bar")
#
#     bar()  # 这个函数具有局部变量的特性，再能在内部调用
# foo()
#
# #结果：
# # in the foo
# # in the bar
#
#
# # 局部作用域和全局作用域的访问顺序
# x = 0
# def grandpa():
#     x = 1
#     def dad():
#         x = 2
#         def son():
#             x = 3
#             print(x)
#         son()
#     dad()
# grandpa()
# #结果：3
# #从里往外一层一层的找
#
# 高阶函数+嵌套函数 = 》装饰器
#
#
#
# import time
#
#
# def deco(func):
#     start_time = time.time()
#     func()
#     stop_time = time.time()
#     print("the func run time is %s" % (stop_time - start_time))
#
#
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
#
# def test2():
#     time.sleep(3)
#     print("in the test2")
#
#
# # 思考怎么给test1,test2增加新功能，先写一个高阶函数deco
# deco(test1)
# deco(test2)  # 但是这是在改变函数的调用方式
# # 结果：
# # in the test1
# # the func run time is 3.0005288124084473
# # in the test2
# # the func run time is 3.000913143157959
#
# # 可以这样：
# # 前面一直在使用高阶函数，也可以考虑嵌套函数
#
#
# 再看：
#
# import time
#
#
# def timer(func):  # timer(test1) ,func = test 就是把test1的内存地址传给func
#     def deco():  # 函数的嵌套。这里就是在内存地址上申明了一个变量
#         start_time = time.time()
#         func()  # 运行了test1
#         stop_time = time.time()
#         print("the func run time is %s" % (stop_time - start_time))
#
#     return deco  # 高阶函数。这里就是返回了函数的内存地址
#
#
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
#
# def test2():
#     time.sleep(3)
#     print("in the test2")
#
#
# test1 = timer(test1)  # print(timer(test1) )的结果就是deco函数的内存地址
# test1()  # 执行的是deco，
#
# # 结果：（没有改变test1的源代码，没有改变test1的调用方式。用到函数的嵌套和高阶函数，但是这样做有点麻烦，每次都要运行装饰器，还要赋值给一个变量名一样的变量）
# # in the test1
# # the func run time is 3.000809669494629
#
# 再看：
# # 如果要直接test1()调用，如何实现。
# import time
#
#
# def timer(func):  # timer(test1) ,func = test 就是把test1的内存地址传给func
#     def deco():  # 函数的嵌套。这里就是在内存地址上申明了一个变量
#         start_time = time.time()
#         func()  # 运行了test1
#         stop_time = time.time()
#         print("the func run time is %s" % (stop_time - start_time))
#
#     return deco  # 高阶函数。这里就是返回了函数的内存地址
#
#
# @timer  # 就等于test1 = timer(test1)
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
#
# @timer  # 就等于test2 = timer(test1)
# def test2():
#     time.sleep(3)
#     print("in the test2")
#
#
# test1()
# test2()
#
#
# #结果：
# # in the test1
# # the func run time is 3.0002071857452393
# # in the test2
# # the func run time is 3.000702381134033
#
# 再看：
# # 如果要直接test1()调用，如何实现。
# import time
#
#
# def timer(func):  # timer(test1) ,func = test 就是把test1的内存地址传给func
#     def deco():  # 函数的嵌套。这里就是在内存地址上申明了一个变量
#         start_time = time.time()
#         func()  # 运行了test1
#         stop_time = time.time()
#         print("the func run time is %s" % (stop_time - start_time))
#
#     return deco  # 高阶函数。这里就是返回了函数的内存地址
#
#
# @timer  # 就等于test1 = timer(test1)
# def test1():
#     time.sleep(3)
#     print("in the test1")
#
#
# test1()
#
# # 结果（可以全部选中，断点打印）：
# # in the test1
# # the func run time is 3.0002071857452393
# # in the test2
# # the func run time is 3.000702381134033
#
#
# # 如果有参数，怎么传参数
# import time
#
#
# def timer(func):
#     def deco(*args, **kwargs):
#         start_time = time.time()
#         func(*args, **kwargs)
#         stop_time = time.time()
#         print("the func run time is %s" % (stop_time - start_time))
#
#     return deco  # 高阶函数。这里就是返回了函数的内存地址
#
#
# @timer  # 就等于test1 = timer(test1)
# def test1():  # 没有参数
#     time.sleep(3)
#     print("in the test1")
#
#
# @timer  # 就等于test2 = timer(test2)
# def test2(age):  # 有参数
#     time.sleep(3)
#     print("test2的参数", age)
#
#
# test1()
#
# test2(23)
# # in the test1
# # the func run time is 3.0001745223999023
# # test2的参数 23
# # the func run time is 3.000623941421509
#
# decorator就是装饰器的意思，又叫语法糖
#
# #比如：
# 有个小需求，某公司的网站有很多页，如果将每个页面定义为一个函数，有些页面需要有权限才能查看
# user, passwd = "xf", "4941"
#
#
# user, passwd = "xf", "4941"
#
#
# # 写装饰器
# def anth(func):
#     def warpper(*args, **kwargs):
#         username = input("Username:").strip()
#         password = input("Password:").strip()
#         if user == username and passwd == password:
#             print("\033[32;1mUser has passed authentication\033[0m")  # 加色
#             func(*args, **kwargs)
#         else:
#             exit("\033[31;1mInvalid username or password\033[0m")
#
#     return warpper
#
#
# def index():
#     print("welcome to index page")
#
#
# @anth
# def home():
#     print("welcome to home page")
#
#
# @anth
# def bbs():
#     print("welcome to bbs page")
#
#
# index()
# home()
# bbs()
# #结果
# # welcome to index page
# # Username:xf
# # Password:4941
# # User has passed authentication
# # welcome to home page
# # Username:xf
# # Password:4941
# # User has passed authentication
# # welcome to bbs page
#
#
# #再看
# #home()函数有返回值
# user, passwd = "xf", "4941"
#
#
# # 写装饰器
# def anth(func):
#     def warpper(*args, **kwargs):
#         username = input("Username:").strip()
#         password = input("Password:").strip()
#         if user == username and passwd == password:
#             print("\033[32;1mUser has passed authentication\033[0m")  # 加色
#             func(*args, **kwargs)
#         else:
#             exit("\033[31;1mInvalid username or password\033[0m")
#
#     return warpper
#
#
# def index():
#     print("welcome to index page")
#
#
# @anth
# def home():
#     print("welcome to home page")
#     return "from home"
#
#
# @anth
# def bbs():
#     print("welcome to bbs page")
#
#
# index()
# print(home())
# bbs()
#  #结果
# # welcome to index page
# # Username:xf
# # Password:4941
# # User has passed authentication
# # welcome to home page
# # None #home()函数的返回值变成空了，因为在装饰器func()里面的返回结果没有赋值给变量
#
# 再看：
# user, passwd = "xf", "4941"
#
#
# # 写装饰器
# def anth(func):
#     def warpper(*args, **kwargs):
#         username = input("Username:").strip()
#         password = input("Password:").strip()
#         if user == username and passwd == password:
#             print("\033[32;1mUser has passed authentication\033[0m")  # 加色
#             res = func(*args, **kwargs)
#             print("---after authenticaion")  # 随便砸装饰一点东西
#             return res
#         else:
#             exit("\033[31;1mInvalid username or password\033[0m")
#
#     return warpper
#
#
# def index():
#     print("welcome to index page")
#
#
# @anth
# def home():
#     print("welcome to home page")
#     return "from home"
#
#
# @anth
# def bbs():
#     print("welcome to bbs page")
#
#
# index()
# print(home())
# bbs()
# #结果：
# welcome to index page
# Username:xf
# Password:4941
# User has passed authentication
# welcome to home page
# ---after authenticaion
# from home           #现在就有返回值了
# Username:
#
#
#
# 面向对象介绍
# 现实生活中对象的总结：
#     世界万物，皆可分类
#     世界万物，皆为对象
#     只要是对象，就肯定属于某种品类
#     只要是对象，肯定有属性
#
# 面向对象编程
#     oop编程是利用"类"和"对象"来创建各种模型来实现对真实世界的描述。
#
# class类
#     一个类既是对以内拥有相同属性的对象的抽象，蓝图，原型。
#
# Object对象
#     一个对象是一个类的实例化后实例，一个类必须经过实例化后才可在程序中调用，一个类可以实例化多个对象，每个对象可以有不同的属性，就像
#     人类是指所有人，每个人是指具体的对象，人与人之间有共性，亦有不同
#
# Encapsulation封装
#     在类中对数据赋值，内部调用对外部用户是透明的，这使类变成了一个胶囊或容器，里面包含着类的数据和方法
#
# Inheritance继承
#     一个类可以派生出子类，在这个父类里定义的属性，方法自动被子类继承
#
# Polymorphism多态
#     简单点说就是：一个接口，多种实现
#
#
#
# class Role(object):
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def shot(self):
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police',
#           'AK47')  # 生成一个角色，相当于Role.buy_gun(),Role要知道是谁在买枪，所以要把r1传进去，就变成Role.buy_gun(r1)，所以每个方法都有一个self，就是谁调用这个类就是谁
# r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
# # 以上代码是角色
#
# 理解：
# 实例化的时候，开辟一块内存。把构建函数里面的东西存到实例化的变量那里。
# 下面的实例方法，存在类的内存里面，所有每个实例方法都有个self
# 实例化，其实就是以role类为模版，在内存里开辟一块空间，存上数据，赋值成一个变量名
#
# # 清晰一下关键术语
# class Role:  # (类名)
#     n = 123  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police', 'AK47')  # 生成一个角色，实例化后得到的对象，就是role这个类的对象
# r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
#
#
# 再看：
# 类变量：通过类和实例都能访问
# class Role:  # (类名)
#     n = 123  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# print(Role.n)  # 结果：123  说明类的变量存在类的内存里的，因为还没有实例化就可以打印
# r1 = Role('Alex', 'police', 'AK47')
# print(r1.n, r1.name)  # 结果：123 Alex
# r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
# print(r2.n, r2.name)  # 结果：123 Jack
#
#
# 再看：
# #如果类里面和实例里面都有同一个变量，先在实例变量里面找，如果没有的话，就在类变量里面找。
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# print(Role.n)  # 结果：123  说明类的变量存在类的内存里的，因为还没有实例化就可以打印
# r1 = Role('Alex', 'police', 'AK47')
# print(r1.n, r1.name)  # 结果：123 Alex
# r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
# print(r2.n, r2.name)  # 结果：123 Jack
# # 结果：
# # 123
# # 123 Alex
# # 123 Jack
# # 可以看出，如果类里面和实例里面都有同一个变量，先在实例变量里面找，如果没有的话，就在类变量里面找。
#
#
# 再看：
# # 清晰一下关键术语
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# print(Role.n)  # 结果：123  说明类的变量存在类的内存里的，因为还没有实例化就可以打印
# r1 = Role('Alex', 'police', 'AK47')
# r1.name = "陈华"
# print(r1.n, r1.name)  # 结果：123 Alex
# r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
# r2.name = "徐伟"
# print(r2.n, r2.name)  # 结果：123 Jack
# # 结果：
# # 123
# # 123 陈华
# # 123 徐伟
#
#
# 再看
# #实例化的时候可以添加新的属性，这个属性只属于该实例本身
#
#
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# print(Role.n)  # 结果：123  说明类的变量存在类的内存里的，因为还没有实例化就可以打印
# r1 = Role('Alex', 'police', 'AK47')
# r1.name = "陈华"
# r1.bullet_prove = True  # 实例化的时候加上一个防弹衣的属性，这样也是可以的。这个属性是r1实例化产生的。只属性r1实例。不属于r2
# print(r1.n, r1.name, r1.bullet_prove)
# r2 = Role('Jack', 'terrorist', 'B22')  # 生成一个角色
# r2.name = "徐伟"
# print(r2.n, r2.name)
# # 结果：
# # 123
# # 123 陈华 True
# # 123 徐伟
#
#
#
# 再看：
# 类变量和实例变量
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police', 'AK47')
# r1.name = "陈华"
# r1.bullet_prove = True  # 实例化的时候加上一个防弹衣的属性，这样也是可以的。这个属性是r1实例化产生的。只属性r1实例。不属于r2
# r1.n = "改类变量"
# print("r1:", r1.weapon, r1.n)
#
# r2 = Role("jack", "terrorist", "B22")
# r2.name = "徐伟"
# print("r2:", r2.name, r2.n)
#
# Role.n = "ABC"  # 改了类变量
#
# print(r1.n, r2.n)
# # 结果：
# # r1: AK47 改类变量
# # r2: 徐伟 123
# # 改类变量 ABC
# #可以看出r1没有改，r2改了。实例里面只要自己没有n的这个属性，都会跟着改，本身有的话就不会改。
#
#
# 类变量的用途？
# 大家共有的属性，节省开销
# class Person:
#     cn = "中国"
#
#     def __init__(self, name, age, addr, cn="china"):
#         self.name = name
#
# #上面的列子里面，cn写在类变量里面，和实例变量里面的效果是一样的。
# #如果写在类变量里面，是在类的内存地址里面，只有一个。如果某个实例要改的话也好改，也不影响其他的
# #如果是写在构造函数里面，每生成一个实例就有会有一个cn，太浪费了
# """
# #
# #
# # class Person:
# #     cn = "中国"
# #
# #     def __init__(self, name, age, addr, cn="china"):
# #         self.name = name
# #
# # #上面的列子里面，cn写在类变量里面，和实例变量里面的效果是一样的。
# # #如果写在类变量里面，是在类的内存地址里面，只有一个
# # #如果是写在构造函数里面，每生成一个实例就有会有一个cn，太浪费了
# """
# 析构函数
# 在实例释放，销毁（运行结束）的时候自动执行的，通常用于做一些收尾工作，比如：关闭一些数据库连接，关闭打开的临时文件。
#
# #__del__的作用是在程序退出或实例释放或销毁的时候，执行。
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def __del__(self):  # 不需要给它传参数
#         print("%s 彻底死了。。。"%self.name)
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police', 'AK47')
# r1.buy_gun("ak47")
# r1.got_shot()
#
# r2 = Role("jack", "terrorist", "B22")
# r2.got_shot()
#
# # 结果：
# # # just bought ak47
# # # ah...,I got shot...
# # # ah...,I got shot...
# # # Alex 彻底死了。。。
# # # jack 彻底死了。。。
# #可以看出：del的作用是在程序退出或实例释放或销毁的时候，执行。
#
# 再看
# # 如果不是要等到结束的时候就执行
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         # 构造函数
#         # 在实例化时做一些类的初始化工作
#         self.name = name  # 叫实例变量（也叫静态属性），赋给了实例。作用域就是实例本身
#         self.role = role
#         self.weapon = weapon
#         self.life_value = life_value
#         self.money = money
#         # 以上代码是属性
#
#     def __del__(self):  # 不需要给它传参数
#         print("%s 彻底死了。。。" % self.name)
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police', 'AK47')
# r1.buy_gun("ak47")
# r1.got_shot()
#
# del r1  # 不要等到结束就得死
#
# r2 = Role("jack", "terrorist", "B22")
# r2.got_shot()
#
# # 结果：
# # just bought ak47
# # ah...,I got shot...
# # Alex 彻底死了。。。
# # ah...,I got shot...
# # jack 彻底死了。。。
#
#
# 私有方法，私有属性
# #属性：静态属性（变量），动态属性（方法），一般我们说属性就是变量，方法就是方法
# #私有：就是外面访问不了，只能自己访问
#
# #私有属性：在前面加两个__,实例是访问不了的。
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         self.__life_value = life_value  # 加两个下划线就变成私有属性了
#         self.money = money
#         # 以上代码是属性
#
#     def __del__(self):  # 不需要给它传参数
#         pass  # print("%s 彻底死了。。。" % self.name)
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police', 'AK47')
# r1.buy_gun("ak47")
# r1.got_shot()
# print(r1.)  #现在就无法调用私有属性了
#
#
# 再看：
# 如何查看私有属性，在内部定义一个方法，把私有属性读出来
#
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         self.__life_value = life_value  # 加两个下划线就变成私有属性了
#         self.money = money
#         # 以上代码是属性
#
#     def __del__(self):  # 不需要给它传参数
#         pass  # print("%s 彻底死了。。。" % self.name)
#
#     def show_status(self):
#         print("name:%s weapon:%s life_val:%s" % (self.name,
#                                                  self.weapon,
#                                                  self.__life_value))  # 在内部是可以调用的，可以定义一个函数把它读出来
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police', 'AK47')
# r1.buy_gun("ak47")
# r1.got_shot()
# print(r1.show_status())  # 现在就可以查看私有属性了
#
# 结果：
# just bought ak47
# ah...,I got shot...
# name:Alex weapon:AK47 life_val:100    #现在就可以读了
# None
#
#
#
# 再看
# 私有属性外面访问不了，里面可以改
#
# class Role:  # (类名)
#     n = 123  # 类变量
#     name = "我是类name"  # 类变量
#
#     def __init__(self, name, role, weapon, life_value=100, money=15000):
#         self.name = name
#         self.role = role
#         self.weapon = weapon
#         self.__life_value = life_value  # 加两个下划线就变成私有属性了
#         self.money = money
#         # 以上代码是属性
#
#     def __del__(self):  # 不需要给它传参数
#         pass  # print("%s 彻底死了。。。" % self.name)
#
#     def show_status(self):
#         print("name:%s weapon:%s life_val:%s" % (self.name,
#                                                  self.weapon,
#                                                  self.__life_value))  # 在内部是可以调用的，可以定义一个函数把它读出来
#
#     def shot(self):  # 类的方法，就是功能的意思。（也叫动态属性，动态属性就是方法。静态属性就是变量）
#         print("shooting...")
#
#     def got_shot(self):
#         self.__life_value -= 50
#         print("ah...,I got shot...")
#
#     def buy_gun(self, gun_name):
#         print("just bought %s" % gun_name)
#     # 以上代码是功能
#
#
# r1 = Role('Alex', 'police', 'AK47')
# r1.buy_gun("ak47")
# r1.got_shot()
# print(r1.show_status())  # 现在就可以查看私有属性了
#
#
# #结果
# # just bought ak47
# # ah...,I got shot...
# # name:Alex weapon:AK47 life_val:50
# # None
#
#
# 私有方法也是一样的，也是加__,和私有属性是一样的
# """
#
# # 私有属性：在前面加两个__
# # class Role:  # (类名)
# #     n = 123  # 类变量
# #     name = "我是类name"  # 类变量
# #
# #     def __init__(self, name, role, weapon, life_value=100, money=15000):
# #         self.name = name
# #         self.role = role
# #         self.weapon = weapon
# #         self.__life_value = life_value  # 加两个下划线就变成私有属性了
# #         self.money = money
# #         # 以上代码是属性
# #
# #     def __del__(self):  # 不需要给它传参数
# #         pass  # print("%s 彻底死了。。。" % self.name)
# #
# #     def show_status(self):
# #         print("name:%s weapon:%s life_val:%s" % (self.name,
# #                                                  self.weapon,
# #                                                  self.__life_value))  # 在内部是可以调用的，可以定义一个函数把它读出来
# #
# #     def __shot(self):  # 前面加__,实例就访问不了了
# #         print("shooting...")
# #
# #     def got_shot(self):
# #         self.__life_value -= 50
# #         print("ah...,I got shot...")
# #
# #     def buy_gun(self, gun_name):
# #         print("just bought %s" % gun_name)
# #     # 以上代码是功能
# #
# #
# # r1 = Role('Alex', 'police', 'AK47')
# # r1.buy_gun("ak47")
# # r1.__shot()     #就访问不了了
# # print(r1.show_status())  # 现在就可以查看私有属性了
#
# # r2 = Role("jack", "terrorist", "B22")
# # r2.got_shot()
#
# # 结果：
# # just bought ak47
# # ah...,I got shot...
# # Alex 彻底死了。。。
# # ah...,I got shot...
# # jack 彻底死了。。。
#
#
# # r1.name = "陈华"
# # r1.bullet_prove = True  # 实例化的时候加上一个防弹衣的属性，这样也是可以的。这个属性是r1实例化产生的。只属性r1实例。不属于r2
# # r1.n = "改类变量"
# # print("r1:", r1.weapon, r1.n)
# #
# # r2 = Role("jack", "terrorist", "B22")
# # r2.name = "徐伟"
# # print("r2:", r2.name, r2.n)
# #
# # Role.n = "ABC"  # 改了类变量
# #
# # print(r1.n, r2.n)
# """
# 继承
# 作用：是减少代码。和现实中的继承一样
# 自己什么也不用做，就可以继承父类的方法
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating..." % self.name)
#
#     def sleep(self):
#         print("%s is sleeping..." % self.name)
#
#     def talk(self):
#         print("%s is talking..." % self.name)
#
#
# class Man(People):
#     pass
#
#
# m1 = Man("zhangsan", 8)
# m1.eat()
# #结果：
# # zhangsan is eating...
#
#
# 再看
# 也可以自己写一些方法
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating..." % self.name)
#
#     def sleep(self):
#         print("%s is sleeping..." % self.name)
#
#     def talk(self):
#         print("%s is talking..." % self.name)
#
#
# class Man(People):
#     def piao(self):
#         print("%s is piaoing...20s...done" % self.name)
#
#
# m1 = Man("zhangsan", 8)
# m1.eat()
# m1.piao()
# 结果：
# zhangsan is eating...
# zhangsan is piaoing...20s...done
#
# 再看
# 重写父类的方法
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating..." % self.name)
#
#     def sleep(self):
#         print("%s is sleeping..." % self.name)
#
#     def talk(self):
#         print("%s is talking..." % self.name)
#
#
# class Man(People):
#     def piao(self):
#         print("%s is piaoing...20s...done" % self.name)
#
#     def sleep(self):
#         print("man is sleeping")
#
#
# m1 = Man("zhangsan", 8)
# m1.eat()
# m1.piao()
# m1.sleep()
#
# #结果
# # zhangsan is eating...
# # zhangsan is piaoing...20s...done
# # man is sleeping
#
#
# 再看
# 重构了父类的方法
#
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating..." % self.name)
#
#     def sleep(self):
#         print("%s is sleeping..." % self.name)
#
#     def talk(self):
#         print("%s is talking..." % self.name)
#
#
# class Man(People):
#     def piao(self):
#         print("%s is piaoing...20s...done" % self.name)
#
#     def sleep(self):
#         People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
#         print("man is sleeping")
#
#
# m1 = Man("zhangsan", 8)
# m1.eat()
# m1.piao()
# m1.sleep()
# #结果
# # zhangsan is eating...
# # zhangsan is piaoing...20s...done
# # zhangsan is sleeping...
# # man is sleeping
#
#
# 再看
# 同一个父类可以被多个子类继承
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating..." % self.name)
#
#     def sleep(self):
#         print("%s is sleeping..." % self.name)
#
#     def talk(self):
#         print("%s is talking..." % self.name)
#
#
# class Man(People):
#     def piao(self):
#         print("%s is piaoing...20s...done" % self.name)
#
#     def sleep(self):
#         People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
#         print("man is sleeping")
#
#
# class Women(People):
#     def get_birth(self):
#         print("%s is born a baby..." % self.name)
#
#
# m1 = Man("zhangsan", 8)
# m1.eat()
# m1.piao()
# m1.sleep()
#
# w1 = Women("chenghua", 26)
# w1.get_birth()
#
# # 结果：
# # zhangsan is eating...
# # zhangsan is piaoing...20s...done
# # zhangsan is sleeping...
# # man is sleeping
# # chenghua is born a baby...
#
#
# 再看：
# 子类之间的方法不可以相互不可以调用
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating..." % self.name)
#
#     def sleep(self):
#         print("%s is sleeping..." % self.name)
#
#     def talk(self):
#         print("%s is talking..." % self.name)
#
#
# class Man(People):
#     def piao(self):
#         print("%s is piaoing...20s...done" % self.name)
#
#     def sleep(self):
#         People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
#         print("man is sleeping")
#
#
# class Women(People):
#     def get_birth(self):
#         print("%s is born a baby..." % self.name)
#
#
# m1 = Man("zhangsan", 8)
# m1.eat()
# m1.piao()
# m1.sleep()
#
# w1 = Women("chenghua", 26)
# w1.get_birth()
# w1.piao()           #就不可以调用
# # 结果：AttributeError: 'Women' object has no attribute 'piao'
#
#
# 再看
# 子类重构父类的初始化方法
# class People:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print("%s is eating..." % self.name)
#
#     def sleep(self):
#         print("%s is sleeping..." % self.name)
#
#     def talk(self):
#         print("%s is talking..." % self.name)
#
#
# class Man(People):
#     def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
#         People.__init__(self, name, age)
#         self.money = money
#         print("%s 一出生就有%s money" % (self.name, self.money))
#
#     def piao(self):
#         print("%s is piaoing...20s...done" % self.name)
#
#     def sleep(self):
#         People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
#         print("man is sleeping")
#
#
# class Women(People):
#     def get_birth(self):
#         print("%s is born a baby..." % self.name)
#
#
# m1 = Man("zhangsan", 8, 10)
# m1.eat()
# m1.piao()
# m1.sleep()
#
# w1 = Women("chenghua", 26)
# w1.get_birth()
#
# # 结果：
# # zhangsan 一出生就有10 money
# # zhangsan is eating...
# # zhangsan is piaoing...20s...done
# # zhangsan is sleeping...
# # man is sleeping
# # chenghua is born a baby...
#
# """
# #
# # #
# # # class People:
# # #     def __init__(self, name, age):
# # #         self.name = name
# # #         self.age = age
# # #
# # #     def eat(self):
# # #         print("%s is eating..." % self.name)
# # #
# # #     def sleep(self):
# # #         print("%s is sleeping..." % self.name)
# # #
# # #     def talk(self):
# # #         print("%s is talking..." % self.name)
# # #
# # #
# # # class Man(People):
# # #     def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
# # #         People.__init__(self, name, age)
# # #         self.money = money
# # #         print("%s 一出生就有%s money" % (self.name, self.money))
# # #
# # #     def piao(self):
# # #         print("%s is piaoing...20s...done" % self.name)
# # #
# # #     def sleep(self):
# # #         People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
# # #         print("man is sleeping")
# # #
# # #
# # # class Women(People):
# # #     def get_birth(self):
# # #         print("%s is born a baby..." % self.name)
# # #
# # #
# # # m1 = Man("zhangsan", 8, 10)
# # # m1.eat()
# # # m1.piao()
# # # m1.sleep()
# # #
# # # w1 = Women("chenghua", 26)
# # # w1.get_birth()
# #
# # # {"approvalPageFlag":false,"contactCode":"","contactName":"","createName":"薛飞","customerCode":"CUST112589","customerName":"薛飞","entAuthStatus":0,"estimatePriceUpdateFlag":0,"orderDevList":[{"category":"FORK","categoryName":"剪叉","commissionSubtract":"0","dayGuidePrice":"145","dayInfoFee":"","dayRentPrice":"145","days":1,"guidePriceCommission":"4","kzCount":18,"maxDayPrice":"435","maxMonthPrice":"4350","minDayPrice":"130","minMonthPrice":"2610","monthGuidePrice":"2900","monthInfoFee":"","monthRentPrice":"2900","num":1,"operateFlag":false,"rentPriceCommission":"4","shigh":"10","shighName":"10米","shighNameAndCategoryName":"10米 剪叉","useDate":"2019-05-06","warehouseCode":"DEP1802000106","warehouseName":"南京仓"}],"orderInfo":{"accountPeriod":"30","area":"320114","balanceType":"3","balanceTypeName":"后付","city":"320100","creditLevel":"A","creditScore":"","entAuthStatus":0,"estimatePrice":"500","isTransport":"1","jobAddress":"江苏省南京市雨花台区雨花街道雨花南路2号雨花台区人民政府","jobType":"1","jobTypeName":"钢结构","kilometre":"20","lat":"31.991562671134364","lon":"118.7790948694178","projectCode":"PROJECT107382","projectName":"auto20190506105346","province":"320000","remarks":"","userAuthStatus":0},"storeCode":"DEP18020003","userAuthStatus":0,"userCode":"USER1903029032"}
# # # {"approvalPageFlag": false, "contactCode": "", "contactName": "", "createName": "\u859b\u98de", "customerCode": "CUST112589", "customerName": "\u859b\u98de", "entAuthStatus": 0, "estimatePriceUpdateFlag": 0, "orderDevList": [{"category": "FORK", "categoryName": "\u526a\u53c9", "commissionSubtract": "0", "dayGuidePrice": "145", "dayInfoFee": "", "dayRentPrice": "145", "days": 1, "guidePriceCommission": "4", "kzCount": 18, "maxDayPrice": "435", "maxMonthPrice": "4350", "minDayPrice": "130", "minMonthPrice": "2610", "monthGuidePrice": "2900", "monthInfoFee": "", "monthRentPrice": "2900", "num": 1, "operateFlag": false, "rentPriceCommission": "4", "shigh": "10", "shighName": "10\u7c73", "shighNameAndCategoryName": "10\u7c73 \u526a\u53c9", "useDate": "2019-05-06", "warehouseCode": "DEP1802000106", "warehouseName": "\u5357\u4eac\u4ed3"}], "orderInfo": {"accountPeriod": "30", "area": "320114", "balanceType": "3", "balanceTypeName": "\u540e\u4ed8", "city": "320100", "creditLevel": "A", "creditScore": "", "entAuthStatus": 0, "estimatePrice": "500", "isTransport": "1", "jobAddress": "\u6c5f\u82cf\u7701\u5357\u4eac\u5e02\u96e8\u82b1\u53f0\u533a\u96e8\u82b1\u8857\u9053\u96e8\u82b1\u5357\u8def2\u53f7\u96e8\u82b1\u53f0\u533a\u4eba\u6c11\u653f\u5e9c", "jobType": "1", "jobTypeName": "\u94a2\u7ed3\u6784", "kilometre": "20", "lat": "31.991562671134364", "lon": "118.7790948694178", "projectCode": "", "projectName": "PROJECT107383", "province": "320000", "remarks": "", "userAuthStatus": 0}, "storeCode": "DEP18020003", "userAuthStatus": 0, "userCode": "USER1903029032"}
# #
# #
# # # d = {'list': [1, 2, 3], 1: 123, '111': 'python3', 'tuple': (4, 5, 6)}
# # # for key, value in d.items():
# # #     print(key, value)
# #
# # #
# # # devhours = 107
# # # devhours += 1
# # # print(devhours)
# #
#
def addone():
    with open('devhours.txt', "r") as f:
        last_hours = f.read()
    with open('devhours.txt', "w") as f:
        f.write(str(int(last_hours) + 1))
    return int(last_hours)

a = addone()
print(a)

