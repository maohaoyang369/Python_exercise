# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 使用for循环生成一个二维列表，[[1,2,3],[4,5,6],[7,8,9]]

result = []
result_new = []

for i in range(1, 10):
    # print(i)
    result.append(i)
for j in range(0, 9, 3):
    result_new.append(result[j:j+3])

print(result_new)
