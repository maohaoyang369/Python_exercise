# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 三个人踢球，踢四次，不能踢给自己（AA BB CC），AC之间不能互传（AC CA）

# 第一种方法

person = ["A", "B", "C"]
result = 0

for i in range(0, 3):
    for j in range(0, 3):
        if i == j or (i == 0 and j == 2) or (i == 2 and j == 0):
            continue
        for k in range(0, 3):
            if j == k or (j == 0 and k == 2) or (j == 2 and k == 0):
                continue
            for m in range(0, 3):
                if k == m or (k == 0 and m == 2) or (k == 2 and m == 0):
                    continue
                result += 1
print(result)

# 第二种方法

count = 0
for one in "ABC":
    for two in "ABC":
        for three in "ABC":
            for four in "ABC":
                result = one + two + three + four
                if not ("AA"in result or "BB" in result or "CC" in result):
                    if not ("AC" in result or "CA" in result):
                        count += 1
print(count)
