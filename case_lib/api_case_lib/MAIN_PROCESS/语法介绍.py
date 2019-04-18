# import keyword
#
# a = "ghjghjkg456123hj"
# b = a.find("h", 2)
#
# print(b)
#
# command = input("请输入命令:")
# while command != 'exit':
#     print(f'输入的命令  是{command}')
#     command = input("  请输入命令")
#
# print("hjkjkhhjkhjkjkhjkjkhjk")
#
#
# def contain(a, b):
#     num = a.find(b)
#     print(num)
#     if num != -1:
#         print(f"{b}包含于{a}")
#     else:
#         raise Exception("{}不包含{}".format(a, b))
#
#
# a = "123456"
# b = "125"
# contain(a, b)
#
#
#


# import traceback
# import time
# from appium import webdriver  # webdriver是基于selenium扩展的一个对象

a = """
废掉一个人最隐蔽的方法：
    就是让他忙碌到没有时间成长，看似每天8点钟上班，晚上10点钟回家
    非常的努力，觉得自己过得非常的充实。
    过去一年半年，自己成长多少，自己清楚。
                                                  ---席慕蓉
"""

# a = "123"
# b = "qwddfdsfdsfddf"
# print("..www.".join(b))
# import os
#
# print(os.getcwd())

# 查看当前的绝对路径
# print("****" * 8)
# print(os.path.abspath('.'))  # 当前目录
# print(os.path.abspath('..'))  # 上层目录
# print(os.path.abspath('./语法介绍.py'))  # 当前文件
# print(os.path.abspath('./test1'))  # 子目录

# desired_caps = {}  # 存储一些配置信息，通过字典键值对来存。吧配置信息传递给appium server
# desired_caps['platformName'] = 'Android'  # 指定自动化的设备
# desired_caps['platformVersion'] = '8.0'  # 设备的操作系统版本
# desired_caps['deviceName'] = 'test'  # 对安卓没啥用，但是不能不写
# # app安装包的路径，如果手机没装的话，会帮你装上。如果装好，可以注释
# # desired_caps['app'] = r'D:\自动化测试用的app\app-Android-release-3.5.2.apk'
# desired_caps['appPackage'] = 'com.znlhzl.znlhzl'  # 应用的包名
# # 告诉appium启动的Activity的名字，安卓应用是由多个Activity组成的
# desired_caps['appActivity'] = 'com.znlhzl.znlhzl.ui.main.SplashActivity'
# desired_caps['unicodeKeyboard'] = True  # 输入中文的话，这个就要打开。给appium自动化用的。输入非ask码用的
# desired_caps['resetKeyboard'] = True  # 配合上面一起用的，据说可以还原之前的输入法
# desired_caps['noReset'] = True  # 非常重要。如果不设置的话。每次运行都会清空里面的数据。
# desired_caps['newCommandTimeout'] = 6000  # 主要是与服务端appiumserver连接的时间，防止断开。6000s
# # 启动Remote RPC
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# print(isinstance(1.1, str))
# False
# print(isinstance(11, int))
# True

# alist = ["a", "b", "c", "d", "e", "f"]
# for i in range(0, 2):  # 两次 0 1
#     for name in alist:
#         print(name)
#         if name == "b":
#             break
# print("over")


# def func():
#     "这个是函数的注释"
#     print("函数")
#
#
# print(func.__doc__)
# # 结果：这个是函数的注释
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n // x)
#             break
#     else:
#         print(n, 'is a prime number')


# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print("%d*%d=%d" % (col, row, col * row), end="\t")  # 打印99乘法表
#         col += 1
#     print("")
#     row += 1


# for x in range(1, 10):
#     for y in range(1, x + 1):
#         print("{}*{}={} \t".format(y, x, y * x), end="")
#     print("")

# alist = ["a", "b", "c", "d", "e", "f"]
# for i in range(0, 2):  # 两次 0 1
#     for name in alist:
#         print(name)
#         if name == "b":
#             break
# print("over")


# boys = ["mike", "jack", "tom"]
# girls = ["lisa", "linda", "mary"]
# for boy in boys:
#     for girl in girls:
#         print("%s shakes %s" % (boy, girl))
# print("run over")


# def hello(a, b):
#     print(a + b)
#     return a ** b
#
#
# # hello(2, 4)
#
# s = hello(2, 89)
# print(s + 1)


# print("{}*{}={} \t".format(2, 3, 6), end="")
print("sadsads\ta",end="sss")