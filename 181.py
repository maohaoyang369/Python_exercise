# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 把[1,2,3,4,5,6]转换为字典{1:2,3:4,5:6}

example = [1, 2, 3, 4, 5, 6]
result = {}

for i in range(1, len(example), 2):
    result[i] = i+1

print(result)
