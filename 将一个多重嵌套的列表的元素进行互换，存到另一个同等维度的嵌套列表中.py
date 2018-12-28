#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个多重嵌套的列表的元素进行互换，存到另一个同等维度的嵌套列表中
# 例如：[[1,2,3],[4,5,6]]互换后变成[[1,4],[2,5],[3,6]]

sentance = [[1, 2, 3], [4, 5, 6]]
result = [[0,0], [0,0], [0,0]]

for i in range(len(sentance)):
    # print(i)
    for j in range(len(sentance[i])):
        # print(j)
        print(sentance[i][j])
        result[j][i] = sentance[i][j]
    # result[2].append(sentance[i][j])
print(result)
    # print(i[0],i[1])
    # for m in i:
    #     print(m)


