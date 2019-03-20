# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成一个列表["1a","2b","3c","4d","5e"]

sentence = []

for i in range(1, 6):
    sentence.append(str(i)+chr(97+i-1))
print(sentence)
