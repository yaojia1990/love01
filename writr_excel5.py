#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 8:59
# @Author  : YaoJa
# excel写入追加
import xlwt
import xlrd
from xlutils.copy import copy


def write_excel_xls(path, sheet_name, value):
    # 获取需要写入数据的行数
    index = len(value)
    # 新建一个工作簿
    workbook = xlwt.Workbook(encoding='utf-8')
    # 在工作簿中新建一个表格
    sheet = workbook.add_sheet(sheet_name)
    # 向表格中写入数据（对应的行和列）
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])
        # 保存工作簿
    workbook.save('path.xls')
    print('xls格式表格写入数据成功')


def write_excel_xls_append(path, value):
    # 获取需要写入数据的行数
    index = len(value)
    # 打开工作簿
    workbook = xlrd.open_workbook(path)
    # 获取工作簿中的所有表格
    sheets = workbook.sheet_names()
    # 获取工作簿中所有表格中的第一个表格
    worksheet = workbook.sheet_by_name(sheets[0])
    # 获取表格中已存在的数据的行数
    rows_old = worksheet.nrows
    # 将xlrd对象拷贝转化为xlwt对象
    new_workbook = copy(workbook)
    # 获取转化后工作簿中的第一个表格
    new_worksheet = new_workbook.get_sheet(0)
    for i in range(0, index):
        for j in range(0, len(value[i])):
            # 追加写入数据，注意是从i+rows_old行开始写入
            new_worksheet.write(i+rows_old, j, value[i][j])
    new_workbook.save(path)
    print('xls格式表格【追加】写入数据成功')

book_name_xls = 'xls格式测试工作簿'
sheet_name_xls = 'xls格式测试表'
value_title = [['姓名', '性别', '年龄', '城市', '职业']]
value1 = [["张三", "男", "19", "杭州", "研发工程师"],
          ["李四", "男", "22", "北京", "医生"],
          ["王五", "女", "33", "珠海", "出租车司机"], ]

value2 = [["Tom", "男", "21", "西安", "测试工程师"],
          ["Jones", "女", "34", "上海", "产品经理"],
          ["Cat", "女", "56", "上海", "教师"]]

write_excel_xls(book_name_xls, sheet_name_xls, value_title)