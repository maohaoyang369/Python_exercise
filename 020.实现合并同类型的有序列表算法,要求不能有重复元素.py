#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 实现合并同类型的有序列表算法，要求不能有重复元素

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
