# !/usr/bin/env python
# -*- coding: utf-8 -*-

# a = [-1,2,3,-3,0,-5,5]  生成一个列表，-1左边是小于它的，右边是大于它的

a = [-1, 2, 3, -3, 0, -5, 5]

result = []

for i in range(len(a)):
    if a[i] < -1:
        result.insert(0, a[i])
    if a[i] >= -1:
        result.append(a[i])

print(result)
