#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/4/10 21:24
# @Author : XueFei

"""
程序的3大流程：
    顺序：从上向下，顺序执行代码
    分支(if)：根据条件判断，决定执行代码的分支
    循环(for,while)：让特定的代码重复执行

"""


#
# # 简单条件判断
# age2 = int(input("你今年几岁："))
#
# if age2 >= 18:
#     print("你长大了，你可以进去玩了")
#     print("记得时间不要太长")
# else:
#     print("你还小，回家写作业去吧！！！")
#
# print("看看这句话是不是一直打印")
# #
# # 条件控制加逻辑运算符
# chinese = int(input("请输入你的chinese的成绩："))
# English = int(input("请输入你的English的成绩："))
#
# if chinese >= 80 or English >= 70:
#     print("成绩合格")
# else:
#     print("成绩不合格，请继续努力")
#
# # if elif else
# festival = input("请输入节日：")
# if festival == "情人节":
#     print("买花")
# elif festival == "生日":
#     print("买生日蛋糕")
# elif festival == "元宵节":
#     print("买生日蛋糕")
# else:
#     print("每天都是情人节")
#
# # if 嵌套
# has_ticket = True
# knife_length = 50
#
# if has_ticket:
#     print("检票完成，请通过")
#     if knife_length >= 30:
#         print("但是刀太长了，还是不可以进入")
#     else:
#         print("请进入候车室")
#
# else:
#     print("请先买票奥")
#
# # if嵌套
# number = int(input("请输入一个正整数："))
# if number >= 0:
#     if number % 2 == 0:
#         if number % 3 == 0:
#             print("您输入的数字能整除2，也能整除3")
#         else:
#             print("您输入的数字能整除2，但不能整除3")
#     else:
#         if number % 3 == 0:
#             print("您输入的数字不能整除2，但能整除3")
#         else:
#             print("您输入的数字既不能整除2，也不能整除3")
# else:
#     print("请输入正整数")
#
# # if 实现石头剪刀布
# player = int(input("玩家输入要出的拳--石头（1）/剪刀（2）/布（3）:"))
# computer = random.randint(1, 3)
# print("玩家出的拳头是：%d ———电脑出的拳头是：%d" % (player, computer))
# if ((player == 1 and computer == 2)
#         or (player == 2 and computer == 3)
#         or (player == 3 and computer == 1)):
#     print("玩家赢")
# elif player == computer:
#     print("太巧了，你和电脑出的一样")
# else:
#     print("电脑赢")

# 循环
# for循环和while循环，两者的相同点在于都能循环做一件重复的事情；不同点在于
# for循环是在序列穷尽时停止
# while循环是在条件不成立时停止。


# for循环
# 简单遍历  for的写法
# languages = ["C", "C++", "Perl", "Python"]
# for i in languages:
#     print(i)

# 简单遍历 while写法
# languages = ["C", "C++", "Perl", "Python"]
# i = 0
# while i < len(languages):
#     print(languages[i])
#     i = i + 1
# # 简单遍历
# languages = ["C", "C++", "Perl", "Python"]
# for i in languages:
#     print("第{}门课程是:{}".format(languages.index(i) + 1, i))

#
# # 遍历加判断加运算
# salary_before = [1000, 2000, 15000, 20000]
# salary_after = []
# for i in salary_before:
#     if i >= 15000:
#         salary_after.append(int(0.9 * i))
# print(salary_after)

# # 遍历---列表生成式
# salary_before = [1000, 2000, 15000, 20000]
# salary_after = [int(0.9 * one) for one in salary_before]
# print(salary_after)
# range
# range() 函数可创建一个整数列表，一般用在 for 循环中
# range(start, stop, [step])
# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
# for n in range(50, 101, 5):
#     print(n)

# sumData = 0
# for i in range(1, 101):
#     sumData += i
#
# print(sumData)


# 循环嵌套
# boys = ["mike", "jack", "tom"]
# girls = ["lisa", "linda", "mary"]
# for boy in boys:
#     for girl in girls:
#         print("%s shakes %s" % (boy, girl))
# print("run over")

# for嵌套和range和
# for x in range(1, 10):
#     for y in range(1, x + 1):
#         print("{}*{}={} \t".format(y, x, y * x), end="")  # \t是空格,end="\n"默认，打印的时候换行
#     print("")  # 每个大循环换行

# while循环
# n = 1
# sum = 0
# while n < 101:
#     sum = sum + n
#     n += 1
# print(sum)
#
#
# result = 0
# i = 0
# while i <= 100:
#     if i % 2 == 0:
#         result += i
#     i += 1
# print("0~100之间偶数求和结果 = %d" % result)


# a = input("请输入任意字符：")
# while a != "exit":
#     print("你在循环中，按'exit'退出")
#     a = input("请输入任意字符：")
# print("您已退出")


# numbers = [12, 37, 5, 42, 8, 43, 67, 6886]
# a = []
# b = []
# while len(numbers) > 0:
#     number = numbers.pop()
#     if number % 2 != 0:
#         a.append(number)
#     else:
#         b.append(number)
# print(a, b)

# break和continue的用法
# break的用法
# break是条出整个循环，后面的循环都不要管了
# for i in "python":
#     if i == "h":
#         break
#     print(i)
# p y t


# continue的用法
# continue是条出本次循环，后面的循环继续做
# for i in "python":
#     if i == "h":
#         continue
#     print(i)
# 结果：pyton

# return和print理解

# """
# 在程序开发中，有时候，会希望 一个函数执行结束后，告诉调用者一个结果，以便调用者针对具体的结果做后续的处理
# 返回值 是函数 完成工作后，最后 给调用者的 一个结果
# 在函数中使用 return 关键字可以返回结果
# 调用函数一方，可以 使用变量 来 接收 函数的返回结果
# """
#
x = 1
def a():
    global x
    x = 2
    print("函数里面的x值是:{}".format(x))
# a()
print(f"函数外面的x值是:{x}")
a()
print("函数外面的x值是:%s"%(x))


# class test1:
#     def __init__(self, w):
#         if w > 3:
#             self.a()
#         else:
#             self.b()
#
#     def a(self):
#         print("这是方法a的")
#
#     def b(self):
#         print("这是方法b的")
#
#
# t = test1(6)
