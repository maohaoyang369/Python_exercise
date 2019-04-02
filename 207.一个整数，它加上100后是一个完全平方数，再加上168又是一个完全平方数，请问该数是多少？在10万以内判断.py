# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？在10万以内判断

# 分析：
# 1 x 在10万里面，x是某个数，不知道是谁
# 2 (x+100)开方 = y y整数，
# 3 (x++100+168)开方 = z z 整数
# 4 开方：math.sqrt  
# 5 怎么判断z 和y 是否整数？
# y**2是整数且是x++100
# z**2是整数且是x++100+168

import math

result = []

for i in range(1, 100000):
    y = math.sqrt(i+100)
    z = math.sqrt(i+100+168)
    if (int(y)**2 == i+100) and (int(z)**2 == i+100+168):
        # print(i)
        result.append(i)

print(result)
