#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 8:07
# @Author  : YaoJa
# 设置单元格宽度
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
worksheet.write(0, 0, 'My Cell Contents')
worksheet.write(0, 1, '今天很开心')
worksheet.write(1, 0, '001')
# 设置单元格宽度
worksheet.col(0).width = 4444
worksheet.col(1).width = 4444
worksheet.row(0).height = 2222
workbook.save('cell_width.xls')
