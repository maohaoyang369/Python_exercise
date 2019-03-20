#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将文件前面加上三位数字

import os
import re

path = os.chdir('D:\\python\\exercise')

i = 1

for files in os.listdir(path):
    if ".py" in files:
        # print(files)
        number = str()
        # if re.search(r"\d{3}", files):
        #     break
        if i // 100 != 0:
            number = str(i)
            # print(str(i))
            # print(str(i // 100) + str(i // 10 % 10) + str(i % 10))
        elif (i // 10 % 10) != 0:
            # print("0" + str(i))
            number = "0" + str(i)
            # print("0" + str(i // 10 % 10) + str(i % 10))
        elif (i % 10) != 0 and (i % 10) != 1 and (i % 10) != 2 and (i % 10) != 3:
            number = "00" + str(i % 10)
            # print("00" + str(i % 10))

        os.rename(files, number+files)
        i += 1
        print(number+files)

