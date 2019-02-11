#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个list包含10个数字，要求生成新的list，list里面的数都比之前的数多1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in a[:10]:
    # print(i)
    b.append(i+1)
print(b)