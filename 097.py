#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入一个年份，输出是否为闰年
# 是闰年的条件：
# 能被4整除但不能被100整除，或者能被400整除的年份都是闰年

year = int(input("Enter the year："))
if year % 4 == 0  and year % 100 != 0:
    print("This is the leap year!")
elif year % 400 == 0:
    print("This is the leap year!")
else:
    print("This is not the leap year!")