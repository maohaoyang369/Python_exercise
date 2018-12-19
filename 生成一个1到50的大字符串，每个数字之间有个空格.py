#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成一个1到50的大字符串，每个数字之间有个空格

result = ""
for i in range(1,51):
    if i == 51:
        result = result + str(i)
    result = result + str(i) + " "
print(result)