# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 202.[1,2,3,4,5]  确定3 在第几个位置

a = [1, 2, 3, 4, 5]


def find_element(l, elment):
    for i in range(len(l)):
        if l[i] == elment:
            return i


print(find_element([1, 2, 3, 4, 5], 3))
print(find_element([1, 2, 3, 4, 5], 5))
