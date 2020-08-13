#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 8:20
# @Author  : YaoJa
# 输入一个日期到单元格
import xlwt
import  datetime
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('My Sheet')
style = xlwt.XFStyle()  # 初始化样式
style.num_format_str = 'M/D/YY'  # Other options: D-MMM-YY, D-MMM, MMM-YY, h:mm, h:mm:ss, h:mm, h:mm:ss, M/D/YY h:mm, mm:ss
worksheet.write(1, 0, datetime.datetime.now(), style)
workbook.save('Excel_Workbook.xls')


