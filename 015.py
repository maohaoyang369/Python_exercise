#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 分离list1与list2中相同部分与不同部分

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

same = []
different = []

for i in list1:
    for j in list2:
        if i == j:
            same.append(i)
        elif i != j and:
            different.append(i)
print(same)
print(different)