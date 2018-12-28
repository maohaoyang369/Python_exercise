#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个字典的 key和value 互换

sentance = {1: 2, 2: 3, 4: 5}
result = {}

for i, j in sentance.items():
    result[j] = i

print(result)