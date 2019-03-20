#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 下面有一个小程序，计算一个字符串中每个字符出现的次数

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for i in message:
    count.setdefault(i, 0)        # 当i第一次进入字典时，值为0
    count[i] += 1        # 递增

print(count)