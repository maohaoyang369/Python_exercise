# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 读入一个数字，并判断是否正数，是的话打印“是正数！”，否则打印“不是正数”

num = input("Please enter a number：")
for i in num:
    if i not in "01234567890.-+":
        print("Wrong number!")
    elif float(num) > 0:
        print("是正数")
    elif float(num) < 0:
        print("不是正数")
    break
