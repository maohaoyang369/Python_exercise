#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 从字典中取出值最大的key

# 第一种方法

d = {'a':1,'b':2, 'c':3, 'd':4, 'e':4}

max_value = d['a']
result = []
for m, n in d.items():
    print(m, n)
    if n > max_value:
        max_value = n
        result = []
        result.append(m)
    elif n == max_value:
        result.append(m)
print(result)

# 第二种方法

d = {'a':1,'b':2, 'c':3, 'd':4, 'e':4}

max_value = max(d.values())
result = []
for m, n in d.items():
    # print(m,n)
    if n == max_value:
        result.append(m)
print(result)