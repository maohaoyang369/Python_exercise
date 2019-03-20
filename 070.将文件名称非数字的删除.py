#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将文件名称非数字的删除

import os
import re
import string


path = os.chdir('D:\\python')     # 文件路径


for files in os.listdir(path):
    if ".py" in files:      # 判断文件类型
        # print(files)
        number = str()
        if re.search(r"\d{3}", files):
            numbers = []
            for i in files[0:3]:        # 取前三位
                if i in string.digits:
                    numbers.append(i)
            new_number = "".join(numbers)
            print(new_number)
            os.rename(files, new_number+".py")
        print(files)



