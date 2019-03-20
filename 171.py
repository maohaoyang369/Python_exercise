# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成一个列表["z1","y2","x3","w4","v5"]

sentence = []

for i in range(1, 6):
    sentence.append(chr(122-i+1)+str(i))
print(sentence)
