# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计名字列表中，各名字的首字母在名字列表中出现的次数

name = ["Alice", "Monica", "Joha", "Ocean", "Peter", "Mike"]
name_count = {}
result = 0
for i in name:
    # print(i)
    # print(i[0])
    name_count[i[0]] = 0
if name_count[i[0]] in name_count.keys():
    name_count[i[0]] += 1
print(name_count)
