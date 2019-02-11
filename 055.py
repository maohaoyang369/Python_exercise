#!/usr/bin/env python
# -*- coding: utf-8 -*-!

# 计算1 - 1/2 + 1/3 - 1/4 + … + 1/99 - 1/100 + …直到最后一项的绝对值小于10的-5次幂为止

count = 1
i = 1

while True:
    i = i+1
    if 1/i < pow(10, -5):
        break
    else:
        if i % 2 == 0:
            count = count - 1 / i
        else:
            count = count + 1/i

print(count)

