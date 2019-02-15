# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 求矩阵四个边的和
# 1  2   3   4   5
# 1  2   3   4   5
# 1  2   3   4   5
# 1  2   3   4   5
# 1  2   3   4   5

l = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]

for i in range(len(l)):                # 求出矩阵
    for j in range(len(l[i])):
        print(l[i][j], end="  ")
    print("")

result = 0
for i in range(len(l)):
    for j in range(len(l[i])):
        if i == 0 or i == 4:
            result += l[i][j]
        else:
            if j == 0 or j == 4:
                result += l[i][j]

print(result)
