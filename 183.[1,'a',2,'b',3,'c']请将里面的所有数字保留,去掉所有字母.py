# !/usr/bin/env python
# -*- coding: utf-8 -*-

# [1,"a",2,"b",3,"c"]请将里面的所有数字保留，去掉所有字母

example = [1, "a", 2, "b", 3, "c"]
result = []

for i in example:
    if isinstance(i, (int, float)):
        result.append(i)

print(result)
