# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 求25这个数字可以整除的所有数字

num = 25
result = []
for i in range(1, 26):
    if num % i == 0:
        result.append(i)
print(result)
