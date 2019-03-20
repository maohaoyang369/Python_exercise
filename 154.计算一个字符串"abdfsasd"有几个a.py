# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 计算一个字符串"abdfsasd"有几个a

sentence = "abdfsasd"
count = 0
for i in sentence:
    if i == "a":
        count += 1
print("There are ", count)
