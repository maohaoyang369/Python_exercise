# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 从1遍历到10，计算有几个偶数

count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print("一共有", count, "个偶数")
