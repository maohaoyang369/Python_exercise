# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将列表中[[1,2,3],[4,5,6],[7,8,9]]的所有奇数进行求和

example = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = 0

for i in example:
    # print(i)
    for j in i:
        # print(j)
        if j % 2 == 1:
            result += j

print(result)
