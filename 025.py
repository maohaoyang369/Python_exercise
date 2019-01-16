#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 将列表元素交替地作为建和值来创建字典

sentance = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sentance_dic = {}

if len(sentance) % 2 == 0:
    for i in range(len(sentance)):
        if i % 2 == 0:
            sentance_dic[sentance[i]] = sentance[i+1]

if len(sentance) % 2 == 1:
    for j in range(len(sentance)):
        if j % 2 == 0 and j != len(sentance)-1:
            sentance_dic[sentance[j]] = sentance[j + 1]
        elif j == len(sentance)-1:
            sentance_dic[sentance[j]] = None

print(sentance_dic)

