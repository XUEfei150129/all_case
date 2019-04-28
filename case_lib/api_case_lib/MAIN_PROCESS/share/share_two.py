#! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/4/6 20:04
# @Author : XueFei


import random
import string
from datetime import datetime

"""
Python语言里面一切数据类型都是对象
对象就是语言描述中涉及的物体。

在Python语言中也会涉及到 对象， 这些对象 包含了一定的 数据 信息。
Python语言中，所有的 数据 都被称之为 对象。

我们写的Python代码， 就是要 处理各种 对象 ，从而完成具体的任务。
常见数据（对象）（数据对象）类型：
    整数， 比如 3
    小数（也叫浮点数） ，比如 6.5
        Python语言中的 数字对象 是可以进行 数学运算的。
    字符串 ， 比如 ‘你好’
        内置函数，获取字符串长度。获取类型
        常用方法：
            .count .startswith .endswith .find .isalpha .isdigit -str.join .split .lower
            .upper .replace .strip

    列表，比如 [1, 2, ‘你好’]
        常用方法：


    元组，比如 (1, 2, ‘你好’)
    字典，比如 {1:’mike’, 2:’jack’}


"""

#整数类型
a = "22"
print(id(a))

a = 0
print(a)

a = -12
print(a)

# 浮点数，就是带小数点的数字
a = 22.5
print(a)

a = 0.0
print(a)

a = -12.6
print(a)

# 数学运算
print(8 + 5)
# 5 + 8 就是一个表达式，被 Python解释器 执行后，会产生一个新的整数 对象 13。
print(999 - 111)

print(8 * 9)

print(9 / 8)

print(9 // 4)

print(7 % 4)

print(10 ** 2)

print(5 * 4 / 2 + 1)







a = "11 23DSSDFS"
print(a.split(" ")[1])

b = a.count("SS")
print(b)

str1 = "abcdefa"
print("%%%" * 50)
print(len(str1))
print(str1.find("a"))

alist = ["i", "like", "football"]
print("-".join(alist))

tel = input("请输入需要查询的手机号：")
if tel.isdigit():
    if len(tel) == 11 and int(tel[0]) == 1:
        if tel.startswith("139") or tel.startswith("187"):
            print("中国移动")
        elif tel.startswith("156") or tel.startswith("187"):
            print("中国联通")
        else:
            print("中国电信")
    else:
        print("您的手机位数不对！！！或首位出错")
else:
    print("请输入的手机号码有非法字符")

a = "45456"
b = a.startswith("123")
print(b)

a = "456123hj"
b = a.find("h", 2)
print(b)



#
a = input("请输入您的姓名：")
print(len(a))
name = a.strip()
print(len(name))







a = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=10))
print(a)



a = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(a)












name_list = ["zhangsan", "lisi", "wangwu"]
# 根据索引取值
print(name_list[2])

# 根据值取索引
print(name_list.index("lisi"))

# 修改列表中指定位置的数据
name_list[2] = "李四"
print(name_list)

# append方法可以向列表的末尾增加数据
name_list.append("王小二")
print(name_list)

# .insert方法可以向列表的指定位置增加数据
name_list.insert(0, "女神")
print("%" * 59)
print(name_list)
# .extend方法可以将其他列表中的内容，追加到当前列表的末尾
a = [1, 3, "python", "hello"]
b = [3, 4, "who"]
a.extend(b)
print(a)

# .remove方法可以删除列表中指定的数据,多个相同的数据，只能删第一个
c = ["xuefei", "zhangyuwen", "你好", "你好", "python", "hello"]
c.remove("你好")
print(c)

# .pop方法默认可以把列表中最后一个元素删除
c = ["xuefei", "zhangyuwen", "你好", "python", "hello"]
c.pop()
print(c)

#  .pop方法可以指定索引删除元素
c = ["xuefei", "zhangyuwen", "你好", "python", "hello"]
c.pop(2)
print(c)

# .clear方法可以清空列表
c = ["xuefei", "zhangyuwen", "你好", "python", "hello"]
c.clear()
print(c)

# count 方法可以统计列表中某一元素出现的次数
name_list = ["zhangsan", "lisi", "wangwu", "zhangsan"]
counts = name_list.count("zhangsan")
print("在列表中张三出现的次数是%s" % counts)

# .del函数可以删除列表
c = ["xuefei", "zhangyuwen", "你好", "python", "hello"]

del c[0]
print(1111111111111111111111111111)
print(c)

# len()函数可以统计列表里面元素的个数
c = ["xuefei", "zhangyuwen", "你好", "python", "hello"]
print("列表c里面包含的元素个数是：%s" % (len(c)))

# 介绍两个跟列表排序相关的方法 .sort()
# 升序
c = ["xuefei", "zhangyuwen", "2", "python", "hello"]
d = [2, 1, 4, 6, 2, 3, 67]
c.sort()
d.sort()
print(c)
print(d)

# 降序
c = ["xuefei", "zhangyuwen", "python", "hello"]
d = [2, 1, 4, 6, 2, 3, 67]
c.sort(reverse=True)
d.sort(reverse=True)
print(c)
print(d)

# 逆序（反转）
c = ["xuefei", "zhangyuwen", "python", "hello"]
d = [2, 1, 4, 6, 2, 3, 67]
c.reverse()
d.reverse()
print(c)
print(d)

def contain(a, b):
    num = a.find(b)
    if num != -1:
        print("{}包含{}".format(a, b))
    else:
        raise Exception(f"{a}不包含{b}")


a = "qwesfdfddf"
b = "qwe233"
contain(a, b)


import random
b = []
for i in range(10000):
    a = random.randint(0, 1)
    b.append(a)
print("1出现的次数是:{}次".format(b.count(1)))
print(f"0出现的次数是:{b.count(0)}次")

