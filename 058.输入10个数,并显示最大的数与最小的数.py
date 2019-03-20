#!/usr/bin/env python
# -*- coding: utf-8 -*-

num = []

for i in range(10):
    num.append(float(input("Please enter numbers: ")))

# print(num)

result = sorted(num)

# print(result)

print("最大数字为：" + str(result[0]))
print("最小数字为：" + str(result[-1]))
 