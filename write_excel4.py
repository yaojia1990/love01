#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/4 8:31
# @Author  : YaoJa
import xlwt
# 指定file以tf-8格式打开
file = xlwt.Workbook(encoding='utf-8')
# 指定打开的文件名
table = file.add_sheet('data')
# 字典数据
data = {
    '1': ['张三', 150, 120, 100],
    '2': ['李四', 90, 99, 95],
    '3': ['王五', 60, 66, 68]
}

ldata = []
# for循环指定取出key值存入num中
# num = [a for a in data]
num = []
for a in data:
    num.append(a)
# 字典数据取出后需要先排序
num.sort()
# print(num)
# for循环将data字典中的键和值分批的保存在ldata中
for x in num:
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)
print(ldata)

# 将数据写入文件,i是enumerate()函数返回的序号数
# i,j等于excel里面的行row 列col
for i, p in enumerate(ldata):
    for j, q in enumerate(p):
        print(i, j, q)
        table.write(i, j, q)
file.save('data.xls')

