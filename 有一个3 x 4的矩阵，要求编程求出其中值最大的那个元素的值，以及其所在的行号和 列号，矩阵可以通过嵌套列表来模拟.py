#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 有一个3 x 4的矩阵，要求编程求出其中值最大的那个元素的值，
# 以及其所在的行号和列号，矩阵可以通过嵌套列表来模拟


# 遍历嵌套列表的每一个元素
# 与初始变量值进行比较
# 保存下最大的元素
# 取出对应的行号和列号

array = [[1, 2, 3], [4, 14, 6], [7, 8, 9]]
max_value = array[0][0]
x = 0
y = 0

for i in range(len(array)):
    for j in range(len(array[i])):
        # print(j)
        if array[i][j] > max_value:
            max_value = array[i][j]
            x = i
            y = j
print(max_value)
print(x, y)

