# coding=utf-8
import xlrd
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        """
        :param file_name: excel的文件路径，可以默认存在一个地方
        :param sheet_id: sheet，第一个是0.依次向下
        """
        if file_name:
            self.file_name = file_name  # 传的话就是用传的地址
            self.sheet_id = sheet_id
        else:
            self.file_name = r'D:\all_case\Excel\年龄表.xls'  # 不传的话就用给定的地址
            self.sheet_id = 0  # 0是第一个sheet
        self.data = self.get_data()  # self.data就会excel里面内容的一个对象

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    # 获取某一个单元格的内容
    def get_cell_value(self, row, col):  # col是列。都是从0开始
        return self.data.cell_value(row, col)

    # 写入数据 如下：传入的数据是5,4,100   调用的时候，EXcel不能是打开状态
    def write_value(self, row, col, value):
        """

        :param row: 对应Excel的行数
        :param col: 对应Excel的列数
        :param value: 填入的数值
        :return:
        """
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 获取某一行的内容
    def get_row_values(self, row):
        """

        :param row:
        :return:
        """
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 获取某一列的内容
    def get_cols_data(self, col_id=None):
        if col_id is not None:
            cols = self.data.col_values(col_id)
        else:
            cols = self.data.col_values(0)
        return cols


if __name__ == '__main__':
    opers = OperationExcel()
    print(opers.get_cols_data(0))
