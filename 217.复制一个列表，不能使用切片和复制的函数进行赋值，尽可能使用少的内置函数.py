# !/usr/bin/env python
# -*- coding: utf-8 -*-

a = [1, 2, 3, 4, 5]
arr_length = 0
for i in a:
    arr_length += 1


def iter_arr(n):
    arr = []
    i = 0
    while i <= n-1:
        arr += [i]
        i += 1
    return arr


result = [""]*arr_length
for i in iter_arr(arr_length):
    result[i] = a[i]

print(result)
