# !/usr/bin/env python
# -*- coding: utf-8 -*-

# {1:'a',2:"b",3:'c'}，将所有key的数字求和，将value的所有字符串拼接为一个字符串

example = {1:'a', 2:"b", 3:'c'}
count = 0
result = ""

for m, n in example.items():
    # print(m,n)
    count += m
    result += n

print(count)
print(result)
