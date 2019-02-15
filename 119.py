# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 取出列表的最大值

a = [1, 2, 3, 4]


def max(a):
    max_num = a[0]
    for i in a:
        if i > max_num:
            max_num = i
    return max_num


print(max(a))
