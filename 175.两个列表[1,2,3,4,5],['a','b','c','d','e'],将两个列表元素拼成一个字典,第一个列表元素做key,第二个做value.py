# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 两个列表[1,2,3,4,5],["a","b","c","d","e"]，将两个列表元素拼成一个字典，第一个列表元素做key，第二个做value

sentance_a = [1, 2, 3, 4, 5]
sentance_b = ["a", "b", "c", "d", "e"]
sentence = {}

for i in range(5):
    sentence[sentance_a[i]] = sentance_b[i]

print(sentence)
