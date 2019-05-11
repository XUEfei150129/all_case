# ! /usr/bin/env/python3
# coding=utf-8
# @Time : 2019/5/10 21:33
# @Author : XueFei

"""
# 继承
# 作用：是减少代码。和现实中的继承一样
# 自己什么也不用做，就可以继承父类的方法
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    pass


m1 = Man("zhangsan", 8)
m1.eat()
#结果：
# zhangsan is eating...

# 再看
# 也可以自己写一些方法
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def piao(self):
        print("%s is piaoing...20s...done" % self.name)


m1 = Man("zhangsan", 8)
m1.eat()
m1.piao()
# 结果：
# zhangsan is eating...
# zhangsan is piaoing...20s...done


# 再看
# 重写父类的方法
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        print("man is sleeping")


m1 = Man("zhangsan", 8)
m1.eat()
m1.piao()
m1.sleep()

#结果
# zhangsan is eating...
# zhangsan is piaoing...20s...done
# man is


# 再看
# 重构了父类的方法

class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
        print("man is sleeping")


m1 = Man("zhangsan", 8)
m1.eat()
m1.piao()
m1.sleep()
#结果
# zhangsan is eating...
# zhangsan is piaoing...20s...done
# zhangsan is sleeping...
# man is sleeping



# 再看
# 同一个父类可以被多个子类继承
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
        print("man is sleeping")


class Women(People):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("zhangsan", 8)
m1.eat()
m1.piao()
m1.sleep()

w1 = Women("chenghua", 26)
w1.get_birth()

# 结果：
# zhangsan is eating...
# zhangsan is piaoing...20s...done
# zhangsan is sleeping...
# man is sleeping
# chenghua is born a baby...





# 再看：
# 子类之间的方法不可以相互不可以调用
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
        print("man is sleeping")


class Women(People):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("zhangsan", 8)
m1.eat()
m1.piao()
m1.sleep()

w1 = Women("chenghua", 26)
w1.get_birth()
w1.piao()           #就不可以调用
# 结果：AttributeError: 'Women' object has no attribute 'piao'

# 再看
# 子类重构父类的初始化方法
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
        People.__init__(self, name, age)
        self.money = money
        print("%s 一出生就有%s money" % (self.name, self.money))

    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
        print("man is sleeping")


class Women(People):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("zhangsan", 8, 10)
m1.eat()
m1.piao()
m1.sleep()

w1 = Women("chenghua", 26)  #女生还是传两个参数
w1.get_birth()

# 结果：
# zhangsan 一出生就有10 money
# zhangsan is eating...
# zhangsan is piaoing...20s...done
# zhangsan is sleeping...
# man is sleeping
# chenghua is born a baby...


上面的重构父类还有一种这样的方法（两种写法一样，稍微方便了一点，如果父类的类名字改了，这里就不要改了。）
class People:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
        # People.__init__(self, name, age)
        super(Man, self).__init__(name, age)
        self.money = money
        print("%s 一出生就有%s money" % (self.name, self.money))

    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
        print("man is sleeping")


class Women(People):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("zhangsan", 8, 10)
m1.eat()
m1.piao()
m1.sleep()

w1 = Women("chenghua", 26)
w1.get_birth()

#结果
# zhangsan 一出生就有10 money
# zhangsan is eating...
# zhangsan is piaoing...20s...done
# zhangsan is sleeping...
# man is sleeping
# chenghua is born a baby...

经典类和新式类的主要区别体现在在继承上


# class People  （经典类）
class People(object):  # 新式类    经典类和新式类在多继承上的方式有所不同
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Man(People):
    def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
        # People.__init__(self, name, age)  #经典类的写法
        super(Man, self).__init__(name, age)  # 新式类的写法
        self.money = money
        print("%s 一出生就有%s money" % (self.name, self.money))

    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
        print("man is sleeping")


class Women(People):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("zhangsan", 8, 10)
m1.eat()
m1.piao()
m1.sleep()

w1 = Women("chenghua", 26)
w1.get_birth()

# 结果
# zhangsan 一出生就有10 money
# zhangsan is eating...
# zhangsan is piaoing...20s...done
# zhangsan is sleeping...
# man is sleeping
# chenghua is born a baby...


多继承
多继承 ：不是所有语言都继承多继承的，java是不支持的，python是支持的

84节25分
"""


# class People  （经典类）
class People(object):  # 新式类    经典类和新式类在多继承上的方式有所不同
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("%s is eating..." % self.name)

    def sleep(self):
        print("%s is sleeping..." % self.name)

    def talk(self):
        print("%s is talking..." % self.name)


class Relation(object):
    def make_friends(self, obj):
        print("%s is making friends with %s" % (self.name, obj.name))


class Man(People, Relation):
    def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
        # People.__init__(self, name, age)  #经典类的写法
        super(Man, self).__init__(name, age)  # 新式类的写法
        self.money = money
        print("%s 一出生就有%s money" % (self.name, self.money))

    def piao(self):
        print("%s is piaoing...20s...done" % self.name)

    def sleep(self):
        People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
        print("man is sleeping")


class Women(People, Relation):
    def get_birth(self):
        print("%s is born a baby..." % self.name)


m1 = Man("zhangsan", 8, 10)

w1 = Women("chenghua", 26)

m1.make_friends(w1)
