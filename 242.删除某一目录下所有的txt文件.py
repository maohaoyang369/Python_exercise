# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 算法：
# 取出某个目录内，1小时内新建的所有文件名。
# 遍历这个目录，取到所有的文件
# 每个文件用stat取到创建时间
# 用创建时间和当前时间去比对，是否小于3600
# 放到一个列表里面

import os
import time
import os.path

dir_path = os.chdir("d:\\python\\pic11111")
dir_path = os.getcwd()
current_timestamp = time.time()
result = []

for i in os.listdir(dir_path):
    # print(i)
    if os.path.isfile(i):
        if current_timestamp-os.stat(i).st_ctime <= 3600:
            result.append("d:\\python\\pic11111"+"\\"+i)

print(result)
