# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 用嵌套列表的方式，来输出一个矩阵 统计对角线之和
# 1 2 3
# 4 5 6
# 7 8 9

# 1[0][0]      2[0][1]       3[0][2] 
# 4[1][0]      5[1][1]       6[1][2]
# 7[2][0]      8[2][1]       9[2][2]

# 第一种方法

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in matrix:
    # print(i)
    for m in i:
        print(m, end=" ")
    print("")

# 第二种方法

s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(s)):
    for j in range(len(s[i])):
        print(s[i][j], end="  ")
    print("")

# 统计对角线之和

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

result = 0
for i in range(len(m)):
    for j in range(len(m[i])):
        if i == j:
            result += m[i][j]
# print(result)
for i in range(len(m)):
    for j in range(len(m[i])):
        if i + j == 2:
            result += m[i][j]
print(result)
