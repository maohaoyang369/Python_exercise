#!/usr/bin/env python
# -*- coding: utf-8 -*-!

# 对一个列表求和，如列表是[4, 3, 6]，求和结果是 [4, 7, 13]，
# 每一项的值都等与该项的值加上前一项的值

sentance = [4, 3, 6]

result = []
for i in range(len(sentance)):
    # print(i)
    result.append(sum(sentance[0:i+1]))
print(result)