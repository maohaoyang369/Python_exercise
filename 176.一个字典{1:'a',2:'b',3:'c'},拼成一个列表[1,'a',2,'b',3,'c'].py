# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个字典{1:"a",2:"b",3:"c"}，拼成一个列表[1,"a",2,"b",3,"c"]

sentence = {1:"a", 2:"b", 3:"c"}
result = []

for m, n in sentence.items():
    # print(m)
    # print(n)
    result.append(m)
    result.append(n)

print(result)
