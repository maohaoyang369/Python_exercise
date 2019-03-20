# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 读入一个数字，判断是否奇数还是偶数

num = input("Please enter a number：")
for i in num:
    if i not in "01234567890":
        print("It's not number!")
    elif int(num) % 2 == 0:
        print("是偶数")
    else:
        print("是奇数")
    break
