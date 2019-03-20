# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 统计名字列表中，各名字的首字母在名字列表中出现的次数

name = ["Alice", "Monica", "Joha", "Ocean", "Peter", "Mike", "Jon", "Msfsd"]
name_count = []
result = {}
for i in name:
    name_count.append(i[0])
for j in name_count:
    # print(j)
    result.setdefault(j, 0)     # setdefault 键不存在于字典中，将会添加键和指定的值
    result[j] += 1

# print(name_count)
print(result)
