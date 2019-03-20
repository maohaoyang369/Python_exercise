# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 比较两个数的大小，返回不同的结果


def cmp(a, b):
    if not isinstance(a, (int, float))or not isinstance(b, (int, float)):
        raise TypeError
    if a > b:
        return 1
    elif a == b:
        return 0
    else:
        return -1


print(cmp(1, 1))
print(cmp(2, 1))
print(cmp(-1, 1))
