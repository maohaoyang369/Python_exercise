# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 把列表中所有的数字求和，字符串数字也要算上 a = [1,2,3,[4,5,6],{1:6,2:8,"a":"12"}]

a = [1, 2, 3, [4, 5, 6], {1: 6, 2: 8, "a": "12"}]
result = 0
for i in a:
    if isinstance(i, int):
        result += i
    if isinstance(i, list):
        for j in i:
            if isinstance(j, int):
                result += j
    if isinstance(i, dict):
        for j in i.keys():
            if isinstance(j, int):
                result += j
        for j in i.values():
            if isinstance(j, int):
                result += j
            else:
                if j.isdigit():
                    result += int(j)

print(result)
