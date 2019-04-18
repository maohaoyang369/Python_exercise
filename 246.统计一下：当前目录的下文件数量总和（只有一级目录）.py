#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计一下：当前目录的下文件数量总和（只有一级目录）

import os.path
import os

file_count = 0

for i in os.listdir("D:\\python36"):
    file_count += 1

print(file_count)

# ----------------------------

file_count = 0
dir_count = 0

for i in os.listdir("e:\\pic"):
    if os.path.isdir(i):
        dir_count += 1
    else:
        file_count += 1

print(file_count)
print(dir_count)
