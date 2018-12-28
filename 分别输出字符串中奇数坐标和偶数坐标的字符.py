#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 分别输出字符串中奇数坐标和偶数坐标的字符

sentance = "fkljweoij"
sentance_single = ""
sentance_double = ""

for i in range(len(sentance)):
    if i % 2 == 0:
        sentance_single += sentance[i]
    elif i % 2 == 1:
        sentance_double += sentance[i]

print(sentance_single)
print(sentance_double)
