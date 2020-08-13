#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 7:49
# @Author  : YaoJa
# 创建一个xecel


import xlwt
# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行、列、值
worksheet.write(1, 0, label='this is test')

# 保存
workbook.save('Excel_test.xls')
