#!/usr/bin/env python
# # -*- coding: utf-8 -*-


def merge_list(list_a, list_b):
    mergelist = []
    for i in list_a:
        # print(i)
        mergelist.append(i)
    for j in list_b:
        if j not in mergelist:
            mergelist.append(j)
    return mergelist


print(merge_list([1, 2, 3], [1, 2, 78, 9]))
