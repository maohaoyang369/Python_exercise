# !/usr/bin/env python
# -*- coding: utf-8 -*-

# {1:'a',2:"b",3:'c'}将key和value进行交换，生成一个新字典

example = {1:'a', 2:"b", 3:'c'}
result = {}

for m, n in example.items():
    # print(m,n)
    result[n] = m

print(result)
