# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 找出一个多维数组的鞍点，即该位置上的元素在该行上最大，在该列上最小，也可能没有鞍点
# [[1,2],[3,4],[5,6]]


def get_row(arr, n):
    return arr[n]


def get_col(arr, n):
    col = []
    for i in arr:
        col.append(i[n])
    return col


# print get_row([[1,2],[3,4],[5,6]],1)
# print get_col([[1,2],[3,4],[5,6]],1)

s = [[1, 2], [3, 4], [5, 6]]

for i in range(len(s)):
    for j in range(len(s[i])):
        if max(get_row(s, i)) == s[i][j] and min(get_col(s, j)) == s[i][j]:
            print("anchor point:%s" % s[i][j])
