# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 三个数字排序


def max(a):
    max_num = a[0]
    for i in a:
        if i > max_num:
            max_num = i
    return max_num


s = [2, 5, 9]
a = max(s)
s.remove(a)
b = max(s)
s.remove(b)
c = s[0]
print(a, b, c)
