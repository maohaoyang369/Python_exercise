# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 将一个列表[1,2,3,4,5]每个元素值扩大10倍后，在每个元素后面加上“abc”三个字母放到列表里面

sentence = [1, 2, 3, 4, 5]
sentance_new = []

for i in sentence:
    sentance_new.append(str(i*10)+"abc")

print(sentance_new)
