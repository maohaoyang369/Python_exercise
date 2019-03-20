# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个函数，实现两个数相加，函数参数a,b


def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return None
    else:
        result = a + b
        return result


print(add(3, 4))
print(add("3", 4))
