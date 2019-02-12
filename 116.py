# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入3个数字，达到3个数字求和，结束程序

count = 0
for i in range(3):
    num = input("请输入数字：")
    count += int(num)
print(count)
