#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 分离list1与list2中相同部分与不同部分

list1 = [1, 2, 3, 4, 5, 100]
list2 = [3, 4, 5, 6, 7, 8, 9, 100]

same = []
different = []

for i in list1:
    for j in list2:
        if i == j:
            same.append(i)
    if i not in same:
        different.append(i)

for m in list2:
    for n in list1:
        if m == n and m not in same:
            same.append(m)
    if m not in same:
        different.append(m)

print(same)
print(different)