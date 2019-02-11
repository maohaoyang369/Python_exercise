#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 找出s ="aabbccddffffxxxx"中，出现次数最多的字母

# 第一种方法

s = "aabbccddxxxxffff"
letters = []
times = 0
for i in s:
    if s.count(i) > times:
        letters = []
        letters.append(i)
        times = s.count(i)
    elif s.count(i) == times:
        letters.append(i)
print(list(set(letters)))

# 第二种方法

s = "aabbccddffffxxxx"
count = {}        

for i in s:        # 统计字符串出现的个数
    # print(i)
    count.setdefault(i, 0)
    count[i] += 1
# print(count)

max_value = count['a']
result = []

for m, n in count.items():        # 取出字典value最大的key
    # print(m,n)
    if n > max_value:
        max_value = n
        result = []
        result.append(m)
    elif n == max_value:
        result.append(m)
print(result)

# 第三种方法：将字典中key 和value 调换

a = "aabbccddeeefff"
d0 = dict()
d1 = dict()
for i in a:
    if i not in d0:
        d0[i] = 0
    d0[i] += 1

s = 0
for k, v in d0.items():
    if v not in d1:
        d1[v] = ""
    d1[v] = d1[v] + k
    if v < s:
        d1.pop(v)
    else:
        s = v
print(d1[list(d1.keys())[0]])
