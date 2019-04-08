# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 按列表中第一个值的大小进行排序  a = [(-1,),(1,1),(-2,2,3),(2,2)]

a = [(-1,), (1, 1), (-2, 2, 3), (2, 2)]


def func(b):
    return b[0]


a.sort(key=func)
print(a)

# 按列表中元组中的和的大小进行排序 a = [(-1,),(1,1),(-2,2,3),(2,2)]

a = [(-1,), (1, 1), (-2, 2, 3), (2, 2)]


def func(b):
    return sum(b)


a.sort(key=func)
print(a)
