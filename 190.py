#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 生成字典{“a”:1,”c”:3,”e”:5,”g”:7,”i”:9}

import string

letters = string.ascii_letters[0:9]
result = {}

for i in range(0, len(letters), 2):
    result[letters[i]] = i+1

print(result)
