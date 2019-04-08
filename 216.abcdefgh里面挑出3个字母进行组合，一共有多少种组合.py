# !/usr/bin/env python
# -*- coding: utf-8 -*-

# "abcdefgh"里面挑出3个字母进行组合，一共有多少种组合，要求三个字母中不能有任何重复的字母，
# 三个字母的同时出现次数，在所有组合中只能出现一次，例如出现abc了，不能出现cab和bca等

result = []

for i in "abcdefgh":
    for j in "abcdefgh":
        for m in "abcdefgh":
            s = i+j+m
            if s.count(i) > 1 or s.count(j) > 1 or s.count(m) > 1:
                continue
            if sorted(list(s)) not in list(map(lambda x:sorted(list(x)), result)):
                result.append(s)

print(len(result))
