# -*- coding:UTF-8 -*-
# python_version = 3.5

filecount = 0

file1 = open('wenben.txt', 'r', encoding='utf-8-sig')
fw = open(r'C:\Users\viruser.v-desktop\Desktop\fdc_wenben\fdc_txt_result'+str(filecount)+'.txt', 'w+', encoding='utf-8-sig')
for i in file1:
    print(len(i))
    if len(i) == 1:
        filecount += 1
        fw = open(r'C:\Users\viruser.v-desktop\Desktop\fdc_wenben\fdc_txt_result'+str(filecount)+'.txt', 'w+', encoding='utf-8-sig')
    else:
        fw.write(i)
