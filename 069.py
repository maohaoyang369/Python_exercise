#!/usr/bin/env python
# # -*- coding: utf-8 -*-

# 一个包含多个数字的列表，请使用随机的方式，将每个数字+1后，生成新列表

import random

sentence = [1, 2, 3, 4, 55, 6, 6, 77]
random.shuffle(sentence)
result = []

for i in sentence:
    result.append(i+1)

print(result)



