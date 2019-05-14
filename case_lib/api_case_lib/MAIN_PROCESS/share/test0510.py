# # ! /usr/bin/env/python3
# # coding=utf-8
# # @Time : 2019/5/10 21:33
# # @Author : XueFei
#
# """
# # 继承
# # 作用：是减少代码。和现实中的继承一样
# # 自己什么也不用做，就可以继承父类的方法
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
# # 再看
# # 也可以自己写一些方法
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
# # 结果：
# # zhangsan is eating...
# # zhangsan is piaoing...20s...done
#
#
# # 再看
# # 重写父类的方法
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
# # man is
#
#
# # 再看
# # 重构了父类的方法
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
#
# # 再看
# # 同一个父类可以被多个子类继承
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
#
#
#
# # 再看：
# # 子类之间的方法不可以相互不可以调用
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
# # 再看
# # 子类重构父类的初始化方法
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
# w1 = Women("chenghua", 26)  #女生还是传两个参数
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
#
# 上面的重构父类还有一种这样的方法（两种写法一样，稍微方便了一点，如果父类的类名字改了，这里就不要改了。）
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
#         # People.__init__(self, name, age)
#         super(Man, self).__init__(name, age)
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
# #结果
# # zhangsan 一出生就有10 money
# # zhangsan is eating...
# # zhangsan is piaoing...20s...done
# # zhangsan is sleeping...
# # man is sleeping
# # chenghua is born a baby...
#
# 经典类和新式类的主要区别体现在在继承上
#
#
# # class People  （经典类）
# class People(object):  # 新式类    经典类和新式类在多继承上的方式有所不同
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
#         # People.__init__(self, name, age)  #经典类的写法
#         super(Man, self).__init__(name, age)  # 新式类的写法
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
# # 结果
# # zhangsan 一出生就有10 money
# # zhangsan is eating...
# # zhangsan is piaoing...20s...done
# # zhangsan is sleeping...
# # man is sleeping
# # chenghua is born a baby...
# """
#
# """
# 多继承
# 多继承 ：不是所有语言都继承多继承的，java是不支持的，python是支持的
#
# # class People  （经典类）
# class People(object):  # 新式类    经典类和新式类在多继承上的方式有所不同
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
# class Relation(object):
#     def make_friends(self, obj):
#         print("%s is making friends with %s" % (self.name, obj.name))
#
#
# class Man(People, Relation):  # 执行的顺序默认是从左到右，实例化的时候，父类如果有实例化参数，会先去找有实例化参数的类
#     def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
#         # People.__init__(self, name, age)  #经典类的写法
#         super(Man, self).__init__(name, age)  # 新式类的写法
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
# class Women(People, Relation):
#     def get_birth(self):
#         print("%s is born a baby..." % self.name)
#
#
# m1 = Man("zhangsan", 8, 10)
#
# w1 = Women("chenghua", 26)
#
# m1.make_friends(w1)  # 因为都继承了Relation
#
# # 结果：
# # zhangsan 一出生就有10 money
# # zhangsan is making friends with chenghua
#
# 再看：看两个父类是如何联系起来的(有点难理解)
#
# # class People  （经典类）
# class People(object):  # 新式类    经典类和新式类在多继承上的方式有所不同
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.friends = []
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
# class Relation(object):
#     def make_friends(self, obj):
#         print("%s is making friends with %s" % (self.name, obj.name))
#         self.friends.append(obj)
#
#
# class Man(People, Relation):  # 执行的顺序默认是从左到右，实例化的时候，父类如果有实例化参数，会先去找有实例化参数的类
#     def __init__(self, name, age, money):  # 重构初始化函数,这样的话，父类和其他子类就不要在传参数了
#         # People.__init__(self, name, age)  #经典类的写法
#         super(Man, self).__init__(name, age)  # 新式类的写法
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
# class Women(People, Relation):
#     def get_birth(self):
#         print("%s is born a baby..." % self.name)
#
#
# m1 = Man("zhangsan", 8, 10)
#
# w1 = Women("chenghua", 26)
#
# m1.make_friends(w1)  # 因为都继承了Relation
# print(m1.friends[0].name)
#
# # 结果：
# # zhangsan 一出生就有10 money
# # zhangsan is making friends with chenghua
# # chenghua
#
#
# 新式类和经典类的区别在哪里：
#
# 就是在多继承上的顺序问题
# py2经典类是按深度优先来继承得，新式类是按广度优先来继承的
# py3经典类和新式类都是统一按广度优先来继承的
#
# class People(object):  # 新式类    经典类和新式类在多继承上的方式有所不同
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.friends = []
#         print("---doens't run ")
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
# class Relation(object):
#     def __init__(self, n1, n2):
#         print("init in relation")
#
#     def make_friends(self, obj):
#         print("%s is making friends with %s" % (self.name, obj.name))
#         self.friends.append(obj)
#
#
# class Man(People, Relation):  # 如果两个都有够着函数的话，谁在前面就执行谁的实例化，从左到右。如果其中一个没有，就执行另外一个的构造函数
#
#     def piao(self):
#         print("%s is piaoing...20s...done" % self.name)
#
#     def sleep(self):
#         People.sleep(self)  # 调用父类的方法，在执行子类的方法，加self就是把自己实例传进去
#         print("man is sleeping")
#
#
# class Women(People, Relation):
#     def get_birth(self):
#         print("%s is born a baby..." % self.name)
#
#
# m1 = Man("zhangsan", 8)
#
# # 结果：
# # init in relation      当Relation在前面时，就去执行Relation，的实例化参数。class Man(Relation,People)
# # ---doens't run        当People在前面时，就去执行People，的实例化参数。class Man(People,Relation)
#
# 再看
# D继承BC，BC都继承A。继承的策略叫“广度优先”，就是先把横向的策略都查完，在往上面A查。python3里面都是广度优先。同样的场景（D继承BC，BC继承A，B里面没有初始化函数，C和A里面有初始化函数）在python2里面就是“深度优先。但是如果A继承于（object）新式类的话，”
# BC里面都有就按D继承的顺序来
# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#
#
# class C(A):
#     def __init__(self):
#         print("C")
#
#
# class D(B, C):
#     pass
#
#
# obj = D()
#
#
# #结果
# # B
#
#
# 再看
# B里面没有就找C
# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     pass
#     # def __init__(self):
#     #     print("B")
#
#
# class C(A):
#     def __init__(self):
#         print("C")
#
#
# class D(B, C):
#     pass
#
#
# obj = D()
#
#
# #结果
# # C
#
#
# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     pass
#     # def __init__(self):
#     #     print("B")
#
#
# class C(A):
#     pass
#     # def __init__(self):
#     #     print("C")
#
#
# class D(B, C):
#     pass
#
#
# obj = D()
#
#
# #结果
# # A
#
#
# 描述一个学校，讲师，学员的3个类，
# 1
# 2
# 3
# """
#
#
# # 1
# # class School(
# #     object):  # 以后写类都是用新式类，虽然py3里面都是按照广度优先。说不定以后就必须要加Object，基类，所有类的类。以后如果要在面向对象里面加点东西，就需要在基类里面加就行了
# #     def __init__(self, name, addr):
# #         self.name = name
# #         self.addr = addr
# #         self.students = []
# #         self.teachers = []
# #
# #     def enroll(self, stu_obj):  # stu_obj学生实例
# #
# #         print("为学员%s 办理注册手续" % stu_obj.name)
# #         self.students.append(stu_obj)
# #
# #
# # class SchoolMember(object):
# #     def __init__(self, name, age, sex):
# #         self.name = name
# #         self.age = age
# #         self.sex = sex
# #
# #     def tell(self):
# #         pass
# #
# #
# # class Teacher(SchoolMember):
# #     def __init__(self, name, age, sex, salary, course):
# #         super(Teacher, self).__init__(name, age, sex)
# #         self.salary = salary
# #         self.course = course
# #
# #     def tell(self):
# #         print("""
# #         ---- info of Teacher : {} ----
# #         Name : {}
# #         Age : {}
# #         Salary : {}
# #         Course : {}
# #         """.format(self.name, self.name, self.age, self.sex, self.salary, self.course))
# #
# #     def teach(self):
# #         print("%s is teaching couese [%s]" % (self.name, self.course))
# #
# #
# # class Student(SchoolMember):
# #     def __init__(self, name, age, sex, stu_id, grade):
# #         super(Student, self).__init__(name, age, sex)
# #         self.stu_id = stu_id
# #         self.grade = grade
# #
# #     def tell(self):
# #         print("""
# #         ---- info of Student : {} ----
# #         Name : {}
# #         Age : {}
# #         Sex : {}
# #         Stu_id : {}
# #         Grade : {}
# #         """.format(self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
# #
# #     def pay_tuition(self, amount):
# #         print("%s has paid tution for $%s" % (self.name, amount))
# #
# #
# # school = School("老男孩IT", "沙河")  # 实例化一个学校
# # t1 = Teacher("Oldboy", 56, "MF", 2000000, "Linux")  # 实例化老师
# # t2 = Teacher("Alex", 22, "M", 3000, "pythonDevOps")  # 实例化老师
# # s1 = Student("Chenhua", 36, "MF", 1001, "pythonDevOps")  # 实例化学生
# # s2 = Student("徐伟", 36, "MF", 1002, "Linux")  # 实例化学生
# #
# # t1.tell()
# # s1.tell()
# # 结果：
# # ---- info
# # of
# # Teacher: Oldboy - ---
# # Name: Oldboy
# # Age: 56
# # Salary: MF
# # Course: 2000000
# #
# # ---- info
# # of
# # Student: Chenhua - ---
# # Name: Chenhua
# # Age: 36
# # Sex: MF
# # Stu_id: 1001
# # Grade: pythonDevOps
#
#
# # 2
# # class School(
# #     object):  # 以后写类都是用新式类，虽然py3里面都是按照广度优先。说不定以后就必须要加Object，基类，所有类的类。以后如果要在面向对象里面加点东西，就需要在基类里面加就行了
# #     def __init__(self, name, addr):
# #         self.name = name
# #         self.addr = addr
# #         self.students = []
# #         self.staffs = []
# #
# #     def enroll(self, stu_obj):  # stu_obj学生实例
# #
# #         print("为学员%s 办理注册手续" % stu_obj.name)
# #         self.students.append(stu_obj)
# #
# #     def hire(self, staff_obj):
# #         self.staffs.append(staff_obj)
# #         print("雇佣新员工%s " % staff_obj.name)
# #
# #
# #
# # class SchoolMember(object):
# #     def __init__(self, name, age, sex):
# #         self.name = name
# #         self.age = age
# #         self.sex = sex
# #
# #     def tell(self):
# #         pass
# #
# #
# # class Teacher(SchoolMember):
# #     def __init__(self, name, age, sex, salary, course):
# #         super(Teacher, self).__init__(name, age, sex)
# #         self.salary = salary
# #         self.course = course
# #
# #     def tell(self):
# #         print("""
# #         ---- info of Teacher : {} ----
# #         Name : {}
# #         Age : {}
# #         Salary : {}
# #         Course : {}
# #         """.format(self.name, self.name, self.age, self.sex, self.salary, self.course))
# #
# #     def teach(self):
# #         print("%s is teaching couese [%s]" % (self.name, self.course))
# #
# #
# # class Student(SchoolMember):
# #     def __init__(self, name, age, sex, stu_id, grade):
# #         super(Student, self).__init__(name, age, sex)
# #         self.stu_id = stu_id
# #         self.grade = grade
# #
# #     def tell(self):
# #         print("""
# #         ---- info of Student : {} ----
# #         Name : {}
# #         Age : {}
# #         Sex : {}
# #         Stu_id : {}
# #         Grade : {}
# #         """.format(self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
# #
# #     def pay_tuition(self, amount):
# #         print("%s has paid tution for $%s" % (self.name, amount))
# #
# #
# # school = School("老男孩IT", "沙河")  # 实例化一个学校
# # t1 = Teacher("Oldboy", 56, "MF", 2000000, "Linux")  # 实例化老师
# # t2 = Teacher("Alex", 22, "M", 3000, "pythonDevOps")  # 实例化老师
# # s1 = Student("Chenhua", 36, "MF", 1001, "pythonDevOps")  # 实例化学生
# # s2 = Student("徐伟", 36, "MF", 1002, "Linux")  # 实例化学生
# #
# # t1.tell()
# #
# # s1.tell()
# #
# # school.hire(t1)
# # school.enroll(s1)
# #
# # print(school.students)
# # print(school.staffs)
#
# # 结果
# # ---- info
# # of
# # Teacher: Oldboy - ---
# # Name: Oldboy
# # Age: 56
# # Salary: MF
# # Course: 2000000
# #
# # ---- info
# # of
# # Student: Chenhua - ---
# # Name: Chenhua
# # Age: 36
# # Sex: MF
# # Stu_id: 1001
# # Grade: pythonDevOps
# #
# # 雇佣新员工Oldboy
# # 为学员Chenhua
# # 办理注册手续
# # [ < __main__.Student
# # object
# # at
# # 0x033AE3D0 >]  #对应的是一个人
# # [ < __main__.Teacher
# # object
# # at
# # 0x033AE390 >]     #对应的是一个人
#
#
# # 3
# class School(
#     object):  # 以后写类都是用新式类，虽然py3里面都是按照广度优先。说不定以后就必须要加Object，基类，所有类的类。以后如果要在面向对象里面加点东西，就需要在基类里面加就行了
#     def __init__(self, name, addr):
#         self.name = name
#         self.addr = addr
#         self.students = []
#         self.staffs = []
#
#     def enroll(self, stu_obj):  # stu_obj学生实例
#
#         print("为学员%s 办理注册手续" % stu_obj.name)
#         self.students.append(stu_obj)
#
#     def hire(self, staff_obj):
#         self.staffs.append(staff_obj)
#         print("雇佣新员工%s " % staff_obj.name)
#
#
# class SchoolMember(object):
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#
#     def tell(self):
#         pass
#
#
# class Teacher(SchoolMember):
#     def __init__(self, name, age, sex, salary, course):
#         super(Teacher, self).__init__(name, age, sex)
#         self.salary = salary
#         self.course = course
#
#     def tell(self):
#         print("""
#         ---- info of Teacher : {} ----
#         Name : {}
#         Age : {}
#         Salary : {}
#         Course : {}
#         """.format(self.name, self.name, self.age, self.sex, self.salary, self.course))
#
#     def teach(self):
#         print("%s is teaching couese [%s]" % (self.name, self.course))
#
#
# class Student(SchoolMember):
#     def __init__(self, name, age, sex, stu_id, grade):
#         super(Student, self).__init__(name, age, sex)
#         self.stu_id = stu_id
#         self.grade = grade
#
#     def tell(self):
#         print("""
#         ---- info of Student : {} ----
#         Name : {}
#         Age : {}
#         Sex : {}
#         Stu_id : {}
#         Grade : {}
#         """.format(self.name, self.name, self.age, self.sex, self.stu_id, self.grade))
#
#     def pay_tuition(self, amount):
#         print("%s has paid tution for $%s" % (self.name, amount))
#
#
# school = School("老男孩IT", "沙河")  # 实例化一个学校
# t1 = Teacher("Oldboy", 56, "MF", 2000000, "Linux")  # 实例化老师
# t2 = Teacher("Alex", 22, "M", 3000, "pythonDevOps")  # 实例化老师
# s1 = Student("Chenhua", 36, "MF", 1001, "pythonDevOps")  # 实例化学生
# s2 = Student("徐伟", 36, "MF", 1002, "Linux")  # 实例化学生
#
# t1.tell()
#
# s1.tell()
#
# school.hire(t1)
# school.enroll(s1)
# school.enroll(s2)  # 再注册一个人
#
# print(school.students)
# print(school.staffs)
# school.staffs[0].teach()  # 让第一个老师教课
#
# for stu in school.students:  # 让每个学生交5000块钱
#     stu.pay_tuition(5000)
#
#
# #结果
# #     ---- info
# #     of
# #     Teacher: Oldboy - ---
# #     Name: Oldboy
# #     Age: 56
# #     Salary: MF
# #     Course: 2000000
# #
# #     ---- info
# #     of
# #     Student: Chenhua - ---
# #     Name: Chenhua
# #     Age: 36
# #     Sex: MF
# #     Stu_id: 1001
# #     Grade: pythonDevOps
# #
# # 雇佣新员工Oldboy
# # 为学员Chenhua
# # 办理注册手续
# # 为学员徐伟
# # 办理注册手续
# # [ < __main__.Student
# # object
# # at
# # 0x018F03F0 >, < __main__.Student
# # object
# # at
# # 0x018F0410 >]
# # [ < __main__.Teacher
# # object
# # at
# # 0x018F03B0 >]
# # Oldboy is teaching
# # couese[Linux]
# # Chenhua
# # has
# # paid
# # tution
# # for $5000
# # 徐伟
# # has
# # paid
# # tution
# # for $5000


a = "nihao"
b = "{}".format(a)
c = a
print(b)
print(c)
