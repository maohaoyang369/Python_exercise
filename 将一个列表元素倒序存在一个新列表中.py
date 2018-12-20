#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 将一个列表元素倒序存在一个新列表中

a = [1, 2, 3, 4, 5]
b = []
for i in a:
    b.insert(0, i)
print(b)