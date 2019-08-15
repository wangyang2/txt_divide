# -*- coding: UTF-8 -*-
# python_version = 3.5
# convert excel to txt if necessary

import xlrd
import io
list1 = []
data = xlrd.open_workbook('fdc_wenben.xls')
table = data.sheet_by_name(u'Sheet1')

for i in table.col_values(1):
    if len(i) != 0:
        i = i.strip()
        i = i.replace("\n", "")
        list1.append(i)

print(len(list1))

file1 = io.open('wenben.txt', 'w', encoding='utf-8-sig')

for i in list1:
    file1.write(i + "\n" + "\n")
