#-*- coding: utf-8 -*-
import xlrd

def ReadExcel(sheetx,rowx,colx):
    #使用xlrd的open_workbook方法打开一个本地的路径的文件
    a=xlrd.open_workbook("E:\dataExcel.xlsx")
    #sheet_by_index读取excel表的第几个sheet
    b=a.sheet_by_index(sheetx)
    #取第几行第几列的值
    c=b.cell_value(rowx,colx)
    return c   #retun返回函数，调用ReadExcel()这个方法的时候返回值c
