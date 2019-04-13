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
import random


# 简单条件判断
age = int(input("你今年几岁："))

if age >= 18:
    print("你长大了，你可以进去玩了")
    print("记得时间不要太长")
else:
    print("你还小，回家写作业去吧！！！")

print("看看这句话是不是一直打印")
#
# 条件控制加逻辑运算符
chinese = int(input("请输入你的chinese的成绩："))
English = int(input("请输入你的English的成绩："))

if chinese >= 80 or English >= 70:
    print("成绩合格")
else:
    print("成绩不合格，请继续努力")

# if elif else
festival = input("请输入节日：")
if festival == "情人节":
    print("买花")
elif festival == "生日":
    print("买生日蛋糕")
elif festival == "元宵节":
    print("买生日蛋糕")
else:
    print("每天都是情人节")

# if 嵌套
has_ticket = True
knife_length = 50

if has_ticket:
    print("检票完成，请通过")
    if knife_length >= 30:
        print("但是刀太长了，还是不可以进入")
    else:
        print("请进入候车室")

else:
    print("请先买票奥")

# if嵌套
number = int(input("请输入一个正整数："))
if number >= 0:
    if number % 2 == 0:

        if number % 3 == 0:
            print("您输入的数字能整除2，也能整除3")
        else:
            print("您输入的数字能整除2，但不能整除3")
    else:
        if number % 3 == 0:
            print("您输入的数字不能整除2，但能整除3")
        else:
            print("您输入的数字既不能整除2，也不能整除3")
else:
    print("请输入正整数")

# if 实现石头剪刀布
player = int(input("玩家输入要出的拳--石头（1）/剪刀（2）/布（3）:"))
computer = random.randint(1, 3)
print("玩家出的拳头是：%d ———电脑出的拳头是：%d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家赢")
elif (player == computer):
    print("太巧了，你和电脑出的一样")
else:
    print("电脑赢")
