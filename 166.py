# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入a,b,c三个数，求最大的那个

import sys


def is_num(n):        # 定义函数  判断是不是数字
    for i in n:
        if i not in "0123456789":
            return False
    return True


num = {}
result = [0, 0]

for i in "abc":
    num[i] = input("Please enter number "+i+":")
    if not is_num(num[i]):
        print("Please enter number!")
        sys.exit()

for m, n in num.items():
    if int(n) > result[1]:
        result[1] = int(n)
        result[0] = m
print("最大的是", result[0])

# print(num)
