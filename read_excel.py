#!/usr/local/bin/python3
#coding:utf-8
# @Time    : 2019/1/24 14:20
# @Author  : Hollow
# @FileName: test11.py
# @Software: PyCharm


import xlrd

# #打开excel表格
# data = xlrd.open_workbook('data.xlsx')
# table = data.sheet_by_name(u'Sheet1') #通过名称获取
#
#
# nrows = table.nrows  #获取总行数
# ncols = table.ncols  #获取总列数
#
# print(table.row_values(1))
# print(table.col_values(1))

class ExcelUtil():
    '''数据初始化'''
    def __init__(self,excelPath,sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName) #通过名称获取
        #获取第一行作为key值
        self.key = self.table.row_values(0)
        #获取总行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print('总行数小于1')
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                #从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.key[x]] = values[x]
                r.append(s)
                j+=1
            return r

if __name__=="__main__":
    filepath = "D:\\PycharmProjects\\untitled3\\data.xlsx"
    sheetName = 'Sheet1'
    data = ExcelUtil(filepath,sheetName)
    print(data.dict_data())






