#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入3个数字，以逗号隔开，输出其中最大的数

num = []
for i in range(3):
    num.append(input("Enter a number："))
    num.sort()
    # print(','.join(num))
print("The biggest is：" + num[-1])