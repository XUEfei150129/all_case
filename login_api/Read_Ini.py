# coding=utf-8
import configparser


class Read_Ini(object):

    def __init__(self):
        """
        声明这个类的时候，就要传入配置文件的地址和节点
        :param node: 配置中选取的节点
        :param file_name: 配置文件的地址
        """
        # if file_name == None:
        # 	file_name = r"D:\ruleUI\config\LocalElement.ini"
        # self.node = node
        # self.cf = self.load_ini(file_name)
        pass

    # 加载文件
    # file_name 要是绝对路径
    def load_ini(self, file_name=r"D:\all_case\login_api\user_name.ini"):
        """
        读取配置文件
        :param file_name: 配置文件的地址
        :return:
        """
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    # 获取用户的姓名，和密码
    #不同的环境，需要更换node值
    def get_value(self, key, node="user_name_password_uat"):
        """
        :param node 对应的是配置文件中的节点
        :param key: 配置文件中页面元素对应的名称
        :return: 元素的选取方式和元素数据
        """

        data = self.load_ini().get(node, key)
        data = data.split(">")
        return data


if __name__ == '__main__':
    read_init = Read_Ini()
    print(read_init.get_value("zhukuankuan"))
